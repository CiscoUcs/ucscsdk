"""This module contains the general information for IppoolIpV6Pooled ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IppoolIpV6PooledConsts():
    ASSIGNED_FALSE = "false"
    ASSIGNED_NO = "no"
    ASSIGNED_TRUE = "true"
    ASSIGNED_YES = "yes"
    CONS_CNT_ASSIGNED_TO_SINGLE = "assigned-to-single"
    CONS_CNT_AVAILABLE = "available"
    SCOPE_PRIVATE = "private"
    SCOPE_PUBLIC = "public"


class IppoolIpV6Pooled(ManagedObject):
    """This is IppoolIpV6Pooled class."""

    consts = IppoolIpV6PooledConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("IppoolIpV6Pooled", "ippoolIpV6Pooled", "[id]", VersionMeta.Version112a, "InputOutput", 0x1f, [], ["read-only"], ['ippoolPool'], [], ["Get"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "block_dn": MoPropertyMeta("block_dn", "blockDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cons_cnt": MoPropertyMeta("cons_cnt", "consCnt", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["assigned-to-single", "available"], ["0-4294967295"]), 
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x4, 0, 256, None, [], []), 
        "id_released_time": MoPropertyMeta("id_released_time", "idReleasedTime", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "poolable_dn": MoPropertyMeta("poolable_dn", "poolableDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "prefix": MoPropertyMeta("prefix", "prefix", "byte", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-127"]), 
        "prev_assigned_to_dn": MoPropertyMeta("prev_assigned_to_dn", "prevAssignedToDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "scope": MoPropertyMeta("scope", "scope", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["private", "public"], []), 
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "assigned": "assigned", 
        "assignedToDn": "assigned_to_dn", 
        "blockDn": "block_dn", 
        "childAction": "child_action", 
        "consCnt": "cons_cnt", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "id": "id", 
        "idReleasedTime": "id_released_time", 
        "poolableDn": "poolable_dn", 
        "prefix": "prefix", 
        "prevAssignedToDn": "prev_assigned_to_dn", 
        "primDns": "prim_dns", 
        "rn": "rn", 
        "scope": "scope", 
        "secDns": "sec_dns", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.assigned = None
        self.assigned_to_dn = None
        self.block_dn = None
        self.child_action = None
        self.cons_cnt = None
        self.def_gw = None
        self.id_released_time = None
        self.poolable_dn = None
        self.prefix = None
        self.prev_assigned_to_dn = None
        self.prim_dns = None
        self.scope = None
        self.sec_dns = None
        self.status = None

        ManagedObject.__init__(self, "IppoolIpV6Pooled", parent_mo_or_dn, **kwargs)

