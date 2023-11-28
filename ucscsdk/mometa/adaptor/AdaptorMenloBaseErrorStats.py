"""This module contains the general information for AdaptorMenloBaseErrorStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorMenloBaseErrorStatsConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorMenloBaseErrorStats(ManagedObject):
    """This is AdaptorMenloBaseErrorStats class."""

    consts = AdaptorMenloBaseErrorStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorMenloBaseErrorStats", "adaptorMenloBaseErrorStats", "menlo-base-error-stats", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], [], ['adaptorMenloBaseErrorStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "correctable_errors": MoPropertyMeta("correctable_errors", "correctableErrors", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "correctable_errors_delta": MoPropertyMeta("correctable_errors_delta", "correctableErrorsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "correctable_errors_delta_avg": MoPropertyMeta("correctable_errors_delta_avg", "correctableErrorsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "correctable_errors_delta_max": MoPropertyMeta("correctable_errors_delta_max", "correctableErrorsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "correctable_errors_delta_min": MoPropertyMeta("correctable_errors_delta_min", "correctableErrorsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "uncorrectable_errors": MoPropertyMeta("uncorrectable_errors", "uncorrectableErrors", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uncorrectable_errors_delta": MoPropertyMeta("uncorrectable_errors_delta", "uncorrectableErrorsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uncorrectable_errors_delta_avg": MoPropertyMeta("uncorrectable_errors_delta_avg", "uncorrectableErrorsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uncorrectable_errors_delta_max": MoPropertyMeta("uncorrectable_errors_delta_max", "uncorrectableErrorsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uncorrectable_errors_delta_min": MoPropertyMeta("uncorrectable_errors_delta_min", "uncorrectableErrorsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "correctableErrors": "correctable_errors", 
        "correctableErrorsDelta": "correctable_errors_delta", 
        "correctableErrorsDeltaAvg": "correctable_errors_delta_avg", 
        "correctableErrorsDeltaMax": "correctable_errors_delta_max", 
        "correctableErrorsDeltaMin": "correctable_errors_delta_min", 
        "dn": "dn", 
        "intervals": "intervals", 
        "normalizedTimeCol": "normalized_time_col", 
        "rn": "rn", 
        "statsReported": "stats_reported", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "uncorrectableErrors": "uncorrectable_errors", 
        "uncorrectableErrorsDelta": "uncorrectable_errors_delta", 
        "uncorrectableErrorsDeltaAvg": "uncorrectable_errors_delta_avg", 
        "uncorrectableErrorsDeltaMax": "uncorrectable_errors_delta_max", 
        "uncorrectableErrorsDeltaMin": "uncorrectable_errors_delta_min", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.correctable_errors = None
        self.correctable_errors_delta = None
        self.correctable_errors_delta_avg = None
        self.correctable_errors_delta_max = None
        self.correctable_errors_delta_min = None
        self.intervals = None
        self.normalized_time_col = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.uncorrectable_errors = None
        self.uncorrectable_errors_delta = None
        self.uncorrectable_errors_delta_avg = None
        self.uncorrectable_errors_delta_max = None
        self.uncorrectable_errors_delta_min = None
        self.update = None

        ManagedObject.__init__(self, "AdaptorMenloBaseErrorStats", parent_mo_or_dn, **kwargs)

