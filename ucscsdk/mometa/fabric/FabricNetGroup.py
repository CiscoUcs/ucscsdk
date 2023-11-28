"""This module contains the general information for FabricNetGroup ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricNetGroupConsts():
    INT_ID_NONE = "none"
    OWNER_MANAGEMENT = "management"
    OWNER_POLICY = "policy"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    POOL_TYPE_NON_QUALIFER = "non-qualifer"
    POOL_TYPE_QUALIFER = "qualifer"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_DUAL = "dual"
    SWITCH_ID_MGMT = "mgmt"


class FabricNetGroup(ManagedObject):
    """This is FabricNetGroup class."""

    consts = FabricNetGroupConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricNetGroup", "fabricNetGroup", "net-group-[name]", VersionMeta.Version111a, "InputOutput", 0xff, [], ["admin", "ext-lan-config", "ext-lan-policy", "ls-network"], ['fabricEthLan', 'fabricLanCloud'], ['fabricEthVlanPc', 'fabricEthVlanPortEp', 'fabricPooledVlan', 'fabricSwSubGroup'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "native_net": MoPropertyMeta("native_net", "nativeNet", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []), 
        "native_net_dn": MoPropertyMeta("native_net_dn", "nativeNetDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["management", "policy"], []), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "pool_type": MoPropertyMeta("pool_type", "poolType", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["non-qualifer", "qualifer"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "dual", "mgmt"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((defaultValue|mgmt|vlan-compression|vlan-uncompressed|vp-compression),){0,4}(defaultValue|mgmt|vlan-compression|vlan-uncompressed|vp-compression){0,1}""", [], []), 
    }

    prop_map = {
        "assigned": "assigned", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "id": "id", 
        "intId": "int_id", 
        "name": "name", 
        "nativeNet": "native_net", 
        "nativeNetDn": "native_net_dn", 
        "owner": "owner", 
        "peerDn": "peer_dn", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "poolType": "pool_type", 
        "rn": "rn", 
        "size": "size", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.assigned = None
        self.child_action = None
        self.descr = None
        self.flt_aggr = None
        self.id = None
        self.int_id = None
        self.native_net = None
        self.native_net_dn = None
        self.owner = None
        self.peer_dn = None
        self.policy_level = None
        self.policy_owner = None
        self.pool_type = None
        self.size = None
        self.status = None
        self.switch_id = None
        self.type = None

        ManagedObject.__init__(self, "FabricNetGroup", parent_mo_or_dn, **kwargs)

