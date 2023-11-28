"""This module contains the general information for BiosVfIntegratedGraphicsApertureSize ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfIntegratedGraphicsApertureSizeConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_INTEGRATED_GRAPHICS_APERTURE_SIZE_1024MB = "1024mb"
    VP_INTEGRATED_GRAPHICS_APERTURE_SIZE_128MB = "128mb"
    VP_INTEGRATED_GRAPHICS_APERTURE_SIZE_2048MB = "2048mb"
    VP_INTEGRATED_GRAPHICS_APERTURE_SIZE_256MB = "256mb"
    VP_INTEGRATED_GRAPHICS_APERTURE_SIZE_4096MB = "4096mb"
    VP_INTEGRATED_GRAPHICS_APERTURE_SIZE_512MB = "512mb"
    VP_INTEGRATED_GRAPHICS_APERTURE_SIZE_PLATFORM_DEFAULT = "platform-default"
    VP_INTEGRATED_GRAPHICS_APERTURE_SIZE_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfIntegratedGraphicsApertureSize(ManagedObject):
    """This is BiosVfIntegratedGraphicsApertureSize class."""

    consts = BiosVfIntegratedGraphicsApertureSizeConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfIntegratedGraphicsApertureSize", "biosVfIntegratedGraphicsApertureSize", "Integrated-Graphics-Aperture-Size", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_integrated_graphics_aperture_size": MoPropertyMeta("vp_integrated_graphics_aperture_size", "vpIntegratedGraphicsApertureSize", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1024mb", "128mb", "2048mb", "256mb", "4096mb", "512mb", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpIntegratedGraphicsApertureSize": "vp_integrated_graphics_aperture_size", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_integrated_graphics_aperture_size = None

        ManagedObject.__init__(self, "BiosVfIntegratedGraphicsApertureSize", parent_mo_or_dn, **kwargs)

