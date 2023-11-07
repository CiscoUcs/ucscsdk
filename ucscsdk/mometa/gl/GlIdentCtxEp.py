"""This module contains the general information for GlIdentCtxEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlIdentCtxEpConsts():
    pass


class GlIdentCtxEp(ManagedObject):
    """This is GlIdentCtxEp class."""

    consts = GlIdentCtxEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("GlIdentCtxEp", "glIdentCtxEp", "icp", VersionMeta.Version201b, "InputOutput", 0xf, [], ["read-only"], ['glOperationEp', 'glPolicyResolutionEp', 'glServiceProfile'], ['glIdentCtxOp', 'glIdentCtxResOp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_conflicts": MoPropertyMeta("num_of_conflicts", "numOfConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_server_pool_and_id_conflicts": MoPropertyMeta("num_of_server_pool_and_id_conflicts", "numOfServerPoolAndIdConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "index": "index", 
        "numOfConflicts": "num_of_conflicts", 
        "numOfServerPoolAndIdConflicts": "num_of_server_pool_and_id_conflicts", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.index = None
        self.num_of_conflicts = None
        self.num_of_server_pool_and_id_conflicts = None
        self.status = None

        ManagedObject.__init__(self, "GlIdentCtxEp", parent_mo_or_dn, **kwargs)

