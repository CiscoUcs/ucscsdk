"""This module contains the general information for StorageVirtualDriveOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageVirtualDriveOperationConsts():
    LC_CLEAR_TRANSPORT_READY = "clear-transport-ready"
    LC_DEGRADED = "degraded"
    LC_DELETE = "delete"
    LC_HIDE = "hide"
    LC_OFFLINE = "offline"
    LC_ONLINE = "online"
    LC_REMOTE_TRIGGER = "remoteTrigger"
    LC_RESTORE = "restore"
    LC_SECURE_DRIVE_GROUP = "secure-drive-group"
    LC_TRANSPORT_READY = "transport-ready"
    LC_UNHIDE = "unhide"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class StorageVirtualDriveOperation(ManagedObject):
    """This is StorageVirtualDriveOperation class."""

    consts = StorageVirtualDriveOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageVirtualDriveOperation", "storageVirtualDriveOperation", "remote-oper", VersionMeta.Version131a, "InputOutput", 0x7f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['storageVirtualDrive'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "admin_name": MoPropertyMeta("admin_name", "adminName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["clear-transport-ready", "degraded", "delete", "hide", "offline", "online", "remoteTrigger", "restore", "secure-drive-group", "transport-ready", "unhide"], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "adminName": "admin_name", 
        "childAction": "child_action", 
        "dn": "dn", 
        "lastModified": "last_modified", 
        "lc": "lc", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "rn": "rn", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_name = None
        self.child_action = None
        self.last_modified = None
        self.lc = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "StorageVirtualDriveOperation", parent_mo_or_dn, **kwargs)

