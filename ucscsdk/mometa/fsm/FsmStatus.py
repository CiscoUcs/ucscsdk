"""This module contains the general information for FsmStatus ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FsmStatusConsts():
    STATE_FAIL = "fail"
    STATE_IN_PROGRESS = "inProgress"
    STATE_NOP = "nop"
    STATE_PENDING = "pending"
    STATE_SKIP = "skip"
    STATE_SUCCESS = "success"
    STATE_THROTTLED = "throttled"


class FsmStatus(ManagedObject):
    """This is FsmStatus class."""

    consts = FsmStatusConsts()
    naming_props = set(['convertedEpRef'])

    mo_meta = MoMeta("FsmStatus", "fsmStatus", "status-[converted_ep_ref]", VersionMeta.Version101a, "InputOutput", 0x7f, [], ["read-only"], ['computeSystem', 'topSystem'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "converted_ep_ref": MoPropertyMeta("converted_ep_ref", "convertedEpRef", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x2, 1, 510, None, [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "object_class_name": MoPropertyMeta("object_class_name", "objectClassName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "remote_ep_ref": MoPropertyMeta("remote_ep_ref", "remoteEpRef", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "system_name": MoPropertyMeta("system_name", "systemName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "convertedEpRef": "converted_ep_ref", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "objectClassName": "object_class_name", 
        "remoteEpRef": "remote_ep_ref", 
        "rn": "rn", 
        "state": "state", 
        "status": "status", 
        "systemName": "system_name", 
    }

    def __init__(self, parent_mo_or_dn, converted_ep_ref, **kwargs):
        self._dirty_mask = 0
        self.converted_ep_ref = converted_ep_ref
        self.child_action = None
        self.descr = None
        self.name = None
        self.object_class_name = None
        self.remote_ep_ref = None
        self.state = None
        self.status = None
        self.system_name = None

        ManagedObject.__init__(self, "FsmStatus", parent_mo_or_dn, **kwargs)

