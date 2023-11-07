"""This module contains the general information for StorageControllerOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageControllerOperationConsts():
    ADMIN_ACTION_TRIGGER_CANCELED = "canceled"
    ADMIN_ACTION_TRIGGER_IDLE = "idle"
    ADMIN_ACTION_TRIGGER_TRIGGERED = "triggered"
    LC_CLEAR_BOOT_CONFIGURATION = "clear-boot-configuration"
    LC_CLEAR_FOREIGN_CONFIGURATION = "clear-foreign-configuration"
    LC_DISABLE_SECURITY = "disable-security"
    LC_ENABLE_SECURITY = "enable-security"
    LC_IMPORT_FOREIGN_CONFIGURATION = "import-foreign-configuration"
    LC_MODIFY_KEY = "modify-key"
    LC_REMOTE_TRIGGER = "remoteTrigger"
    LC_SKIP_INITIAL_CONFIG = "skip-initial-config"
    LC_UNLOCK_DISK = "unlock-disk"
    LC_UNPIN_CACHE_ALL = "unpin-cache-all"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class StorageControllerOperation(ManagedObject):
    """This is StorageControllerOperation class."""

    consts = StorageControllerOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageControllerOperation", "storageControllerOperation", "remote-oper", VersionMeta.Version131a, "InputOutput", 0xff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['storageController'], ['faultInst'], ["Get"])

    prop_meta = {
        "admin_action_trigger": MoPropertyMeta("admin_action_trigger", "adminActionTrigger", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["canceled", "idle", "triggered"], []), 
        "admin_security_key": MoPropertyMeta("admin_security_key", "adminSecurityKey", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["clear-boot-configuration", "clear-foreign-configuration", "disable-security", "enable-security", "import-foreign-configuration", "modify-key", "remoteTrigger", "skip-initial-config", "unlock-disk", "unpin-cache-all"], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "adminActionTrigger": "admin_action_trigger", 
        "adminSecurityKey": "admin_security_key", 
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
        self.admin_action_trigger = None
        self.admin_security_key = None
        self.child_action = None
        self.last_modified = None
        self.lc = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "StorageControllerOperation", parent_mo_or_dn, **kwargs)

