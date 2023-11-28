"""This module contains the general information for StorageHddMotherBoardTempStatsHist ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageHddMotherBoardTempStatsHistConsts():
    LEFT_INLET_TEMP_NOT_APPLICABLE = "not-applicable"
    LEFT_INLET_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    LEFT_INLET_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    LEFT_INLET_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    LEFT_OUTLET_TEMP_NOT_APPLICABLE = "not-applicable"
    LEFT_OUTLET_TEMP_AVG_NOT_APPLICABLE = "not-applicable"
    LEFT_OUTLET_TEMP_MAX_NOT_APPLICABLE = "not-applicable"
    LEFT_OUTLET_TEMP_MIN_NOT_APPLICABLE = "not-applicable"
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
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


class StorageHddMotherBoardTempStatsHist(ManagedObject):
    """This is StorageHddMotherBoardTempStatsHist class."""

    consts = StorageHddMotherBoardTempStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageHddMotherBoardTempStatsHist", "storageHddMotherBoardTempStatsHist", "[id]", VersionMeta.Version151a, "OutputOnly", 0xf, [], ["read-only"], ['storageHddMotherBoardTempStats'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version151a, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "left_inlet_temp": MoPropertyMeta("left_inlet_temp", "leftInletTemp", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_inlet_temp_avg": MoPropertyMeta("left_inlet_temp_avg", "leftInletTempAvg", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_inlet_temp_max": MoPropertyMeta("left_inlet_temp_max", "leftInletTempMax", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_inlet_temp_min": MoPropertyMeta("left_inlet_temp_min", "leftInletTempMin", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_outlet_temp": MoPropertyMeta("left_outlet_temp", "leftOutletTemp", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_outlet_temp_avg": MoPropertyMeta("left_outlet_temp_avg", "leftOutletTempAvg", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_outlet_temp_max": MoPropertyMeta("left_outlet_temp_max", "leftOutletTempMax", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "left_outlet_temp_min": MoPropertyMeta("left_outlet_temp_min", "leftOutletTempMin", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "right_inlet_temp": MoPropertyMeta("right_inlet_temp", "rightInletTemp", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_inlet_temp_avg": MoPropertyMeta("right_inlet_temp_avg", "rightInletTempAvg", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_inlet_temp_max": MoPropertyMeta("right_inlet_temp_max", "rightInletTempMax", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_inlet_temp_min": MoPropertyMeta("right_inlet_temp_min", "rightInletTempMin", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_outlet_temp": MoPropertyMeta("right_outlet_temp", "rightOutletTemp", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_outlet_temp_avg": MoPropertyMeta("right_outlet_temp_avg", "rightOutletTempAvg", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_outlet_temp_max": MoPropertyMeta("right_outlet_temp_max", "rightOutletTempMax", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "right_outlet_temp_min": MoPropertyMeta("right_outlet_temp_min", "rightOutletTempMin", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "leftInletTemp": "left_inlet_temp", 
        "leftInletTempAvg": "left_inlet_temp_avg", 
        "leftInletTempMax": "left_inlet_temp_max", 
        "leftInletTempMin": "left_inlet_temp_min", 
        "leftOutletTemp": "left_outlet_temp", 
        "leftOutletTempAvg": "left_outlet_temp_avg", 
        "leftOutletTempMax": "left_outlet_temp_max", 
        "leftOutletTempMin": "left_outlet_temp_min", 
        "mostRecent": "most_recent", 
        "rightInletTemp": "right_inlet_temp", 
        "rightInletTempAvg": "right_inlet_temp_avg", 
        "rightInletTempMax": "right_inlet_temp_max", 
        "rightInletTempMin": "right_inlet_temp_min", 
        "rightOutletTemp": "right_outlet_temp", 
        "rightOutletTempAvg": "right_outlet_temp_avg", 
        "rightOutletTempMax": "right_outlet_temp_max", 
        "rightOutletTempMin": "right_outlet_temp_min", 
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
        self.left_inlet_temp = None
        self.left_inlet_temp_avg = None
        self.left_inlet_temp_max = None
        self.left_inlet_temp_min = None
        self.left_outlet_temp = None
        self.left_outlet_temp_avg = None
        self.left_outlet_temp_max = None
        self.left_outlet_temp_min = None
        self.most_recent = None
        self.right_inlet_temp = None
        self.right_inlet_temp_avg = None
        self.right_inlet_temp_max = None
        self.right_inlet_temp_min = None
        self.right_outlet_temp = None
        self.right_outlet_temp_avg = None
        self.right_outlet_temp_max = None
        self.right_outlet_temp_min = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "StorageHddMotherBoardTempStatsHist", parent_mo_or_dn, **kwargs)

