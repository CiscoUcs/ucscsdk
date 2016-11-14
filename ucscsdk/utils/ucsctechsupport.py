# Copyright 2013 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains the APIs used to create and download tech_support file.
"""

import os
import time
import datetime
import logging
from ..ucscexception import UcscValidationException, \
    UcscWarning, \
    UcscOperationError
from ..mometa.sysdebug.SysdebugTechSupportCmdOpt import \
    SysdebugTechSupportCmdOpt, SysdebugTechSupportCmdOptConsts

log = logging.getLogger('ucscentral')


def _validate_download_args(file_dir, file_name):
    if file_dir is None:
        raise UcscValidationException(
            'file_dir is a required parameter')

    if file_name is None:
        raise UcscValidationException(
            'file_name is a required parameter')

    if not file_name.endswith('.tar'):
        raise UcscValidationException('file_name should end with .tar')


def _create_download_dir(file_dir):
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)


def _get_creation_ts():
    dt1 = datetime.datetime(1970, 1, 1, 12, 0, 0, 0)
    dt2 = datetime.datetime.utcnow()
    return int((dt2 - dt1).total_seconds())


def _bootstrap_tech_support_mo(creation_ts):
    from ..mometa.top.TopSystem import TopSystem
    from ..mometa.sysdebug.SysdebugTechSupport import SysdebugTechSupport, \
        SysdebugTechSupportConsts
    from ..mometa.sysdebug.SysdebugTechSupFileRepository import \
        SysdebugTechSupFileRepository

    top_system = TopSystem()
    ts_file_repo = SysdebugTechSupFileRepository(parent_mo_or_dn=top_system)
    ts_mo = SysdebugTechSupport(
        parent_mo_or_dn=ts_file_repo,
        creation_ts=str(creation_ts),
        admin_state=SysdebugTechSupportConsts.ADMIN_STATE_START)
    return ts_mo


def _bootstrap_domain_tech_support_mo(creation_ts, domain_dn):
    from ..mometa.sysdebug.SysdebugTechSupportOp import \
        SysdebugTechSupportOp, SysdebugTechSupportOpConsts
    from ..mometa.sysdebug.SysdebugTechSupFileRepository import \
        SysdebugTechSupFileRepository

    ts_domain_file_repo = SysdebugTechSupFileRepository(
        parent_mo_or_dn=domain_dn)
    ts_domain_mo = SysdebugTechSupportOp(
        parent_mo_or_dn=ts_domain_file_repo,
        creation_ts=str(creation_ts),
        admin_state=SysdebugTechSupportOpConsts.ADMIN_STATE_START)
    return ts_domain_mo


def _check_for_failure(err):
    # The following error messages define the criteria for
    # the poll loop to be interrupted by an exception.
    # There are occasinal Request Timeouts, which could be ignored
    # if the subsequent calls are being replied to by the server.
    failure_conditions = ["urlopen error",
                          "TechSupport creation timed out",
                          "TechSupport creation failed"]
    for each in failure_conditions:
        if each in str(err):
            raise


def _fail_and_remove_ts(handle, ts_mo, err):
    if ts_mo:
        handle.remove_mo(ts_mo)
        handle.commit()
    raise UcscOperationError("Techsupport creation", err)


def _fail_and_remove_domain_ts(handle, ts_mo, err):
    # In case of domain ts remove, just set the mo, backend will remove it
    # from domain
    if ts_mo:
        ts_mo.admin_state = "delete"
        handle.set_mo(ts_mo)
        handle.commit()
    raise UcscOperationError("Domain techsupport creation", err)


def poll_wait_for_tech_support(handle, ts_mo, timeout):
    from ..mometa.sysdebug.SysdebugTechSupport import \
        SysdebugTechSupportConsts as tsconsts

    poll_interval = 5
    duration = timeout
    while True:
        try:
            ts = handle.query_dn(ts_mo.dn)
            if ts is None:
                _fail_and_remove_ts(handle, ts, 'failed')
            if ts.oper_state == tsconsts.OPER_STATE_AVAILABLE:
                break
            if ts.oper_state == tsconsts.OPER_STATE_FAILED or \
                    ts.oper_state == tsconsts.OPER_STATE_UNAVAILABLE:
                _fail_and_remove_ts(handle, ts, 'failed')
            time.sleep(min(duration, poll_interval))
            duration = max(0, (duration - poll_interval))
            if duration == 0:
                _fail_and_remove_ts(
                    handle, ts, 'timed out')
        except Exception as err:
            _check_for_failure(err)
    return ts


def download_tech_support(handle, name, file_dir, file_name):
    try:
        handle.file_download(url_suffix="techsupport/" + name,
                             file_dir=str(file_dir),
                             file_name=str(file_name))
    except Exception as err:
        UcscWarning(str(err))


def _remove_tech_support(handle, ts_mo):
    ts_mo.admin_state = "delete"
    handle.set_mo(ts_mo)
    handle.commit()


def get_tech_support(handle, file_dir=None, file_name=None,
                     remove_from_ucsc=False,
                     download=True,
                     timeout=1200):
    """
    This operation creates the technical support file for UcsCentral.

    Args:
        handle (UcscHandle): UcsCentral connection handle
        file_dir (str): directory to download techsupport file to
        file_name (str): name for the backup file
        remove_from_ucsc (boolean): True/False, False - by default
        download (boolean): True/False, True - by default
        timeout (number) : time in seconds for which method waits
                           for the techsupport to generate before it exits.
    Example:
        file_dir = "/home/user/backup"\n
        file_name = "techsupport.tar"\n
        get_tech_support(handle, file_dir=file_dir, file_name=file_name)

    """

    if download:
        _validate_download_args(file_dir, file_name)
        _create_download_dir(file_dir)

    ts_mo = _bootstrap_tech_support_mo(_get_creation_ts())
    SysdebugTechSupportCmdOpt(parent_mo_or_dn=ts_mo)

    handle.add_mo(ts_mo)
    handle.commit()

    log.debug("Techsupport creation started")

    # poll for tech support to complete
    ts_mo = poll_wait_for_tech_support(handle, ts_mo, timeout)

    log.debug("Techsupport creation completed")
    # download tech support file
    if download:
        if handle.is_local_download_supported():
            download_tech_support(handle, ts_mo.name, file_dir, file_name)
            log.debug("Downloading techsupport complete")
        else:
            log.debug("Local download is not supported for this "
                      "UcsCentral version")

    # remove tech support file from Ucs Central
    if remove_from_ucsc:
        _remove_tech_support(handle, ts_mo)
        log.debug("Removed techsupport from UcsCentral")


def _is_valid_arg(param, kwargs):
    return param in kwargs and kwargs[param] is not None


def _set_ts_options_ucsm(ts_cmd_opt, kwargs):
    ts_cmd_opt.major_opt_type = \
        SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_UCSM


def _set_ts_options_ucsm_mgmt(ts_cmd_opt, kwargs):
    ts_cmd_opt.major_opt_type = \
        SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_UCSM_MGMT


def _validate_chassis_options(kwargs):
    if not _is_valid_arg("chassis_id", kwargs):
        raise UcscValidationException('chassis_id should be specified')
    if "cimc_id" not in kwargs and \
            "iom_id" not in kwargs and \
            "cartridge_id" not in kwargs:
        raise UcscValidationException(
            'cimc_id/iom_id/cartridge_id should be specified')


def _set_ts_options_chassis(ts_cmd_opt, kwargs):
    _validate_chassis_options(kwargs)
    ts_cmd_opt.chassis_id = str(kwargs["chassis_id"])
    ts_cmd_opt.major_opt_type = \
        SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_CHASSIS
    if _is_valid_arg("cimc_id", kwargs):
        ts_cmd_opt.chassis_cimc_id = str(kwargs["cimc_id"])

        if _is_valid_arg("adapter_id", kwargs):
            ts_cmd_opt.cimc_adapter_id = str(kwargs["adapter_id"])
        else:
            ts_cmd_opt.cimc_adapter_id = \
                SysdebugTechSupportCmdOptConsts.CIMC_ADAPTER_ID_ALL
    elif _is_valid_arg("iom_id", kwargs):
        ts_cmd_opt.chassis_iom_id = str(kwargs["iom_id"])
    elif _is_valid_arg("cartridge_id", kwargs):
        ts_cmd_opt.chassis_cartridge_id = str(kwargs["cartridge_id"])
        if ts_cmd_opt.chassis_cartridge_id != "all":
            if _is_valid_arg("cartridge_cimc_id", kwargs):
                ts_cmd_opt.cartridge_cimc_id = str(
                    kwargs["cartridge_cimc_id"])
            else:
                raise UcscValidationException(
                    'cartridge_cimc_id should be specified')


def _validate_rackserver_options(kwargs):
    if not _is_valid_arg("rack_server_id", kwargs):
        raise UcscValidationException(
            'rack_server_id should be specified')


def _set_ts_options_rackserver(ts_cmd_opt, kwargs):
    _validate_rackserver_options(kwargs)
    ts_cmd_opt.rack_server_id = str(kwargs["rack_server_id"])
    ts_cmd_opt.major_opt_type = \
        SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_SERVER

    if _is_valid_arg("rack_adapter_id", kwargs):
        ts_cmd_opt.rack_server_adapter_id = str(kwargs["rack_adapter_id"])
    else:
        ts_cmd_opt.rack_server_adapter_id = \
            SysdebugTechSupportCmdOptConsts.RACK_SERVER_ADAPTER_ID_ALL


def _validate_fex_options(kwargs):
    if not _is_valid_arg("fex_id", kwargs):
        raise UcscValidationException('fex_id should be specified')


def _set_ts_options_fex(ts_cmd_opt, kwargs):
    _validate_fex_options(kwargs)
    ts_cmd_opt.fab_ext_id = str(kwargs["fex_id"])
    ts_cmd_opt.major_opt_type = \
        SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_FEX


def _validate_servermemory_options(kwargs):
    if not _is_valid_arg("server_id_list", kwargs):
        raise UcscValidationException(
            'server_id_list should be specified')


def _set_ts_options_servermemory(ts_cmd_opt, kwargs):
    _validate_servermemory_options(kwargs)
    ts_cmd_opt.server_id_list = str(kwargs["server_id_list"])
    ts_cmd_opt.major_opt_type = \
        SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_SERVER_MEMORY


def _set_ts_command_options(ts_cmd_opt, kwargs):
    if _is_valid_arg("command_options", kwargs):
        ts_cmd_opt.command_options = str(kwargs["command_options"])


def _set_ts_options(option, ts_cmd_opt, kwargs):
    if option == "ucsm":
        _set_ts_options_ucsm(ts_cmd_opt, kwargs)
    elif option == "ucsm-mgmt":
        _set_ts_options_ucsm_mgmt(ts_cmd_opt, kwargs)
    elif option == "chassis":
        _set_ts_options_chassis(ts_cmd_opt, kwargs)
    elif option == "fabric-extender":
        _set_ts_options_fex(ts_cmd_opt, kwargs)
    elif option == "rack-server":
        _set_ts_options_rackserver(ts_cmd_opt, kwargs)
    elif option == "server-memory":
        _set_ts_options_servermemory(ts_cmd_opt, kwargs)
    else:
        raise UcscValidationException(
            'Unrecognised option value: ' + option)

    _set_ts_command_options(ts_cmd_opt, kwargs)


def poll_wait_for_domain_tech_support_init(handle, creation_ts, ts_domain_mo):
    duration = 30
    poll_interval = 2
    ts_mo = []
    filter_str = '(creation_ts, %s, type="eq")' % (str(creation_ts))
    while True:
        ts_mo = handle.query_classid("SysdebugTechSupport",
                                     filter_str=filter_str, dme="resource-mgr")
        if ts_mo != []:
            break
        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            _fail_and_remove_domain_ts(
                handle, ts_domain_mo, 'failed')

    log.debug("Techsupport creation for domain initiated")
    return ts_mo


def poll_wait_for_domain_tech_support(handle, ts_mo, ts_domain_mo, timeout):
    # poll for tech support mo to complete
    from ..mometa.sysdebug.SysdebugTechSupport import \
        SysdebugTechSupportConsts as SysdebugTechSupportConsts
    duration = timeout
    poll_interval = 5
    while True:
        ts = handle.query_dn(ts_mo.dn, dme="resource-mgr")
        if ts.oper_state == \
                SysdebugTechSupportConsts.OPER_STATE_AVAILABLE:
            break
        if ts.oper_state == \
                SysdebugTechSupportConsts.OPER_STATE_FAILED or \
                ts.oper_state == \
                SysdebugTechSupportConsts.OPER_STATE_UNAVAILABLE:
            _fail_and_remove_domain_ts(handle, ts_domain_mo, 'failed')
        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            ts_domain_mo = handle.query_dn(ts_domain_mo.dn)
            _fail_and_remove_domain_ts(handle, ts_domain_mo, 'failed')

    log.debug("Techsupport creation completed")
    return ts


def get_domain_tech_support(handle, domain_ip,
                            domain_name=None,
                            option="ucsm",
                            timeout=1200,
                            **kwargs):
    """
    This operation creates the technical support file for
    the specified Ucs Domain with specific parameters.
    Note: No support for download tech support file from domain for now


    Args:
        handle (UcscHandle): UcsCentral connection handle
        domain_ip (str): IP of domain, it can be None provided domain_name is
                            valid
        domain_name (str): Name of domain, applicable only if domain_ip is None
        option (str): categorty of technical support to be created.
                      possible values:
                        - ucsm
                        - ucsm-mgmt
                        - chassis:
                            Mandates that user specifies "chassis_id"
                            Either "cimc_id" or "iom_id" or "cartridge_id"
                            When specific "cartridge_id" is given, instead of
                                "all",
                            mandatory "cartridge_cimc_id" must also be given
                        - fabric-extender
                            Mandates that user specifies "fex_id"
                        - rack-server
                            Mandates that user specifies "rack_server_id"
                        - server-memory
                            Mandates that user specifies "server_id_list"
        kwargs: key=value pairs relevant to the seleced option

    Example:

        get_domain_tech_support(handle, domain_ip='192.168.1.1'
                                option="ucsm")

        get_domain_tech_support(handle, domain_ip=None,
                                domain_name="test_domain", option="ucs-mgmt")

        get_domain_tech_support(handle, domain_ip = '192.168.1.1',
                                option="chassis",
                                file_dir=".",
                                file_name="techsupport.tar",
                                chassis_id=1,
                                cimc_id=1,
                                adapter_id=1)

    """

    from .ucscdomain import get_domain, _is_domain_available

    domain = get_domain(handle, domain_ip, domain_name)

    if _is_domain_available(handle, domain.id):
        domain_dn = domain.dn
    else:
        raise UcscOperationError(
            "Get domain techsupport",
            "Domain with IP %s or name %s not registered or "
            "lost visibility with UcsCentral" %
            (domain_ip, domain_name))

    creation_ts = _get_creation_ts()
    ts_domain_mo = _bootstrap_domain_tech_support_mo(
        creation_ts, domain_dn=domain_dn)
    ts_cmd_opt = SysdebugTechSupportCmdOpt(parent_mo_or_dn=ts_domain_mo)
    _set_ts_options(option, ts_cmd_opt, kwargs)

    handle.add_mo(ts_domain_mo)
    handle.commit()

    log.debug("Techsupport creation started")
    # poll for tech support mo to get initiated, it should return list with
    # one element
    ts_mo_list = poll_wait_for_domain_tech_support_init(
        handle, creation_ts, ts_domain_mo)

    # poll for tech support operation to get completed
    poll_wait_for_domain_tech_support(
        handle, ts_mo_list[0], ts_domain_mo, timeout)
