"""This module contains the general information for LicenseSource ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LicenseSourceConsts():
    ALWAYS_USE_FALSE = "false"
    ALWAYS_USE_NO = "no"
    ALWAYS_USE_TRUE = "true"
    ALWAYS_USE_YES = "yes"


class LicenseSource(ManagedObject):
    """This is LicenseSource class."""

    consts = LicenseSourceConsts()
    naming_props = set([])

    mo_meta = MoMeta("LicenseSource", "licenseSource", "source", VersionMeta.Version111a, "InputOutput", 0xf, [], ["read-only"], ['licenseFile'], [], ["Get"])

    prop_meta = {
        "always_use": MoPropertyMeta("always_use", "alwaysUse", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "file_sku": MoPropertyMeta("file_sku", "fileSku", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "host_id": MoPropertyMeta("host_id", "hostId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "host_name": MoPropertyMeta("host_name", "hostName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "sku": MoPropertyMeta("sku", "sku", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor_daemon_path": MoPropertyMeta("vendor_daemon_path", "vendorDaemonPath", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "alwaysUse": "always_use", 
        "childAction": "child_action", 
        "dn": "dn", 
        "fileSku": "file_sku", 
        "hostId": "host_id", 
        "hostName": "host_name", 
        "rn": "rn", 
        "sku": "sku", 
        "status": "status", 
        "vendorDaemonPath": "vendor_daemon_path", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.always_use = None
        self.child_action = None
        self.file_sku = None
        self.host_id = None
        self.host_name = None
        self.sku = None
        self.status = None
        self.vendor_daemon_path = None

        ManagedObject.__init__(self, "LicenseSource", parent_mo_or_dn, **kwargs)

