"""This module contains the general information for SysdebugBackupBehavior ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SysdebugBackupBehaviorConsts():
    CLEAR_ON_BACKUP_FALSE = "false"
    CLEAR_ON_BACKUP_NO = "no"
    CLEAR_ON_BACKUP_TRUE = "true"
    CLEAR_ON_BACKUP_YES = "yes"
    FORMAT_ASCII = "ascii"
    FORMAT_BINARY = "binary"
    INTERVAL_1HOUR = "1hour"
    INTERVAL_1MONTH = "1month"
    INTERVAL_1WEEK = "1week"
    INTERVAL_24HOURS = "24hours"
    INTERVAL_2HOURS = "2hours"
    INTERVAL_4HOURS = "4hours"
    INTERVAL_8HOURS = "8hours"
    INTERVAL_NEVER = "never"
    PROTO_FTP = "ftp"
    PROTO_HTTP = "http"
    PROTO_NFS_COPY = "nfs-copy"
    PROTO_NONE = "none"
    PROTO_SCP = "scp"
    PROTO_SFTP = "sftp"
    PROTO_TFTP = "tftp"


class SysdebugBackupBehavior(ManagedObject):
    """This is SysdebugBackupBehavior class."""

    consts = SysdebugBackupBehaviorConsts()
    naming_props = set([])

    mo_meta = MoMeta("SysdebugBackupBehavior", "sysdebugBackupBehavior", "backup", VersionMeta.Version101a, "InputOutput", 0x1fff, [], ["admin", "domain-group-management", "operations"], ['sysdebugMEpLogPolicy'], [], ["Get", "Set"])

    prop_meta = {
        "action": MoPropertyMeta("action", "action", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""((defaultValue|none|log-full|on-clear|timer|on-assoc-change),){0,5}(defaultValue|none|log-full|on-clear|timer|on-assoc-change){0,1}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "clear_on_backup": MoPropertyMeta("clear_on_backup", "clearOnBackup", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["false", "no", "true", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "format": MoPropertyMeta("format", "format", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["ascii", "binary"], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
        "interval": MoPropertyMeta("interval", "interval", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["1hour", "1month", "1week", "24hours", "2hours", "4hours", "8hours", "never"], []), 
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["ftp", "http", "nfs-copy", "none", "scp", "sftp", "tftp"], []), 
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, 0, 64, None, [], []), 
        "remote_path": MoPropertyMeta("remote_path", "remotePath", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, 1, 128, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, None, [], []), 
    }

    prop_map = {
        "action": "action", 
        "childAction": "child_action", 
        "clearOnBackup": "clear_on_backup", 
        "dn": "dn", 
        "format": "format", 
        "hostname": "hostname", 
        "interval": "interval", 
        "proto": "proto", 
        "pwd": "pwd", 
        "remotePath": "remote_path", 
        "rn": "rn", 
        "status": "status", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.action = None
        self.child_action = None
        self.clear_on_backup = None
        self.format = None
        self.hostname = None
        self.interval = None
        self.proto = None
        self.pwd = None
        self.remote_path = None
        self.status = None
        self.user = None

        ManagedObject.__init__(self, "SysdebugBackupBehavior", parent_mo_or_dn, **kwargs)

