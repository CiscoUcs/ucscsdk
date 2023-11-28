"""This module contains the general information for ProcessorErrorStats ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ProcessorErrorStatsConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ProcessorErrorStats(ManagedObject):
    """This is ProcessorErrorStats class."""

    consts = ProcessorErrorStatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorErrorStats", "processorErrorStats", "error-stats", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['processorUnit'], ['processorErrorStatsHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mirroring_inter_sock_errors": MoPropertyMeta("mirroring_inter_sock_errors", "mirroringInterSockErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mirroring_inter_sock_errors_avg": MoPropertyMeta("mirroring_inter_sock_errors_avg", "mirroringInterSockErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mirroring_inter_sock_errors_max": MoPropertyMeta("mirroring_inter_sock_errors_max", "mirroringInterSockErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mirroring_inter_sock_errors_min": MoPropertyMeta("mirroring_inter_sock_errors_min", "mirroringInterSockErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mirroring_inter_sock_errors_running": MoPropertyMeta("mirroring_inter_sock_errors_running", "mirroringInterSockErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mirroring_intra_sock_errors": MoPropertyMeta("mirroring_intra_sock_errors", "mirroringIntraSockErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mirroring_intra_sock_errors_avg": MoPropertyMeta("mirroring_intra_sock_errors_avg", "mirroringIntraSockErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mirroring_intra_sock_errors_max": MoPropertyMeta("mirroring_intra_sock_errors_max", "mirroringIntraSockErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mirroring_intra_sock_errors_min": MoPropertyMeta("mirroring_intra_sock_errors_min", "mirroringIntraSockErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mirroring_intra_sock_errors_running": MoPropertyMeta("mirroring_intra_sock_errors_running", "mirroringIntraSockErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "smi_link_corr_errors": MoPropertyMeta("smi_link_corr_errors", "smiLinkCorrErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "smi_link_corr_errors_avg": MoPropertyMeta("smi_link_corr_errors_avg", "smiLinkCorrErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "smi_link_corr_errors_max": MoPropertyMeta("smi_link_corr_errors_max", "smiLinkCorrErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "smi_link_corr_errors_min": MoPropertyMeta("smi_link_corr_errors_min", "smiLinkCorrErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "smi_link_corr_errors_running": MoPropertyMeta("smi_link_corr_errors_running", "smiLinkCorrErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "smi_link_uncorr_errors": MoPropertyMeta("smi_link_uncorr_errors", "smiLinkUncorrErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "smi_link_uncorr_errors_avg": MoPropertyMeta("smi_link_uncorr_errors_avg", "smiLinkUncorrErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "smi_link_uncorr_errors_max": MoPropertyMeta("smi_link_uncorr_errors_max", "smiLinkUncorrErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "smi_link_uncorr_errors_min": MoPropertyMeta("smi_link_uncorr_errors_min", "smiLinkUncorrErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "smi_link_uncorr_errors_running": MoPropertyMeta("smi_link_uncorr_errors_running", "smiLinkUncorrErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "sparing_errors": MoPropertyMeta("sparing_errors", "sparingErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "sparing_errors_avg": MoPropertyMeta("sparing_errors_avg", "sparingErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "sparing_errors_max": MoPropertyMeta("sparing_errors_max", "sparingErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "sparing_errors_min": MoPropertyMeta("sparing_errors_min", "sparingErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "sparing_errors_running": MoPropertyMeta("sparing_errors_running", "sparingErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
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
        "intervals": "intervals", 
        "mirroringInterSockErrors": "mirroring_inter_sock_errors", 
        "mirroringInterSockErrorsAvg": "mirroring_inter_sock_errors_avg", 
        "mirroringInterSockErrorsMax": "mirroring_inter_sock_errors_max", 
        "mirroringInterSockErrorsMin": "mirroring_inter_sock_errors_min", 
        "mirroringInterSockErrorsRunning": "mirroring_inter_sock_errors_running", 
        "mirroringIntraSockErrors": "mirroring_intra_sock_errors", 
        "mirroringIntraSockErrorsAvg": "mirroring_intra_sock_errors_avg", 
        "mirroringIntraSockErrorsMax": "mirroring_intra_sock_errors_max", 
        "mirroringIntraSockErrorsMin": "mirroring_intra_sock_errors_min", 
        "mirroringIntraSockErrorsRunning": "mirroring_intra_sock_errors_running", 
        "normalizedTimeCol": "normalized_time_col", 
        "rn": "rn", 
        "smiLinkCorrErrors": "smi_link_corr_errors", 
        "smiLinkCorrErrorsAvg": "smi_link_corr_errors_avg", 
        "smiLinkCorrErrorsMax": "smi_link_corr_errors_max", 
        "smiLinkCorrErrorsMin": "smi_link_corr_errors_min", 
        "smiLinkCorrErrorsRunning": "smi_link_corr_errors_running", 
        "smiLinkUncorrErrors": "smi_link_uncorr_errors", 
        "smiLinkUncorrErrorsAvg": "smi_link_uncorr_errors_avg", 
        "smiLinkUncorrErrorsMax": "smi_link_uncorr_errors_max", 
        "smiLinkUncorrErrorsMin": "smi_link_uncorr_errors_min", 
        "smiLinkUncorrErrorsRunning": "smi_link_uncorr_errors_running", 
        "sparingErrors": "sparing_errors", 
        "sparingErrorsAvg": "sparing_errors_avg", 
        "sparingErrorsMax": "sparing_errors_max", 
        "sparingErrorsMin": "sparing_errors_min", 
        "sparingErrorsRunning": "sparing_errors_running", 
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
        self.intervals = None
        self.mirroring_inter_sock_errors = None
        self.mirroring_inter_sock_errors_avg = None
        self.mirroring_inter_sock_errors_max = None
        self.mirroring_inter_sock_errors_min = None
        self.mirroring_inter_sock_errors_running = None
        self.mirroring_intra_sock_errors = None
        self.mirroring_intra_sock_errors_avg = None
        self.mirroring_intra_sock_errors_max = None
        self.mirroring_intra_sock_errors_min = None
        self.mirroring_intra_sock_errors_running = None
        self.normalized_time_col = None
        self.smi_link_corr_errors = None
        self.smi_link_corr_errors_avg = None
        self.smi_link_corr_errors_max = None
        self.smi_link_corr_errors_min = None
        self.smi_link_corr_errors_running = None
        self.smi_link_uncorr_errors = None
        self.smi_link_uncorr_errors_avg = None
        self.smi_link_uncorr_errors_max = None
        self.smi_link_uncorr_errors_min = None
        self.smi_link_uncorr_errors_running = None
        self.sparing_errors = None
        self.sparing_errors_avg = None
        self.sparing_errors_max = None
        self.sparing_errors_min = None
        self.sparing_errors_running = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "ProcessorErrorStats", parent_mo_or_dn, **kwargs)

