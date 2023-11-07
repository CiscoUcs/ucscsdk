"""This module contains the general information for ProcPrtCounts ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ProcPrtCountsConsts():
    pass


class ProcPrtCounts(ManagedObject):
    """This is ProcPrtCounts class."""

    consts = ProcPrtCountsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcPrtCounts", "procPrtCounts", "prtCnt", VersionMeta.Version101a, "InputOutput", 0xf, [], ["read-only"], ['procManager'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dbtxs": MoPropertyMeta("dbtxs", "dbtxs", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "total": MoPropertyMeta("total", "total", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dbtxs": "dbtxs", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "total": "total", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.dbtxs = None
        self.status = None
        self.total = None

        ManagedObject.__init__(self, "ProcPrtCounts", parent_mo_or_dn, **kwargs)

