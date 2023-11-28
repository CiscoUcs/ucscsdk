"""This module contains the general information for IppoolPool ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IppoolPoolConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    POOL_TYPE_NON_QUALIFER = "non-qualifer"
    POOL_TYPE_QUALIFER = "qualifer"


class IppoolPool(ManagedObject):
    """This is IppoolPool class."""

    consts = IppoolPoolConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("IppoolPool", "ippoolPool", "ip-pool-[name]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["read-only"], ['orgDomainGroup', 'orgOrg'], ['faultInst', 'ippoolBlock', 'ippoolIpV6Block', 'ippoolIpV6Pooled', 'ippoolPooled'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "pool_type": MoPropertyMeta("pool_type", "poolType", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["non-qualifer", "qualifer"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "v4_assigned": MoPropertyMeta("v4_assigned", "v4Assigned", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "v4_size": MoPropertyMeta("v4_size", "v4Size", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "v6_assigned": MoPropertyMeta("v6_assigned", "v6Assigned", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "v6_size": MoPropertyMeta("v6_size", "v6Size", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "assigned": "assigned", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "poolType": "pool_type", 
        "rn": "rn", 
        "size": "size", 
        "status": "status", 
        "v4Assigned": "v4_assigned", 
        "v4Size": "v4_size", 
        "v6Assigned": "v6_assigned", 
        "v6Size": "v6_size", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.assigned = None
        self.child_action = None
        self.descr = None
        self.flt_aggr = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.pool_type = None
        self.size = None
        self.status = None
        self.v4_assigned = None
        self.v4_size = None
        self.v6_assigned = None
        self.v6_size = None

        ManagedObject.__init__(self, "IppoolPool", parent_mo_or_dn, **kwargs)

