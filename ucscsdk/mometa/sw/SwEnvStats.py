"""This module contains the general information for SwEnvStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SwEnvStatsConsts():
    FAN_CTRLR_INLET1_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET1_AVG_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET1_MAX_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET1_MIN_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET2_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET2_AVG_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET2_MAX_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET2_MIN_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET3_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET3_AVG_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET3_MAX_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET3_MIN_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET4_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET4_AVG_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET4_MAX_NOT_APPLICABLE = "not-applicable"
    FAN_CTRLR_INLET4_MIN_NOT_APPLICABLE = "not-applicable"
    MAIN_BOARD_OUTLET1_NOT_APPLICABLE = "not-applicable"
    MAIN_BOARD_OUTLET1_AVG_NOT_APPLICABLE = "not-applicable"
    MAIN_BOARD_OUTLET1_MAX_NOT_APPLICABLE = "not-applicable"
    MAIN_BOARD_OUTLET1_MIN_NOT_APPLICABLE = "not-applicable"
    MAIN_BOARD_OUTLET2_NOT_APPLICABLE = "not-applicable"
    MAIN_BOARD_OUTLET2_AVG_NOT_APPLICABLE = "not-applicable"
    MAIN_BOARD_OUTLET2_MAX_NOT_APPLICABLE = "not-applicable"
    MAIN_BOARD_OUTLET2_MIN_NOT_APPLICABLE = "not-applicable"
    PSU_CTRLR_INLET1_NOT_APPLICABLE = "not-applicable"
    PSU_CTRLR_INLET1_AVG_NOT_APPLICABLE = "not-applicable"
    PSU_CTRLR_INLET1_MAX_NOT_APPLICABLE = "not-applicable"
    PSU_CTRLR_INLET1_MIN_NOT_APPLICABLE = "not-applicable"
    PSU_CTRLR_INLET2_NOT_APPLICABLE = "not-applicable"
    PSU_CTRLR_INLET2_AVG_NOT_APPLICABLE = "not-applicable"
    PSU_CTRLR_INLET2_MAX_NOT_APPLICABLE = "not-applicable"
    PSU_CTRLR_INLET2_MIN_NOT_APPLICABLE = "not-applicable"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class SwEnvStats(ManagedObject):
    """This is SwEnvStats class."""

    consts = SwEnvStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("SwEnvStats", "swEnvStats", "envstats", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['networkElement'], ['swEnvStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fan_ctrlr_inlet1": MoPropertyMeta("fan_ctrlr_inlet1", "fanCtrlrInlet1", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet1_avg": MoPropertyMeta("fan_ctrlr_inlet1_avg", "fanCtrlrInlet1Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet1_max": MoPropertyMeta("fan_ctrlr_inlet1_max", "fanCtrlrInlet1Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet1_min": MoPropertyMeta("fan_ctrlr_inlet1_min", "fanCtrlrInlet1Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet2": MoPropertyMeta("fan_ctrlr_inlet2", "fanCtrlrInlet2", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet2_avg": MoPropertyMeta("fan_ctrlr_inlet2_avg", "fanCtrlrInlet2Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet2_max": MoPropertyMeta("fan_ctrlr_inlet2_max", "fanCtrlrInlet2Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet2_min": MoPropertyMeta("fan_ctrlr_inlet2_min", "fanCtrlrInlet2Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet3": MoPropertyMeta("fan_ctrlr_inlet3", "fanCtrlrInlet3", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet3_avg": MoPropertyMeta("fan_ctrlr_inlet3_avg", "fanCtrlrInlet3Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet3_max": MoPropertyMeta("fan_ctrlr_inlet3_max", "fanCtrlrInlet3Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet3_min": MoPropertyMeta("fan_ctrlr_inlet3_min", "fanCtrlrInlet3Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet4": MoPropertyMeta("fan_ctrlr_inlet4", "fanCtrlrInlet4", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet4_avg": MoPropertyMeta("fan_ctrlr_inlet4_avg", "fanCtrlrInlet4Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet4_max": MoPropertyMeta("fan_ctrlr_inlet4_max", "fanCtrlrInlet4Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "fan_ctrlr_inlet4_min": MoPropertyMeta("fan_ctrlr_inlet4_min", "fanCtrlrInlet4Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "main_board_outlet1": MoPropertyMeta("main_board_outlet1", "mainBoardOutlet1", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "main_board_outlet1_avg": MoPropertyMeta("main_board_outlet1_avg", "mainBoardOutlet1Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "main_board_outlet1_max": MoPropertyMeta("main_board_outlet1_max", "mainBoardOutlet1Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "main_board_outlet1_min": MoPropertyMeta("main_board_outlet1_min", "mainBoardOutlet1Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "main_board_outlet2": MoPropertyMeta("main_board_outlet2", "mainBoardOutlet2", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "main_board_outlet2_avg": MoPropertyMeta("main_board_outlet2_avg", "mainBoardOutlet2Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "main_board_outlet2_max": MoPropertyMeta("main_board_outlet2_max", "mainBoardOutlet2Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "main_board_outlet2_min": MoPropertyMeta("main_board_outlet2_min", "mainBoardOutlet2Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "psu_ctrlr_inlet1": MoPropertyMeta("psu_ctrlr_inlet1", "psuCtrlrInlet1", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "psu_ctrlr_inlet1_avg": MoPropertyMeta("psu_ctrlr_inlet1_avg", "psuCtrlrInlet1Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "psu_ctrlr_inlet1_max": MoPropertyMeta("psu_ctrlr_inlet1_max", "psuCtrlrInlet1Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "psu_ctrlr_inlet1_min": MoPropertyMeta("psu_ctrlr_inlet1_min", "psuCtrlrInlet1Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "psu_ctrlr_inlet2": MoPropertyMeta("psu_ctrlr_inlet2", "psuCtrlrInlet2", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "psu_ctrlr_inlet2_avg": MoPropertyMeta("psu_ctrlr_inlet2_avg", "psuCtrlrInlet2Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "psu_ctrlr_inlet2_max": MoPropertyMeta("psu_ctrlr_inlet2_max", "psuCtrlrInlet2Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "psu_ctrlr_inlet2_min": MoPropertyMeta("psu_ctrlr_inlet2_min", "psuCtrlrInlet2Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fanCtrlrInlet1": "fan_ctrlr_inlet1", 
        "fanCtrlrInlet1Avg": "fan_ctrlr_inlet1_avg", 
        "fanCtrlrInlet1Max": "fan_ctrlr_inlet1_max", 
        "fanCtrlrInlet1Min": "fan_ctrlr_inlet1_min", 
        "fanCtrlrInlet2": "fan_ctrlr_inlet2", 
        "fanCtrlrInlet2Avg": "fan_ctrlr_inlet2_avg", 
        "fanCtrlrInlet2Max": "fan_ctrlr_inlet2_max", 
        "fanCtrlrInlet2Min": "fan_ctrlr_inlet2_min", 
        "fanCtrlrInlet3": "fan_ctrlr_inlet3", 
        "fanCtrlrInlet3Avg": "fan_ctrlr_inlet3_avg", 
        "fanCtrlrInlet3Max": "fan_ctrlr_inlet3_max", 
        "fanCtrlrInlet3Min": "fan_ctrlr_inlet3_min", 
        "fanCtrlrInlet4": "fan_ctrlr_inlet4", 
        "fanCtrlrInlet4Avg": "fan_ctrlr_inlet4_avg", 
        "fanCtrlrInlet4Max": "fan_ctrlr_inlet4_max", 
        "fanCtrlrInlet4Min": "fan_ctrlr_inlet4_min", 
        "intervals": "intervals", 
        "mainBoardOutlet1": "main_board_outlet1", 
        "mainBoardOutlet1Avg": "main_board_outlet1_avg", 
        "mainBoardOutlet1Max": "main_board_outlet1_max", 
        "mainBoardOutlet1Min": "main_board_outlet1_min", 
        "mainBoardOutlet2": "main_board_outlet2", 
        "mainBoardOutlet2Avg": "main_board_outlet2_avg", 
        "mainBoardOutlet2Max": "main_board_outlet2_max", 
        "mainBoardOutlet2Min": "main_board_outlet2_min", 
        "normalizedTimeCol": "normalized_time_col", 
        "psuCtrlrInlet1": "psu_ctrlr_inlet1", 
        "psuCtrlrInlet1Avg": "psu_ctrlr_inlet1_avg", 
        "psuCtrlrInlet1Max": "psu_ctrlr_inlet1_max", 
        "psuCtrlrInlet1Min": "psu_ctrlr_inlet1_min", 
        "psuCtrlrInlet2": "psu_ctrlr_inlet2", 
        "psuCtrlrInlet2Avg": "psu_ctrlr_inlet2_avg", 
        "psuCtrlrInlet2Max": "psu_ctrlr_inlet2_max", 
        "psuCtrlrInlet2Min": "psu_ctrlr_inlet2_min", 
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
        self.fan_ctrlr_inlet1 = None
        self.fan_ctrlr_inlet1_avg = None
        self.fan_ctrlr_inlet1_max = None
        self.fan_ctrlr_inlet1_min = None
        self.fan_ctrlr_inlet2 = None
        self.fan_ctrlr_inlet2_avg = None
        self.fan_ctrlr_inlet2_max = None
        self.fan_ctrlr_inlet2_min = None
        self.fan_ctrlr_inlet3 = None
        self.fan_ctrlr_inlet3_avg = None
        self.fan_ctrlr_inlet3_max = None
        self.fan_ctrlr_inlet3_min = None
        self.fan_ctrlr_inlet4 = None
        self.fan_ctrlr_inlet4_avg = None
        self.fan_ctrlr_inlet4_max = None
        self.fan_ctrlr_inlet4_min = None
        self.intervals = None
        self.main_board_outlet1 = None
        self.main_board_outlet1_avg = None
        self.main_board_outlet1_max = None
        self.main_board_outlet1_min = None
        self.main_board_outlet2 = None
        self.main_board_outlet2_avg = None
        self.main_board_outlet2_max = None
        self.main_board_outlet2_min = None
        self.normalized_time_col = None
        self.psu_ctrlr_inlet1 = None
        self.psu_ctrlr_inlet1_avg = None
        self.psu_ctrlr_inlet1_max = None
        self.psu_ctrlr_inlet1_min = None
        self.psu_ctrlr_inlet2 = None
        self.psu_ctrlr_inlet2_avg = None
        self.psu_ctrlr_inlet2_max = None
        self.psu_ctrlr_inlet2_min = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "SwEnvStats", parent_mo_or_dn, **kwargs)

