"""This module contains the general information for AdaptorUnitAssocCtx ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorUnitAssocCtxConsts():
    pass


class AdaptorUnitAssocCtx(ManagedObject):
    """This is AdaptorUnitAssocCtx class."""

    consts = AdaptorUnitAssocCtxConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AdaptorUnitAssocCtx", "adaptorUnitAssocCtx", "adaptorunit-assoc-ctx-[id]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['lsServerAssocCtx'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fru_cap_dn": MoPropertyMeta("fru_cap_dn", "fruCapDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "pci_addr": MoPropertyMeta("pci_addr", "pciAddr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fruCapDn": "fru_cap_dn", 
        "id": "id", 
        "pciAddr": "pci_addr", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.fru_cap_dn = None
        self.pci_addr = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorUnitAssocCtx", parent_mo_or_dn, **kwargs)

