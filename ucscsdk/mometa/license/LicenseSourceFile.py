"""This module contains the general information for LicenseSourceFile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LicenseSourceFileConsts():
    EXP_NEVER = "never"
    TYPE_FEATURE = "feature"
    TYPE_INCREMENT = "increment"
    TYPE_UPGRADE = "upgrade"


class LicenseSourceFile(ManagedObject):
    """This is LicenseSourceFile class."""

    consts = LicenseSourceFileConsts()
    naming_props = set(['id', 'line'])

    mo_meta = MoMeta("LicenseSourceFile", "licenseSourceFile", "src-[id]:[line]", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["read-only"], ['licenseInstance'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "exp": MoPropertyMeta("exp", "exp", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "host_id": MoPropertyMeta("host_id", "hostId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, 1, 32, None, [], []), 
        "line": MoPropertyMeta("line", "line", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "pak": MoPropertyMeta("pak", "pak", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "quant": MoPropertyMeta("quant", "quant", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sig": MoPropertyMeta("sig", "sig", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["feature", "increment", "upgrade"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "exp": "exp", 
        "hostId": "host_id", 
        "id": "id", 
        "line": "line", 
        "pak": "pak", 
        "quant": "quant", 
        "rn": "rn", 
        "sig": "sig", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, line, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.line = line
        self.child_action = None
        self.exp = None
        self.host_id = None
        self.pak = None
        self.quant = None
        self.sig = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LicenseSourceFile", parent_mo_or_dn, **kwargs)

