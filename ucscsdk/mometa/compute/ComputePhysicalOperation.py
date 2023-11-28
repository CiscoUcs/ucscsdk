"""This module contains the general information for ComputePhysicalOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputePhysicalOperationConsts():
    ADMIN_POWER_ADMIN_DOWN = "admin-down"
    ADMIN_POWER_ADMIN_UP = "admin-up"
    ADMIN_POWER_BMC_RESET_IMMEDIATE = "bmc-reset-immediate"
    ADMIN_POWER_BMC_RESET_WAIT = "bmc-reset-wait"
    ADMIN_POWER_CMOS_RESET_IMMEDIATE = "cmos-reset-immediate"
    ADMIN_POWER_CYCLE_IMMEDIATE = "cycle-immediate"
    ADMIN_POWER_CYCLE_WAIT = "cycle-wait"
    ADMIN_POWER_DIAGNOSTIC_INTERRUPT = "diagnostic-interrupt"
    ADMIN_POWER_HARD_RESET_IMMEDIATE = "hard-reset-immediate"
    ADMIN_POWER_HARD_RESET_WAIT = "hard-reset-wait"
    ADMIN_POWER_IPMI_RESET = "ipmi-reset"
    ADMIN_POWER_KVM_RESET = "kvm-reset"
    ADMIN_POWER_POLICY = "policy"
    LC_DECOMMISSION = "decommission"
    LC_DISCOVERED = "discovered"
    LC_MIGRATE = "migrate"
    LC_REDISCOVER = "rediscover"
    LC_REMOTE_TRIGGER = "remoteTrigger"
    LC_REMOVE = "remove"
    LC_RESET_TO_FACTORY = "resetToFactory"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class ComputePhysicalOperation(ManagedObject):
    """This is ComputePhysicalOperation class."""

    consts = ComputePhysicalOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePhysicalOperation", "computePhysicalOperation", "remote-oper", VersionMeta.Version112a, "InputOutput", 0x7f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "admin_power": MoPropertyMeta("admin_power", "adminPower", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["admin-down", "admin-up", "bmc-reset-immediate", "bmc-reset-wait", "cmos-reset-immediate", "cycle-immediate", "cycle-wait", "diagnostic-interrupt", "hard-reset-immediate", "hard-reset-wait", "ipmi-reset", "kvm-reset", "policy"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["decommission", "discovered", "migrate", "rediscover", "remoteTrigger", "remove", "resetToFactory"], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "adminPower": "admin_power", 
        "childAction": "child_action", 
        "dn": "dn", 
        "lastModified": "last_modified", 
        "lc": "lc", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "rn": "rn", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_power = None
        self.child_action = None
        self.last_modified = None
        self.lc = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "ComputePhysicalOperation", parent_mo_or_dn, **kwargs)

