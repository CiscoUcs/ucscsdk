"""This module contains the general information for PolicyScope ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyScopeConsts():
    RESOLVE_TYPE_NAME = "name"
    RESOLVE_TYPE_RN = "rn"


class PolicyScope(ManagedObject):
    """This is PolicyScope class."""

    consts = PolicyScopeConsts()
    naming_props = set(['policyType', 'resolveType', 'policyName'])

    mo_meta = MoMeta("PolicyScope", "policyScope", "scope-[policy_type]-[resolve_type]-[policy_name]", VersionMeta.Version201b, "InputOutput", 0x7f, [], ["read-only"], ['policyContext'], ['policyPolicyDestClass', 'policyRequestor'], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "policy_name": MoPropertyMeta("policy_name", "policyName", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "policy_type": MoPropertyMeta("policy_type", "policyType", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "resolve_type": MoPropertyMeta("resolve_type", "resolveType", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x10, None, None, None, ["name", "rn"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "policyName": "policy_name", 
        "policyType": "policy_type", 
        "resolveType": "resolve_type", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, policy_type, resolve_type, policy_name, **kwargs):
        self._dirty_mask = 0
        self.policy_type = policy_type
        self.resolve_type = resolve_type
        self.policy_name = policy_name
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "PolicyScope", parent_mo_or_dn, **kwargs)

