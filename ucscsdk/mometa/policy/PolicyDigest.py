"""This module contains the general information for PolicyDigest ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyDigestConsts():
    REQUESTOR_OWNERSHIP_LOCAL = "local"
    REQUESTOR_OWNERSHIP_PENDING_POLICY = "pending-policy"
    REQUESTOR_OWNERSHIP_POLICY = "policy"
    REQUESTOR_OWNERSHIP_UNSPECIFIED = "unspecified"
    RESOLVE_TYPE_NAME = "name"
    RESOLVE_TYPE_RN = "rn"


class PolicyDigest(ManagedObject):
    """This is PolicyDigest class."""

    consts = PolicyDigestConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PolicyDigest", "policyDigest", "policy-[name]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "context": MoPropertyMeta("context", "context", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "label": MoPropertyMeta("label", "label", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "on_behalf_of_ident": MoPropertyMeta("on_behalf_of_ident", "onBehalfOfIdent", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "on_behalf_of_type": MoPropertyMeta("on_behalf_of_type", "onBehalfOfType", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "requestor_ownership": MoPropertyMeta("requestor_ownership", "requestorOwnership", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "resolve_type": MoPropertyMeta("resolve_type", "resolveType", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["name", "rn"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "usage": MoPropertyMeta("usage", "usage", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "context": "context", 
        "descr": "descr", 
        "dn": "dn", 
        "label": "label", 
        "name": "name", 
        "onBehalfOfIdent": "on_behalf_of_ident", 
        "onBehalfOfType": "on_behalf_of_type", 
        "requestorOwnership": "requestor_ownership", 
        "resolveType": "resolve_type", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "usage": "usage", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.context = None
        self.descr = None
        self.label = None
        self.on_behalf_of_ident = None
        self.on_behalf_of_type = None
        self.requestor_ownership = None
        self.resolve_type = None
        self.status = None
        self.type = None
        self.usage = None

        ManagedObject.__init__(self, "PolicyDigest", parent_mo_or_dn, **kwargs)

