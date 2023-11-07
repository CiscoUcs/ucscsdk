"""This module contains the general information for StorageLocalDiskOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageLocalDiskOperationConsts():
    ADMIN_VIRTUAL_DRIVE_ID_UNSPECIFIED = "unspecified"
    LC_CLEAR_SECURE_DRIVE = "clear-secure-drive"
    LC_CLEAR_SECURE_FOREIGN_CONFIG_DRIVE = "clear-secure-foreign-config-drive"
    LC_DEDICATED_HOT_SPARE = "dedicated-hot-spare"
    LC_ENABLE_SECURITY = "enable-security"
    LC_GLOBAL_HOT_SPARE = "global-hot-spare"
    LC_JBOD = "jbod"
    LC_LED_OFF = "led-off"
    LC_LED_ON = "led-on"
    LC_PREPARE_FOR_REMOVAL = "prepare-for-removal"
    LC_REMOTE_TRIGGER = "remoteTrigger"
    LC_REMOVE_HOT_SPARE = "remove-hot-spare"
    LC_UNCONFIGURED_GOOD = "unconfigured-good"
    LC_UNDO_PREPARE_FOR_REMOVAL = "undo-prepare-for-removal"
    LC_UNLOCK_FOREIGN_DRIVE = "unlock-foreign-drive"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class StorageLocalDiskOperation(ManagedObject):
    """This is StorageLocalDiskOperation class."""

    consts = StorageLocalDiskOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageLocalDiskOperation", "storageLocalDiskOperation", "remote-oper", VersionMeta.Version131a, "InputOutput", 0xff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['storageLocalDisk'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "admin_security_key": MoPropertyMeta("admin_security_key", "adminSecurityKey", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "admin_virtual_drive_id": MoPropertyMeta("admin_virtual_drive_id", "adminVirtualDriveId", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["clear-secure-drive", "clear-secure-foreign-config-drive", "dedicated-hot-spare", "enable-security", "global-hot-spare", "jbod", "led-off", "led-on", "prepare-for-removal", "remoteTrigger", "remove-hot-spare", "unconfigured-good", "undo-prepare-for-removal", "unlock-foreign-drive"], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "adminSecurityKey": "admin_security_key", 
        "adminVirtualDriveId": "admin_virtual_drive_id", 
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
        self.admin_security_key = None
        self.admin_virtual_drive_id = None
        self.child_action = None
        self.last_modified = None
        self.lc = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "StorageLocalDiskOperation", parent_mo_or_dn, **kwargs)

