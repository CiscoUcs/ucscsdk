"""This module contains the general information for SysdebugLogControlModule ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SysdebugLogControlModuleConsts():
    DEFAULT_LEVEL_CRIT = "crit"
    DEFAULT_LEVEL_DEBUG0 = "debug0"
    DEFAULT_LEVEL_DEBUG1 = "debug1"
    DEFAULT_LEVEL_DEBUG2 = "debug2"
    DEFAULT_LEVEL_DEBUG3 = "debug3"
    DEFAULT_LEVEL_DEBUG4 = "debug4"
    DEFAULT_LEVEL_INFO = "info"
    DEFAULT_LEVEL_MAJOR = "major"
    DEFAULT_LEVEL_MINOR = "minor"
    DEFAULT_LEVEL_WARN = "warn"
    LEVEL_CRIT = "crit"
    LEVEL_DEBUG0 = "debug0"
    LEVEL_DEBUG1 = "debug1"
    LEVEL_DEBUG2 = "debug2"
    LEVEL_DEBUG3 = "debug3"
    LEVEL_DEBUG4 = "debug4"
    LEVEL_INFO = "info"
    LEVEL_MAJOR = "major"
    LEVEL_MINOR = "minor"
    LEVEL_WARN = "warn"
    RESET_LOG_CONTROL_MODULE_FALSE = "false"
    RESET_LOG_CONTROL_MODULE_NO = "no"
    RESET_LOG_CONTROL_MODULE_TRUE = "true"
    RESET_LOG_CONTROL_MODULE_YES = "yes"


class SysdebugLogControlModule(ManagedObject):
    """This is SysdebugLogControlModule class."""

    consts = SysdebugLogControlModuleConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("SysdebugLogControlModule", "sysdebugLogControlModule", "module-[name]", VersionMeta.Version101a, "InputOutput", 0xff, [], ["admin", "operations"], ['sysdebugLogControlDomain'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "default_level": MoPropertyMeta("default_level", "defaultLevel", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["crit", "debug0", "debug1", "debug2", "debug3", "debug4", "info", "major", "minor", "warn"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "level": MoPropertyMeta("level", "level", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["crit", "debug0", "debug1", "debug2", "debug3", "debug4", "info", "major", "minor", "warn"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []), 
        "reset_log_control_module": MoPropertyMeta("reset_log_control_module", "resetLogControlModule", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "defaultLevel": "default_level", 
        "dn": "dn", 
        "level": "level", 
        "name": "name", 
        "resetLogControlModule": "reset_log_control_module", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.default_level = None
        self.level = None
        self.reset_log_control_module = None
        self.status = None

        ManagedObject.__init__(self, "SysdebugLogControlModule", parent_mo_or_dn, **kwargs)

