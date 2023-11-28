"""This module contains the general information for LsbootBootSecurity ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsbootBootSecurityConsts():
    SECURE_BOOT_FALSE = "false"
    SECURE_BOOT_NO = "no"
    SECURE_BOOT_TRUE = "true"
    SECURE_BOOT_YES = "yes"


class LsbootBootSecurity(ManagedObject):
    """This is LsbootBootSecurity class."""

    consts = LsbootBootSecurityConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootBootSecurity", "lsbootBootSecurity", "boot-security", VersionMeta.Version112a, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['lsbootDef', 'lsbootPolicy'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "secure_boot": MoPropertyMeta("secure_boot", "secureBoot", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "secureBoot": "secure_boot", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.secure_boot = None
        self.status = None

        ManagedObject.__init__(self, "LsbootBootSecurity", parent_mo_or_dn, **kwargs)

