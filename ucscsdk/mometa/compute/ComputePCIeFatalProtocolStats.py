"""This module contains the general information for ComputePCIeFatalProtocolStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputePCIeFatalProtocolStatsConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputePCIeFatalProtocolStats(ManagedObject):
    """This is ComputePCIeFatalProtocolStats class."""

    consts = ComputePCIeFatalProtocolStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePCIeFatalProtocolStats", "computePCIeFatalProtocolStats", "pciefat-protocol-stats", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['computeBoard'], ['computePCIeFatalProtocolStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dllp_errors": MoPropertyMeta("dllp_errors", "dllpErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dllp_errors_avg": MoPropertyMeta("dllp_errors_avg", "dllpErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dllp_errors_max": MoPropertyMeta("dllp_errors_max", "dllpErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dllp_errors_min": MoPropertyMeta("dllp_errors_min", "dllpErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dllp_errors_running": MoPropertyMeta("dllp_errors_running", "dllpErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "flow_control_errors": MoPropertyMeta("flow_control_errors", "flowControlErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "flow_control_errors_avg": MoPropertyMeta("flow_control_errors_avg", "flowControlErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "flow_control_errors_max": MoPropertyMeta("flow_control_errors_max", "flowControlErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "flow_control_errors_min": MoPropertyMeta("flow_control_errors_min", "flowControlErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "flow_control_errors_running": MoPropertyMeta("flow_control_errors_running", "flowControlErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
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
        "childAction": "child_action", 
        "dllpErrors": "dllp_errors", 
        "dllpErrorsAvg": "dllp_errors_avg", 
        "dllpErrorsMax": "dllp_errors_max", 
        "dllpErrorsMin": "dllp_errors_min", 
        "dllpErrorsRunning": "dllp_errors_running", 
        "dn": "dn", 
        "flowControlErrors": "flow_control_errors", 
        "flowControlErrorsAvg": "flow_control_errors_avg", 
        "flowControlErrorsMax": "flow_control_errors_max", 
        "flowControlErrorsMin": "flow_control_errors_min", 
        "flowControlErrorsRunning": "flow_control_errors_running", 
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
        self.child_action = None
        self.dllp_errors = None
        self.dllp_errors_avg = None
        self.dllp_errors_max = None
        self.dllp_errors_min = None
        self.dllp_errors_running = None
        self.flow_control_errors = None
        self.flow_control_errors_avg = None
        self.flow_control_errors_max = None
        self.flow_control_errors_min = None
        self.flow_control_errors_running = None
        self.intervals = None
        self.normalized_time_col = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ComputePCIeFatalProtocolStats", parent_mo_or_dn, **kwargs)

