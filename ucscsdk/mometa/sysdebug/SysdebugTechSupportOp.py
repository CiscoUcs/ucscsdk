"""This module contains the general information for SysdebugTechSupportOp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SysdebugTechSupportOpConsts():
    ADMIN_STATE_CREATED = "created"
    ADMIN_STATE_DELETE = "delete"
    ADMIN_STATE_INIT = "init"
    ADMIN_STATE_PREPARE_DOWNLOAD = "prepare-download"
    ADMIN_STATE_START = "start"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class SysdebugTechSupportOp(ManagedObject):
    """This is SysdebugTechSupportOp class."""

    consts = SysdebugTechSupportOpConsts()
    naming_props = set(['creationTS'])

    mo_meta = MoMeta("SysdebugTechSupportOp", "sysdebugTechSupportOp", "remote-oper-[creation_ts]", VersionMeta.Version151a, "InputOutput", 0xff, [], ["admin", "operations"], ['sysdebugTechSupFileRepository'], ['faultInst', 'sysdebugTechSupportCmdOpt'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["created", "delete", "init", "prepare-download", "start"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "creation_ts": MoPropertyMeta("creation_ts", "creationTS", "ulong", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, 1, 128, None, [], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "creationTS": "creation_ts", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "lastModified": "last_modified", 
        "name": "name", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "rn": "rn", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, creation_ts, **kwargs):
        self._dirty_mask = 0
        self.creation_ts = creation_ts
        self.admin_state = None
        self.child_action = None
        self.ep_dn = None
        self.last_modified = None
        self.name = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "SysdebugTechSupportOp", parent_mo_or_dn, **kwargs)

