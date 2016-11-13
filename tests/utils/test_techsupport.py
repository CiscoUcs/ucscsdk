from ..connection.info import custom_setup, custom_teardown
from ucscsdk.utils.ucsctechsupport import *
handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


def test_001_techsupport_operations():

    get_tech_support(handle, file_dir="/Users/guest/Desktop/",
                     file_name="tech_support.tar", remove_from_ucsc=True)
    get_domain_tech_support(handle, domain_ip="10.10.10.1")
