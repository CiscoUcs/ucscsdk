"""This module contains the general information for ExtvmmNetworkSets ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ExtvmmNetworkSetsConsts():
    pass


class ExtvmmNetworkSets(ManagedObject):
    """This is ExtvmmNetworkSets class."""

    consts = ExtvmmNetworkSetsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtvmmNetworkSets", "extvmmNetworkSets", "network-sets", VersionMeta.Version141a, "InputOutput", 0xf, [], ["admin", "ls-network", "ls-network-policy"], ['fabricLanCloud'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "gen_num": MoPropertyMeta("gen_num", "genNum", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "genNum": "gen_num", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.flt_aggr = None
        self.gen_num = None
        self.status = None

        ManagedObject.__init__(self, "ExtvmmNetworkSets", parent_mo_or_dn, **kwargs)

