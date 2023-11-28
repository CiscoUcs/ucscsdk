"""This module contains the general information for GlPool ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlPoolConsts():
    IDENT_TYPE_IP_V4 = "ipV4"
    IDENT_TYPE_IP_V6 = "ipV6"
    IDENT_TYPE_IQN = "iqn"
    IDENT_TYPE_MAC = "mac"
    IDENT_TYPE_UUID = "uuid"
    IDENT_TYPE_VLAN = "vlan"
    IDENT_TYPE_WWNN = "wwnn"
    IDENT_TYPE_WWPN = "wwpn"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class GlPool(ManagedObject):
    """This is GlPool class."""

    consts = GlPoolConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("GlPool", "glPool", "pool-[id]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["read-only"], ['glPoolInvEp'], ['glOperationEp', 'messageEp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "ident_type": MoPropertyMeta("ident_type", "identType", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipV4", "ipV6", "iqn", "mac", "uuid", "vlan", "wwnn", "wwpn"], []), 
        "inv_dn": MoPropertyMeta("inv_dn", "invDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "org_dn": MoPropertyMeta("org_dn", "orgDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "policy_class_name": MoPropertyMeta("policy_class_name", "policyClassName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "identType": "ident_type", 
        "invDn": "inv_dn", 
        "name": "name", 
        "orgDn": "org_dn", 
        "policyClassName": "policy_class_name", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.ident_type = None
        self.inv_dn = None
        self.name = None
        self.org_dn = None
        self.policy_class_name = None
        self.policy_owner = None
        self.status = None

        ManagedObject.__init__(self, "GlPool", parent_mo_or_dn, **kwargs)

