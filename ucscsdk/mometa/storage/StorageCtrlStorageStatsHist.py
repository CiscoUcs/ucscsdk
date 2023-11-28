"""This module contains the general information for StorageCtrlStorageStatsHist ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageCtrlStorageStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class StorageCtrlStorageStatsHist(ManagedObject):
    """This is StorageCtrlStorageStatsHist class."""

    consts = StorageCtrlStorageStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageCtrlStorageStatsHist", "storageCtrlStorageStatsHist", "[id]", VersionMeta.Version131a, "OutputOnly", 0xf, [], ["read-only"], ['storageCtrlStorageStats'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cpu_load": MoPropertyMeta("cpu_load", "cpuLoad", "float", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "cpu_load_avg": MoPropertyMeta("cpu_load_avg", "cpuLoadAvg", "float", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "cpu_load_max": MoPropertyMeta("cpu_load_max", "cpuLoadMax", "float", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "cpu_load_min": MoPropertyMeta("cpu_load_min", "cpuLoadMin", "float", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version131a, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "memory_usage": MoPropertyMeta("memory_usage", "memoryUsage", "float", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "memory_usage_avg": MoPropertyMeta("memory_usage_avg", "memoryUsageAvg", "float", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "memory_usage_max": MoPropertyMeta("memory_usage_max", "memoryUsageMax", "float", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "memory_usage_min": MoPropertyMeta("memory_usage_min", "memoryUsageMin", "float", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "cpuLoad": "cpu_load", 
        "cpuLoadAvg": "cpu_load_avg", 
        "cpuLoadMax": "cpu_load_max", 
        "cpuLoadMin": "cpu_load_min", 
        "dn": "dn", 
        "id": "id", 
        "memoryUsage": "memory_usage", 
        "memoryUsageAvg": "memory_usage_avg", 
        "memoryUsageMax": "memory_usage_max", 
        "memoryUsageMin": "memory_usage_min", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.cpu_load = None
        self.cpu_load_avg = None
        self.cpu_load_max = None
        self.cpu_load_min = None
        self.memory_usage = None
        self.memory_usage_avg = None
        self.memory_usage_max = None
        self.memory_usage_min = None
        self.most_recent = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "StorageCtrlStorageStatsHist", parent_mo_or_dn, **kwargs)

