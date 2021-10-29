"""This module contains the general information for GlRequestorEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlRequestorEpConsts():
    pass


class GlRequestorEp(ManagedObject):
    """This is GlRequestorEp class."""

    consts = GlRequestorEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("GlRequestorEp", "glRequestorEp", "reqep", VersionMeta.Version201b, "InputOutput", 0xf, [], ["read-only"], [u'glBlockOp', u'glIdentCtxOp', u'glIdentCtxResOp', u'glPolicyAlgorithmedOp', u'glPolicyOp', u'glPolicyResOp', u'glPoolOp', u'glServerPoolResOp', u'glTemplateOp', u'glTemplateResOp', u'glVxanOp', u'glVxanResOp'], [u'glRequestor'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "index": "index", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.index = None
        self.status = None

        ManagedObject.__init__(self, "GlRequestorEp", parent_mo_or_dn, **kwargs)

