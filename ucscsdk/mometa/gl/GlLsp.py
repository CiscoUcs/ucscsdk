"""This module contains the general information for GlLsp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlLspConsts():
    TYPE_INITIAL_TEMPLATE = "initial-template"
    TYPE_INSTANCE = "instance"
    TYPE_UPDATING_TEMPLATE = "updating-template"


class GlLsp(ManagedObject):
    """This is GlLsp class."""

    consts = GlLspConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("GlLsp", "glLsp", "lsp-[id]", VersionMeta.Version201b, "InputOutput", 0x3f, [], ["admin"], ['glRequest'], ['glOperationEp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "compute_instance_dn": MoPropertyMeta("compute_instance_dn", "computeInstanceDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "lsp_dn": MoPropertyMeta("lsp_dn", "lspDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "org_dn": MoPropertyMeta("org_dn", "orgDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["initial-template", "instance", "updating-template"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "computeInstanceDn": "compute_instance_dn", 
        "dn": "dn", 
        "id": "id", 
        "lspDn": "lsp_dn", 
        "orgDn": "org_dn", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.compute_instance_dn = None
        self.lsp_dn = None
        self.org_dn = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "GlLsp", parent_mo_or_dn, **kwargs)

