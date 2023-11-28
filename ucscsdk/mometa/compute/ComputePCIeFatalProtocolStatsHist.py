"""This module contains the general information for ComputePCIeFatalProtocolStatsHist ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputePCIeFatalProtocolStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputePCIeFatalProtocolStatsHist(ManagedObject):
    """This is ComputePCIeFatalProtocolStatsHist class."""

    consts = ComputePCIeFatalProtocolStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputePCIeFatalProtocolStatsHist", "computePCIeFatalProtocolStatsHist", "[id]", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["read-only"], ['computePCIeFatalProtocolStats'], [], [None])

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
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111a, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
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
        "id": "id", 
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
        self.most_recent = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "ComputePCIeFatalProtocolStatsHist", parent_mo_or_dn, **kwargs)

