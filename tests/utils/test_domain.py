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

from nose.tools import *
from ..connection.info import custom_setup, custom_teardown
from ucscsdk.mometa.org.OrgDomainGroup import OrgDomainGroup
from ucscsdk.mometa.compute.ComputeSystemQual import ComputeSystemQual
from ucscsdk.mometa.compute.ComputeOwnerQual import ComputeOwnerQual
handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


@with_setup(setup, teardown)
def test_001_create_domain_group():
    dom_grp_name = "new_test_domgrp"
    mo = OrgDomainGroup(parent_mo_or_dn="domaingroup-root", name=dom_grp_name)
    handle.remove_mo(mo)
    handle.commit()

    handle.add_mo(mo)
    handle.commit()
    found = False
    mo_list = handle.query_classid("orgDomainGroup")
    for i in range(0, len(mo_list)):
        if mo_list[i].name == dom_grp_name:
            found = True
            break

    assert_equal(found, True)
    handle.remove_mo(mo)
    handle.commit()


@with_setup(setup, teardown)
def test_002_create_domain_qual_policy():
    dom_qual_name = "new_dom_qual"
    dom_qual_mo = ComputeSystemQual(
        parent_mo_or_dn="org-root", name="new_dom_qual")
    handle.remove_mo(dom_qual_mo)
    handle.commit()

    handle.add_mo(dom_qual_mo)
    handle.commit()

    owner_name = "admin"
    mo = ComputeOwnerQual(parent_mo_or_dn="org-root/system-qualifier-" +
                          dom_qual_name, name=owner_name, regex="test_*")
    handle.add_mo(mo)
    handle.commit()
    obj = handle.query_dn("org-root/system-qualifier-" +
                          dom_qual_name + "/owner-" + owner_name)
    assert_equal(obj.regex, "test_*")

    handle.remove_mo(dom_qual_mo)
    handle.commit()


@with_setup(setup, teardown)
def test_003_domain_register():
    from ucscsdk.utils.ucscdomain import domain_register
    domain_register(handle, domain_name_or_ip="10.10.10.1",
                    username="guest", password="password")


@with_setup(setup, teardown)
def test_003_domain_status():
    from ucscsdk.utils.ucscdomain import is_domain_registered, \
        get_domain_operational_status
    if is_domain_registered(handle, domain_name_or_ip="10.10.10.1"):
        print(get_domain_operational_status(handle, "10.10.10.1"))


@raises(Exception)
@with_setup(setup, teardown)
def test_004_domain_unregister():
    from ucscsdk.utils.ucscdomain import domain_unregister
    domain_unregister(handle, "10.10.10.5")
