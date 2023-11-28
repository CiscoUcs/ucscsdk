"""This module contains the general information for StatsDbSummaryMeta ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StatsDbSummaryMetaConsts():
    pass


class StatsDbSummaryMeta(ManagedObject):
    """This is StatsDbSummaryMeta class."""

    consts = StatsDbSummaryMetaConsts()
    naming_props = set([])

    mo_meta = MoMeta("StatsDbSummaryMeta", "statsDbSummaryMeta", "summary-meta", VersionMeta.Version111b, "InputOutput", 0xf, [], ["admin"], ['topRoot'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "daily_last_run": MoPropertyMeta("daily_last_run", "dailyLastRun", "ulong", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dailyLastRun": "daily_last_run", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.daily_last_run = None
        self.status = None

        ManagedObject.__init__(self, "StatsDbSummaryMeta", **kwargs)

