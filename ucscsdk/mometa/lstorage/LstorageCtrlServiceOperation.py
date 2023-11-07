"""This module contains the general information for LstorageCtrlServiceOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LstorageCtrlServiceOperationConsts():
    REMOTE_ADMIN_STATE_IN_MAINTENANCE = "in-maintenance"
    REMOTE_ADMIN_STATE_IN_SERVICE = "in-service"
    REMOTE_ADMIN_STATE_REMOTE_TRIGGER = "remoteTrigger"
    REMOTE_FAIL_OVER_STATE_FORCE_TRIGGER = "force-trigger"
    REMOTE_FAIL_OVER_STATE_REMOTE_TRIGGER = "remoteTrigger"
    REMOTE_FAIL_OVER_STATE_TRIGGER = "trigger"
    REMOTE_FAIL_OVER_STATE_TRIGGERED = "triggered"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class LstorageCtrlServiceOperation(ManagedObject):
    """This is LstorageCtrlServiceOperation class."""

    consts = LstorageCtrlServiceOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageCtrlServiceOperation", "lstorageCtrlServiceOperation", "remote-oper", VersionMeta.Version131a, "InputOutput", 0x7f, [], ["admin", "ls-storage", "pn-equipment", "pn-maintenance", "pn-policy"], [], ['faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "remote_admin_state": MoPropertyMeta("remote_admin_state", "remoteAdminState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["in-maintenance", "in-service", "remoteTrigger"], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "remote_fail_over_state": MoPropertyMeta("remote_fail_over_state", "remoteFailOverState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["force-trigger", "remoteTrigger", "trigger", "triggered"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lastModified": "last_modified", 
        "remoteAdminState": "remote_admin_state", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "remoteFailOverState": "remote_fail_over_state", 
        "rn": "rn", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.last_modified = None
        self.remote_admin_state = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.remote_fail_over_state = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "LstorageCtrlServiceOperation", parent_mo_or_dn, **kwargs)

