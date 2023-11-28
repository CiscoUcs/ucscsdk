"""This module contains the general information for PolicyPolicyDestClass ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyPolicyDestClassConsts():
    ACTION_DELETE = "delete"
    ACTION_LOCALIZE = "localize"
    ACTION_NO_ACTION = "no-action"
    OVERWRITE_FALSE = "false"
    OVERWRITE_NO = "no"
    OVERWRITE_TRUE = "true"
    OVERWRITE_YES = "yes"


class PolicyPolicyDestClass(ManagedObject):
    """This is PolicyPolicyDestClass class."""

    consts = PolicyPolicyDestClassConsts()
    naming_props = set([])

    mo_meta = MoMeta("PolicyPolicyDestClass", "policyPolicyDestClass", "destclass", VersionMeta.Version201b, "InputOutput", 0xf, [], ["read-only"], ['policyScope'], ['policyDestClass'], ["get"])

    prop_meta = {
        "action": MoPropertyMeta("action", "action", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["delete", "localize", "no-action"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "mo_dn": MoPropertyMeta("mo_dn", "moDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "overwrite": MoPropertyMeta("overwrite", "overwrite", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "action": "action", 
        "childAction": "child_action", 
        "dn": "dn", 
        "moDn": "mo_dn", 
        "name": "name", 
        "overwrite": "overwrite", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.action = None
        self.child_action = None
        self.mo_dn = None
        self.name = None
        self.overwrite = None
        self.status = None

        ManagedObject.__init__(self, "PolicyPolicyDestClass", parent_mo_or_dn, **kwargs)

