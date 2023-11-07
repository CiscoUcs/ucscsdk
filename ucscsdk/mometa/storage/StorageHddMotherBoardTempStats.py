"""This module contains the general information for StorageHddMotherBoardTempStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageHddMotherBoardTempStatsConsts():
    LEFT_INLET_TEMP_NOT_APPLICABLE = "not-applicable"
    LEFT_INLET_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    LEFT_INLET_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    LEFT_INLET_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    LEFT_OUTLET_TEMP_NOT_APPLICABLE = "not-applicable"
    LEFT_OUTLET_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    LEFT_OUTLET_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    LEFT_OUTLET_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    RIGHT_INLET_TEMP_NOT_APPLICABLE = "not-applicable"
    RIGHT_INLET_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    RIGHT_INLET_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    RIGHT_INLET_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    RIGHT_OUTLET_TEMP_NOT_APPLICABLE = "not-applicable"
    RIGHT_OUTLET_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    RIGHT_OUTLET_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    RIGHT_OUTLET_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class StorageHddMotherBoardTempStats(ManagedObject):
    """This is StorageHddMotherBoardTempStats class."""

    consts = StorageHddMotherBoardTempStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageHddMotherBoardTempStats", "storageHddMotherBoardTempStats", "hdd-mobo-temp-stats", VersionMeta.Version151a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], [], ['storageHddMotherBoardTempStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "left_inlet_temp": MoPropertyMeta("left_inlet_temp", "leftInletTemp", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_inlet_temp_avg": MoPropertyMeta("left_inlet_temp_avg", "leftInletTempAvg", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_inlet_temp_max": MoPropertyMeta("left_inlet_temp_max", "leftInletTempMax", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_inlet_temp_min": MoPropertyMeta("left_inlet_temp_min", "leftInletTempMin", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_outlet_temp": MoPropertyMeta("left_outlet_temp", "leftOutletTemp", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_outlet_temp_avg": MoPropertyMeta("left_outlet_temp_avg", "leftOutletTempAvg", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_outlet_temp_max": MoPropertyMeta("left_outlet_temp_max", "leftOutletTempMax", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_outlet_temp_min": MoPropertyMeta("left_outlet_temp_min", "leftOutletTempMin", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "right_inlet_temp": MoPropertyMeta("right_inlet_temp", "rightInletTemp", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_inlet_temp_avg": MoPropertyMeta("right_inlet_temp_avg", "rightInletTempAvg", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_inlet_temp_max": MoPropertyMeta("right_inlet_temp_max", "rightInletTempMax", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_inlet_temp_min": MoPropertyMeta("right_inlet_temp_min", "rightInletTempMin", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_outlet_temp": MoPropertyMeta("right_outlet_temp", "rightOutletTemp", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_outlet_temp_avg": MoPropertyMeta("right_outlet_temp_avg", "rightOutletTempAvg", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_outlet_temp_max": MoPropertyMeta("right_outlet_temp_max", "rightOutletTempMax", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_outlet_temp_min": MoPropertyMeta("right_outlet_temp_min", "rightOutletTempMin", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "leftInletTemp": "left_inlet_temp", 
        "leftInletTempAvg": "left_inlet_temp_avg", 
        "leftInletTempMax": "left_inlet_temp_max", 
        "leftInletTempMin": "left_inlet_temp_min", 
        "leftOutletTemp": "left_outlet_temp", 
        "leftOutletTempAvg": "left_outlet_temp_avg", 
        "leftOutletTempMax": "left_outlet_temp_max", 
        "leftOutletTempMin": "left_outlet_temp_min", 
        "normalizedTimeCol": "normalized_time_col", 
        "rightInletTemp": "right_inlet_temp", 
        "rightInletTempAvg": "right_inlet_temp_avg", 
        "rightInletTempMax": "right_inlet_temp_max", 
        "rightInletTempMin": "right_inlet_temp_min", 
        "rightOutletTemp": "right_outlet_temp", 
        "rightOutletTempAvg": "right_outlet_temp_avg", 
        "rightOutletTempMax": "right_outlet_temp_max", 
        "rightOutletTempMin": "right_outlet_temp_min", 
        "rn": "rn", 
        "statsReported": "stats_reported", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.intervals = None
        self.left_inlet_temp = None
        self.left_inlet_temp_avg = None
        self.left_inlet_temp_max = None
        self.left_inlet_temp_min = None
        self.left_outlet_temp = None
        self.left_outlet_temp_avg = None
        self.left_outlet_temp_max = None
        self.left_outlet_temp_min = None
        self.normalized_time_col = None
        self.right_inlet_temp = None
        self.right_inlet_temp_avg = None
        self.right_inlet_temp_max = None
        self.right_inlet_temp_min = None
        self.right_outlet_temp = None
        self.right_outlet_temp_avg = None
        self.right_outlet_temp_max = None
        self.right_outlet_temp_min = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "StorageHddMotherBoardTempStats", parent_mo_or_dn, **kwargs)

