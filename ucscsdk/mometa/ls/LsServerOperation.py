"""This module contains the general information for LsServerOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsServerOperationConsts():
    STATE_ADMIN_DOWN = "admin-down"
    STATE_ADMIN_UP = "admin-up"
    STATE_BMC_RESET_IMMEDIATE = "bmc-reset-immediate"
    STATE_BMC_RESET_WAIT = "bmc-reset-wait"
    STATE_CMOS_RESET_IMMEDIATE = "cmos-reset-immediate"
    STATE_CYCLE_IMMEDIATE = "cycle-immediate"
    STATE_CYCLE_WAIT = "cycle-wait"
    STATE_DIAGNOSTIC_INTERRUPT = "diagnostic-interrupt"
    STATE_DOWN = "down"
    STATE_HARD_RESET_IMMEDIATE = "hard-reset-immediate"
    STATE_HARD_RESET_WAIT = "hard-reset-wait"
    STATE_IPMI_RESET = "ipmi-reset"
    STATE_KVM_RESET = "kvm-reset"
    STATE_REMOTE_TRIGGER = "remoteTrigger"
    STATE_SOFT_SHUT_DOWN = "soft-shut-down"
    STATE_SOFT_SHUT_DOWN_ONLY = "soft-shut-down-only"
    STATE_UP = "up"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class LsServerOperation(ManagedObject):
    """This is LsServerOperation class."""

    consts = LsServerOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsServerOperation", "lsServerOperation", "remote-oper", VersionMeta.Version112a, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-oper", "ls-server-policy"], ['computeInstance', 'lsServer'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["admin-down", "admin-up", "bmc-reset-immediate", "bmc-reset-wait", "cmos-reset-immediate", "cycle-immediate", "cycle-wait", "diagnostic-interrupt", "down", "hard-reset-immediate", "hard-reset-wait", "ipmi-reset", "kvm-reset", "remoteTrigger", "soft-shut-down", "soft-shut-down-only", "up"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lastModified": "last_modified", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "rn": "rn", 
        "state": "state", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.last_modified = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.state = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "LsServerOperation", parent_mo_or_dn, **kwargs)

