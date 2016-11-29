# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains APIs to facilitate UcsCentral Firmware management
"""

import logging
import os
import time
import datetime
from ..ucscexception import UcscValidationException, \
    UcscOperationError, \
    UcscWarning, \
    UcscConnectionError

from ucscsdk.utils.ccoimage import get_ucsc_cco_image_list
from ucscsdk.utils.ccoimage import get_ucsc_cco_image
from ucscsdk.ucscgenutils import Progress

from ucscsdk.mometa.top.TopSystem import TopSystem
from ucscsdk.mometa.firmware.FirmwareCatalogue import FirmwareCatalogue
from ucscsdk.mometa.firmware.FirmwareDownloader import \
        FirmwareDownloader, \
        FirmwareDownloaderConsts
from ucscsdk.mometa.firmware.FirmwareDistributable import \
        FirmwareDistributable, \
        FirmwareDistributableConsts
from ucscsdk.mometa.firmware.FirmwareInfraPack import FirmwareInfraPack
from ucscsdk.mometa.firmware.FirmwareCatalogPack import \
        FirmwareCatalogPack
from ucscsdk.mometa.trig.TrigSched import TrigSched
from ucscsdk.mometa.trig.TrigSched import TrigSchedConsts
from ucscsdk.mometa.trig.TrigAbsWindow import TrigAbsWindow
from ucscsdk.mometa.firmware.FirmwareDownloadPolicy import \
        FirmwareDownloadPolicy
from ucscsdk.utils.ucscdomain import get_domain_group_dn

log = logging.getLogger('ucscentral')


def get_firmware_bundles(handle, bundle_type=None,
                         fw_platform=None):
    '''
    Return the list of firmware bundles that have been imported or available
    for import to Ucs Central

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        bundle_type (str): Type of bunde,
                            provider-bundle - ucs-central
                            catalog - ucs catalog bundle
                            b-series-bundle - ucs b series bundle
                            c-series-bundle - ucs c series bundle
                            m-series-bundle - ucs m series bundle
                            infrastructure-bundle - ucs infra bundle
        fw_platform (str): platform type, valid if bundle_type is infra bundle
                                         classic - 6100/6200 platform
                                         mini - 6300 mini platform
                                         3gen - 6300 3rdgen platform
    Returns:
       bundles : List of requested bundles
    Example:
        get_firmware_bundles(handle, bundle_type="catalog")
        get_firmware_bundles(handle, bundle_type="b-series-bundle")
        get_firmware_bundles(handle, bundle_type="infrastructure-bundle")
        get_firmware_bundles(handle, bundle_type="infrastructure-bundle",
                             fw_platform="mini")
    '''
    filter_str = None

    fw_infra_bundle_map = {'classic': 'ucs-k9-bundle-infra',
                           'mini': 'ucs-mini-k9-bundle-infra',
                           '3gen': 'ucs-6300-k9-bundle-infra'}
    if bundle_type is not None:
        filter_str = '(type, %s, type="eq")' % bundle_type

    if bundle_type == 'infrastructure-bundle' and fw_platform is not None:
        filter_bundle = '(name, %s, type="re")' % fw_infra_bundle_map[
            fw_platform]
        filter_str = filter_str + " and " + filter_bundle

    bundles = handle.query_classid(
        class_id="FirmwareDistributable", filter_str=filter_str)

    i = 1
    if bundles == []:
        log.debug("No Firmware Bundles found")
    else:
        log.debug("Firmwares Bundles:")
        log.debug(
            "No.                      Name                                  "
            "Type                  Status    ")
        log.debug(
            "=== ================================================= ========="
            "=============    ===============")
        for bundle in bundles:
            log.debug(" %2d %-50s %-25s %-18s" %
                      (i, bundle.name, bundle.type, bundle.oper_dnld_status))
            i += 1
    return bundles


def get_failed_dw_firmware_bundles(handle):
    '''
    Return the list of firmware bundles that have been downloaded on the
    Ucs Central

    Args:
        handle (UcscHandle): UcsCentral Connection handle
    Returns:
       failed_dw_bundles : List of failed download bundles
    Example:
        get_failed_dw_firmware_bundles(handle)
    '''
    filter_str = None

    filter_str = '(transfer_state, "failed", type="eq")'
    failed_dw_bundles = handle.query_classid(
        class_id="FirmwareDownloader", filter_str=filter_str)

    i = 1
    if failed_dw_bundles == []:
        log.debug("No Failed Download Firmware Bundles found")
    else:
        log.debug("Failed Downloads:")
        log.debug(
            "No.                      Name                                  "
            "Error Code                 Error Description     ")
        log.debug(
            "=== ================================================= ========="
            "================== ==============================")
        for bundle in failed_dw_bundles:
            log.debug(
                " %2d %-50s %-30s %-30s" %
                (i,
                 bundle.file_name,
                 bundle.fsm_rmt_inv_err_code,
                 bundle.fsm_rmt_inv_err_descr))
            i += 1
    return failed_dw_bundles


def get_cco_firmware_image(image_name, username, password, download_dir,
                           mdf_id_list=(284308174,), proxy=None,
                           progress=Progress()):
    '''
    Downloads the firmware from CCO given the image name
    Args:
        image_name (str): Name of the image to be downloaded from cco
        username (str): username to connect to cco image server
        password (str): password to connect to cco image server
        mdf_id_list (list): list of mdf id
                            284308174 - ucs central firmware images(default)
                            283612660 - ucs infra bundle and catalog
                            283853163 - b-series ucs blade servers
                            283862063 - c-series ucs rack servers
        proxy (str): proxy used for connection
    Example:
        get_cco_firmware_image(image_name='ucs-central-bundle.1.5.1a.bin',
                          username='guest', password='password',
                          download_dir='/Users/guest/Downloads/')
    '''

    images = get_ucsc_cco_image_list(username=username,
                                     password=password,
                                     mdf_id_list=mdf_id_list,
                                     proxy=proxy)

    image_dict = {}
    for image in images:
        image_dict[image.image_name] = image

    if image_name not in image_dict:
        raise UcscOperationError("Get CCO image", "Image not available")

    # download image
    image = image_dict[image_name]
    get_ucsc_cco_image(
        image,
        file_dir=download_dir,
        proxy=proxy,
        progress=progress)


def firmware_add_local(handle, local_path, file_name,
                       timeout=15 * 60, progress=Progress()):
    '''
    Import the firmware to UcsCentral from local drive

    Args:
        local_path (str): Local directory where image resides
        file_name (str): Name of the image in the local directory
        timeout (number): Timeout in seconds for the image to get uploaded to
                          ucs central
    Example:
        firmware_add_local(handle,"/Users/guest/Downloads/",
                                  "ucs-k9-bundle-b-series.3.1.1h.B.bin")
    '''
    if not local_path:
        raise UcscValidationException("Missing local_path argument")
    if not file_name:
        raise UcscValidationException("Missing file_name argument")

    file_path = os.path.join(local_path, file_name)
    if not os.path.exists(file_path):
        raise UcscValidationException("File does not exist")

    top_system = TopSystem()
    firmware_catalogue = FirmwareCatalogue(parent_mo_or_dn=top_system)
    firmware_downloader = FirmwareDownloader(
        parent_mo_or_dn=firmware_catalogue,
        file_name=file_name)
    firmware_downloader.server = FirmwareDownloaderConsts.PROTOCOL_LOCAL
    firmware_downloader.protocol = FirmwareDownloaderConsts.PROTOCOL_LOCAL
    firmware_downloader.admin_state = \
        FirmwareDownloaderConsts.ADMIN_STATE_RESTART

    try:
        log.debug("Start uploading firmware")
        uri_suffix = "operations/file-%s/image.txt?Cookie=%s" % (
            file_name, handle.cookie)
        handle.file_upload(url_suffix=uri_suffix,
                           file_dir=local_path,
                           file_name=file_name,
                           progress=progress)

    except Exception as err:
        UcscWarning(str(err))
        raise UcscOperationError("Upload firmware", "upload failed")

    handle.add_mo(firmware_downloader, modify_present=True)
    handle.commit()

    start = datetime.datetime.now()
    while not firmware_downloader.transfer_state == \
            FirmwareDownloaderConsts.TRANSFER_STATE_DOWNLOADED:
        firmware_downloader = handle.query_dn(firmware_downloader.dn)
        if firmware_downloader.transfer_state == \
                FirmwareDownloaderConsts.TRANSFER_STATE_FAILED:
            raise UcscOperationError(
                    "Import of %s " % file_name,
                    "%s" % firmware_downloader.fsm_rmt_inv_err_descr)
        if (datetime.datetime.now() - start).total_seconds() > timeout:
            raise UcscOperationError(
                "Import of %s" % file_name,  "operation timed out")
        time.sleep(1)

    return firmware_downloader


def firmware_add_remote(handle, remote_path, file_name, protocol, hostname,
                        username="", password=""):
    '''
    Import the firmware to UcsCentral from remote location

    Args:
        remote_path (str): Remote path where image resides
        file_name (str): Name of the image in the remote directory
        protocol (str): Protocol for the remote communication
        hostname (str): IP address or the host name of the remote server
        username (str): Username for the remote server access
        password  (str): Password for the remote server access
    Example:
        firmware_add_remote(handle,
                            file_name="ucs-k9-bundle-b-series.3.1.1h.B.bin",
                            remote_path="/remote_path/", hostname="10.10.1.1",
                            protocol="scp",username="guest",password="password")
    '''
    if not hostname:
        raise UcscValidationException("Missing hostname argument")
    if not remote_path:
        raise UcscValidationException("Missing remote_path argument")
    if not file_name:
        raise UcscValidationException("Missing file_name argument")
    if not protocol:
        raise UcscValidationException("Missing protocol argument")

    if protocol is not FirmwareDownloaderConsts.PROTOCOL_TFTP:
        if not username:
            raise UcscValidationException("Missing username argument")
        if not password:
            raise UcscValidationException("Missing password argument")

    top_system = TopSystem()
    firmware_catalogue = FirmwareCatalogue(parent_mo_or_dn=top_system)
    firmware_downloader = FirmwareDownloader(
        parent_mo_or_dn=firmware_catalogue,
        file_name=file_name)
    firmware_downloader.remote_path = remote_path
    firmware_downloader.protocol = protocol
    firmware_downloader.server = hostname
    firmware_downloader.user = username
    firmware_downloader.pwd = password
    firmware_downloader.admin_state = \
        FirmwareDownloaderConsts.ADMIN_STATE_RESTART

    handle.add_mo(firmware_downloader, modify_present=True)
    handle.commit()


def firmware_remove(handle, image_name):
    '''
    Removes the image from UcsCentral

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        image_name (str): Name of the image to be deleted

    Example:
        firmware_remove(handle,
                        image_name="ucs-k9-bundle-b-series.3.1.1h.B.bin")
    '''

    top_system = TopSystem()
    firmware_catalogue = FirmwareCatalogue(parent_mo_or_dn=top_system)
    firmware_distributable = FirmwareDistributable(
        parent_mo_or_dn=firmware_catalogue,
        name=image_name)

    dn = firmware_distributable.dn
    mo = handle.query_dn(dn)
    if mo is None or mo.oper_dnld_status != \
            FirmwareDistributableConsts.OPER_DNLD_STATUS_DOWNLOADED:
        raise UcscOperationError(
            "Firmware remove",
            "Image not available on UCS Central.")

    mo.admin_state = FirmwareDistributableConsts.ADMIN_STATE_DELETED
    handle.set_mo(mo)
    handle.commit()


def _validate_firmware_bundle(handle, bundle_type, version):
    '''
    Internal function to validate firmware bundle for domain fw_update
    '''
    if bundle_type == "catalog":
        filter_str = '(type, %s, type="eq")' % "catalog"
    else:
        filter_infra = '(type, %s, type="eq")' % "infrastructure-bundle"
        if bundle_type == "classic":
            filter_bundle = '(inv_tag, %s, type="eq")' % "bundle-infra"
        if bundle_type == "mini":
            filter_bundle = '(inv_tag, %s, type="eq")' % "bundle-mini-infra"
        if bundle_type == "classic-3gen":
            filter_bundle = '(inv_tag, %s, type="eq")' % "bundle-6300-infra"

        filter_str = filter_infra + " and " + filter_bundle

    bundles = handle.query_classid(
        class_id="FirmwareDistributable", filter_str=filter_str)
    for bundle in bundles:
        if bundle.version == version:
            return True
    raise UcscOperationError(
        "Validate firmware bundle",
        "Bundle %s not available on UCS Central" %
        version)


def _add_firmware_infra_pack(handle, dn, fw_version):
    '''
    Internal add firmware infra package for domain fw_update
    '''
    fw_infra = FirmwareInfraPack(parent_mo_or_dn=dn,
                                 name="default",
                                 mode="staged",
                                 infra_bundle_version=fw_version)
    handle.add_mo(fw_infra, modify_present=True)


def schedule_infra_fw_update(handle, domain_group, schedule, user_ack_en=True,
                             fi_6100_6200_ver=None, fi_mini_6300_ver=None,
                             fi_6300_ver=None, catalog_ver=None):
    """
    Schedules infra fw update for the domain group
    Note: infra fw update will happen only for the bundles which are imported
          to UcsCentral

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        schedule(string): Date string in format YYYY-MM-DDTHH:MM:SS
                          eg. 2016-08-30T05:19:05,
                          you can use "now" to trigger immediate fw_update
        domain_group(string): Full domain_group with root/<org_name>/..
        user_ack_en(boolean): Enable/Disable user ack for firmware update
                            By default True
        fi_6100_6200_ver: FI 6100/6200 FW version
        fi_mini_6300_ver: FI Mini 6300 FW version
        fi_6300_ver:      FI 3rd Gen 6300 FW version
        catalog_ver:      Catalog version
    Returns:
        None

    Example:
        schedule_infra_fw_update(handle, domain_group="root", schedule="now")
        schedule_infra_fw_update(handle, domain_group="root",
                                schedule="2016-08-31T22:33:07",
                                fi_mini_6300_ver="3.1(1j)A",
                                catalog_ver="3.1(1)T")
    """
    if schedule == "now":
        date_str = datetime.datetime.today().strftime("%Y-%m-%dT%H:%M:%S")
    else:
        date_str = schedule
        if (datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
                < datetime.datetime.today()):
            raise UcscValidationException(
                "Schedule can not be past date %s " % schedule)

    domain_group_dn = get_domain_group_dn(handle, domain_group)
    fw_infra_policy_dn = domain_group_dn + "/fw-infra-policy"

    if fi_6100_6200_ver is not None:
        _validate_firmware_bundle(handle, "classic", fi_6100_6200_ver)
        classic_fw_dn = fw_infra_policy_dn + "/fw-family-ucs-classic "
        _add_firmware_infra_pack(handle, classic_fw_dn, fi_6100_6200_ver)

    if fi_mini_6300_ver is not None:
        _validate_firmware_bundle(handle, "mini", fi_mini_6300_ver)
        mini_fw_dn = fw_infra_policy_dn + "/fw-family-ucs-mini"
        _add_firmware_infra_pack(handle, mini_fw_dn, fi_mini_6300_ver)

    if fi_6300_ver is not None:
        _validate_firmware_bundle(handle, "classic-3gen", fi_6300_ver)
        classic_3gen_fw_dn = fw_infra_policy_dn + "/fw-family-ucs-classic-3gen"
        _add_firmware_infra_pack(handle, classic_3gen_fw_dn, fi_6300_ver)

    if catalog_ver is not None:
        _validate_firmware_bundle(handle, "catalog", catalog_ver)
        catalog_pack = FirmwareCatalogPack(parent_mo_or_dn=domain_group_dn,
                                           name="default",
                                           catalog_version=catalog_ver)
        handle.add_mo(catalog_pack, modify_present=True)

    handle.commit()

    admin_state = (TrigSchedConsts.ADMIN_STATE_UNTRIGGERED,
                   TrigSchedConsts.ADMIN_STATE_USER_ACK)[user_ack_en]

    fw_update_sched = TrigSched(parent_mo_or_dn=domain_group_dn,
                                name="infra-fw",
                                admin_state=admin_state,
                                sched_mode=TrigSchedConsts.SCHED_MODE_ADVANCED,
                                sched_type=TrigSchedConsts.SCHED_TYPE_DEFAULT)

    handle.add_mo(fw_update_sched, modify_present=True)
    handle.commit()

    fw_update_sched_window = TrigAbsWindow(parent_mo_or_dn=fw_update_sched.dn,
                                           name="infra-fw",
                                           date=date_str)
    handle.add_mo(fw_update_sched_window, modify_present=True)
    handle.commit()


def _validate_proxy_details(
        proxy_name_or_ip, proxy_port, proxy_username, proxy_password):
    '''
    Internal method to performs proxy arguments validation and returns
    proxy string
    '''
    proxy_str = None

    if (proxy_name_or_ip is None) or (proxy_port is None):
        raise UcscValidationException(
            'proxy_name_or_ip and proxy_port should be specified')

    proxy_str = proxy_name_or_ip + ":" + proxy_port

    if proxy_username != '':
        if proxy_password != '':
            proxy_str = proxy_username + ":" + proxy_password + "@" + \
                proxy_name_or_ip + ":" + proxy_port
        else:
            proxy_str = proxy_username + '@' + \
                proxy_name_or_ip + ":" + proxy_port

    return proxy_str


def _is_valid_cisco_connection(cisco_username, cisco_password, proxy_str):
    '''
    This internal method validates connection to the cisco for firmware update
    TODO: Need to verify connection to cisco from central
    '''
    image_list = []
    image_list = get_ucsc_cco_image_list(username=cisco_username,
                                         password=cisco_password,
                                         proxy=proxy_str)

    if image_list == []:
        UcscWarning("Connection to cisco.com failed")
        return False
    return True


def sync_firmware_update_from_cisco(handle, cisco_username, cisco_password,
                                    sync_enable=False, sync_frequencey="daily",
                                    proxy_enable=False,
                                    proxy_name_or_ip=None, proxy_port=None,
                                    proxy_username="", proxy_password=""):
    """
    Sync domain firmware updates from cisco

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        cisco_username (str): cisco username to connect to image server
        cisco_password (str): cisco password to connect to image server
        sync_enable (boolean): if True, sync to cisco.com enable for
                               firmware update
                               False by default
        sync_frequencey (string): if sync is enabled, this dictates the
                                  frequencey of sync
                                  ['daily', 'weekly', 'bi-weekly', 'on demand']
                                  'daily' by default
        proxy_enable (boolean): if True, proxy to access cisco.com is enabled
                                False by default
        # Proxy details in case proxy_enable is True
        proxy_name_or_ip (str) : Proxy hostname or IP address
        proxy_port (str) : Proxy port to access proxy
        proxy_username (str) : Proxy username to access proxy, if any
        proxy_password (str) : Proxy password to access proxy, if any

    Example:
        sync_firmware_update_from_cisco(handle, cisco_username = "guest",
                                        cisco_password="password",
                                        sync_enable = True,
                                        sync_frequencey= "weekly",
                                        proxy_enable = False)
        sync_firmware_update_from_cisco(handle, cisco_username = "guest",
                                        cisco_password="password",
                                        sync_enable = True,
                                        sync_frequencey= "on demand",
                                        proxy_enable = True,
                                        proxy_username = "admin",
                                        proxy_name_or_ip = "192.168.1.1",
                                        proxy_port = "8080")
    """

    if proxy_enable:
        proxy_str = _validate_proxy_details(proxy_name_or_ip, proxy_port,
                                            proxy_username, proxy_password)
        http_proxy = proxy_name_or_ip + ":" + proxy_port
    else:
        proxy_str = None
        http_proxy = ''

    if not _is_valid_cisco_connection(
            cisco_username, cisco_password, proxy_str):
        UcscConnectionError(
            "Connection to cisco.com failed with provided credentials")

    sync_frequencey_map = {'daily': '1day',
                           'weekly': '1week',
                           'bi-weekly': '2week',
                           'on demand': 'on-demand'}
    if sync_enable:
        sync_admin_state = "enable"
        sync_frequencey = sync_frequencey_map[sync_frequencey]
    else:
        sync_admin_state = "disable"

    sync_fw_update = FirmwareDownloadPolicy(
            parent_mo_or_dn="domaingroup-root",
            type="Cisco",
            download_interval=sync_frequencey,
            username=cisco_username,
            password=cisco_password,
            policy_admin_state=sync_admin_state,
            http_proxy=http_proxy,
            proxy_user=proxy_username,
            proxy_pwd=proxy_password)

    handle.set_mo(sync_fw_update)
    handle.commit()
