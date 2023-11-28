"""This module contains the general information for PolicyControlEpOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyControlEpOperationConsts():
    ACK_STATE_ACKED = "acked"
    ACK_STATE_NO_ACK = "no-ack"
    ACK_STATE_REMOTE_TRIGGER = "remoteTrigger"
    SUSPEND_STATE_OFF = "off"
    SUSPEND_STATE_ON = "on"
    SUSPEND_STATE_REMOTE_TRIGGER = "remoteTrigger"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class PolicyControlEpOperation(ManagedObject):
    """This is PolicyControlEpOperation class."""

    consts = PolicyControlEpOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("PolicyControlEpOperation", "policyControlEpOperation", "remote-oper", VersionMeta.Version121a, "InputOutput", 0x7f, [], ["admin"], ['policyControlEp'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "ack_state": MoPropertyMeta("ack_state", "ackState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["acked", "no-ack", "remoteTrigger"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspend_state": MoPropertyMeta("suspend_state", "suspendState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["off", "on", "remoteTrigger"], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "ackState": "ack_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "lastModified": "last_modified", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "rn": "rn", 
        "status": "status", 
        "suspendState": "suspend_state", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.ack_state = None
        self.child_action = None
        self.last_modified = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.suspend_state = None
        self.trigger_status = None

        ManagedObject.__init__(self, "PolicyControlEpOperation", parent_mo_or_dn, **kwargs)

