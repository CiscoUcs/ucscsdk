"""This module contains the general information for DomainFamilyCapProvider ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class DomainFamilyCapProviderConsts():
    FAMILY_UCS_CLASSIC = "ucs-classic"
    FAMILY_UCS_CLASSIC_3GEN = "ucs-classic-3gen"
    FAMILY_UCS_CLASSIC_4GEN = "ucs-classic-4gen"
    FAMILY_UCS_CLASSIC_5GEN = "ucs-classic-5gen"
    FAMILY_UCS_MINI = "ucs-mini"
    FAMILY_UCS_X_SERIES_DIRECT = "ucs-x-series-direct"


class DomainFamilyCapProvider(ManagedObject):
    """This is DomainFamilyCapProvider class."""

    consts = DomainFamilyCapProviderConsts()
    naming_props = set(['model'])

    mo_meta = MoMeta("DomainFamilyCapProvider", "domainFamilyCapProvider", "model-[model]", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["read-only"], ['capabilityCatalogue'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "family": MoPropertyMeta("family", "family", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ucs-classic", "ucs-classic-3gen", "ucs-classic-4gen", "ucs-classic-5gen", "ucs-mini", "ucs-x-series-direct"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version121a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "family": "family", 
        "model": "model", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, model, **kwargs):
        self._dirty_mask = 0
        self.model = model
        self.child_action = None
        self.family = None
        self.status = None

        ManagedObject.__init__(self, "DomainFamilyCapProvider", parent_mo_or_dn, **kwargs)

