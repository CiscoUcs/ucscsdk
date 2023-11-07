"""This module contains the general information for GlPathEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlPathEpConsts():
    pass


class GlPathEp(ManagedObject):
    """This is GlPathEp class."""

    consts = GlPathEpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("GlPathEp", "glPathEp", "path-[id]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["admin"], ['glRequest'], ['glInventoryEp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "leaf_lsp_dn": MoPropertyMeta("leaf_lsp_dn", "leafLspDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "leaf_org_dn": MoPropertyMeta("leaf_org_dn", "leafOrgDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "leafLspDn": "leaf_lsp_dn", 
        "leafOrgDn": "leaf_org_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.leaf_lsp_dn = None
        self.leaf_org_dn = None
        self.status = None

        ManagedObject.__init__(self, "GlPathEp", parent_mo_or_dn, **kwargs)

