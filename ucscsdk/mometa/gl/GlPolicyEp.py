"""This module contains the general information for GlPolicyEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlPolicyEpConsts():
    pass


class GlPolicyEp(ManagedObject):
    """This is GlPolicyEp class."""

    consts = GlPolicyEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("GlPolicyEp", "glPolicyEp", "paep", VersionMeta.Version201b, "InputOutput", 0xf, [], ["read-only"], [u'glOperationEp', u'glPolicyResolutionEp'], [u'glPolicyAlgorithmedOp', u'glPolicyOp', u'glPolicyResOp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_advance_policy_conflicts": MoPropertyMeta("num_of_advance_policy_conflicts", "numOfAdvancePolicyConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_conflicts": MoPropertyMeta("num_of_conflicts", "numOfConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_simple_policy_conflicts": MoPropertyMeta("num_of_simple_policy_conflicts", "numOfSimplePolicyConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "index": "index", 
        "numOfAdvancePolicyConflicts": "num_of_advance_policy_conflicts", 
        "numOfConflicts": "num_of_conflicts", 
        "numOfSimplePolicyConflicts": "num_of_simple_policy_conflicts", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.index = None
        self.num_of_advance_policy_conflicts = None
        self.num_of_conflicts = None
        self.num_of_simple_policy_conflicts = None
        self.status = None

        ManagedObject.__init__(self, "GlPolicyEp", parent_mo_or_dn, **kwargs)

