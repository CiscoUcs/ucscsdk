"""This module contains the general information for HcCatalogList ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class HcCatalogListConsts():
    REFRESH_FALSE = "false"
    REFRESH_NO = "no"
    REFRESH_TRUE = "true"
    REFRESH_YES = "yes"


class HcCatalogList(ManagedObject):
    """This is HcCatalogList class."""

    consts = HcCatalogListConsts()
    naming_props = set([])

    mo_meta = MoMeta("HcCatalogList", "hcCatalogList", "catalog-list", None, "InputOutput", 0x1f, [], ["admin"], [u'hcHolder'], [u'hcCatalogSource'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", None, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "refresh": MoPropertyMeta("refresh", "refresh", "string", None, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "refresh": "refresh", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.flt_aggr = None
        self.refresh = None
        self.status = None

        ManagedObject.__init__(self, "HcCatalogList", parent_mo_or_dn, **kwargs)

