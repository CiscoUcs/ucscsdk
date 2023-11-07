"""This module contains the general information for LicenseContents ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LicenseContentsConsts():
    pass


class LicenseContents(ManagedObject):
    """This is LicenseContents class."""

    consts = LicenseContentsConsts()
    naming_props = set(['featureName'])

    mo_meta = MoMeta("LicenseContents", "licenseContents", "contents-[feature_name]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['licenseFile'], ['licenseFeatureLine'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "feature_name": MoPropertyMeta("feature_name", "featureName", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, 1, 64, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "total_quant": MoPropertyMeta("total_quant", "totalQuant", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "featureName": "feature_name", 
        "rn": "rn", 
        "status": "status", 
        "totalQuant": "total_quant", 
        "vendor": "vendor", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, feature_name, **kwargs):
        self._dirty_mask = 0
        self.feature_name = feature_name
        self.child_action = None
        self.status = None
        self.total_quant = None
        self.vendor = None
        self.version = None

        ManagedObject.__init__(self, "LicenseContents", parent_mo_or_dn, **kwargs)

