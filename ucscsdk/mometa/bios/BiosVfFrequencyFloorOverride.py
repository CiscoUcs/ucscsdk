"""This module contains the general information for BiosVfFrequencyFloorOverride ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfFrequencyFloorOverrideConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_FREQUENCY_FLOOR_OVERRIDE_DISABLED = "disabled"
    VP_FREQUENCY_FLOOR_OVERRIDE_ENABLED = "enabled"
    VP_FREQUENCY_FLOOR_OVERRIDE_PLATFORM_DEFAULT = "platform-default"
    VP_FREQUENCY_FLOOR_OVERRIDE_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfFrequencyFloorOverride(ManagedObject):
    """This is BiosVfFrequencyFloorOverride class."""

    consts = BiosVfFrequencyFloorOverrideConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfFrequencyFloorOverride", "biosVfFrequencyFloorOverride", "Frequency-Floor-Override", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_frequency_floor_override": MoPropertyMeta("vp_frequency_floor_override", "vpFrequencyFloorOverride", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpFrequencyFloorOverride": "vp_frequency_floor_override", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_frequency_floor_override = None

        ManagedObject.__init__(self, "BiosVfFrequencyFloorOverride", parent_mo_or_dn, **kwargs)

