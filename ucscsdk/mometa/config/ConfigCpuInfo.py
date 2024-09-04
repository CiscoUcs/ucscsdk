"""This module contains the general information for ConfigCpuInfo ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigCpuInfoConsts():
    ARCH_DUAL_CORE_OPTERON = "Dual-Core_Opteron"
    ARCH_INTEL_P4_C = "Intel_P4_C"
    ARCH_OPTERON = "Opteron"
    ARCH_PENTIUM_4 = "Pentium_4"
    ARCH_TURION_64 = "Turion_64"
    ARCH_XEON = "Xeon"
    ARCH_XEON_MP = "Xeon_MP"
    ARCH_ZEN = "Zen"
    ARCH_ANY = "any"
    SPEED_UNSPECIFIED = "unspecified"


class ConfigCpuInfo(ManagedObject):
    """This is ConfigCpuInfo class."""

    consts = ConfigCpuInfoConsts()
    naming_props = set(['arch'])

    mo_meta = MoMeta("ConfigCpuInfo", "configCpuInfo", "cpu-info-[arch]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['configServerItem'], [], [None])

    prop_meta = {
        "arch": MoPropertyMeta("arch", "arch", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x2, None, None, None, ["Dual-Core_Opteron", "Intel_P4_C", "Opteron", "Pentium_4", "Turion_64", "Xeon", "Xeon_MP", "Zen", "any"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "count": MoPropertyMeta("count", "count", "ushort", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "speed": MoPropertyMeta("speed", "speed", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "arch": "arch", 
        "childAction": "child_action", 
        "count": "count", 
        "dn": "dn", 
        "rn": "rn", 
        "speed": "speed", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, arch, **kwargs):
        self._dirty_mask = 0
        self.arch = arch
        self.child_action = None
        self.count = None
        self.speed = None
        self.status = None

        ManagedObject.__init__(self, "ConfigCpuInfo", parent_mo_or_dn, **kwargs)

