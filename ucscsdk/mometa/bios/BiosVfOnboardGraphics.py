"""This module contains the general information for BiosVfOnboardGraphics ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfOnboardGraphicsConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_ONBOARD_GRAPHICS_DISABLED = "disabled"
    VP_ONBOARD_GRAPHICS_ENABLED = "enabled"
    VP_ONBOARD_GRAPHICS_PLATFORM_DEFAULT = "platform-default"
    VP_ONBOARD_GRAPHICS_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfOnboardGraphics(ManagedObject):
    """This is BiosVfOnboardGraphics class."""

    consts = BiosVfOnboardGraphicsConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfOnboardGraphics", "biosVfOnboardGraphics", "Onboard-Graphics", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_onboard_graphics": MoPropertyMeta("vp_onboard_graphics", "vpOnboardGraphics", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpOnboardGraphics": "vp_onboard_graphics", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_onboard_graphics = None

        ManagedObject.__init__(self, "BiosVfOnboardGraphics", parent_mo_or_dn, **kwargs)

