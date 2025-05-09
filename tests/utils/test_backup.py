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

from ucscsdk.ucschandle import UcscHandle
from ucscsdk.utils.ucscbackup import *
from nose.plugins.attrib import attr
from ..connection.info import custom_setup, custom_teardown, \
    get_local_config_params, get_remote_config_params, \
    get_domain_params, skipped
import os


local_download = get_local_config_params("backup_local_download")
remote_download = get_remote_config_params("backup_remote_download")
local_import = get_local_config_params("config_local_import")
remote_import = get_remote_config_params("config_remote_import")
domain_params = get_domain_params(1)

if local_download is not None:
    local_file_dir = local_download['file_dir']
    local_file_name = local_download['file_name']

if remote_download is not None:
    remote_file_dir = remote_download['file_dir']
    remote_file_name = remote_download['file_name']
    hostname = remote_download['hostname']
    protocol = remote_download['protocol']
    username = remote_download['username']
    password = remote_download['password']
    remote_file_path = os.path.join(remote_file_dir, remote_file_name)

handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)


def test_001_backup_local():
    if local_download is None:
        skipped("Arguments missing in config file")(test_001_backup_local)()
    backup_local(handle, local_file_dir, local_file_name,
                 remove_from_ucsc=True)


def test_002_backup_remote():
    if remote_download is None:
        skipped("Arguments missing in config file")(test_002_backup_remote)()
    backup_remote(handle, remote_file_dir, remote_file_name,
                  hostname=hostname,
                  preserve_pooled_values=False,
                  protocol=protocol,
                  username=username, password=password)


def test_003_backup_domain():
    if remote_download is None or domain_params is None:
        skipped("Arguments missing in config file")(test_003_backup_domain)()
    backup_domain_remote(handle, remote_file_dir,
                         remote_file_name,
                         timeout=240, preserve_pooled_values=False,
                         domain_ip=domain_params[0]['ip'], hostname=hostname,
                         protocol=protocol,
                         username=username, password=password)


def test_004_export_config_local():
    if local_download is None:
        skipped("Arguments missing in config file")(
            test_004_export_config_local)()
    export_config_local(handle, local_file_dir, local_file_name,
                        remove_from_ucsc=True)


def test_005_export_config_remote():
    if remote_download is None:
        skipped("Arguments missing in config file")(
            test_005_export_config_remote)()
    export_config_remote(handle, remote_file_dir, remote_file_name,
                         preserve_pooled_values=False,
                         hostname=hostname,
                         protocol=protocol,
                         username=username,
                         password=password)


def test_006_export_config_domain():
    if remote_download is None or domain_params is None:
        skipped("Arguments missing in config file")(
            test_006_export_config_domain)()
    export_config_domain_remote(handle, remote_file_dir,
                                "backup_config_domain.xml", timeout=120,
                                domain_ip=domain_params[0]['ip'],
                                preserve_pooled_values=False,
                                hostname=hostname,
                                protocol=protocol,
                                username=username,
                                password=password)


@attr('config-disruptive')
def test_007_import_config_from_ucscentral():
    import_config_ucscentral(handle, "all-cfg.tgz")


@attr('config-disruptive')
def test_008_import_config_from_local():
    if local_import is None:
        skipped("Arguments missing in config file")(
            test_008_import_config_from_local)()
    import_config_local(handle, local_import['file_dir'],
                        local_import['file_name'])


@attr('config-disruptive')
def test_009_import_config_from_remote():
    if remote_import is None:
        skipped("Arguments missing in config file")(
            test_009_import_config_from_remote)()
    import_config_remote(handle, remote_import['file_dir'],
                         remote_import['file_name'],
                         hostname=remote_import['hostname'],
                         protocol=remote_import['protocol'],
                         username=remote_import['username'],
                         password=remote_import['password'])


@attr('config-disruptive')
def test_010_import_config_domain():
    if domain_params is None:
        skipped("Arguments missing in config file")(
            test_009_import_config_domain)()
    # Import from UcsCentral for domain
    import_config_domain(handle, to_domain_ip=domain_params[0]['ip'],
                         from_domain_ip=domain_params[1]['ip'],
                         config_file="all-cfg")


def test_011_schedule_backup():
    schedule_backup(handle, max_bkup_files=3)


def test_012_schedule_backup_remote():
    if remote_download is None:
        skipped("Arguments missing in config file")(
            test_012_schedule_backup_remote)()
    schedule_backup(handle, max_bkup_files=4, remote_enabled=True,
                    file_path=remote_file_path,
                    hostname=hostname,
                    protocol=protocol,
                    username=username,
                    password=password)


def test_013_schedule_backup_domain():
    schedule_backup_domain(handle, max_bkup_files=4)


def test_014_schedule_backup_domain_remote():
    if remote_download is None:
        skipped("Arguments missing in config file")(
            test_014_schedule_backup_domain_remote)()
    schedule_backup_domain(handle, max_bkup_files=4, remote_enabled=True,
                           file_path=remote_file_path,
                           hostname=hostname,
                           protocol=protocol,
                           username=username,
                           password=password,
                           domain_group="root")


def test_015_schedule_export_config():
    schedule_export_config(handle, max_bkup_files=4)


def test_016_schedule_export_config_remote():
    if remote_download is None:
        skipped("Arguments missing in config file")(
            test_016_schedule_export_config_remote)()
    schedule_export_config(handle, max_bkup_files=4, remote_enabled=True,
                           file_path=remote_file_path,
                           hostname=hostname, protocol=protocol,
                           username=username, password=password)


def test_017_schedule_export_config_domain():
    schedule_export_config_domain(handle, max_bkup_files=5)


def test_018_schedule_export_config_domain_remote():
    if remote_download is None:
        skipped("Arguments missing in config file")(
            test_018_schedule_export_config_domain_remote)()
    schedule_export_config_domain(handle, max_bkup_files=4,
                                  remote_enabled=True,
                                  file_path=remote_file_path,
                                  hostname=hostname,
                                  protocol=protocol,
                                  username=username, password=password,
                                  domain_group="root")


def test_019_schedule_backup_remove():
    remove_schedule_backup(handle)


def test_020_schedule_export_config_remove():
    remove_schedule_export_config(handle)


def test_021_schedule_backup_domain_remove():
    remove_schedule_backup_domain(handle, domain_group="root")


def test_022_schedule_export_config_domain_remove():
    remove_schedule_export_config_domain(handle, domain_group="root")


def test_023_backup_local_with_file_download(mocker):
    if local_download is None:
        skipped("Arguments missing in config file")(test_023_backup_local_with_file_download)()

    mocker.patch.object(UcscHandle, 'is_local_download_supported', return_stmt=True)

    backup_local(handle, local_file_dir, local_file_name,
                    remove_from_ucsc=True)

    file_name = os.path.join(local_file_dir, local_file_name)

    assert os.path.exists(file_name), f"File {local_file_dir} was not downloaded to {local_file_name}"
