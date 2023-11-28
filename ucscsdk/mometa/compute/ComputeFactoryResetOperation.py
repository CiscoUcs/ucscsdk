"""This module contains the general information for ComputeFactoryResetOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeFactoryResetOperationConsts():
    CREATE_INITIAL_VOLUMES_CREATE_INITIAL_VOLUMES = "create-initial-volumes"
    CREATE_INITIAL_VOLUMES_NO_INIT = "no-init"
    CREATE_INITIAL_VOLUMES_UNKNOWN = "unknown"
    FLEX_STORAGE_SCRUB_NO_SCRUB = "no-scrub"
    FLEX_STORAGE_SCRUB_SCRUB = "scrub"
    FLEX_STORAGE_SCRUB_UNKNOWN = "unknown"
    OPER_STATUS_CIMC_RESET_COMPLETE = "cimc-reset-complete"
    OPER_STATUS_CIMC_RESET_IN_PROGRESS = "cimc-reset-in-progress"
    OPER_STATUS_IDLE = "idle"
    OPER_STATUS_RUNNING = "running"
    OPER_STATUS_SCRUB_STAGE_COMPLETE = "scrub-stage-complete"
    RESET_TRIGGER_CANCELED = "canceled"
    RESET_TRIGGER_IDLE = "idle"
    RESET_TRIGGER_TRIGGERED = "triggered"
    STORAGE_SCRUB_NO_SCRUB = "no-scrub"
    STORAGE_SCRUB_SCRUB = "scrub"
    STORAGE_SCRUB_UNKNOWN = "unknown"


class ComputeFactoryResetOperation(ManagedObject):
    """This is ComputeFactoryResetOperation class."""

    consts = ComputeFactoryResetOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeFactoryResetOperation", "computeFactoryResetOperation", "factory-reset", VersionMeta.Version151a, "InputOutput", 0xff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "create_initial_volumes": MoPropertyMeta("create_initial_volumes", "createInitialVolumes", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["create-initial-volumes", "no-init", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flex_storage_scrub": MoPropertyMeta("flex_storage_scrub", "flexStorageScrub", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["no-scrub", "scrub", "unknown"], []), 
        "oper_status": MoPropertyMeta("oper_status", "operStatus", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cimc-reset-complete", "cimc-reset-in-progress", "idle", "running", "scrub-stage-complete"], []), 
        "reset_trigger": MoPropertyMeta("reset_trigger", "resetTrigger", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["canceled", "idle", "triggered"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_scrub": MoPropertyMeta("storage_scrub", "storageScrub", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["no-scrub", "scrub", "unknown"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "createInitialVolumes": "create_initial_volumes", 
        "dn": "dn", 
        "flexStorageScrub": "flex_storage_scrub", 
        "operStatus": "oper_status", 
        "resetTrigger": "reset_trigger", 
        "rn": "rn", 
        "status": "status", 
        "storageScrub": "storage_scrub", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.create_initial_volumes = None
        self.flex_storage_scrub = None
        self.oper_status = None
        self.reset_trigger = None
        self.status = None
        self.storage_scrub = None

        ManagedObject.__init__(self, "ComputeFactoryResetOperation", parent_mo_or_dn, **kwargs)

