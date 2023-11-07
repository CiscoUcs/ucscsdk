"""This module contains the general information for PolicyPolicyScopeContext ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyPolicyScopeContextConsts():
    pass


class PolicyPolicyScopeContext(ManagedObject):
    """This is PolicyPolicyScopeContext class."""

    consts = PolicyPolicyScopeContextConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PolicyPolicyScopeContext", "policyPolicyScopeContext", "context-[name]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin"], ['policyPolicyScopeCont'], ['policyPolicyScope'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "context": MoPropertyMeta("context", "context", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x2, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "context": "context", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.context = None
        self.status = None

        ManagedObject.__init__(self, "PolicyPolicyScopeContext", parent_mo_or_dn, **kwargs)

