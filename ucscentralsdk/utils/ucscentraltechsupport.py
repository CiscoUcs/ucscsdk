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
from ..ucscentralexception import UcsCentralValidationException, UcsCentralWarning

log = logging.getLogger('ucscentral')

def get_ucscentral_tech_support(handle, file_dir=None, file_name=None,
                         remove_from_ucscentral=False,
                         download_techsupp=True,
                         timeout_in_sec=1200):

    from ..mometa.top.TopSystem import TopSystem
    from ..mometa.sysdebug.SysdebugTechSupport import SysdebugTechSupport, \
        SysdebugTechSupportConsts
    from ..mometa.sysdebug.SysdebugTechSupFileRepository import \
        SysdebugTechSupFileRepository
    from ..mometa.sysdebug.SysdebugTechSupportCmdOpt import \
        SysdebugTechSupportCmdOpt, SysdebugTechSupportCmdOptConsts

    if download_techsupp:
        if file_name is None:
            raise UcsValidationException('provide file_name')
        if file_dir is None:
            raise UcsValidationException('provide dir_name')

        if not file_name.endswith('.tar'):
            raise UcsValidationException('file_name should end with .tar')

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

    # Converting timedelta in to total seconds for Python version compatibility
    dt1 = datetime.datetime(1970, 1, 1, 12, 0, 0, 0)
    dt2 = datetime.datetime.utcnow()
    creation_ts = int((dt2 - dt1).total_seconds())

    # create SysdebugTechSupport
    top_system = TopSystem()
    sysdebug_techsup_file_repo = SysdebugTechSupFileRepository(
        parent_mo_or_dn=top_system)
    sys_debug_tech_support = SysdebugTechSupport(
        parent_mo_or_dn=sysdebug_techsup_file_repo,
        creation_ts=str(creation_ts),
        admin_state=SysdebugTechSupportConsts.ADMIN_STATE_START)

    sys_debug_tech_support_cmd_opt = SysdebugTechSupportCmdOpt(
        parent_mo_or_dn=sys_debug_tech_support)


    sys_debug_tech_support_cmd_opt.is_exclude_data = \
           SysdebugTechSupportCmdOptConsts.IS_EXCLUDE_DATA_NO
    # Parameter Set Ucs Central
    handle.add_mo(sys_debug_tech_support)
    handle.commit()

    log.debug("Techsupport creation started")
    # poll for tech support to complete
    duration = timeout_in_sec
    poll_interval = 2
    status = False

    while True:
        tech_support = handle.query_dn(sys_debug_tech_support.dn)
        if tech_support.oper_state == \
                SysdebugTechSupportConsts.OPER_STATE_AVAILABLE:
            status = True
        if status:
            break
        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            handle.remove_mo(tech_support)
            handle.commit()
            raise UcsCentralValidationException('TechSupport file creation timed out')

    log.debug("Techsupport creation complete, Downling techsupport now")
    # download tech support file
    if download_techsupp:
        url_suffix = "techsupport/" + tech_support.name
        try:
            handle.file_download(url_suffix=url_suffix,
                                 file_dir=file_dir,
                                 file_name=file_name)
        except Exception as err:
            UcsCentralWarning(str(err))

    log.debug("Downling techsupport complete")
    # remove tech support file from Ucs Central
    if remove_from_ucscentral:
        tech_support.admin_state = "delete"
        handle.set_mo(tech_support)
        handle.commit()

    return tech_support

def get_domain_tech_support(handle, domain_ip,
                         domain_name=None,
                         ucs_manager=False,
                         ucs_mgmt=False,
                         chassis_id=None, cimc_id=None,
                         adapter_id=None, iom_id=None,
                         fex_id=None,
                         rack_server_id=None, rack_adapter_id=None,
                         timeout_in_sec=900):
    """
    This operation creates and downloads the technical support file for
    the specified Ucs Domain with specific parameters.
    Note: No support for download tech support file from domain for now


    Args:
        handle (UcsCentralHandle): UcsCentral connection handle
        domain_ip (str): IP of domain, it can be None provided domain_name is valid
        domain_name (str): Name of domain, applicable only if domain_ip is None.
        ucs_manager (bool): True/False,
                            False - by default
                            Create TechSupport for UCSM, if true
        ucs_mgmt (bool): True/False,
                         False - by default
                         Create and TechSupport for UCSM Management
                         services(excluding Fabric interconnects), if true
        chassis_id (int): chassis id
        cimc_id (int/string): for a specific chassis. Can be 'all'.
        adapter_id (int/string): for a specific chassis. Can be 'all'.
        iom_id (int/string): for a specific chassis. Can be 'all'.
        fex_id (int): id of a fabric extender.
        rack_server_id (int): id of a rack server.
        rack_adapter_id (int/string): adaptor_id for a specific rack server.
                              Can be 'all'.
        timeout_in_sec (int): specifies the time in seconds after which
                                the operation times-out.

    Example:

        get_domain_tech_support(handle, domain_ip='192.168.1.1'
                            ucs_manager=True)

        get_domain_tech_support(handle, domain_ip=None, domain_name="test_domain",
                            chassis_id=1,cimc_id=1, adapter_id=1)

    """

    from .ucscentraldomain import get_domain
    from ..mometa.sysdebug.SysdebugTechSupportOp import SysdebugTechSupportOp, \
        SysdebugTechSupportOpConsts
    from ..mometa.sysdebug.SysdebugTechSupport import SysdebugTechSupport, \
        SysdebugTechSupportConsts
    from ..mometa.sysdebug.SysdebugTechSupFileRepository import \
        SysdebugTechSupFileRepository
    from ..mometa.sysdebug.SysdebugTechSupportCmdOpt import \
        SysdebugTechSupportCmdOpt, SysdebugTechSupportCmdOptConsts

    # Converting timedelta in to total seconds for Python version compatibility
    dt1 = datetime.datetime(1970, 1, 1, 12, 0, 0, 0)
    dt2 = datetime.datetime.utcnow()
    creation_ts = int((dt2 - dt1).total_seconds())

    # create SysdebugTechSupport
    domain = get_domain(handle, domain_ip, domain_name)
    if (domain.available_physical_cnt == str(0)):
        raise UcsCentralValidationException("Domain with IP %s or name %s not registered or "
                                            "lost visibility with ucscentral" % (domain_ip,domain_name))
    else:
        domain_dn = domain.dn

    sysdebug_techsup_file_repo = SysdebugTechSupFileRepository(
        parent_mo_or_dn=domain_dn)
    sys_debug_tech_support_op = SysdebugTechSupportOp(
        parent_mo_or_dn=sysdebug_techsup_file_repo,
        creation_ts=str(creation_ts),
        admin_state=SysdebugTechSupportOpConsts.ADMIN_STATE_START)

    sys_debug_tech_support_cmd_opt = SysdebugTechSupportCmdOpt(
        parent_mo_or_dn=sys_debug_tech_support_op)

    # Parameter Set UCSM
    if ucs_manager:
        sys_debug_tech_support_cmd_opt.major_opt_type = \
            SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_UCSM
    elif ucs_mgmt:
        sys_debug_tech_support_cmd_opt.major_opt_type = \
            SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_UCSM_MGMT
    elif chassis_id is not None:
        if cimc_id is not None:
            sys_debug_tech_support_cmd_opt.chassis_cimc_id = str(cimc_id)
            sys_debug_tech_support_cmd_opt.chassis_id = str(chassis_id)
            sys_debug_tech_support_cmd_opt.major_opt_type = \
                SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_CHASSIS

            if adapter_id is None:
                sys_debug_tech_support_cmd_opt.cimc_adapter_id = \
                    SysdebugTechSupportCmdOptConsts.CIMC_ADAPTER_ID_ALL
            else:
                sys_debug_tech_support_cmd_opt.cimc_adapter_id = \
                    str(adapter_id)
        elif iom_id is not None:
            sys_debug_tech_support_cmd_opt.chassis_iom_id = str(iom_id)
            sys_debug_tech_support_cmd_opt.chassis_id = str(chassis_id)
            sys_debug_tech_support_cmd_opt.major_opt_type = \
                SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_CHASSIS
    elif rack_server_id is not None:
        sys_debug_tech_support_cmd_opt.rack_server_id = str(iom_id)

        if rack_adapter_id is None:
            sys_debug_tech_support_cmd_opt.rack_server_adapter_id = \
                SysdebugTechSupportCmdOptConsts.RACK_SERVER_ADAPTER_ID_ALL
        else:
            sys_debug_tech_support_cmd_opt.rack_server_adapter_id = \
                str(rack_adapter_id)
            sys_debug_tech_support_cmd_opt.major_opt_type = \
                SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_SERVER
    elif fex_id is not None:
        sys_debug_tech_support_cmd_opt.fab_ext_id = str(iom_id)
        sys_debug_tech_support_cmd_opt.major_opt_type = \
            SysdebugTechSupportCmdOptConsts.MAJOR_OPT_TYPE_FEX

    handle.add_mo(sys_debug_tech_support_op)
    handle.commit()

    log.debug("Techsupport creation started")
    # poll for tech support mo to get created
    duration = 60
    poll_interval = 2
    status = False
    filter_str = '(creation_ts, %s, type="eq")' % (str(creation_ts))
    while True:
        sys_debug_tech_supports = handle.query_classid("SysdebugTechSupport",
                filter_str=filter_str,dme="resource-mgr")
        if sys_debug_tech_supports != []:
            status = True
        if status:
            break
        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            handle.remove_mo(sys_debug_tech_support_op)
            handle.commit()
            raise UcsValidationException('TechSupport file creation timed out')

    # poll for tech support mo to complete
    tech_support_dn = sys_debug_tech_supports[0].dn
    duration = timeout_in_sec
    poll_interval = 2
    status = False
    while True:
        tech_support = handle.query_dn(tech_support_dn, dme="resource-mgr")
        if tech_support.oper_state == \
                SysdebugTechSupportConsts.OPER_STATE_AVAILABLE:
            status = True
        if status:
            break
        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            handle.remove_mo(sys_debug_tech_support_op)
            handle.commit()
            handle.remove_mo(tech_support)
            handle.commit(dme="resource-mgr")
            raise UcsValidationException('TechSupport file creation timed out')

    log.debug("Techsupport creation completed")
    return tech_support

