"""This module contains the general information for StorageNvmeStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageNvmeStatsConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    TEMPERATURE_NOT_APPLICABLE = "not-applicable"
    TEMPERATURE_AVG_NOT_APPLICABLE = "not-applicable"
    TEMPERATURE_MAX_NOT_APPLICABLE = "not-applicable"
    TEMPERATURE_MIN_NOT_APPLICABLE = "not-applicable"


class StorageNvmeStats(ManagedObject):
    """This is StorageNvmeStats class."""

    consts = StorageNvmeStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageNvmeStats", "storageNvmeStats", "nvme-stats", VersionMeta.Version201b, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], [u'storageController'], [u'storageNvmeStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "drive_life_used_percentage": MoPropertyMeta("drive_life_used_percentage", "driveLifeUsedPercentage", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "drive_life_used_percentage_avg": MoPropertyMeta("drive_life_used_percentage_avg", "driveLifeUsedPercentageAvg", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "drive_life_used_percentage_max": MoPropertyMeta("drive_life_used_percentage_max", "driveLifeUsedPercentageMax", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "drive_life_used_percentage_min": MoPropertyMeta("drive_life_used_percentage_min", "driveLifeUsedPercentageMin", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "temperature_avg": MoPropertyMeta("temperature_avg", "temperatureAvg", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "temperature_max": MoPropertyMeta("temperature_max", "temperatureMax", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "temperature_min": MoPropertyMeta("temperature_min", "temperatureMin", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "driveLifeUsedPercentage": "drive_life_used_percentage", 
        "driveLifeUsedPercentageAvg": "drive_life_used_percentage_avg", 
        "driveLifeUsedPercentageMax": "drive_life_used_percentage_max", 
        "driveLifeUsedPercentageMin": "drive_life_used_percentage_min", 
        "intervals": "intervals", 
        "normalizedTimeCol": "normalized_time_col", 
        "rn": "rn", 
        "statsReported": "stats_reported", 
        "status": "status", 
        "suspect": "suspect", 
        "temperature": "temperature", 
        "temperatureAvg": "temperature_avg", 
        "temperatureMax": "temperature_max", 
        "temperatureMin": "temperature_min", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.drive_life_used_percentage = None
        self.drive_life_used_percentage_avg = None
        self.drive_life_used_percentage_max = None
        self.drive_life_used_percentage_min = None
        self.intervals = None
        self.normalized_time_col = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.temperature = None
        self.temperature_avg = None
        self.temperature_max = None
        self.temperature_min = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "StorageNvmeStats", parent_mo_or_dn, **kwargs)

