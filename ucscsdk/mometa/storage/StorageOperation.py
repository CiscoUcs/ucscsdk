"""This module contains the general information for StorageOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageOperationConsts():
    END_TIME_N_A = "N/A"
    NAME_CONSISTENCY_CHECK = "consistency-check"
    NAME_COPYBACK = "copyback"
    NAME_INITIALIZATION = "initialization"
    NAME_PATROL_READ = "patrol-read"
    NAME_REBUILD = "rebuild"
    NAME_RECONSTRUCTION = "reconstruction"
    NAME_RELEARNING = "relearning"
    OPER_STATE_COMPLETED = "completed"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_IN_PROGRESS = "in-progress"
    OPER_STATE_UNKNOWN = "unknown"
    PROGRESS_NOT_APPLICABLE = "not-applicable"
    PROGRESS_UNKNOWN = "unknown"
    START_TIME_N_A = "N/A"


class StorageOperation(ManagedObject):
    """This is StorageOperation class."""

    consts = StorageOperationConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("StorageOperation", "storageOperation", "op-[name]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['storageController', 'storageLocalDisk', 'storageRaidBattery', 'storageVirtualDrive'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "end_time": MoPropertyMeta("end_time", "endTime", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["N/A"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, None, ["consistency-check", "copyback", "initialization", "patrol-read", "rebuild", "reconstruction", "relearning"], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["completed", "failed", "in-progress", "unknown"], []), 
        "progress": MoPropertyMeta("progress", "progress", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable", "unknown"], ["0-101"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "start_time": MoPropertyMeta("start_time", "startTime", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["N/A"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "status_descr": MoPropertyMeta("status_descr", "statusDescr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "endTime": "end_time", 
        "name": "name", 
        "operState": "oper_state", 
        "progress": "progress", 
        "rn": "rn", 
        "startTime": "start_time", 
        "status": "status", 
        "statusDescr": "status_descr", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.end_time = None
        self.oper_state = None
        self.progress = None
        self.start_time = None
        self.status = None
        self.status_descr = None

        ManagedObject.__init__(self, "StorageOperation", parent_mo_or_dn, **kwargs)

