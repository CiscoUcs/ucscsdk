"""This module contains the general information for FabricBreakoutOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricBreakoutOperationConsts():
    BREAKOUT_TYPE_10G_4X = "10g-4x"
    BREAKOUT_TYPE_25G_4X = "25g-4x"
    BREAKOUT_TYPE_UNKNOWN = "unknown"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class FabricBreakoutOperation(ManagedObject):
    """This is FabricBreakoutOperation class."""

    consts = FabricBreakoutOperationConsts()
    naming_props = set(['slotId', 'portId'])

    mo_meta = MoMeta("FabricBreakoutOperation", "fabricBreakoutOperation", "remoper-slot-[slot_id]-port-[port_id]", VersionMeta.Version141a, "InputOutput", 0xff, [], ["admin", "ext-lan-config", "ext-lan-policy", "ext-san-config", "ext-san-policy"], ['fabricCablingSw'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "breakout_type": MoPropertyMeta("breakout_type", "breakoutType", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["10g-4x", "25g-4x", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-108"]), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], ["1-2"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "breakoutType": "breakout_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "lastModified": "last_modified", 
        "portId": "port_id", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "rn": "rn", 
        "slotId": "slot_id", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, port_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.port_id = port_id
        self.breakout_type = None
        self.child_action = None
        self.last_modified = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "FabricBreakoutOperation", parent_mo_or_dn, **kwargs)

