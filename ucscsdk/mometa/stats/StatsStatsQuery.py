"""This module contains the general information for StatsStatsQuery ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StatsStatsQueryConsts():
    READY_FALSE = "false"
    READY_NO = "no"
    READY_TRUE = "true"
    READY_YES = "yes"


class StatsStatsQuery(ManagedObject):
    """This is StatsStatsQuery class."""

    consts = StatsStatsQueryConsts()
    naming_props = set(['queryId'])

    mo_meta = MoMeta("StatsStatsQuery", "statsStatsQuery", "query-[query_id]", VersionMeta.Version111b, "InputOutput", 0x1f, [], ["read-only"], ['statsStatsQueryHolder'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "query_id": MoPropertyMeta("query_id", "queryId", "ulong", VersionMeta.Version111b, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "ready": MoPropertyMeta("ready", "ready", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "timestamp": MoPropertyMeta("timestamp", "timestamp", "ulong", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "queryId": "query_id", 
        "ready": "ready", 
        "rn": "rn", 
        "status": "status", 
        "timestamp": "timestamp", 
    }

    def __init__(self, parent_mo_or_dn, query_id, **kwargs):
        self._dirty_mask = 0
        self.query_id = query_id
        self.child_action = None
        self.ready = None
        self.status = None
        self.timestamp = None

        ManagedObject.__init__(self, "StatsStatsQuery", parent_mo_or_dn, **kwargs)

