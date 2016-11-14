from ..connection.info import custom_setup, custom_teardown
from ucscsdk.utils.ucscbackup import *
handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


def test_001_backup():
    # Local full_state backup
    backup_local(handle, "/Users/guest/", "backup_full_state.tgz",
                 remove_from_ucsc=True)
    # Remote full_state backup
    backup_remote(handle, "/ws/guest-bgl/", "backup_full_state.tgz",
                  preserve_pooled_values=False, hostname="192.168.1.10",
                  protocol="scp", username="guest", password="password")
    # Domain remote backup
    backup_domain_remote(handle, "/ws/guest-bgl/",
                         "backup_full_state_domain.tgz",
                         timeout=240, preserve_pooled_values=False,
                         domain_ip="10.10.10.1", hostname="192.168.1.10",
                         protocol="scp",
                         username="guest", password="password")


def test_002_export_config():
    export_config_local(handle, "/Users/guest/", "backup_full_state.tgz",
                        remove_from_ucsc=True)
    export_config_remote(handle, "/ws/guest-bgl/", "backup_full_state.tgz",
                         preserve_pooled_values=False, hostname="192.168.1.10",
                         protocol="scp", username="guest", password="password")

    export_config_domain_remote(handle, "/ws/guest-bgl/",
                                "backup_config_domain.xml", timeout=120,
                                domain_ip="10.10.10.1",
                                preserve_pooled_values=False,
                                hostname="192.168.1.10", protocol="scp",
                                username="guest", password="password")


def test_003_import_config():
    # Import from ucsc/local/remote
    import_config_ucscentral(handle, "all-cfg.2.tgz")
    import_config_local(handle, "/Users/guest/Desktop/",
                        "backup_config_all.tgz")
    import_config_remote(handle, "/ws/guest-bgl/", "backup_full_state.tgz",
                         hostname="192.168.1.10", protocol="scp",
                         username="guest", password="password")

    # Import from UcsCentral for domain
    import_config_domain(handle, to_domain_ip="10.10.10.5",
                         from_domain_ip="10.10.10.1", config_file="all-cfg")


def test_004_schedule_backup():
    schedule_backup(handle, max_bkup_files=3)
    schedule_backup(handle, max_bkup_files=4, remote_enabled=True,
                    file_path="/ws/admin/config.tgz", hostname="192.168.1.10",
                    protocol="scp", username="guest", password="password")
    schedule_backup_domain(handle, max_bkup_files=4)
    schedule_backup_domain(handle, max_bkup_files=4, remote_enabled=True,
                           file_path="/ws/admin/config.tgz",
                           hostname="192.168.1.10", protocol="scp",
                           username="guest", password="password",
                           domain_group="root")


def test_005_schedule_export_config():
    # Schedule backup/export-config optional remote_enabled
    schedule_export_config(handle, max_bkup_files=4)
    schedule_export_config(handle, max_bkup_files=4, remote_enabled=True,
                           file_path="/ws/admin/config.tgz",
                           hostname="192.168.1.10", protocol="scp",
                           username="guest", password="password")

    schedule_export_config_domain(handle, max_bkup_files=5)
    schedule_export_config_domain(handle, max_bkup_files=4,
                                  remote_enabled=True,
                                  file_path="/ws/admin/config.tgz",
                                  hostname="192.168.1.10",
                                  protocol="scp",
                                  username="guest", password="password",
                                  domain_group="root")


def test_006_schedule_remove():
    # Remove schedule backup/export-config
    remove_schedule_backup(handle)
    remove_schedule_export_config(handle)
    # Remove schedule backup/export-config for domain
    remove_schedule_backup_domain(handle, domain_group="root")
    remove_schedule_export_config_domain(handle, domain_group="root")
