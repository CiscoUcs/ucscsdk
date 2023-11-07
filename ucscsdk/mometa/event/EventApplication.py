"""This module contains the general information for EventApplication ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EventApplicationConsts():
    pass


class EventApplication(ManagedObject):
    """This is EventApplication class."""

    consts = EventApplicationConsts()
    naming_props = set(['type', 'ip'])

    mo_meta = MoMeta("EventApplication", "eventApplication", "type-[type]ip-[ip]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subscribe_status": MoPropertyMeta("subscribe_status", "subscribeStatus", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((subscribed|failed),){0,1}(subscribed|failed){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ip": "ip", 
        "rn": "rn", 
        "status": "status", 
        "subscribeStatus": "subscribe_status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, ip, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.ip = ip
        self.child_action = None
        self.status = None
        self.subscribe_status = None

        ManagedObject.__init__(self, "EventApplication", parent_mo_or_dn, **kwargs)

