"""This module contains the general information for BiosVfEnhancedPowerCappingSupport ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfEnhancedPowerCappingSupportConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_ENHANCED_POWER_CAPPING_DISABLED = "disabled"
    VP_ENHANCED_POWER_CAPPING_ENABLED = "enabled"
    VP_ENHANCED_POWER_CAPPING_PLATFORM_DEFAULT = "platform-default"
    VP_ENHANCED_POWER_CAPPING_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfEnhancedPowerCappingSupport(ManagedObject):
    """This is BiosVfEnhancedPowerCappingSupport class."""

    consts = BiosVfEnhancedPowerCappingSupportConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfEnhancedPowerCappingSupport", "biosVfEnhancedPowerCappingSupport", "Enhanced-PowerCapping-Support", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_enhanced_power_capping": MoPropertyMeta("vp_enhanced_power_capping", "vpEnhancedPowerCapping", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpEnhancedPowerCapping": "vp_enhanced_power_capping", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_enhanced_power_capping = None

        ManagedObject.__init__(self, "BiosVfEnhancedPowerCappingSupport", parent_mo_or_dn, **kwargs)

