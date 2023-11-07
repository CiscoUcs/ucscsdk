"""This module contains the general information for ProcessorUnitAssocCtx ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ProcessorUnitAssocCtxConsts():
    STEPPING_UNSPECIFIED = "unspecified"


class ProcessorUnitAssocCtx(ManagedObject):
    """This is ProcessorUnitAssocCtx class."""

    consts = ProcessorUnitAssocCtxConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcessorUnitAssocCtx", "processorUnitAssocCtx", "procunit-assoc-ctx", VersionMeta.Version111a, "InputOutput", 0xf, [], ["read-only"], ['lsServerAssocCtx'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fru_cap_dn": MoPropertyMeta("fru_cap_dn", "fruCapDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "stepping": MoPropertyMeta("stepping", "stepping", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fruCapDn": "fru_cap_dn", 
        "rn": "rn", 
        "status": "status", 
        "stepping": "stepping", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.fru_cap_dn = None
        self.status = None
        self.stepping = None

        ManagedObject.__init__(self, "ProcessorUnitAssocCtx", parent_mo_or_dn, **kwargs)

