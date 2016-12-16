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

from ucscsdk.utils.ucscfirmware import *
from nose.plugins.attrib import attr
from ucscsdk import set_log_level
from ..connection.info import custom_setup, custom_teardown, \
    get_local_config_params, get_remote_config_params, \
    get_cisco_account_params, skipped


local_upload = get_local_config_params("firmware_local_upload")
remote_upload = get_remote_config_params("firmware_remote_upload")
local_download = get_local_config_params("firmware_download")
cisco_account = get_cisco_account_params()


if cisco_account is not None:
    cisco_username = cisco_account['username']
    cisco_password = cisco_account['password']
    proxy_host = cisco_account['proxy_host']
    proxy_port = cisco_account['proxy_port']
    proxy_username = cisco_account['proxy_username']
    proxy_password = cisco_account['proxy_password']

handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


def test_001_get_firmware_bundles():
    # Get Images Library
    set_log_level(logging.ERROR)
    bundles = get_firmware_bundles(handle, bundle_type="infrastructure-bundle",
                                   fw_platform="mini")
    bundles = get_firmware_bundles(handle, bundle_type="catalog",
                                   fw_platform="bundle-6300-infra")
    bundles = get_firmware_bundles(handle, bundle_type="infrastructure-bundle")
    bundles = get_firmware_bundles(handle, bundle_type="b-series-bundle")
    failed_dw = get_failed_dw_firmware_bundles(handle)


@attr('slow')
def test_002_get_cco_images():
    if local_download is None or cisco_account is None:
        skipped("Arguments missing in config file")(
            test_002_get_cco_images)()
    image_list = get_ucsc_cco_image_list(username="guest", password="password")
    set_log_level(logging.ERROR)
    for image in image_list:
        if image.image_name == "ucs-central-bundle.1.2.1d.bin":
            dw_image = image
            break
    get_ucsc_cco_image(image=dw_image, file_dir=local_download['file_dir'])


@attr('slow')
def test_003_add_firmware_local():
    if local_upload is None:
        skipped("Arguments missing in config file")(
            test_003_add_firmware_local)()
    firmware_add_local(handle, local_upload['file_dir'],
                       local_upload['file_name'])


@attr('slow')
def test_004_add_firmware_remote():
    import time
    if remote_upload is None:
        skipped("Arguments missing in config file")(
            test_004_add_firmware_remote)()
    firmware_add_remote(handle,
                        file_name=remote_upload['file_name'],
                        remote_path=remote_upload['file_dir'],
                        hostname=remote_upload['hostname'],
                        protocol=remote_upload['protocol'],
                        username=remote_upload['username'],
                        password=remote_upload['password'])
    # sleep so that firmware upload is successful
    time.sleep(15)


@attr('config-disruptive')
def test_005_remove_firmware():
    firmware_remove(handle, image_name=remote_upload['file_name'])


@attr('config-disruptive')
def test_006_schedule_infra_firmware_update():
    schedule_infra_fw_update(handle, domain_group="root",
                             schedule="2016-08-31T22:33:07",
                             fi_mini_6300_ver="3.1(1j)A",
                             catalog_ver="3.1(1)T")


def test_007_sync_firmware_update():
    if cisco_account is None:
        skipped("Arguments missing in config file")(
            test_007_sync_firmware_update)()
    sync_firmware_update_from_cisco(handle, cisco_username=cisco_username,
                                    cisco_password=cisco_password,
                                    sync_enable=True,
                                    sync_frequencey="on demand",
                                    proxy_enable=True,
                                    proxy_username=proxy_username,
                                    proxy_name_or_ip=proxy_host,
                                    proxy_port=proxy_port)
