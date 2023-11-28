"""This module contains the general information for ComputePCIeFatalStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputePCIeFatalStatsConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputePCIeFatalStats(ManagedObject):
    """This is ComputePCIeFatalStats class."""

    consts = ComputePCIeFatalStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePCIeFatalStats", "computePCIeFatalStats", "pciefat-stats", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['computeBoard'], ['computePCIeFatalStatsHist'], [None])

    prop_meta = {
        "acs_violation_errors": MoPropertyMeta("acs_violation_errors", "acsViolationErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "acs_violation_errors_avg": MoPropertyMeta("acs_violation_errors_avg", "acsViolationErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "acs_violation_errors_max": MoPropertyMeta("acs_violation_errors_max", "acsViolationErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "acs_violation_errors_min": MoPropertyMeta("acs_violation_errors_min", "acsViolationErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "acs_violation_errors_running": MoPropertyMeta("acs_violation_errors_running", "acsViolationErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "malformed_tlp_errors": MoPropertyMeta("malformed_tlp_errors", "malformedTLPErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "malformed_tlp_errors_avg": MoPropertyMeta("malformed_tlp_errors_avg", "malformedTLPErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "malformed_tlp_errors_max": MoPropertyMeta("malformed_tlp_errors_max", "malformedTLPErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "malformed_tlp_errors_min": MoPropertyMeta("malformed_tlp_errors_min", "malformedTLPErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "malformed_tlp_errors_running": MoPropertyMeta("malformed_tlp_errors_running", "malformedTLPErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "poisoned_tlp_errors": MoPropertyMeta("poisoned_tlp_errors", "poisonedTLPErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "poisoned_tlp_errors_avg": MoPropertyMeta("poisoned_tlp_errors_avg", "poisonedTLPErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "poisoned_tlp_errors_max": MoPropertyMeta("poisoned_tlp_errors_max", "poisonedTLPErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "poisoned_tlp_errors_min": MoPropertyMeta("poisoned_tlp_errors_min", "poisonedTLPErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "poisoned_tlp_errors_running": MoPropertyMeta("poisoned_tlp_errors_running", "poisonedTLPErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "surprise_link_down_errors": MoPropertyMeta("surprise_link_down_errors", "surpriseLinkDownErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "surprise_link_down_errors_avg": MoPropertyMeta("surprise_link_down_errors_avg", "surpriseLinkDownErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "surprise_link_down_errors_max": MoPropertyMeta("surprise_link_down_errors_max", "surpriseLinkDownErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "surprise_link_down_errors_min": MoPropertyMeta("surprise_link_down_errors_min", "surpriseLinkDownErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "surprise_link_down_errors_running": MoPropertyMeta("surprise_link_down_errors_running", "surpriseLinkDownErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "acsViolationErrors": "acs_violation_errors", 
        "acsViolationErrorsAvg": "acs_violation_errors_avg", 
        "acsViolationErrorsMax": "acs_violation_errors_max", 
        "acsViolationErrorsMin": "acs_violation_errors_min", 
        "acsViolationErrorsRunning": "acs_violation_errors_running", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "malformedTLPErrors": "malformed_tlp_errors", 
        "malformedTLPErrorsAvg": "malformed_tlp_errors_avg", 
        "malformedTLPErrorsMax": "malformed_tlp_errors_max", 
        "malformedTLPErrorsMin": "malformed_tlp_errors_min", 
        "malformedTLPErrorsRunning": "malformed_tlp_errors_running", 
        "normalizedTimeCol": "normalized_time_col", 
        "poisonedTLPErrors": "poisoned_tlp_errors", 
        "poisonedTLPErrorsAvg": "poisoned_tlp_errors_avg", 
        "poisonedTLPErrorsMax": "poisoned_tlp_errors_max", 
        "poisonedTLPErrorsMin": "poisoned_tlp_errors_min", 
        "poisonedTLPErrorsRunning": "poisoned_tlp_errors_running", 
        "rn": "rn", 
        "statsReported": "stats_reported", 
        "status": "status", 
        "surpriseLinkDownErrors": "surprise_link_down_errors", 
        "surpriseLinkDownErrorsAvg": "surprise_link_down_errors_avg", 
        "surpriseLinkDownErrorsMax": "surprise_link_down_errors_max", 
        "surpriseLinkDownErrorsMin": "surprise_link_down_errors_min", 
        "surpriseLinkDownErrorsRunning": "surprise_link_down_errors_running", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.acs_violation_errors = None
        self.acs_violation_errors_avg = None
        self.acs_violation_errors_max = None
        self.acs_violation_errors_min = None
        self.acs_violation_errors_running = None
        self.child_action = None
        self.intervals = None
        self.malformed_tlp_errors = None
        self.malformed_tlp_errors_avg = None
        self.malformed_tlp_errors_max = None
        self.malformed_tlp_errors_min = None
        self.malformed_tlp_errors_running = None
        self.normalized_time_col = None
        self.poisoned_tlp_errors = None
        self.poisoned_tlp_errors_avg = None
        self.poisoned_tlp_errors_max = None
        self.poisoned_tlp_errors_min = None
        self.poisoned_tlp_errors_running = None
        self.stats_reported = None
        self.status = None
        self.surprise_link_down_errors = None
        self.surprise_link_down_errors_avg = None
        self.surprise_link_down_errors_max = None
        self.surprise_link_down_errors_min = None
        self.surprise_link_down_errors_running = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ComputePCIeFatalStats", parent_mo_or_dn, **kwargs)

