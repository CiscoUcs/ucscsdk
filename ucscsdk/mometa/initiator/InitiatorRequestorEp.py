"""This module contains the general information for InitiatorRequestorEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class InitiatorRequestorEpConsts():
    ALLOC_STATE_ALLOCATED = "allocated"
    ALLOC_STATE_ALLOCATING = "allocating"
    ALLOC_STATE_FAILED = "failed"
    ALLOC_STATE_NONE = "none"


class InitiatorRequestorEp(ManagedObject):
    """This is InitiatorRequestorEp class."""

    consts = InitiatorRequestorEpConsts()
    naming_props = set(['sysId', 'id'])

    mo_meta = MoMeta("InitiatorRequestorEp", "initiatorRequestorEp", "req-sysid-[sys_id]-id-[id]", VersionMeta.Version131a, "InputOutput", 0x3f, [], ["read-only"], ['topSystem'], ['initiatorGroupEp'], [None])

    prop_meta = {
        "alloc_state": MoPropertyMeta("alloc_state", "allocState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "allocating", "failed", "none"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sys_id": MoPropertyMeta("sys_id", "sysId", "uint", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
        "sys_name": MoPropertyMeta("sys_name", "sysName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "allocState": "alloc_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "id": "id", 
        "rn": "rn", 
        "status": "status", 
        "sysId": "sys_id", 
        "sysName": "sys_name", 
    }

    def __init__(self, parent_mo_or_dn, sys_id, id, **kwargs):
        self._dirty_mask = 0
        self.sys_id = sys_id
        self.id = id
        self.alloc_state = None
        self.child_action = None
        self.ep_dn = None
        self.status = None
        self.sys_name = None

        ManagedObject.__init__(self, "InitiatorRequestorEp", parent_mo_or_dn, **kwargs)

