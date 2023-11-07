"""This module contains the general information for LicenseFeatureLine ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LicenseFeatureLineConsts():
    EXP_NEVER = "never"
    TYPE_FEATURE = "feature"
    TYPE_INCREMENT = "increment"
    TYPE_UPGRADE = "upgrade"


class LicenseFeatureLine(ManagedObject):
    """This is LicenseFeatureLine class."""

    consts = LicenseFeatureLineConsts()
    naming_props = set(['id', 'type'])

    mo_meta = MoMeta("LicenseFeatureLine", "licenseFeatureLine", "FeatureLine-[id]:[type]", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["read-only"], ['licenseContents'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "exp": MoPropertyMeta("exp", "exp", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "file_sku": MoPropertyMeta("file_sku", "fileSku", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, 1, 32, None, [], []), 
        "pak": MoPropertyMeta("pak", "pak", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "quant": MoPropertyMeta("quant", "quant", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sig": MoPropertyMeta("sig", "sig", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "sku": MoPropertyMeta("sku", "sku", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x20, None, None, None, ["feature", "increment", "upgrade"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "exp": "exp", 
        "fileSku": "file_sku", 
        "id": "id", 
        "pak": "pak", 
        "quant": "quant", 
        "rn": "rn", 
        "sig": "sig", 
        "sku": "sku", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, type, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.type = type
        self.child_action = None
        self.exp = None
        self.file_sku = None
        self.pak = None
        self.quant = None
        self.sig = None
        self.sku = None
        self.status = None

        ManagedObject.__init__(self, "LicenseFeatureLine", parent_mo_or_dn, **kwargs)

