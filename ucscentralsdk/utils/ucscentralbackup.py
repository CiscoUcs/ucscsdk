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
This module contains APIs to facilitate UcsCentral backup and import
"""

import os
import platform
import time
import datetime
import logging
import sys
from ..ucscentralexception import UcsCentralValidationException, UcsCentralWarning

log = logging.getLogger('ucscentral')

def backup_ucscentral(handle, file_dir, file_name, timeout_in_sec=600,
               remote_enabled=False, protocol=None,
               host_name="localhost",username=None, password=None,
               preserve_pooled_values=False,):
    """
    backup_ucscentral helps create and download UcsCentral full-state backup.

    Args:
        handle (UcsCentralHandle): UcsCentral Connection handle
        file_dir (str): directory to download ucs backup file to
        file_name (str): name for the backup file
                         (supported file extension '.tgz')
        timeout_in_sec (number) : time in seconds for which method waits
                              for the backUp file to generate before it exits.
        remote_enabled (boolean): True if Remote backup is enabled
                                  False - by default
        protocol (str): Transfer protocol for remote backup ['ftp','sftp','tftp','scp']
        hostname (str): Hostname/IP for the remote backup
        username (str): Username for remote backup
        password (str): Password for remote backup
        preserve_pooled_values (boolean): True/False,
                                          False - by default

    Example:
        file_dir = "/home/user/backup"\n
        file_name = "config_backup.tgz"\n
        backup_ucscentral(handle, file_dir=test_support, file_name=file_name)\n

        backup_ucscentral(handle, file_dir=test_support, file_name=file_name,
                    remote_enabled=True, protocol='scp',hostname='192.168.1.1',
                    username='admin',password='password')\n

    """
    from ..mometa.mgmt.MgmtBackup import MgmtBackup, MgmtBackupConsts
    from ..mometa.top.TopSystem import TopSystem

    backup_type = "full-state"
    preserve_pooled_values = False

    if not file_dir:
        raise UcsCentralValidationException("Missing file_dir argument")
    if not file_name:
        raise UcsCentralValidationException("Missing file_name argument")

    top_system = TopSystem()

    if remote_enabled:
        if (not file_name.endswith('.tgz')):
            raise UcsCentralValidationException("file_name must be .tgz format")

        file_path = file_dir + file_name
        mgmt_backup = MgmtBackup(parent_mo_or_dn=top_system,
                                 hostname=host_name,
                                 admin_state=MgmtBackupConsts.ADMIN_STATE_ENABLED,
                                 proto=protocol,
                                 type=backup_type,
                                 remote_file=file_path,
                                 user=username,
                                 pwd=password)
    else:
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        file_string = platform.node().lower() \
                    + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "/" + file_string + "_" + backup_type + "_backup.tgz"

        mgmt_backup = MgmtBackup(parent_mo_or_dn=top_system,
                                 hostname=host_name,
                                 admin_state=MgmtBackupConsts.ADMIN_STATE_ENABLED,
                                 proto=MgmtBackupConsts.PROTO_HTTP,
                                 type=backup_type,
                                 remote_file=file_path)

    if preserve_pooled_values:
        mgmt_backup.preserve_pooled_values = \
            MgmtBackupConsts.PRESERVE_POOLED_VALUES_YES
    else:
        mgmt_backup.preserve_pooled_values = \
            MgmtBackupConsts.PRESERVE_POOLED_VALUES_NO

    handle.add_mo(mgmt_backup,modify_present=True)
    handle.commit()

    mgmt_backup = handle.query_dn(dn=mgmt_backup.dn)
    admin_state_temp = mgmt_backup.admin_state
    # Checking for the backup to compete.
    duration = timeout_in_sec
    poll_interval = 2

    log.debug("Starting Backup ")
    while True:
        mgmt_backup = handle.query_dn(dn=mgmt_backup.dn)
        admin_state_temp = mgmt_backup.admin_state

        # Break condition:- if state id disabled then break
        if admin_state_temp == MgmtBackupConsts.ADMIN_STATE_DISABLED:
            break

        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            handle.remove_mo(mgmt_backup)
            handle.commit()
            raise UcsCentralValidationException('backup_ucscentral timed out')

    # download backup
    log.debug("Backup done, starting Download ")

    if not remote_enabled:
        file_source = "backupfile" + file_path
        try:
            handle.file_download(url_suffix=file_source,
                                 file_dir=file_dir,
                                 file_name=file_name)
        except Exception as err:
            UcsCentralValidationException("Download Error.....")
            UcsCentralWarning(str(err))
            handle.remove_mo(mgmt_backup)
            handle.commit()

    # remove backup from ucscentral
    handle.remove_mo(mgmt_backup)
    handle.commit()

def config_export_ucscentral(handle, file_dir, file_name, timeout_in_sec=600,
               remote_enabled=False, protocol=None,
               host_name="localhost",username=None, password=None,
               preserve_pooled_values=False,):
    """
    config_export_ucscentral helps export and download UcsCentral config-all backup.

    Args:
        handle (UcsCentralHandle): UcsCentral Connection handle
        file_dir (str): directory to download ucs backup file to
        file_name (str): name for the backup file
                         (supported file extension are '.tar.gz' and '.xml')
        timeout_in_sec (number) : time in seconds for which method waits
                              for the backUp file to generate before it exits.
        remote_enabled (boolean): True if Remote backup is enabled
                                  False - by default
        protocol (str): Transfer protocol for remote backup ['ftp','sftp','tftp','scp']
        hostname (str): Hostname/IP for the remote backup
        username (str): Username for remote backup
        password (str): Password for remote backup
        preserve_pooled_values (boolean): True/False,
                                            False - by default

    Example:
        file_dir = "/home/user/backup"\n
        file_name = "config_export.tgz"\n
        config_export_ucscentral(handle, file_dir=test_support, file_name=file_name)\n

        config_export_ucscentral(handle, file_dir=test_support, file_name=file_name,
                    remote_enabled=True, protocol='scp',hostname='192.168.1.1',
                    username='admin',password='password')\n

    """
    from ..mometa.mgmt.MgmtDataExporter import MgmtDataExporter, MgmtDataExporterConsts
    from ..mometa.top.TopSystem import TopSystem

    backup_type = "config-all"
    if not file_dir:
        raise UcsCentralValidationException("Missing file_dir argument")
    if not file_name:
        raise UcsCentralValidationException("Missing file_name argument")

    top_system = TopSystem()

    if remote_enabled:
        if (not file_name.endswith('.tgz')):
            raise UcsCentralValidationException("file_name must be .tgz format")

        file_path = file_dir + file_name
        mgmt_export = MgmtDataExporter(parent_mo_or_dn=top_system,
                                 hostname=host_name,
                                 admin_state=MgmtDataExporterConsts.ADMIN_STATE_ENABLED,
                                 proto=protocol,
                                 type=backup_type,
                                 remote_file=file_path,
                                 user=username,
                                 pwd=password)
    else:
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        file_string = platform.node().lower() \
            + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "/" + file_string + "_" + backup_type + "_backup.tgz"

        mgmt_export = MgmtDataExporter(parent_mo_or_dn=top_system,
                                 hostname=host_name,
                                 admin_state=MgmtDataExporterConsts.ADMIN_STATE_ENABLED,
                                 proto=MgmtDataExporterConsts.PROTO_HTTP,
                                 type=backup_type,
                                 remote_file=file_path)

    if preserve_pooled_values:
        mgmt_export.preserve_pooled_values = \
            MgmtDataExporterConsts.PRESERVE_POOLED_VALUES_YES
    else:
        mgmt_export.preserve_pooled_values = \
            MgmtDataExporterConsts.PRESERVE_POOLED_VALUES_NO

    handle.add_mo(mgmt_export,modify_present=True)
    handle.commit()

    mgmt_export = handle.query_dn(dn=mgmt_export.dn)
    admin_state_temp = mgmt_export.admin_state
    log.debug("Starting config export ")
    # Checking for the backup to compete.
    duration = timeout_in_sec
    poll_interval = 2

    while True:
        mgmt_export = handle.query_dn(dn=mgmt_export.dn)
        admin_state_temp = mgmt_export.admin_state

        # Break condition:- if state id disabled then break
        if admin_state_temp == MgmtDataExporterConsts.ADMIN_STATE_DISABLED:
            break

        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            handle.remove_mo(mgmt_export)
            handle.commit()
            raise UcsCentralValidationException('config_export_ucscentral timed out')

    # download backup
    log.debug("Config exported, now Downloading")

    if not remote_enabled:
        file_source = "backupfile" + file_path
        try:
            handle.file_download(url_suffix=file_source,
                                 file_dir=file_dir,
                                 file_name=file_name)
        except Exception as err:
            UcsCentralValidationException("Download Error.....")
            UcsCentralWarning(str(err))
            handle.remove_mo(mgmt_backup)
            handle.commit()

    # remove backup from ucs
    handle.remove_mo(mgmt_export)
    handle.commit()

def _fail_and_remove_domain_backup(handle, backup_status_mo, err):
    if backup_status_mo:
        handle.remove_mo(backup_status_mo)
        handle.commit(dme="resource-mgr")
    raise UcsCentralValidationException(err)

def _backup_or_configexport_domain(handle, backup_type, file_dir, file_name, domain_ip, domain_name, host_name,
        preserve_pooled_values, protocol, username, password, timeout_in_sec):

    """
    This internal function helps create domain full_state backup or export config to remote location
    Note: This is internal function, should use either backup_domain or backup_config_export
    Args:
        handle (UcsCentralHandle): UcsCentral Connection handle
        file_dir (str): directory to download ucs backup file to
        file_name (str): name for the backup file
                         (supported file extension is '.tgz')
        backup_type (str): Either full-state or config-all.
        timeout_in_sec (number) : time in seconds for which method waits
                              for the backUp file to generate before it exits.
        domain_ip(str): IP of domain, it can be 'None' if valid domain_name is provided
        domain_name(str): Domain name, valid only if domain_ip is None
        protocol (str): Transfer protocol for remote backup ['ftp','sftp','tftp','scp']
        hostname (str): Hostname/IP for the remote backup
        username (str): Username for remote backup
        password (str): Password for remote backup
        preserve_pooled_values (boolean): True/False,
                                          False - by default

    """
    from ..mometa.mgmt.MgmtBackupOperation import MgmtBackupOperation, MgmtBackupOperationConsts
    from ..mometa.mgmt.MgmtBackup import MgmtBackup, MgmtBackupConsts
    from .ucscentraldomain import get_domain

    preserve_pooled_values = False

    if not file_dir:
        raise UcsCentralValidationException("Missing file_dir argument")
    if not file_name:
        raise UcsCentralValidationException("Missing file_name argument")
    if not domain_ip:
        raise UcsCentralValidationException("Missing domain_ip argument")

    if backup_type == 'full-state':
        if (not file_name.endswith('.tgz')):
            raise UcsCentralValidationException("file_name must be .tgz format")
    elif backup_type == 'config-all':
        if (not file_name.endswith('.xml')):
            raise UcsCentralValidationException("file_name must be .xml format")

    domain = get_domain(handle, domain_ip, domain_name)
    if (domain.available_physical_cnt == str(0)):
        raise UcsCentralValidationException("Domain with IP %s or name %s not registered or "
                                            "lost visibility with ucscentral" % (domain_ip,domain_name))
    else:
        domain_dn = domain.dn

    file_path = file_dir + file_name

    mgmt_backup = MgmtBackupOperation(parent_mo_or_dn=domain_dn,
                             hostname=host_name,
                             admin_state=MgmtBackupOperationConsts.ADMIN_STATE_ENABLED,
                             proto=protocol,
                             type=backup_type,
                             remote_file=file_path,
                             user=username,
                             pwd=password)
    if preserve_pooled_values:
        mgmt_backup.preserve_pooled_values = \
            MgmtBackupOperationConsts.PRESERVE_POOLED_VALUES_YES
    else:
        mgmt_backup.preserve_pooled_values = \
            MgmtBackupOperationConsts.PRESERVE_POOLED_VALUES_NO

    handle.set_mo(mgmt_backup)
    handle.commit()

    log.debug("Triggering Domain Backup ")
    duration = 30
    poll_interval = 2
    backup_status_dn = "extpol/reg/clients/client-"  + domain.id + "/backup-" + host_name
    while True:
        backup_status = handle.query_dn(dn=backup_status_dn, dme="resource-mgr")
        if backup_status != None:
            break

        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            raise UcsCentralValidationException('Backup or config export of domain not triggered')

    log.debug("Domain Backup Triggered")

    # Checking for the backup to become available.
    log.debug("Waiting for Domain Backup to become available")
    duration = timeout_in_sec
    poll_interval = 5

    while True:
        backup_status = handle.query_dn(backup_status_dn, dme="resource-mgr")
        if backup_status.over_all_status == \
                MgmtBackupConsts.OVER_ALL_STATUS_ALL_SUCCESS:
            break
        if backup_status.over_all_status != MgmtBackupConsts.OVER_ALL_STATUS_WORK_IN_PROGRESS:
            _fail_and_remove_domain_backup(handle, backup_status, 'Domain backup failed')
        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration - poll_interval))
        if duration == 0:
            _fail_and_remove_domain_backup(handle, backup_status, 'Domain backup timed out')

    log.debug("Domain backup is available")

def backup_domain(handle, file_dir, file_name,
               domain_ip,  protocol, host_name,
               username, password,
               domain_name= None,preserve_pooled_values=False, timeout_in_sec=600):
    """
    backup_domain  helps create domain full_state backup and download it to remote location.
    Note: Domain backup will always be remote backup
    Args:
        handle (UcsCentralHandle): UcsCentral Connection handle
        file_dir (str): directory to download ucs backup file to
        file_name (str): name for the backup file
                         (supported file extension is '.tgz')
        timeout_in_sec (number) : time in seconds for which method waits
                              for the backUp file to generate before it exits.
        domain_ip(str): IP of domain, it can be 'None' if valid domain_name is provided
        domain_name(str): Domain name, valid only if domain_ip is None
        protocol (str): Transfer protocol for remote backup ['ftp','sftp','tftp','scp']
        hostname (str): Hostname/IP for the remote backup
        username (str): Username for remote backup
        password (str): Password for remote backup
        preserve_pooled_values (boolean): True/False,
                                          False - by default

    Example:
        file_dir = "/home/user/backup"\n
        file_name = "config_backup.tgz"\n

        backup_domain(handle, file_dir=test_support, file_name=file_name,
                    domain_ip='10.10.10.1', protocol='scp',hostname='192.168.1.1',
                    username='admin',password='password')\n

    """
    backup_type = "full-state"
    return _backup_or_configexport_domain(handle, backup_type, file_dir, file_name, domain_ip, domain_name, host_name,
            preserve_pooled_values, protocol, username, password, timeout_in_sec)

def config_export_domain(handle, file_dir, file_name,
               domain_ip, host_name,  protocol,
               username, password,
               domain_name=None,preserve_pooled_values=False, timeout_in_sec=600):
    """
    config_export_domain helps create domain config export and download it to remote location.
    Note: Domain config export will always be remote export

    Args:
        handle (UcsCentralHandle): UcsCentral Connection handle
        file_dir (str): directory to download ucs backup file to
        file_name (str): name for the backup file
                         (supported file extension is '.tgz')
        timeout_in_sec (number) : time in seconds for which method waits
                              for the backUp file to generate before it exits.
        domain_ip(str): IP of domain, it can be 'None' if valid domain_name is provided
        domain_name(str): Domain name, valid only if domain_ip is None
        protocol (str): Transfer protocol for remote backup ['ftp','sftp','tftp','scp']
        hostname (str): Hostname/IP for the remote backup
        username (str): Username for remote backup
        password (str): Password for remote backup
        preserve_pooled_values (boolean): True/False,
                                          False - by default

    Example:
        file_dir = "/home/user/backup"\n
        file_name = "config_backup.xml"\n
        config_export_domain(handle, file_dir=test_support, file_name=file_name,
                    username='admin',password='password')\n
                    domain_ip='10.10.10.1', protocol='scp',hostname='192.168.1.1',
    """
    backup_type = "config-all"
    return _backup_or_configexport_domain(handle, backup_type, file_dir, file_name, domain_ip, domain_name, host_name,
            preserve_pooled_values, protocol, username, password, timeout_in_sec)

def config_import_ucscentral(handle, file_dir, file_name, merge=False,
               remote_enabled=False, protocol=None, host_name="localhost",
               username=None, password=None):
    """
    This operation uploads a UcsCentral config export taken earlier via GUI
    or config_export_ucscentral operation. User can perform an import while the
    system is up and running.

    Args:
        handle (UcsCentralHandle): connection handle
        file_dir (str): directory containing ucs backup file
        file_name (str): backup file name to be imported
        merge (boolean): True/False, specifies whether to merge the backup
                        configuration with the existing UCS Central configuration

        remote_enabled (boolean): True if Remote import is enabled
                                  False - by default
        protocol (str): Transfer protocol for remote import ['ftp','sftp','tftp','scp']
        hostname (str): Hostname/IP for the remote import
        username (str): Username for remote import
        password (str): Password for remote import

    Example:
        file_dir = "/home/user/backup"\n
        file_name = "config_export.tgz"\n
        config_import_ucscentral(handle, file_dir=test_support, file_name=file_name, merge=True)\n

        config_import_ucscentral(handle, file_dir=test_support, file_name=file_name,
                    remote_enabled=True, protocol='scp',hostname='192.168.1.1',
                    username='admin',password='password')\n

    """

    from ..mometa.top.TopSystem import TopSystem
    from ..mometa.mgmt.MgmtDataImporter import MgmtDataImporter, MgmtDataImporterConsts

    if not file_dir:
        raise UcsCentralValidationException("Missing file_dir argument")
    if not file_name:
        raise UcsCentralValidationException("Missing file_name argument")

    file_path = os.path.join(file_dir, file_name)

    if (not file_name.endswith('.tgz')):
        raise UcsCentralValidationException("file_name must be .tgz format")

    top_system = TopSystem()
    if remote_enabled == True:

        mgmt_importer = MgmtDataImporter(
            parent_mo_or_dn=top_system,
            hostname=host_name,
            remote_file=file_path,
            proto=protocol,
            user=username,
            pwd=password,
            admin_state=MgmtDataImporterConsts.ADMIN_STATE_ENABLED)
    else:
        if not os.path.exists(file_path):
            raise UcsCentralValidationException("Backup File not found <%s>" %
                                                 file_path)
        mgmt_importer = MgmtDataImporter(
            parent_mo_or_dn=top_system,
            hostname=host_name,
            remote_file='/'+ file_name,
            proto=MgmtDataImporterConsts.PROTO_HTTP,
            admin_state=MgmtDataImporterConsts.ADMIN_STATE_ENABLED)

    if merge:
        mgmt_importer.action = MgmtDataImporterConsts.ACTION_MERGE
    else:
        mgmt_importer.action = MgmtDataImporterConsts.ACTION_REPLACE

    if remote_enabled != True:
        uri_suffix = "operations/file-%s/importconfig.txt?Cookie=%s" % (file_name, handle.cookie)
        handle.file_upload(url_suffix=uri_suffix,
                           file_dir=file_dir,
                           file_name=file_name)

    handle.add_mo(mgmt_importer,modify_present=True)
    handle.commit()

    return mgmt_importer

