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
import os
import sys
import time
import datetime
from ..ucscentralexception import UcsCentralValidationException, UcsCentralWarning

def domain_register_to_ucscentral(handle, domain_name_or_ip, 
                         username, password,
                         timeout = 2*60):
    """
    This method registers Ucs domain to Ucs Central.

    Args:
        handle (UcsCentralHandle): UcsCentral Connection handle
        domain_name_or_ip (str): Domain name or IP
        username(str): User name of the domain
        password(str): Password of the domain

    Returns:
        domain_register object 

    Example:
        domain_register_to_ucscentral(handle, domain_name_or_ip="192.168.1.1", 
                                username="admin",password="password")
    """

    from ucscentralsdk.mometa.policy.PolicyControlEpOp import\
        PolicyControlEpOp, PolicyControlEpOpConsts

    parent_dn = "holder/domain-ep"

    domain_register = PolicyControlEpOp(parent_mo_or_dn=parent_dn,
                                 host_name_or_ip = domain_name_or_ip,
                                 name=username,
                                 password=password)
    domain_register.action_event = PolicyControlEpOpConsts.ACTION_EVENT_REGISTER 
    handle.add_mo(domain_register, modify_present=True)
    handle.commit()

    start = datetime.datetime.now()
    while not domain_register.registration_state == PolicyControlEpOpConsts.REGISTRATION_STATE_REGISTERED:
        domain_register = handle.query_dn(domain_register.dn)
        if domain_register.registration_state == PolicyControlEpOpConsts.REGISTRATION_STATE_FAILED:
            raise UcsCentralValidationException("Registration of '%s' failed. Error: %s" %
				(domain_name_or_ip, domain_register.fsm_rmt_inv_err_descr))
        if (datetime.datetime.now() - start).total_seconds() > timeout:
            raise UcsCentralValidationException("Registration of '%s' timed out, Error: %s" %  
                                (domain_name_or_ip, domain_register.fsm_rmt_inv_err_descr))

    return domain_register

def get_domain(handle, domain_ip, domain_name=None):
    """
    This method gets the DN for the Ucs domain.

    Args:
        handle (UcsCentralHandle): UcsCentral Connection handle
        domain_ip(str): IP of domain, it can be 'None' if valid domain_name is provided
        domain_name(str): Optional Domain name, valid only if domain_ip is None

    Returns:
        domain object

    Example:
        get_domain_dn(handle, domain_ip="192.168.1.1", domain_name=" ") 
        get_domain_dn(handle, domain_ip=None, domain_name="test-dom") 
    """

    if domain_ip:
        filter_str = '(address, %s, type="eq")' % domain_ip
    else:
        filter_str = '(name, %s, type="eq")' % domain_name

    domain = handle.query_classid(class_id='ComputeSystem', filter_str=filter_str)

    if ((len(domain) != 1)):
        raise UcsCentralValidationException("Domain with IP %s or name %s does not exist" % 
                                            (domain_ip,domain_name))
    
    return domain[0]    

def domain_group_create(handle, name, 
                         descr="",
                         parent_dn="domaingroup-root"):
    """
    This method creates Domain Group.

    Args:
        handle (UcsCentralHandle): UcsCentral Connection handle
        name (str): Name of the domain group.
        descr (str): Basic description.
        parent_dn (str): Parent org for the domain group

    Returns:
        None

    Example:
        domain_group_create(handle, name="sample_dom_grp")
    """

    from ucscentralsdk.mometa.org.OrgDomainGroup import\
        OrgDomainGroup

    org = handle.query_dn(parent_dn)
    if not org:
        raise UcsCentralValidationException("org '%s' does not exist" % parent_dn)

    mo = OrgDomainGroup(parent_mo_or_dn=org.dn,
                                 name=name,
                                 descr=descr)
    handle.add_mo(mo)
    handle.commit()

def get_domain_group_dn(handle, domain_group):

    """
    This utility funciton gets domain_group dn given the domain group name.

    Args:
        handle (UcsCentralHandle): UcsCentral Connection handle
        domain_ip(str): IP of domain, it can be 'None' if valid domain_name is provided
        domain_group(string): Full domain_group with root/<org_name>/<sub-org_name>..
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
        domain_org.append(domain_group_dn_prefix+org)

    domain_group_dn = ("/").join(domain_org)
    dn = handle.query_dn(domain_group_dn)

    if not dn:
        raise UcsCentralValidationException("Domain Group %s doesn't exist" %
                            domain_group)
    return domain_group_dn

def domain_assign_to_domaingroup(handle, domain_ip, 
                                domain_group, domain_name=None):
    """
    This method registers Domain to ucscentral.

    Args:
        handle (UcsCentralHandle): UcsCentral Connection handle
        domain_ip(str): IP of domain, it can be 'None' if valid domain_name is provided
        domain_group(string): Full domain_group with root/<org_name>/<sub-org_name>..
        domain_name(str): Optional Domain name, valid only if domain_ip is None

    Returns:
        None

    Example:
        domain_assign_to_domaingroup(handle, name="sample_dom_grp")
    """

    from ucscentralsdk.mometa.compute.ComputeGroupMembership import\
        ComputeGroupMembership

    domain_group_dn = get_domain_group_dn(handle, domain_group)

    compute_class = handle.query_classid(class_id="ComputeResourceAggrEp")
    compute_dn = compute_class[0].dn
    
    if domain_ip == None:
        if domain_name == None:
            raise UcsCentralValidationException("Provide either valid domain_ip or domain_name")
        else:
            domain = get_domain(handle, domain_ip=None, domain_name=domain_name)
            domain_ip = domain.address

    domain_assign = ComputeGroupMembership(parent_mo_or_dn = compute_dn,
                                        ip = domain_ip, group_dn = domain_group_dn)
    handle.set_mo(domain_assign)
    handle.commit()

    return domain_assign

