"""This module contains the general information for IqnpoolAddr ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IqnpoolAddrConsts():
    CONS_CNT_ASSIGNED_TO_SINGLE = "assigned-to-single"
    CONS_CNT_AVAILABLE = "available"
    DOMAIN_CNT_DEFINED_BY_SINGLE = "defined-by-single"
    DOMAIN_CNT_UNDEFINED = "undefined"
    EP_POOL_CNT_NOT_DEFINED_IN_POOL = "not-defined-in-pool"
    GLOBAL_POOL_CNT_NOT_DEFINED_IN_POOL = "not-defined-in-pool"
    SCOPE_PRIVATE = "private"
    SCOPE_PUBLIC = "public"
    SYS_CNT_DEFINED_BY_SINGLE = "defined-by-single"
    SYS_CNT_UNDEFINED = "undefined"


class IqnpoolAddr(ManagedObject):
    """This is IqnpoolAddr class."""

    consts = IqnpoolAddrConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("IqnpoolAddr", "iqnpoolAddr", "[id]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["read-only"], ['iqnpoolUniverse'], ['faultInst', 'identpoolConsumed', 'identpoolPoolable'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cons_cnt": MoPropertyMeta("cons_cnt", "consCnt", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["assigned-to-single", "available"], ["0-4294967295"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_cnt": MoPropertyMeta("domain_cnt", "domainCnt", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["defined-by-single", "undefined"], ["0-4294967295"]), 
        "ep_pool_cnt": MoPropertyMeta("ep_pool_cnt", "epPoolCnt", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-defined-in-pool"], ["0-4294967295"]), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "generation": MoPropertyMeta("generation", "generation", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "global_pool_cnt": MoPropertyMeta("global_pool_cnt", "globalPoolCnt", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-defined-in-pool"], ["0-4294967295"]), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "scope": MoPropertyMeta("scope", "scope", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["private", "public"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sys_cnt": MoPropertyMeta("sys_cnt", "sysCnt", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["defined-by-single", "undefined"], ["0-4294967295"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "consCnt": "cons_cnt", 
        "dn": "dn", 
        "domainCnt": "domain_cnt", 
        "epPoolCnt": "ep_pool_cnt", 
        "fltAggr": "flt_aggr", 
        "generation": "generation", 
        "globalPoolCnt": "global_pool_cnt", 
        "id": "id", 
        "rn": "rn", 
        "scope": "scope", 
        "status": "status", 
        "sysCnt": "sys_cnt", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.cons_cnt = None
        self.domain_cnt = None
        self.ep_pool_cnt = None
        self.flt_aggr = None
        self.generation = None
        self.global_pool_cnt = None
        self.scope = None
        self.status = None
        self.sys_cnt = None

        ManagedObject.__init__(self, "IqnpoolAddr", parent_mo_or_dn, **kwargs)

