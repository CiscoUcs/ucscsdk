"""This module contains the general information for MgmtBackupOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtBackupOperationConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    PRESERVE_POOLED_VALUES_FALSE = "false"
    PRESERVE_POOLED_VALUES_NO = "no"
    PRESERVE_POOLED_VALUES_TRUE = "true"
    PRESERVE_POOLED_VALUES_YES = "yes"
    PROTO_FTP = "ftp"
    PROTO_HTTP = "http"
    PROTO_NFS_COPY = "nfs-copy"
    PROTO_NONE = "none"
    PROTO_SCP = "scp"
    PROTO_SFTP = "sftp"
    PROTO_TFTP = "tftp"
    REMOTE_BACKUP_OPER_STATE_BACKUP_DELETE = "backup-delete"
    REMOTE_BACKUP_OPER_STATE_BACKUP_NONE = "backup-none"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"
    TYPE_CONFIG_ALL = "config-all"
    TYPE_CONFIG_LOGICAL = "config-logical"
    TYPE_CONFIG_SYSTEM = "config-system"
    TYPE_FULL_STATE = "full-state"


class MgmtBackupOperation(ManagedObject):
    """This is MgmtBackupOperation class."""

    consts = MgmtBackupOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtBackupOperation", "mgmtBackupOperation", "remote-oper", VersionMeta.Version131a, "InputOutput", 0x7fff, [], ["admin"], ['computeSystem'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "post_action": MoPropertyMeta("post_action", "postAction", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "preserve_pooled_values": MoPropertyMeta("preserve_pooled_values", "preservePooledValues", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []), 
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["ftp", "http", "nfs-copy", "none", "scp", "sftp", "tftp"], []), 
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, 0, 64, None, [], []), 
        "remote_backup_oper_state": MoPropertyMeta("remote_backup_oper_state", "remoteBackupOperState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["backup-delete", "backup-none"], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x200, 1, 128, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["config-all", "config-logical", "config-system", "full-state"], []), 
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4000, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "hostname": "hostname", 
        "lastModified": "last_modified", 
        "postAction": "post_action", 
        "preservePooledValues": "preserve_pooled_values", 
        "proto": "proto", 
        "pwd": "pwd", 
        "remoteBackupOperState": "remote_backup_oper_state", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "remoteFile": "remote_file", 
        "rn": "rn", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
        "type": "type", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.hostname = None
        self.last_modified = None
        self.post_action = None
        self.preserve_pooled_values = None
        self.proto = None
        self.pwd = None
        self.remote_backup_oper_state = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.remote_file = None
        self.status = None
        self.trigger_status = None
        self.type = None
        self.user = None

        ManagedObject.__init__(self, "MgmtBackupOperation", parent_mo_or_dn, **kwargs)

