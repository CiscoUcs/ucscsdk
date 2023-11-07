"""This module contains the general information for ComputeFactoryResetOp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeFactoryResetOpConsts():
    CREATE_INITIAL_VOLUMES_CREATE_INITIAL_VOLUMES = "create-initial-volumes"
    CREATE_INITIAL_VOLUMES_NO_INIT = "no-init"
    CREATE_INITIAL_VOLUMES_UNKNOWN = "unknown"
    FLEX_STORAGE_SCRUB_NO_SCRUB = "no-scrub"
    FLEX_STORAGE_SCRUB_SCRUB = "scrub"
    FLEX_STORAGE_SCRUB_UNKNOWN = "unknown"
    RESET_TRIGGER_CANCELED = "canceled"
    RESET_TRIGGER_IDLE = "idle"
    RESET_TRIGGER_TRIGGERED = "triggered"
    STORAGE_SCRUB_NO_SCRUB = "no-scrub"
    STORAGE_SCRUB_SCRUB = "scrub"
    STORAGE_SCRUB_UNKNOWN = "unknown"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class ComputeFactoryResetOp(ManagedObject):
    """This is ComputeFactoryResetOp class."""

    consts = ComputeFactoryResetOpConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeFactoryResetOp", "computeFactoryResetOp", "factory-reset-remote-oper", VersionMeta.Version201b, "InputOutput", 0x1ff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], ['faultInst'], ["get", "set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "create_initial_volumes": MoPropertyMeta("create_initial_volumes", "createInitialVolumes", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["create-initial-volumes", "no-init", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flex_storage_scrub": MoPropertyMeta("flex_storage_scrub", "flexStorageScrub", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["no-scrub", "scrub", "unknown"], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "reset_trigger": MoPropertyMeta("reset_trigger", "resetTrigger", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["canceled", "idle", "triggered"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_scrub": MoPropertyMeta("storage_scrub", "storageScrub", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["no-scrub", "scrub", "unknown"], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "createInitialVolumes": "create_initial_volumes", 
        "dn": "dn", 
        "flexStorageScrub": "flex_storage_scrub", 
        "lastModified": "last_modified", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "resetTrigger": "reset_trigger", 
        "rn": "rn", 
        "status": "status", 
        "storageScrub": "storage_scrub", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.create_initial_volumes = None
        self.flex_storage_scrub = None
        self.last_modified = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.reset_trigger = None
        self.status = None
        self.storage_scrub = None
        self.trigger_status = None

        ManagedObject.__init__(self, "ComputeFactoryResetOp", parent_mo_or_dn, **kwargs)

