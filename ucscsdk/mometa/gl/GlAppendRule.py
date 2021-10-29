"""This module contains the general information for GlAppendRule ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlAppendRuleConsts():
    PATTERN_NUMBER = "number"


class GlAppendRule(ManagedObject):
    """This is GlAppendRule class."""

    consts = GlAppendRuleConsts()
    naming_props = set([])

    mo_meta = MoMeta("GlAppendRule", "glAppendRule", "appendrule", VersionMeta.Version201b, "InputOutput", 0x7f, [], ["admin"], [u'glPolicyNameRuleEp'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "max": MoPropertyMeta("max", "max", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "min": MoPropertyMeta("min", "min", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "pattern": MoPropertyMeta("pattern", "pattern", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["number"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "max": "max", 
        "min": "min", 
        "pattern": "pattern", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.max = None
        self.min = None
        self.pattern = None
        self.status = None

        ManagedObject.__init__(self, "GlAppendRule", parent_mo_or_dn, **kwargs)

