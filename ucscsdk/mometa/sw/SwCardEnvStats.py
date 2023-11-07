"""This module contains the general information for SwCardEnvStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SwCardEnvStatsConsts():
    SLOT_OUTLET1_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET1_AVG_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET1_MAX_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET1_MIN_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET2_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET2_AVG_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET2_MAX_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET2_MIN_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET3_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET3_AVG_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET3_MAX_NOT_APPLICABLE = "not-applicable"
    SLOT_OUTLET3_MIN_NOT_APPLICABLE = "not-applicable"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class SwCardEnvStats(ManagedObject):
    """This is SwCardEnvStats class."""

    consts = SwCardEnvStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("SwCardEnvStats", "swCardEnvStats", "cardenvstats", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['networkElement'], ['swCardEnvStatsHist'], [None])

    prop_meta = {
        "slot_outlet1": MoPropertyMeta("slot_outlet1", "SlotOutlet1", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_outlet1_avg": MoPropertyMeta("slot_outlet1_avg", "SlotOutlet1Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_outlet1_max": MoPropertyMeta("slot_outlet1_max", "SlotOutlet1Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_outlet1_min": MoPropertyMeta("slot_outlet1_min", "SlotOutlet1Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_outlet2": MoPropertyMeta("slot_outlet2", "SlotOutlet2", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_outlet2_avg": MoPropertyMeta("slot_outlet2_avg", "SlotOutlet2Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_outlet2_max": MoPropertyMeta("slot_outlet2_max", "SlotOutlet2Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_outlet2_min": MoPropertyMeta("slot_outlet2_min", "SlotOutlet2Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_outlet3": MoPropertyMeta("slot_outlet3", "SlotOutlet3", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_outlet3_avg": MoPropertyMeta("slot_outlet3_avg", "SlotOutlet3Avg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_outlet3_max": MoPropertyMeta("slot_outlet3_max", "SlotOutlet3Max", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_outlet3_min": MoPropertyMeta("slot_outlet3_min", "SlotOutlet3Min", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "SlotOutlet1": "slot_outlet1", 
        "SlotOutlet1Avg": "slot_outlet1_avg", 
        "SlotOutlet1Max": "slot_outlet1_max", 
        "SlotOutlet1Min": "slot_outlet1_min", 
        "SlotOutlet2": "slot_outlet2", 
        "SlotOutlet2Avg": "slot_outlet2_avg", 
        "SlotOutlet2Max": "slot_outlet2_max", 
        "SlotOutlet2Min": "slot_outlet2_min", 
        "SlotOutlet3": "slot_outlet3", 
        "SlotOutlet3Avg": "slot_outlet3_avg", 
        "SlotOutlet3Max": "slot_outlet3_max", 
        "SlotOutlet3Min": "slot_outlet3_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "normalizedTimeCol": "normalized_time_col", 
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
        self.slot_outlet1 = None
        self.slot_outlet1_avg = None
        self.slot_outlet1_max = None
        self.slot_outlet1_min = None
        self.slot_outlet2 = None
        self.slot_outlet2_avg = None
        self.slot_outlet2_max = None
        self.slot_outlet2_min = None
        self.slot_outlet3 = None
        self.slot_outlet3_avg = None
        self.slot_outlet3_max = None
        self.slot_outlet3_min = None
        self.child_action = None
        self.intervals = None
        self.normalized_time_col = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "SwCardEnvStats", parent_mo_or_dn, **kwargs)

