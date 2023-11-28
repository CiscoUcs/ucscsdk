"""This module contains the general information for FabricSanPinTargetOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricSanPinTargetOperationConsts():
    FABRIC_ID_A = "A"
    FABRIC_ID_B = "B"
    FABRIC_ID_NONE = "NONE"
    FABRIC_ID_DUAL = "dual"
    FABRIC_ID_MGMT = "mgmt"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class FabricSanPinTargetOperation(ManagedObject):
    """This is FabricSanPinTargetOperation class."""

    consts = FabricSanPinTargetOperationConsts()
    naming_props = set(['fabricId'])

    mo_meta = MoMeta("FabricSanPinTargetOperation", "fabricSanPinTargetOperation", "remoper-target-[fabric_id]", VersionMeta.Version141a, "InputOutput", 0x7f, [], ["admin", "ext-san-config", "ext-san-policy"], ['fabricSanPinGroupOperation'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, None, [], []), 
        "fabric_id": MoPropertyMeta("fabric_id", "fabricId", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x8, None, None, None, ["A", "B", "NONE", "dual", "mgmt"], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "fabricId": "fabric_id", 
        "lastModified": "last_modified", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "rn": "rn", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, fabric_id, **kwargs):
        self._dirty_mask = 0
        self.fabric_id = fabric_id
        self.child_action = None
        self.ep_dn = None
        self.last_modified = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "FabricSanPinTargetOperation", parent_mo_or_dn, **kwargs)

