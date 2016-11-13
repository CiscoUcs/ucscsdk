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

import logging
import datetime
from ..ucscexception import UcscValidationException, \
    UcscOperationError

log = logging.getLogger('ucscentral')


def domain_register(handle, domain_name_or_ip,
                    username, password,
                    timeout=2 * 60):
    """
    This method registers Ucs domain to Ucs Central.

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        domain_name_or_ip (str): Domain name or IP
        username(str): User name of the domain
        password(str): Password of the domain

    Returns:
        PolicyControlEpOp object

    Example:
        domain_register(handle, domain_name_or_ip="192.168.1.1",
                        username="admin",password="password")
    """

    from distutils.version import LooseVersion as VERSION
    from ucscsdk.mometa.policy.PolicyControlEpOp import\
        PolicyControlEpOp, PolicyControlEpOpConsts

    if VERSION(handle.get_firmware_version()) < VERSION("1.5"):
        raise UcscOperationError(
                "Domain register",
                "Operation only supported from version 1.5 onwards")

    if is_domain_registered(handle, domain_name_or_ip):
        domain_dn = "holder/domain-ep/control-ep-" + domain_name_or_ip
        domain_register = handle.query_dn(domain_dn)
        log.debug("Domain already registered with Ucs Central")
        return domain_register

    parent_dn = "holder/domain-ep"

    domain_register = PolicyControlEpOp(parent_mo_or_dn=parent_dn,
                                        host_name_or_ip=domain_name_or_ip,
                                        name=username,
                                        password=password)
    domain_register.action_event = \
        PolicyControlEpOpConsts.ACTION_EVENT_REGISTER
    handle.add_mo(domain_register)
    handle.commit()

    start = datetime.datetime.now()
    while not domain_register.registration_state == \
            PolicyControlEpOpConsts.REGISTRATION_STATE_REGISTERED:
        domain_register = handle.query_dn(domain_register.dn)
        if domain_register.registration_state == \
                PolicyControlEpOpConsts.REGISTRATION_STATE_FAILED:
            raise UcscOperationError(
                    "Registration of '%s'" %
                    domain_name_or_ip, "%s" %
                    domain_register.fsm_rmt_inv_err_descr)
        if (datetime.datetime.now() - start).total_seconds() > timeout:
            raise UcscOperationError(
                    "Registration of '%s' " %
                    domain_name_or_ip, "timeout error %s" %
                    domain_register.fsm_rmt_inv_err_descr)

    log.debug("Domain got successfully registered with Ucs Central")
    return domain_register


def is_domain_registered(handle, domain_name_or_ip):
    """
    This method returns Boolean value depending on whether given domain is
    registered with UcsCentral

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        domain_name_or_ip (str): Domain name or IP

    Returns:
        True/False

    Example:
        is_domain_registered(handle, domain_name_or_ip="192.168.1.1")
    """

    from ucscsdk.mometa.policy.PolicyControlEpOp import\
        PolicyControlEpOpConsts

    domain_dn = "holder/domain-ep/control-ep-" + domain_name_or_ip
    domain_register = handle.query_dn(domain_dn)

    if domain_register:
        if domain_register.registration_state == \
                PolicyControlEpOpConsts.REGISTRATION_STATE_REGISTERED:
            return True
        else:
            log.debug("Domain registration is in-progress or has failed")
            return False
    else:
        log.debug("Domain is not registered with UcsCentral")
        return False


def domain_unregister(handle, domain_name_or_ip):
    """
    This method unregisters Ucs domain from Ucs Central.

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        domain_name_or_ip (str): Domain name or IP

    Returns:
        None

    Example:
        domain_unregister(handle, domain_name_or_ip="192.168.1.1")
    """

    from distutils.version import LooseVersion as VERSION
    from ucscsdk.mometa.policy.PolicyControlEpOp import\
        PolicyControlEpOpConsts

    if VERSION(handle.get_firmware_version()) < VERSION("1.5"):
        raise UcscOperationError(
                "Domain unregister",
                "Operation only supported from version 1.5 onwards")

    filter_str = '(host_name_or_ip, %s, type="eq")' % domain_name_or_ip

    domains_registered = handle.query_classid(class_id="PolicyControlEpOp",
                                              filter_str=filter_str)
    if (len(domains_registered) <= 0):
        raise UcscOperationError(
            "Domain unregister",
            "Domain with name or IP %s not registered with UcsCentral"
            % domain_name_or_ip)

    domain_register = domains_registered[0]

    if not _is_domain_available(handle, domain_register.sys_id):
        raise UcscOperationError(
            "Domain unregister",
            "Not able to connect with Domain %s" % domain_name_or_ip)

    domain_register.action_event = \
        PolicyControlEpOpConsts.ACTION_EVENT_UNREGISTER
    handle.set_mo(domain_register)
    handle.commit()

    log.debug("Domain was successfully unregistered from Ucs Central")


def get_domain(handle, domain_ip, domain_name=None):
    """
    This method gets the computeSystem object for the Ucs domain.

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        domain_ip(str): IP of domain, set 'None' if domain_name is valid
        domain_name(str): Optional Domain name, valid only if domain_ip is None

    Returns:
        domain object

    Example:
        get_domain(handle, domain_ip="192.168.1.1", domain_name=" ")
        get_domain(handle, domain_ip=None, domain_name="test-dom")
    """

    if domain_ip:
        filter_str = '(address, %s, type="eq")' % domain_ip
    else:
        filter_str = '(name, %s, type="eq")' % domain_name

    domain = handle.query_classid(
        class_id='ComputeSystem', filter_str=filter_str)

    if (len(domain) <= 0):
        raise UcscOperationError("Get domain",
                                 "Domain with IP %s or name %s "
                                 "does not exist" %
                                 (domain_ip, domain_name))

    return domain[0]


def get_domain_operational_status(handle, domain_ip, domain_name=None):
    """
    This method gets the operational status of the Ucs domain wrt UcsCentral.

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        domain_ip(str): IP of domain, set 'None' if domain_name is valid
        domain_name(str): Optional Domain name, valid only if domain_ip is None

    Returns:
        Operational status of domain

    Example:
        get_domain_operational_status(handle, domain_ip="192.168.1.1")
    """

    domain = get_domain(handle, domain_ip, domain_name)

    if not domain:
        raise UcscOperationError("Get domain operational status",
                                 "Domain with IP %s or name %s "
                                 "does not exist" %
                                 (domain_ip, domain_name))

    extpol_client_dn = "extpol/reg/clients/client-" + domain.id
    extpol_client = handle.query_dn(extpol_client_dn)

    if not extpol_client:
        raise UcscOperationError("Get domain operational status",
                                 "Domain with IP %s or name %s "
                                 "does not exist" %
                                 (domain_ip, domain_name))
    return extpol_client.oper_state


def _is_domain_available(handle, domain_id):
    """
    This internal method returns True if domain is available currently
    else returns False

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        domain_id(str): ID of domain from domain object

    Returns:
        True or False depending on domain's availability

    Example:
        _is_domain_available(handle, domain_id="1008")
    """

    extpol_client_dn = "extpol/reg/clients/client-" + domain_id
    extpol_client = handle.query_dn(extpol_client_dn)

    if (extpol_client and (extpol_client.oper_state == "registered")):
        return True

    return False


def domain_group_create(handle, name,
                        descr="",
                        parent_dn="domaingroup-root"):
    """
    This method creates Domain Group.

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        name (str): Name of the domain group.
        descr (str): Basic description.
        parent_dn (str): Parent org for the domain group

    Returns:
        None

    Example:
        domain_group_create(handle, name="sample_dom_grp")
    """

    from ucscsdk.mometa.org.OrgDomainGroup import\
        OrgDomainGroup

    org = handle.query_dn(parent_dn)
    if not org:
        raise UcscOperationError(
            "Domain group create",
            "org '%s' does not exist" % parent_dn)

    mo = OrgDomainGroup(parent_mo_or_dn=org.dn,
                        name=name,
                        descr=descr)
    handle.add_mo(mo)
    handle.commit()


def get_domain_group_dn(handle, domain_group):
    """
    This utility funciton gets domain_group dn given the domain group name.

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        domain_ip(str): IP of domain, set 'None' if domain_name is valid
        domain_group(string): Full domain_group with root/<org_name>/..
        domain_name(str): Optional Domain name, valid only if domain_ip is None

    Returns:
        domain_group dn, raises Exception if domain group doesn't exist

    Example:
        get_domain_group_dn(handle, domain_group="root/sampleDomGroup")
    """

    domain_org = []
    domain_group_dn_prefix = "domaingroup-"
    orgs = domain_group.split("/")
    for org in orgs:
        domain_org.append(domain_group_dn_prefix + org)

    domain_group_dn = ("/").join(domain_org)
    dn = handle.query_dn(domain_group_dn)

    if not dn:
        raise UcscOperationError("Get domain group dn",
                                 "Domain Group %s doesn't exist" %
                                 domain_group)
    return domain_group_dn


def domain_assign_to_domaingroup(handle, domain_ip,
                                 domain_group, domain_name=None):
    """
    This method registers Domain to UcsCentral.

    Args:
        handle (UcscHandle): UcsCentral Connection handle
        domain_ip(str): IP of domain, set 'None' if domain_name is valid
        domain_group(string): Full domain_group with root/<org_name>/..
        domain_name(str): Optional Domain name, valid only if domain_ip is None

    Returns:
        None

    Example:
        domain_assign_to_domaingroup(handle, domain_ip="192.168.1.1",
                                     domain_group="root/sample_dom_grp")
    """

    from ucscsdk.mometa.compute.ComputeGroupMembership import\
        ComputeGroupMembership

    domain_group_dn = get_domain_group_dn(handle, domain_group)

    compute_class = handle.query_classid(class_id="ComputeResourceAggrEp")
    compute_dn = compute_class[0].dn

    if domain_ip is None:
        if domain_name is None:
            raise UcscValidationException(
                "Provide either valid domain_ip or domain_name")
        else:
            domain = get_domain(handle, domain_ip=None,
                                domain_name=domain_name)
            domain_ip = domain.address

    domain_assign = ComputeGroupMembership(parent_mo_or_dn=compute_dn,
                                           ip=domain_ip,
                                           group_dn=domain_group_dn)
    handle.set_mo(domain_assign)
    handle.commit()

    return domain_assign
