"""This module contains the general information for FirmwareBundleType ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareBundleTypeConsts():
    TYPE_B_SERIES_BUNDLE = "b-series-bundle"
    TYPE_C_SERIES_BUNDLE = "c-series-bundle"
    TYPE_CATALOG = "catalog"
    TYPE_CHASSIS_BUNDLE = "chassis-bundle"
    TYPE_FULL_BUNDLE = "full-bundle"
    TYPE_IMAGE = "image"
    TYPE_INFRASTRUCTURE_BUNDLE = "infrastructure-bundle"
    TYPE_M_SERIES_BUNDLE = "m-series-bundle"
    TYPE_PROVIDER_BUNDLE = "provider-bundle"
    TYPE_S_SERIES_BUNDLE = "s-series-bundle"
    TYPE_SERVICE_PACK_BUNDLE = "service-pack-bundle"
    TYPE_UNKNOWN = "unknown"


class FirmwareBundleType(ManagedObject):
    """This is FirmwareBundleType class."""

    consts = FirmwareBundleTypeConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("FirmwareBundleType", "firmwareBundleType", "-type-[type]", VersionMeta.Version101a, "InputOutput", 0x1f, [], [""], ['firmwareBundleTypeCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "inv_tag": MoPropertyMeta("inv_tag", "invTag", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["b-series-bundle", "c-series-bundle", "catalog", "chassis-bundle", "full-bundle", "image", "infrastructure-bundle", "m-series-bundle", "provider-bundle", "s-series-bundle", "service-pack-bundle", "unknown"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "invTag": "inv_tag", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.inv_tag = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareBundleType", parent_mo_or_dn, **kwargs)

