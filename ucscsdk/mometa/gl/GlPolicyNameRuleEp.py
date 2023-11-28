"""This module contains the general information for GlPolicyNameRuleEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlPolicyNameRuleEpConsts():
    TYPE_NO_AUTO = "no-auto"
    TYPE_RENAME_AFTER_EVALUATE = "rename-after-evaluate"
    TYPE_RENAME_BEFORE_EVALUATE = "rename-before-evaluate"


class GlPolicyNameRuleEp(ManagedObject):
    """This is GlPolicyNameRuleEp class."""

    consts = GlPolicyNameRuleEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("GlPolicyNameRuleEp", "glPolicyNameRuleEp", "policyep", VersionMeta.Version201b, "InputOutput", 0x3f, [], ["admin"], ['glConflictResolutionRuleEp'], ['glAppendRule'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "max_rule_apply_times": MoPropertyMeta("max_rule_apply_times", "maxRuleApplyTimes", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["no-auto", "rename-after-evaluate", "rename-before-evaluate"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maxRuleApplyTimes": "max_rule_apply_times", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.max_rule_apply_times = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "GlPolicyNameRuleEp", parent_mo_or_dn, **kwargs)

