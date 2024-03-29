"""This module contains the general information for BiosVfOSBootWatchdogTimerTimeout ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfOSBootWatchdogTimerTimeoutConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_10_MINUTES = "10-minutes"
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_15_MINUTES = "15-minutes"
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_20_MINUTES = "20-minutes"
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_5_MINUTES = "5-minutes"
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_PLATFORM_DEFAULT = "platform-default"
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfOSBootWatchdogTimerTimeout(ManagedObject):
    """This is BiosVfOSBootWatchdogTimerTimeout class."""

    consts = BiosVfOSBootWatchdogTimerTimeoutConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfOSBootWatchdogTimerTimeout", "biosVfOSBootWatchdogTimerTimeout", "OS-Boot-Watchdog-Timer-Timeout", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_os_boot_watchdog_timer_timeout": MoPropertyMeta("vp_os_boot_watchdog_timer_timeout", "vpOSBootWatchdogTimerTimeout", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["10-minutes", "15-minutes", "20-minutes", "5-minutes", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpOSBootWatchdogTimerTimeout": "vp_os_boot_watchdog_timer_timeout", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_os_boot_watchdog_timer_timeout = None

        ManagedObject.__init__(self, "BiosVfOSBootWatchdogTimerTimeout", parent_mo_or_dn, **kwargs)

