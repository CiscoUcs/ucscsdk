from ..connection.info import custom_setup, custom_teardown
from ucscsdk.utils.ucscfirmware import *
from ucscsdk import set_log_level
handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


def test_001_get_firmware_bundles():
    # Get Images Library
    bundles = get_firmware_bundles(handle, bundle_type="infrastructure-bundle",
                                   fw_platform="mini")
    bundles = get_firmware_bundles(handle, bundle_type="catalog",
                                   fw_platform="bundle-6300-infra")
    bundles = get_firmware_bundles(handle, bundle_type="infrastructure-bundle")
    bundles = get_firmware_bundles(handle, bundle_type="b-series-bundle")
    failed_dw = get_failed_dw_firmware_bundles(handle)


def test_002_get_cco_images():
    image_list = get_ucsc_cco_image_list(username="guest", password="password")
    set_log_level(logging.ERROR)
    for image in image_list:
        if image.image_name == "ucs-central-bundle.1.2.1d.bin":
            dw_image = image
            break
    get_ucsc_cco_image(image=dw_image, file_dir="/Users/guest/Desktop")


def test_003_add_firmware():
    # Import Firmware Bundle - Local
    firmware_add_local(handle, "/Users/guest/Downloads/",
                       "ucs-k9-bundle-b-series.3.1.1h.B.bin")

    # Import Firmware Bundle - Remote
    firmware_add_remote(handle, file_name="ucs-central-bundle.1.2.1d.bin",
                        remote_path="/ws/guest-bgl/",
                        host_name="192.168.1.10",
                        protocol="scp", username="guest", password="password")


def test_004_remove_firmware():
    # Remove Firmware Bundle
    firmware_remove(handle, image_name="aci-n9000-dk9.11.1.1f.bin")


def test_005_schedule_infra_firmware_update():
    schedule_infra_fw_update(handle, domain_group="root",
                             schedule="2016-08-31T22:33:07",
                             fi_mini_6300_ver="3.1(1j)A",
                             catalog_ver="3.1(1)T")


def test_005_sync_firmware_update():
    sync_firmware_update_from_cisco(handle, cisco_username="guest",
                                    cisco_password="password",
                                    sync_enable=True,
                                    sync_frequencey="on demand",
                                    proxy_enable=True,
                                    proxy_username='ppp',
                                    proxy_name_or_ip="192.168.1.50",
                                    proxy_port="8080")
