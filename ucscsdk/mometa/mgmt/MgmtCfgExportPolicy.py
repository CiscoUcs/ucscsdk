"""This module contains the general information for MgmtCfgExportPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtCfgExportPolicyConsts():
    ADMIN_STATE_DISABLE = "disable"
    ADMIN_STATE_ENABLE = "enable"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PROTO_FTP = "ftp"
    PROTO_HTTP = "http"
    PROTO_NFS_COPY = "nfs-copy"
    PROTO_NONE = "none"
    PROTO_SCP = "scp"
    PROTO_SFTP = "sftp"
    PROTO_TFTP = "tftp"
    SCHEDULE_1DAY = "1day"
    SCHEDULE_1WEEK = "1week"
    SCHEDULE_2WEEK = "2week"
    SCHEDULE_STATUS_NOT_FOUND = "not-found"
    SCHEDULE_STATUS_UNKNOWN = "unknown"


class MgmtCfgExportPolicy(ManagedObject):
    """This is MgmtCfgExportPolicy class."""

    consts = MgmtCfgExportPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("MgmtCfgExportPolicy", "mgmtCfgExportPolicy", "cfg-exp-policy-[name]", VersionMeta.Version101a, "InputOutput", 0x7fff, [], ["admin", "operations"], ['orgDomainGroup', 'orgOrg', 'policyDeviceProfile'], ['faultInst', 'mgmtBackupTrigger'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disable", "enable"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "host": MoPropertyMeta("host", "host", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""^$|^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "last_backup": MoPropertyMeta("last_backup", "lastBackup", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "last_enabled_ts": MoPropertyMeta("last_enabled_ts", "lastEnabledTs", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "max_files": MoPropertyMeta("max_files", "maxFiles", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-1023"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["ftp", "http", "nfs-copy", "none", "scp", "sftp", "tftp"], []), 
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, 0, 64, None, [], []), 
        "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, 1, 128, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []), 
        "sched_name": MoPropertyMeta("sched_name", "schedName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "schedule": MoPropertyMeta("schedule", "schedule", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["1day", "1week", "2week"], []), 
        "schedule_status": MoPropertyMeta("schedule_status", "scheduleStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-found", "unknown"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4000, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "host": "host", 
        "intId": "int_id", 
        "lastBackup": "last_backup", 
        "lastEnabledTs": "last_enabled_ts", 
        "maxFiles": "max_files", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "proto": "proto", 
        "pwd": "pwd", 
        "remoteFile": "remote_file", 
        "rn": "rn", 
        "schedName": "sched_name", 
        "schedule": "schedule", 
        "scheduleStatus": "schedule_status", 
        "status": "status", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.host = None
        self.int_id = None
        self.last_backup = None
        self.last_enabled_ts = None
        self.max_files = None
        self.policy_level = None
        self.policy_owner = None
        self.proto = None
        self.pwd = None
        self.remote_file = None
        self.sched_name = None
        self.schedule = None
        self.schedule_status = None
        self.status = None
        self.user = None

        ManagedObject.__init__(self, "MgmtCfgExportPolicy", parent_mo_or_dn, **kwargs)

