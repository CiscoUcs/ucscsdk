"""This module contains the general information for MgmtInbandProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtInbandProfileConsts():
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class MgmtInbandProfile(ManagedObject):
    """This is MgmtInbandProfile class."""

    consts = MgmtInbandProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtInbandProfile", "mgmtInbandProfile", "ib-profile", VersionMeta.Version141a, "InputOutput", 0xff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricLanCloud'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "default_vlan_name": MoPropertyMeta("default_vlan_name", "defaultVlanName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "pool_name": MoPropertyMeta("pool_name", "poolName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "defaultVlanName": "default_vlan_name", 
        "dn": "dn", 
        "name": "name", 
        "policyOwner": "policy_owner", 
        "poolName": "pool_name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.default_vlan_name = None
        self.name = None
        self.policy_owner = None
        self.pool_name = None
        self.status = None

        ManagedObject.__init__(self, "MgmtInbandProfile", parent_mo_or_dn, **kwargs)

