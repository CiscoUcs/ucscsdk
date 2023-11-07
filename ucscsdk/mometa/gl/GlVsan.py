"""This module contains the general information for GlVsan ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlVsanConsts():
    IF_ROLE_DIAG = "diag"
    IF_ROLE_FCOE_NAS_STORAGE = "fcoe-nas-storage"
    IF_ROLE_FCOE_STORAGE = "fcoe-storage"
    IF_ROLE_FCOE_UPLINK = "fcoe-uplink"
    IF_ROLE_MGMT = "mgmt"
    IF_ROLE_MONITOR = "monitor"
    IF_ROLE_NAS_STORAGE = "nas-storage"
    IF_ROLE_NETWORK = "network"
    IF_ROLE_NETWORK_FCOE_UPLINK = "network-fcoe-uplink"
    IF_ROLE_SERVER = "server"
    IF_ROLE_SERVICE = "service"
    IF_ROLE_STORAGE = "storage"
    IF_ROLE_UNKNOWN = "unknown"
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
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"


class GlVsan(ManagedObject):
    """This is GlVsan class."""

    consts = GlVsanConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("GlVsan", "glVsan", "vsan-[id]", VersionMeta.Version201b, "InputOutput", 0x3f, [], ["admin"], ['glVnetInvHolder'], ['messageEp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "context_dn": MoPropertyMeta("context_dn", "contextDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, None, [], []), 
        "deploy_dn": MoPropertyMeta("deploy_dn", "deployDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "globalized_dn": MoPropertyMeta("globalized_dn", "globalizedDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []), 
        "inv_dn": MoPropertyMeta("inv_dn", "invDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Conflict", "ConflictResolved", "FailedToGlobalize", "Globalized", "Globalizing", "NotConflict", "NotEvaluated"], []), 
        "policy_class_name": MoPropertyMeta("policy_class_name", "policyClassName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
        "vnet_id": MoPropertyMeta("vnet_id", "vnetId", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "contextDn": "context_dn", 
        "deployDn": "deploy_dn", 
        "dn": "dn", 
        "globalizedDn": "globalized_dn", 
        "id": "id", 
        "ifRole": "if_role", 
        "invDn": "inv_dn", 
        "name": "name", 
        "operState": "oper_state", 
        "policyClassName": "policy_class_name", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
        "vnetId": "vnet_id", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.context_dn = None
        self.deploy_dn = None
        self.globalized_dn = None
        self.if_role = None
        self.inv_dn = None
        self.name = None
        self.oper_state = None
        self.policy_class_name = None
        self.policy_owner = None
        self.status = None
        self.switch_id = None
        self.type = None
        self.vnet_id = None

        ManagedObject.__init__(self, "GlVsan", parent_mo_or_dn, **kwargs)

