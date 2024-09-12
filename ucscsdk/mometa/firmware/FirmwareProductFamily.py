"""This module contains the general information for FirmwareProductFamily ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareProductFamilyConsts():
    FAMILY_NAME_UCS_CLASSIC = "ucs-classic"
    FAMILY_NAME_UCS_CLASSIC_3GEN = "ucs-classic-3gen"
    FAMILY_NAME_UCS_CLASSIC_4GEN = "ucs-classic-4gen"
    FAMILY_NAME_UCS_CLASSIC_5GEN = "ucs-classic-5gen"
    FAMILY_NAME_UCS_MINI = "ucs-mini"
    FAMILY_NAME_UCS_X_SERIES_DIRECT = "ucs-x-series-direct"


class FirmwareProductFamily(ManagedObject):
    """This is FirmwareProductFamily class."""

    consts = FirmwareProductFamilyConsts()
    naming_props = set(['familyName'])

    mo_meta = MoMeta("FirmwareProductFamily", "firmwareProductFamily", "fw-family-[family_name]", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["admin", "operations"], ['firmwareDomainInfraProfile', 'firmwareInfraPolicy'], ['firmwareInfraPack', 'firmwareInfraPackConfig'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "family_name": MoPropertyMeta("family_name", "familyName", "string", VersionMeta.Version121a, MoPropertyMeta.NAMING, 0x4, None, None, None, ["ucs-classic", "ucs-classic-3gen", "ucs-classic-4gen", "ucs-classic-5gen", "ucs-mini", "ucs-x-series-direct"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "familyName": "family_name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, family_name, **kwargs):
        self._dirty_mask = 0
        self.family_name = family_name
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareProductFamily", parent_mo_or_dn, **kwargs)

