"""This module contains the general information for GlVnicTemplate ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlVnicTemplateConsts():
    pass


class GlVnicTemplate(ManagedObject):
    """This is GlVnicTemplate class."""

    consts = GlVnicTemplateConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("GlVnicTemplate", "glVnicTemplate", "vt-[id]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["read-only"], ['glVnicTemplateEp'], ['glOperationEp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "oper_template_name": MoPropertyMeta("oper_template_name", "operTemplateName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "template_name": MoPropertyMeta("template_name", "templateName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "operTemplateName": "oper_template_name", 
        "rn": "rn", 
        "status": "status", 
        "templateName": "template_name", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.oper_template_name = None
        self.status = None
        self.template_name = None

        ManagedObject.__init__(self, "GlVnicTemplate", parent_mo_or_dn, **kwargs)

