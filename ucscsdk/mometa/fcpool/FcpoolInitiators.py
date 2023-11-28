"""This module contains the general information for FcpoolInitiators ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FcpoolInitiatorsConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    POOL_TYPE_NON_QUALIFER = "non-qualifer"
    POOL_TYPE_QUALIFER = "qualifer"


class FcpoolInitiators(ManagedObject):
    """This is FcpoolInitiators class."""

    consts = FcpoolInitiatorsConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FcpoolInitiators", "fcpoolInitiators", "wwn-pool-[name]", VersionMeta.Version101a, "InputOutput", 0xff, [], ["read-only"], ['orgOrg'], ['faultInst', 'fcpoolBlock', 'fcpoolInitiator'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "max_ports_per_node": MoPropertyMeta("max_ports_per_node", "maxPortsPerNode", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x8, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "pool_type": MoPropertyMeta("pool_type", "poolType", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["non-qualifer", "qualifer"], []), 
        "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x20, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "assigned": "assigned", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "intId": "int_id", 
        "maxPortsPerNode": "max_ports_per_node", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "poolType": "pool_type", 
        "purpose": "purpose", 
        "rn": "rn", 
        "size": "size", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.assigned = None
        self.child_action = None
        self.descr = None
        self.flt_aggr = None
        self.int_id = None
        self.max_ports_per_node = None
        self.policy_level = None
        self.policy_owner = None
        self.pool_type = None
        self.purpose = None
        self.size = None
        self.status = None

        ManagedObject.__init__(self, "FcpoolInitiators", parent_mo_or_dn, **kwargs)

