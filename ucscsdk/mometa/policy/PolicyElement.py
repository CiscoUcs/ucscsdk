"""This module contains the general information for PolicyElement ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyElementConsts():
    OWNERSHIP_LOCAL = "local"
    OWNERSHIP_PENDING_POLICY = "pending-policy"
    OWNERSHIP_POLICY = "policy"
    OWNERSHIP_UNSPECIFIED = "unspecified"


class PolicyElement(ManagedObject):
    """This is PolicyElement class."""

    consts = PolicyElementConsts()
    naming_props = set(['convertedDn'])

    mo_meta = MoMeta("PolicyElement", "policyElement", "element-[converted_dn]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin"], ['policyLocalMap'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "class_type": MoPropertyMeta("class_type", "classType", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "converted_dn": MoPropertyMeta("converted_dn", "convertedDn", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x2, 1, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "policy_dn": MoPropertyMeta("policy_dn", "policyDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "classType": "class_type", 
        "convertedDn": "converted_dn", 
        "dn": "dn", 
        "ownership": "ownership", 
        "policyDn": "policy_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, converted_dn, **kwargs):
        self._dirty_mask = 0
        self.converted_dn = converted_dn
        self.child_action = None
        self.class_type = None
        self.ownership = None
        self.policy_dn = None
        self.status = None

        ManagedObject.__init__(self, "PolicyElement", parent_mo_or_dn, **kwargs)

