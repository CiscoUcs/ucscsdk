"""This module contains the general information for EventEpCtrl ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EventEpCtrlConsts():
    LEVEL_CLEARED = "cleared"
    LEVEL_CONDITION = "condition"
    LEVEL_CRITICAL = "critical"
    LEVEL_INFO = "info"
    LEVEL_MAJOR = "major"
    LEVEL_MINOR = "minor"
    LEVEL_WARNING = "warning"
    REVERT_TIMEOUT_FOREVER = "forever"


class EventEpCtrl(ManagedObject):
    """This is EventEpCtrl class."""

    consts = EventEpCtrlConsts()
    naming_props = set([])

    mo_meta = MoMeta("EventEpCtrl", "eventEpCtrl", "evctrl", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin", "fault", "operations"], [], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "level": MoPropertyMeta("level", "level", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "revert_timeout": MoPropertyMeta("revert_timeout", "revertTimeout", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["forever"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "level": "level", 
        "revertTimeout": "revert_timeout", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.level = None
        self.revert_timeout = None
        self.status = None

        ManagedObject.__init__(self, "EventEpCtrl", parent_mo_or_dn, **kwargs)

