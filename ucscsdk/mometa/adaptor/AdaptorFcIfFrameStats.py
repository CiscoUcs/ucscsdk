"""This module contains the general information for AdaptorFcIfFrameStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorFcIfFrameStatsConsts():
    DUMPED_FRAMES_NA = "NA"
    DUMPED_FRAMES_DELTA_NA = "NA"
    DUMPED_FRAMES_DELTA_AVG_NA = "NA"
    DUMPED_FRAMES_DELTA_MAX_NA = "NA"
    DUMPED_FRAMES_DELTA_MIN_NA = "NA"
    ERROR_FRAMES_NA = "NA"
    ERROR_FRAMES_DELTA_NA = "NA"
    ERROR_FRAMES_DELTA_AVG_NA = "NA"
    ERROR_FRAMES_DELTA_MAX_NA = "NA"
    ERROR_FRAMES_DELTA_MIN_NA = "NA"
    RX_FRAMES_NA = "NA"
    RX_FRAMES_DELTA_NA = "NA"
    RX_FRAMES_DELTA_AVG_NA = "NA"
    RX_FRAMES_DELTA_MAX_NA = "NA"
    RX_FRAMES_DELTA_MIN_NA = "NA"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    TX_FRAMES_NA = "NA"
    TX_FRAMES_DELTA_NA = "NA"
    TX_FRAMES_DELTA_AVG_NA = "NA"
    TX_FRAMES_DELTA_MAX_NA = "NA"
    TX_FRAMES_DELTA_MIN_NA = "NA"


class AdaptorFcIfFrameStats(ManagedObject):
    """This is AdaptorFcIfFrameStats class."""

    consts = AdaptorFcIfFrameStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcIfFrameStats", "adaptorFcIfFrameStats", "fc-if-frame-stats", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['adaptorHostFcIf'], ['adaptorFcIfFrameStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "dumped_frames": MoPropertyMeta("dumped_frames", "dumpedFrames", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "dumped_frames_delta": MoPropertyMeta("dumped_frames_delta", "dumpedFramesDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "dumped_frames_delta_avg": MoPropertyMeta("dumped_frames_delta_avg", "dumpedFramesDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "dumped_frames_delta_max": MoPropertyMeta("dumped_frames_delta_max", "dumpedFramesDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "dumped_frames_delta_min": MoPropertyMeta("dumped_frames_delta_min", "dumpedFramesDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "error_frames": MoPropertyMeta("error_frames", "errorFrames", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "error_frames_delta": MoPropertyMeta("error_frames_delta", "errorFramesDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "error_frames_delta_avg": MoPropertyMeta("error_frames_delta_avg", "errorFramesDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "error_frames_delta_max": MoPropertyMeta("error_frames_delta_max", "errorFramesDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "error_frames_delta_min": MoPropertyMeta("error_frames_delta_min", "errorFramesDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rx_frames": MoPropertyMeta("rx_frames", "rxFrames", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "rx_frames_delta": MoPropertyMeta("rx_frames_delta", "rxFramesDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "rx_frames_delta_avg": MoPropertyMeta("rx_frames_delta_avg", "rxFramesDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "rx_frames_delta_max": MoPropertyMeta("rx_frames_delta_max", "rxFramesDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "rx_frames_delta_min": MoPropertyMeta("rx_frames_delta_min", "rxFramesDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "tx_frames": MoPropertyMeta("tx_frames", "txFrames", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "tx_frames_delta": MoPropertyMeta("tx_frames_delta", "txFramesDelta", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "tx_frames_delta_avg": MoPropertyMeta("tx_frames_delta_avg", "txFramesDeltaAvg", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "tx_frames_delta_max": MoPropertyMeta("tx_frames_delta_max", "txFramesDeltaMax", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "tx_frames_delta_min": MoPropertyMeta("tx_frames_delta_min", "txFramesDeltaMin", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-4294967295"]), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "dumpedFrames": "dumped_frames", 
        "dumpedFramesDelta": "dumped_frames_delta", 
        "dumpedFramesDeltaAvg": "dumped_frames_delta_avg", 
        "dumpedFramesDeltaMax": "dumped_frames_delta_max", 
        "dumpedFramesDeltaMin": "dumped_frames_delta_min", 
        "errorFrames": "error_frames", 
        "errorFramesDelta": "error_frames_delta", 
        "errorFramesDeltaAvg": "error_frames_delta_avg", 
        "errorFramesDeltaMax": "error_frames_delta_max", 
        "errorFramesDeltaMin": "error_frames_delta_min", 
        "intervals": "intervals", 
        "normalizedTimeCol": "normalized_time_col", 
        "rn": "rn", 
        "rxFrames": "rx_frames", 
        "rxFramesDelta": "rx_frames_delta", 
        "rxFramesDeltaAvg": "rx_frames_delta_avg", 
        "rxFramesDeltaMax": "rx_frames_delta_max", 
        "rxFramesDeltaMin": "rx_frames_delta_min", 
        "statsReported": "stats_reported", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "txFrames": "tx_frames", 
        "txFramesDelta": "tx_frames_delta", 
        "txFramesDeltaAvg": "tx_frames_delta_avg", 
        "txFramesDeltaMax": "tx_frames_delta_max", 
        "txFramesDeltaMin": "tx_frames_delta_min", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.dumped_frames = None
        self.dumped_frames_delta = None
        self.dumped_frames_delta_avg = None
        self.dumped_frames_delta_max = None
        self.dumped_frames_delta_min = None
        self.error_frames = None
        self.error_frames_delta = None
        self.error_frames_delta_avg = None
        self.error_frames_delta_max = None
        self.error_frames_delta_min = None
        self.intervals = None
        self.normalized_time_col = None
        self.rx_frames = None
        self.rx_frames_delta = None
        self.rx_frames_delta_avg = None
        self.rx_frames_delta_max = None
        self.rx_frames_delta_min = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.tx_frames = None
        self.tx_frames_delta = None
        self.tx_frames_delta_avg = None
        self.tx_frames_delta_max = None
        self.tx_frames_delta_min = None
        self.update = None

        ManagedObject.__init__(self, "AdaptorFcIfFrameStats", parent_mo_or_dn, **kwargs)

