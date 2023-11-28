"""This module contains the general information for StorageFlexFlashControllerOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageFlexFlashControllerOperationConsts():
    ADMIN_SLOT_NUMBER_1 = "1"
    ADMIN_SLOT_NUMBER_2 = "2"
    ADMIN_SLOT_NUMBER_NA = "NA"
    OPERATION_REQUEST_FORMAT = "format"
    OPERATION_REQUEST_PAIR = "pair"
    OPERATION_REQUEST_RESET = "reset"
    OPERATION_REQUEST_UNKNOWN = "unknown"
    OPERATION_REQUEST_UNPAIR = "unpair"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class StorageFlexFlashControllerOperation(ManagedObject):
    """This is StorageFlexFlashControllerOperation class."""

    consts = StorageFlexFlashControllerOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageFlexFlashControllerOperation", "storageFlexFlashControllerOperation", "remote-oper", VersionMeta.Version201b, "InputOutput", 0x7f, [], ["admin"], ['storageFlexFlashController'], ['faultInst'], [None])

    prop_meta = {
        "admin_slot_number": MoPropertyMeta("admin_slot_number", "adminSlotNumber", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["1", "2", "NA"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "operation_request": MoPropertyMeta("operation_request", "operationRequest", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["format", "pair", "reset", "unknown", "unpair"], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "adminSlotNumber": "admin_slot_number", 
        "childAction": "child_action", 
        "dn": "dn", 
        "lastModified": "last_modified", 
        "operationRequest": "operation_request", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "rn": "rn", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_slot_number = None
        self.child_action = None
        self.last_modified = None
        self.operation_request = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "StorageFlexFlashControllerOperation", parent_mo_or_dn, **kwargs)

