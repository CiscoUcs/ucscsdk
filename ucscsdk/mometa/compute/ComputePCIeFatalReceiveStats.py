"""This module contains the general information for ComputePCIeFatalReceiveStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputePCIeFatalReceiveStatsConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputePCIeFatalReceiveStats(ManagedObject):
    """This is ComputePCIeFatalReceiveStats class."""

    consts = ComputePCIeFatalReceiveStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePCIeFatalReceiveStats", "computePCIeFatalReceiveStats", "pciefat-receive-stats", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['computeBoard'], ['computePCIeFatalReceiveStatsHist'], [None])

    prop_meta = {
        "buffer_overflow_errors": MoPropertyMeta("buffer_overflow_errors", "bufferOverflowErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "buffer_overflow_errors_avg": MoPropertyMeta("buffer_overflow_errors_avg", "bufferOverflowErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "buffer_overflow_errors_max": MoPropertyMeta("buffer_overflow_errors_max", "bufferOverflowErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "buffer_overflow_errors_min": MoPropertyMeta("buffer_overflow_errors_min", "bufferOverflowErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "buffer_overflow_errors_running": MoPropertyMeta("buffer_overflow_errors_running", "bufferOverflowErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "err_fatal_errors": MoPropertyMeta("err_fatal_errors", "errFatalErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "err_fatal_errors_avg": MoPropertyMeta("err_fatal_errors_avg", "errFatalErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "err_fatal_errors_max": MoPropertyMeta("err_fatal_errors_max", "errFatalErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "err_fatal_errors_min": MoPropertyMeta("err_fatal_errors_min", "errFatalErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "err_fatal_errors_running": MoPropertyMeta("err_fatal_errors_running", "errFatalErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "err_non_fatal_errors": MoPropertyMeta("err_non_fatal_errors", "errNonFatalErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "err_non_fatal_errors_avg": MoPropertyMeta("err_non_fatal_errors_avg", "errNonFatalErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "err_non_fatal_errors_max": MoPropertyMeta("err_non_fatal_errors_max", "errNonFatalErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "err_non_fatal_errors_min": MoPropertyMeta("err_non_fatal_errors_min", "errNonFatalErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "err_non_fatal_errors_running": MoPropertyMeta("err_non_fatal_errors_running", "errNonFatalErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "unsupported_request_errors": MoPropertyMeta("unsupported_request_errors", "unsupportedRequestErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unsupported_request_errors_avg": MoPropertyMeta("unsupported_request_errors_avg", "unsupportedRequestErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unsupported_request_errors_max": MoPropertyMeta("unsupported_request_errors_max", "unsupportedRequestErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unsupported_request_errors_min": MoPropertyMeta("unsupported_request_errors_min", "unsupportedRequestErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unsupported_request_errors_running": MoPropertyMeta("unsupported_request_errors_running", "unsupportedRequestErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "bufferOverflowErrors": "buffer_overflow_errors", 
        "bufferOverflowErrorsAvg": "buffer_overflow_errors_avg", 
        "bufferOverflowErrorsMax": "buffer_overflow_errors_max", 
        "bufferOverflowErrorsMin": "buffer_overflow_errors_min", 
        "bufferOverflowErrorsRunning": "buffer_overflow_errors_running", 
        "childAction": "child_action", 
        "dn": "dn", 
        "errFatalErrors": "err_fatal_errors", 
        "errFatalErrorsAvg": "err_fatal_errors_avg", 
        "errFatalErrorsMax": "err_fatal_errors_max", 
        "errFatalErrorsMin": "err_fatal_errors_min", 
        "errFatalErrorsRunning": "err_fatal_errors_running", 
        "errNonFatalErrors": "err_non_fatal_errors", 
        "errNonFatalErrorsAvg": "err_non_fatal_errors_avg", 
        "errNonFatalErrorsMax": "err_non_fatal_errors_max", 
        "errNonFatalErrorsMin": "err_non_fatal_errors_min", 
        "errNonFatalErrorsRunning": "err_non_fatal_errors_running", 
        "intervals": "intervals", 
        "normalizedTimeCol": "normalized_time_col", 
        "rn": "rn", 
        "statsReported": "stats_reported", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "unsupportedRequestErrors": "unsupported_request_errors", 
        "unsupportedRequestErrorsAvg": "unsupported_request_errors_avg", 
        "unsupportedRequestErrorsMax": "unsupported_request_errors_max", 
        "unsupportedRequestErrorsMin": "unsupported_request_errors_min", 
        "unsupportedRequestErrorsRunning": "unsupported_request_errors_running", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.buffer_overflow_errors = None
        self.buffer_overflow_errors_avg = None
        self.buffer_overflow_errors_max = None
        self.buffer_overflow_errors_min = None
        self.buffer_overflow_errors_running = None
        self.child_action = None
        self.err_fatal_errors = None
        self.err_fatal_errors_avg = None
        self.err_fatal_errors_max = None
        self.err_fatal_errors_min = None
        self.err_fatal_errors_running = None
        self.err_non_fatal_errors = None
        self.err_non_fatal_errors_avg = None
        self.err_non_fatal_errors_max = None
        self.err_non_fatal_errors_min = None
        self.err_non_fatal_errors_running = None
        self.intervals = None
        self.normalized_time_col = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.unsupported_request_errors = None
        self.unsupported_request_errors_avg = None
        self.unsupported_request_errors_max = None
        self.unsupported_request_errors_min = None
        self.unsupported_request_errors_running = None
        self.update = None

        ManagedObject.__init__(self, "ComputePCIeFatalReceiveStats", parent_mo_or_dn, **kwargs)

