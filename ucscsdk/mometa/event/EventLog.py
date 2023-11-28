"""This module contains the general information for EventLog ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EventLogConsts():
    pass


class EventLog(ManagedObject):
    """This is EventLog class."""

    consts = EventLogConsts()
    naming_props = set([])

    mo_meta = MoMeta("EventLog", "eventLog", "event-log", VersionMeta.Version101a, "InputOutput", 0xf, [], ["admin", "fault", "operations"], ['topRoot'], ['eventRecord'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "max_size": MoPropertyMeta("max_size", "maxSize", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["500-100000"]), 
        "purge_window": MoPropertyMeta("purge_window", "purgeWindow", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["10-250"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maxSize": "max_size", 
        "purgeWindow": "purge_window", 
        "rn": "rn", 
        "size": "size", 
        "status": "status", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.max_size = None
        self.purge_window = None
        self.size = None
        self.status = None

        ManagedObject.__init__(self, "EventLog", **kwargs)

