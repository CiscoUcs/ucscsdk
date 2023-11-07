"""This module contains the general information for IdentpoolPoolable ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IdentpoolPoolableConsts():
    OWNER_END_POINT = "end-point"
    OWNER_POOL = "pool"


class IdentpoolPoolable(ManagedObject):
    """This is IdentpoolPoolable class."""

    consts = IdentpoolPoolableConsts()
    naming_props = set(['sysId', 'id'])

    mo_meta = MoMeta("IdentpoolPoolable", "identpoolPoolable", "pool-[sys_id]-[id]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["read-only"], ['fcpoolAddr', 'ippoolAddr', 'ippoolIpV6Addr', 'iqnpoolAddr', 'macpoolAddr', 'uuidpoolAddr'], [], [None])

    prop_meta = {
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["end-point", "pool"], []), 
        "pool_dn": MoPropertyMeta("pool_dn", "poolDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sys_id": MoPropertyMeta("sys_id", "sysId", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
    }

    prop_map = {
        "assignedToDn": "assigned_to_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "owner": "owner", 
        "poolDn": "pool_dn", 
        "rn": "rn", 
        "status": "status", 
        "sysId": "sys_id", 
    }

    def __init__(self, parent_mo_or_dn, sys_id, id, **kwargs):
        self._dirty_mask = 0
        self.sys_id = sys_id
        self.id = id
        self.assigned_to_dn = None
        self.child_action = None
        self.owner = None
        self.pool_dn = None
        self.status = None

        ManagedObject.__init__(self, "IdentpoolPoolable", parent_mo_or_dn, **kwargs)

