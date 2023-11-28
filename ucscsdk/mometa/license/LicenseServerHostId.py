"""This module contains the general information for LicenseServerHostId ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LicenseServerHostIdConsts():
    SCOPE_A = "A"
    SCOPE_B = "B"
    SCOPE_SERVER = "server"
    SCOPE_UNKNOWN = "unknown"


class LicenseServerHostId(ManagedObject):
    """This is LicenseServerHostId class."""

    consts = LicenseServerHostIdConsts()
    naming_props = set(['scope'])

    mo_meta = MoMeta("LicenseServerHostId", "licenseServerHostId", "server-host-id-[scope]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['licenseEp'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "host_id": MoPropertyMeta("host_id", "hostId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "scope": MoPropertyMeta("scope", "scope", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, None, None, None, ["A", "B", "server", "unknown"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "hostId": "host_id", 
        "rn": "rn", 
        "scope": "scope", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, scope, **kwargs):
        self._dirty_mask = 0
        self.scope = scope
        self.child_action = None
        self.host_id = None
        self.status = None

        ManagedObject.__init__(self, "LicenseServerHostId", parent_mo_or_dn, **kwargs)

