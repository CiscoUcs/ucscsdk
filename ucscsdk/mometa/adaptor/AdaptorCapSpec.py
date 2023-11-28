"""This module contains the general information for AdaptorCapSpec ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorCapSpecConsts():
    MAXIMUM_UNSPECIFIED = "unspecified"


class AdaptorCapSpec(ManagedObject):
    """This is AdaptorCapSpec class."""

    consts = AdaptorCapSpecConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("AdaptorCapSpec", "adaptorCapSpec", "cap-[type]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['adaptorFruCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fw_version_hi": MoPropertyMeta("fw_version_hi", "fwVersionHi", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "fw_version_lo": MoPropertyMeta("fw_version_lo", "fwVersionLo", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "fw_version_opr": MoPropertyMeta("fw_version_opr", "fwVersionOpr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "maximum": MoPropertyMeta("maximum", "maximum", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "nf_version_lo": MoPropertyMeta("nf_version_lo", "nfVersionLo", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fwVersionHi": "fw_version_hi", 
        "fwVersionLo": "fw_version_lo", 
        "fwVersionOpr": "fw_version_opr", 
        "maximum": "maximum", 
        "nfVersionLo": "nf_version_lo", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.fw_version_hi = None
        self.fw_version_lo = None
        self.fw_version_opr = None
        self.maximum = None
        self.nf_version_lo = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorCapSpec", parent_mo_or_dn, **kwargs)

