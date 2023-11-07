"""This module contains the general information for BiosVfScrubPolicies ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfScrubPoliciesConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_DEMAND_SCRUB_DISABLED = "disabled"
    VP_DEMAND_SCRUB_ENABLED = "enabled"
    VP_DEMAND_SCRUB_PLATFORM_DEFAULT = "platform-default"
    VP_DEMAND_SCRUB_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PATROL_SCRUB_DISABLED = "disabled"
    VP_PATROL_SCRUB_ENABLED = "enabled"
    VP_PATROL_SCRUB_PLATFORM_DEFAULT = "platform-default"
    VP_PATROL_SCRUB_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfScrubPolicies(ManagedObject):
    """This is BiosVfScrubPolicies class."""

    consts = BiosVfScrubPoliciesConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfScrubPolicies", "biosVfScrubPolicies", "Scrub-Policies", VersionMeta.Version121a, "InputOutput", 0x3f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_demand_scrub": MoPropertyMeta("vp_demand_scrub", "vpDemandScrub", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
        "vp_patrol_scrub": MoPropertyMeta("vp_patrol_scrub", "vpPatrolScrub", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpDemandScrub": "vp_demand_scrub", 
        "vpPatrolScrub": "vp_patrol_scrub", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_demand_scrub = None
        self.vp_patrol_scrub = None

        ManagedObject.__init__(self, "BiosVfScrubPolicies", parent_mo_or_dn, **kwargs)

