"""This module contains the general information for BiosVfRedirectionAfterBIOSPOST ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfRedirectionAfterBIOSPOSTConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_REDIRECTION_AFTER_POST_ALWAYS_ENABLE = "always-enable"
    VP_REDIRECTION_AFTER_POST_BOOTLOADER = "bootloader"
    VP_REDIRECTION_AFTER_POST_PLATFORM_DEFAULT = "platform-default"
    VP_REDIRECTION_AFTER_POST_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfRedirectionAfterBIOSPOST(ManagedObject):
    """This is BiosVfRedirectionAfterBIOSPOST class."""

    consts = BiosVfRedirectionAfterBIOSPOSTConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfRedirectionAfterBIOSPOST", "biosVfRedirectionAfterBIOSPOST", "Redirection-After-BIOS-POST", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_redirection_after_post": MoPropertyMeta("vp_redirection_after_post", "vpRedirectionAfterPOST", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["always-enable", "bootloader", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpRedirectionAfterPOST": "vp_redirection_after_post", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_redirection_after_post = None

        ManagedObject.__init__(self, "BiosVfRedirectionAfterBIOSPOST", parent_mo_or_dn, **kwargs)

