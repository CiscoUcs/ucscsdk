"""This module contains the general information for OrgExtension ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class OrgExtensionConsts():
    pass


class OrgExtension(ManagedObject):
    """This is OrgExtension class."""

    consts = OrgExtensionConsts()
    naming_props = set([])

    mo_meta = MoMeta("OrgExtension", "orgExtension", "extension", VersionMeta.Version121a, "InputOutput", 0xf, [], ["read-only"], ['orgOrg'], [], ["Get"])

    prop_meta = {
        "cp_count": MoPropertyMeta("cp_count", "CPCount", "ulong", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "cp_template_count": MoPropertyMeta("cp_template_count", "CPTemplateCount", "ulong", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "sp_count": MoPropertyMeta("sp_count", "SPCount", "ulong", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "template_count": MoPropertyMeta("template_count", "TemplateCount", "ulong", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "CPCount": "cp_count", 
        "CPTemplateCount": "cp_template_count", 
        "SPCount": "sp_count", 
        "TemplateCount": "template_count", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.cp_count = None
        self.cp_template_count = None
        self.sp_count = None
        self.template_count = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "OrgExtension", parent_mo_or_dn, **kwargs)

