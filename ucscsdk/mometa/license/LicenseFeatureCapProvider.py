"""This module contains the general information for LicenseFeatureCapProvider ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LicenseFeatureCapProviderConsts():
    DEPRECATED_FALSE = "false"
    DEPRECATED_NO = "no"
    DEPRECATED_TRUE = "true"
    DEPRECATED_YES = "yes"
    TYPE_BOOLEAN = "boolean"
    TYPE_COUNTED = "counted"


class LicenseFeatureCapProvider(ManagedObject):
    """This is LicenseFeatureCapProvider class."""

    consts = LicenseFeatureCapProviderConsts()
    naming_props = set(['featureName', 'licVendor', 'licVersion', 'vendor', 'model', 'revision'])

    mo_meta = MoMeta("LicenseFeatureCapProvider", "licenseFeatureCapProvider", "feature-[feature_name]-[lic_vendor]|[lic_version]manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version111a, "InputOutput", 0x1fff, [], ["admin"], ['capabilityCatalogue'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_quant": MoPropertyMeta("def_quant", "defQuant", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []), 
        "deprecated": MoPropertyMeta("deprecated", "deprecated", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "feature_name": MoPropertyMeta("feature_name", "featureName", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, 1, 64, None, [], []), 
        "gencount": MoPropertyMeta("gencount", "gencount", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "grace_period": MoPropertyMeta("grace_period", "gracePeriod", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "lic_vendor": MoPropertyMeta("lic_vendor", "licVendor", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []), 
        "lic_version": MoPropertyMeta("lic_version", "licVersion", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x40, 1, 510, None, [], []), 
        "mgmt_plane_ver": MoPropertyMeta("mgmt_plane_ver", "mgmtPlaneVer", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x100, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []), 
        "sku": MoPropertyMeta("sku", "sku", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["boolean", "counted"], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x1000, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "defQuant": "def_quant", 
        "deprecated": "deprecated", 
        "dn": "dn", 
        "featureName": "feature_name", 
        "gencount": "gencount", 
        "gracePeriod": "grace_period", 
        "licVendor": "lic_vendor", 
        "licVersion": "lic_version", 
        "mgmtPlaneVer": "mgmt_plane_ver", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "sku": "sku", 
        "status": "status", 
        "type": "type", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, feature_name, lic_vendor, lic_version, vendor, model, revision, **kwargs):
        self._dirty_mask = 0
        self.feature_name = feature_name
        self.lic_vendor = lic_vendor
        self.lic_version = lic_version
        self.vendor = vendor
        self.model = model
        self.revision = revision
        self.child_action = None
        self.def_quant = None
        self.deprecated = None
        self.gencount = None
        self.grace_period = None
        self.mgmt_plane_ver = None
        self.sku = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LicenseFeatureCapProvider", parent_mo_or_dn, **kwargs)

