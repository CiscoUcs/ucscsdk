"""This module contains the general information for IppoolIpV6Addr ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IppoolIpV6AddrConsts():
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


class IppoolIpV6Addr(ManagedObject):
    """This is IppoolIpV6Addr class."""

    consts = IppoolIpV6AddrConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("IppoolIpV6Addr", "ippoolIpV6Addr", "[id]", VersionMeta.Version112a, "InputOutput", 0x3f, [], ["read-only"], ['ippoolUniverse'], ['faultInst', 'identpoolConsumed', 'identpoolPoolable'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cons_cnt": MoPropertyMeta("cons_cnt", "consCnt", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["assigned-to-single", "available"], ["0-4294967295"]), 
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "display_id": MoPropertyMeta("display_id", "displayId", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_cnt": MoPropertyMeta("domain_cnt", "domainCnt", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["defined-by-single", "undefined"], ["0-4294967295"]), 
        "ep_pool_cnt": MoPropertyMeta("ep_pool_cnt", "epPoolCnt", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-defined-in-pool"], ["0-4294967295"]), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "generation": MoPropertyMeta("generation", "generation", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "global_pool_cnt": MoPropertyMeta("global_pool_cnt", "globalPoolCnt", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-defined-in-pool"], ["0-4294967295"]), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x8, 0, 256, None, [], []), 
        "prefix": MoPropertyMeta("prefix", "prefix", "byte", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-127"]), 
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "scope": MoPropertyMeta("scope", "scope", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["private", "public"], []), 
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sys_cnt": MoPropertyMeta("sys_cnt", "sysCnt", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["defined-by-single", "undefined"], ["0-4294967295"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "consCnt": "cons_cnt", 
        "defGw": "def_gw", 
        "displayId": "display_id", 
        "dn": "dn", 
        "domainCnt": "domain_cnt", 
        "epPoolCnt": "ep_pool_cnt", 
        "fltAggr": "flt_aggr", 
        "generation": "generation", 
        "globalPoolCnt": "global_pool_cnt", 
        "id": "id", 
        "prefix": "prefix", 
        "primDns": "prim_dns", 
        "rn": "rn", 
        "scope": "scope", 
        "secDns": "sec_dns", 
        "status": "status", 
        "sysCnt": "sys_cnt", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.cons_cnt = None
        self.def_gw = None
        self.display_id = None
        self.domain_cnt = None
        self.ep_pool_cnt = None
        self.flt_aggr = None
        self.generation = None
        self.global_pool_cnt = None
        self.prefix = None
        self.prim_dns = None
        self.scope = None
        self.sec_dns = None
        self.status = None
        self.sys_cnt = None

        ManagedObject.__init__(self, "IppoolIpV6Addr", parent_mo_or_dn, **kwargs)

