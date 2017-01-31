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
from ucscsdk.mometa.ls.LsServer import LsServer
sp_test = None
handle = None


def setup():
    global sp_test
    global handle
    handle = custom_setup()
    org = handle.query_dn("org-root")

    sp_test = LsServer(org, name="test", usr_lbl="TEST")
    handle.add_mo(sp_test, True)
    handle.commit()


def teardown():
    handle.remove_mo(sp_test)
    handle.commit()
    custom_teardown(handle)


@raises(Exception)
def test_001_set_ro_property():
    # This is a read only property
    # Should fail with an exception
    sp_test.oper_state = "up"


def test_002_set_rw_property():
    # This is a read write property.
    # Should happen without any issues
    sp_test.descr = "test_description"


@raises(Exception)
def test_003_set_naming_property():
    # This is a naming property. so, it is create only
    # Should fail with an exception
    sp_test.name = "test1"


def test_004_set_prop_multiple():
    # Setting multiple props of object
    sp_test = handle.query_dn("org-root/ls-test")
    sp_test.set_prop_multiple(usr_lbl= "NEW_LABEL",bios_profile_name="NEW_BIOS")
    handle.add_mo(sp_test, modify_present=True)
    handle.commit()
    sp_test = handle.query_dn("org-root/ls-test")
    assert_equal(sp_test.usr_lbl, "NEW_LABEL")
    assert_equal(sp_test.bios_profile_name, "NEW_BIOS")


def test_005_check_prop_match():
    # Checking multiple props match for existing MO
    sp_test = handle.query_dn("org-root/ls-test")
    sp_test.set_prop_multiple(usr_lbl= "NEW_LABEL",bios_profile_name="NEW_BIOS")
    handle.add_mo(sp_test, modify_present=True)
    handle.commit()
    args = {'usr_lbl' : "NEW_LABEL", 'bios_profile_name' : 'TEST_BIOS'}
    exist = sp_test.check_prop_match(**args)
    assert_equal(exist, False)
    args = {'usr_lbl' : "NEW_LABEL", 'bios_profile_name' : 'NEW_BIOS'}
    exist = sp_test.check_prop_match(**args)
    assert_equal(exist, True)


def test_006_clear_prop():
    # Clearing props for existing MO
    sp_test = handle.query_dn("org-root/ls-test")
    sp_test.set_prop_multiple(usr_lbl= "",bios_profile_name="")
    handle.add_mo(sp_test, modify_present=True)
    handle.commit()
    sp_test = handle.query_dn("org-root/ls-test")
    assert_equal(sp_test.usr_lbl, "")
    assert_equal(sp_test.bios_profile_name, "")
