"""This module contains the general information for BiosVfIntelTurboBoostTech ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfIntelTurboBoostTechConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_INTEL_TURBO_BOOST_TECH_DISABLED = "disabled"
    VP_INTEL_TURBO_BOOST_TECH_ENABLED = "enabled"
    VP_INTEL_TURBO_BOOST_TECH_PLATFORM_DEFAULT = "platform-default"
    VP_INTEL_TURBO_BOOST_TECH_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfIntelTurboBoostTech(ManagedObject):
    """This is BiosVfIntelTurboBoostTech class."""

    consts = BiosVfIntelTurboBoostTechConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfIntelTurboBoostTech", "biosVfIntelTurboBoostTech", "Intel-Turbo-Boost-Tech", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_intel_turbo_boost_tech": MoPropertyMeta("vp_intel_turbo_boost_tech", "vpIntelTurboBoostTech", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpIntelTurboBoostTech": "vp_intel_turbo_boost_tech", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_intel_turbo_boost_tech = None

        ManagedObject.__init__(self, "BiosVfIntelTurboBoostTech", parent_mo_or_dn, **kwargs)

