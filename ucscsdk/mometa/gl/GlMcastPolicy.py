"""This module contains the general information for GlMcastPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlMcastPolicyConsts():
    OPER_STATE_CONFLICT = "Conflict"
    OPER_STATE_CONFLICT_RESOLVED = "ConflictResolved"
    OPER_STATE_FAILED_TO_GLOBALIZE = "FailedToGlobalize"
    OPER_STATE_GLOBALIZED = "Globalized"
    OPER_STATE_GLOBALIZING = "Globalizing"
    OPER_STATE_NOT_CONFLICT = "NotConflict"
    OPER_STATE_NOT_EVALUATED = "NotEvaluated"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class GlMcastPolicy(ManagedObject):
    """This is GlMcastPolicy class."""

    consts = GlMcastPolicyConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("GlMcastPolicy", "glMcastPolicy", "mc-policy[id]", VersionMeta.Version201b, "InputOutput", 0x3f, [], ["admin"], ['glVnetInvHolder'], ['messageEp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "context_dn": MoPropertyMeta("context_dn", "contextDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, None, [], []), 
        "deploy_dn": MoPropertyMeta("deploy_dn", "deployDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "globalized_dn": MoPropertyMeta("globalized_dn", "globalizedDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "inv_dn": MoPropertyMeta("inv_dn", "invDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Conflict", "ConflictResolved", "FailedToGlobalize", "Globalized", "Globalizing", "NotConflict", "NotEvaluated"], []), 
        "policy_class_name": MoPropertyMeta("policy_class_name", "policyClassName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "contextDn": "context_dn", 
        "deployDn": "deploy_dn", 
        "dn": "dn", 
        "globalizedDn": "globalized_dn", 
        "id": "id", 
        "invDn": "inv_dn", 
        "name": "name", 
        "operState": "oper_state", 
        "policyClassName": "policy_class_name", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.context_dn = None
        self.deploy_dn = None
        self.globalized_dn = None
        self.inv_dn = None
        self.name = None
        self.oper_state = None
        self.policy_class_name = None
        self.policy_owner = None
        self.status = None

        ManagedObject.__init__(self, "GlMcastPolicy", parent_mo_or_dn, **kwargs)

