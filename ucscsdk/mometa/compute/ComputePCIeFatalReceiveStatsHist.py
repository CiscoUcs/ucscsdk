"""This module contains the general information for ComputePCIeFatalReceiveStatsHist ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputePCIeFatalReceiveStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ComputePCIeFatalReceiveStatsHist(ManagedObject):
    """This is ComputePCIeFatalReceiveStatsHist class."""

    consts = ComputePCIeFatalReceiveStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputePCIeFatalReceiveStatsHist", "computePCIeFatalReceiveStatsHist", "[id]", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["read-only"], ['computePCIeFatalReceiveStats'], [], [None])

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
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111a, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "unsupported_request_errors": MoPropertyMeta("unsupported_request_errors", "unsupportedRequestErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unsupported_request_errors_avg": MoPropertyMeta("unsupported_request_errors_avg", "unsupportedRequestErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unsupported_request_errors_max": MoPropertyMeta("unsupported_request_errors_max", "unsupportedRequestErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unsupported_request_errors_min": MoPropertyMeta("unsupported_request_errors_min", "unsupportedRequestErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unsupported_request_errors_running": MoPropertyMeta("unsupported_request_errors_running", "unsupportedRequestErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
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
        "id": "id", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "unsupportedRequestErrors": "unsupported_request_errors", 
        "unsupportedRequestErrorsAvg": "unsupported_request_errors_avg", 
        "unsupportedRequestErrorsMax": "unsupported_request_errors_max", 
        "unsupportedRequestErrorsMin": "unsupported_request_errors_min", 
        "unsupportedRequestErrorsRunning": "unsupported_request_errors_running", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
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
        self.most_recent = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.unsupported_request_errors = None
        self.unsupported_request_errors_avg = None
        self.unsupported_request_errors_max = None
        self.unsupported_request_errors_min = None
        self.unsupported_request_errors_running = None

        ManagedObject.__init__(self, "ComputePCIeFatalReceiveStatsHist", parent_mo_or_dn, **kwargs)

