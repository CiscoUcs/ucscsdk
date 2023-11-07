"""This module contains the general information for BiosVfNUMAOptimized ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfNUMAOptimizedConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_NUMAOPTIMIZED_DISABLED = "disabled"
    VP_NUMAOPTIMIZED_ENABLED = "enabled"
    VP_NUMAOPTIMIZED_PLATFORM_DEFAULT = "platform-default"
    VP_NUMAOPTIMIZED_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfNUMAOptimized(ManagedObject):
    """This is BiosVfNUMAOptimized class."""

    consts = BiosVfNUMAOptimizedConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfNUMAOptimized", "biosVfNUMAOptimized", "NUMA-optimized", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_numa_optimized": MoPropertyMeta("vp_numa_optimized", "vpNUMAOptimized", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpNUMAOptimized": "vp_numa_optimized", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_numa_optimized = None

        ManagedObject.__init__(self, "BiosVfNUMAOptimized", parent_mo_or_dn, **kwargs)

