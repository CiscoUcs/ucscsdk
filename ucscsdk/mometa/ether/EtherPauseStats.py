"""This module contains the general information for EtherPauseStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EtherPauseStatsConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EtherPauseStats(ManagedObject):
    """This is EtherPauseStats class."""

    consts = EtherPauseStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("EtherPauseStats", "etherPauseStats", "pause-stats", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['etherServerIntFIo'], ['etherPauseStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "recv_pause": MoPropertyMeta("recv_pause", "recvPause", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "recv_pause_delta": MoPropertyMeta("recv_pause_delta", "recvPauseDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "recv_pause_delta_avg": MoPropertyMeta("recv_pause_delta_avg", "recvPauseDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "recv_pause_delta_max": MoPropertyMeta("recv_pause_delta_max", "recvPauseDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "recv_pause_delta_min": MoPropertyMeta("recv_pause_delta_min", "recvPauseDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "resets": MoPropertyMeta("resets", "resets", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "resets_delta": MoPropertyMeta("resets_delta", "resetsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "resets_delta_avg": MoPropertyMeta("resets_delta_avg", "resetsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "resets_delta_max": MoPropertyMeta("resets_delta_max", "resetsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "resets_delta_min": MoPropertyMeta("resets_delta_min", "resetsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "xmit_pause": MoPropertyMeta("xmit_pause", "xmitPause", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "xmit_pause_delta": MoPropertyMeta("xmit_pause_delta", "xmitPauseDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "xmit_pause_delta_avg": MoPropertyMeta("xmit_pause_delta_avg", "xmitPauseDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "xmit_pause_delta_max": MoPropertyMeta("xmit_pause_delta_max", "xmitPauseDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "xmit_pause_delta_min": MoPropertyMeta("xmit_pause_delta_min", "xmitPauseDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "normalizedTimeCol": "normalized_time_col", 
        "recvPause": "recv_pause", 
        "recvPauseDelta": "recv_pause_delta", 
        "recvPauseDeltaAvg": "recv_pause_delta_avg", 
        "recvPauseDeltaMax": "recv_pause_delta_max", 
        "recvPauseDeltaMin": "recv_pause_delta_min", 
        "resets": "resets", 
        "resetsDelta": "resets_delta", 
        "resetsDeltaAvg": "resets_delta_avg", 
        "resetsDeltaMax": "resets_delta_max", 
        "resetsDeltaMin": "resets_delta_min", 
        "rn": "rn", 
        "statsReported": "stats_reported", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
        "xmitPause": "xmit_pause", 
        "xmitPauseDelta": "xmit_pause_delta", 
        "xmitPauseDeltaAvg": "xmit_pause_delta_avg", 
        "xmitPauseDeltaMax": "xmit_pause_delta_max", 
        "xmitPauseDeltaMin": "xmit_pause_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.intervals = None
        self.normalized_time_col = None
        self.recv_pause = None
        self.recv_pause_delta = None
        self.recv_pause_delta_avg = None
        self.recv_pause_delta_max = None
        self.recv_pause_delta_min = None
        self.resets = None
        self.resets_delta = None
        self.resets_delta_avg = None
        self.resets_delta_max = None
        self.resets_delta_min = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None
        self.xmit_pause = None
        self.xmit_pause_delta = None
        self.xmit_pause_delta_avg = None
        self.xmit_pause_delta_max = None
        self.xmit_pause_delta_min = None

        ManagedObject.__init__(self, "EtherPauseStats", parent_mo_or_dn, **kwargs)

