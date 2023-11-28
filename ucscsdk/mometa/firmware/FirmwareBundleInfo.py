"""This module contains the general information for FirmwareBundleInfo ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareBundleInfoConsts():
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


class FirmwareBundleInfo(ManagedObject):
    """This is FirmwareBundleInfo class."""

    consts = FirmwareBundleInfoConsts()
    naming_props = set(['type', 'version'])

    mo_meta = MoMeta("FirmwareBundleInfo", "firmwareBundleInfo", "bundle-[type]-[version]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin", "domain-group-management", "ls-compute", "ls-config-policy", "ls-server-policy"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["b-series-bundle", "c-series-bundle", "catalog", "chassis-bundle", "full-bundle", "image", "infrastructure-bundle", "m-series-bundle", "provider-bundle", "s-series-bundle", "service-pack-bundle", "unknown"], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, type, version, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.version = version
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareBundleInfo", parent_mo_or_dn, **kwargs)

