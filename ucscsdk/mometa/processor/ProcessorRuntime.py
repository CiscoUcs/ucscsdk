"""This module contains the general information for ProcessorRuntime ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ProcessorRuntimeConsts():
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class ProcessorRuntime(ManagedObject):
    """This is ProcessorRuntime class."""

    consts = ProcessorRuntimeConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorRuntime", "processorRuntime", "cpu-rt", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['computeBlade'], ['processorRuntimeHist'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "load": MoPropertyMeta("load", "load", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "load_avg": MoPropertyMeta("load_avg", "loadAvg", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "load_max": MoPropertyMeta("load_max", "loadMax", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "load_min": MoPropertyMeta("load_min", "loadMin", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "normalized_time_col": MoPropertyMeta("normalized_time_col", "normalizedTimeCol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stats_reported": MoPropertyMeta("stats_reported", "statsReported", "int", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uptime": MoPropertyMeta("uptime", "uptime", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "load": "load", 
        "loadAvg": "load_avg", 
        "loadMax": "load_max", 
        "loadMin": "load_min", 
        "normalizedTimeCol": "normalized_time_col", 
        "rn": "rn", 
        "statsReported": "stats_reported", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
        "uptime": "uptime", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.intervals = None
        self.load = None
        self.load_avg = None
        self.load_max = None
        self.load_min = None
        self.normalized_time_col = None
        self.stats_reported = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None
        self.uptime = None

        ManagedObject.__init__(self, "ProcessorRuntime", parent_mo_or_dn, **kwargs)

