"""This module contains the general information for ConfigServerFilter ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigServerFilterConsts():
    ASSOCIATION_ASSOCIATED = "associated"
    ASSOCIATION_ESTABLISHING = "establishing"
    ASSOCIATION_FAILED = "failed"
    ASSOCIATION_NONE = "none"
    ASSOCIATION_REMOVING = "removing"
    ASSOCIATION_THROTTLED = "throttled"
    CPU_ARCH_DUAL_CORE_OPTERON = "Dual-Core_Opteron"
    CPU_ARCH_INTEL_P4_C = "Intel_P4_C"
    CPU_ARCH_OPTERON = "Opteron"
    CPU_ARCH_PENTIUM_4 = "Pentium_4"
    CPU_ARCH_TURION_64 = "Turion_64"
    CPU_ARCH_XEON = "Xeon"
    CPU_ARCH_XEON_MP = "Xeon_MP"
    CPU_ARCH_ZEN = "Zen"
    CPU_ARCH_ANY = "any"
    DECOMMISSIONED_FALSE = "false"
    DECOMMISSIONED_NO = "no"
    DECOMMISSIONED_TRUE = "true"
    DECOMMISSIONED_YES = "yes"
    DISCOVERY_COMPLETE = "complete"
    DISCOVERY_DIAGNOSTICS_COMPLETE = "diagnostics-complete"
    DISCOVERY_DIAGNOSTICS_FAILED = "diagnostics-failed"
    DISCOVERY_DIAGNOSTICS_IN_PROGRESS = "diagnostics-in-progress"
    DISCOVERY_EFIDIAGNOSTICS_IN_PROGRESS = "efidiagnostics-in-progress"
    DISCOVERY_FAILED = "failed"
    DISCOVERY_FRU_IDENTITY_INDETERMINATE = "fru-identity-indeterminate"
    DISCOVERY_FRU_NOT_READY = "fru-not-ready"
    DISCOVERY_FRU_STATE_INDETERMINATE = "fru-state-indeterminate"
    DISCOVERY_ILLEGAL_FRU = "illegal-fru"
    DISCOVERY_IN_PROGRESS = "in-progress"
    DISCOVERY_INSUFFICIENTLY_EQUIPPED = "insufficiently-equipped"
    DISCOVERY_INVALID_ADAPTOR_IOCARD = "invalid-adaptor-iocard"
    DISCOVERY_MALFORMED_FRU_INFO = "malformed-fru-info"
    DISCOVERY_RETRY = "retry"
    DISCOVERY_THROTTLED = "throttled"
    DISCOVERY_UNDISCOVERED = "undiscovered"
    DISCOVERY_USER_ACKNOWLEDGED = "user-acknowledged"
    DISCOVERY_WAITING_FOR_MGMT_ACK = "waiting-for-mgmt-ack"
    DISCOVERY_WAITING_FOR_USER_ACK = "waiting-for-user-ack"
    FAULT_LEVEL_CLEARED = "cleared"
    FAULT_LEVEL_CONDITION = "condition"
    FAULT_LEVEL_CRITICAL = "critical"
    FAULT_LEVEL_INFO = "info"
    FAULT_LEVEL_MAJOR = "major"
    FAULT_LEVEL_MINOR = "minor"
    FAULT_LEVEL_WARNING = "warning"
    FW_OPER_STATE_ACTIVATING = "activating"
    FW_OPER_STATE_BAD_IMAGE = "bad-image"
    FW_OPER_STATE_FAILED = "failed"
    FW_OPER_STATE_PENDING_NEXT_BOOT = "pending-next-boot"
    FW_OPER_STATE_READY = "ready"
    FW_OPER_STATE_REBOOTING = "rebooting"
    FW_OPER_STATE_SCHEDULED = "scheduled"
    FW_OPER_STATE_SET_STARTUP = "set-startup"
    FW_OPER_STATE_THROTTLED = "throttled"
    FW_OPER_STATE_UPDATING = "updating"
    FW_OPER_STATE_UPGRADING = "upgrading"
    OPER_STATE_BIOS_RESTORE = "bios-restore"
    OPER_STATE_CMOS_RESET = "cmos-reset"
    OPER_STATE_COMPUTE_FAILED = "compute-failed"
    OPER_STATE_COMPUTE_MISMATCH = "compute-mismatch"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_CONFIG_FAILURE = "config-failure"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_DIAGNOSTICS = "diagnostics"
    OPER_STATE_DIAGNOSTICS_FAILED = "diagnostics-failed"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_DISCOVERY = "discovery"
    OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    OPER_STATE_INACCESSIBLE = "inaccessible"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_INOPERABLE = "inoperable"
    OPER_STATE_MAINTENANCE = "maintenance"
    OPER_STATE_MAINTENANCE_FAILED = "maintenance-failed"
    OPER_STATE_OK = "ok"
    OPER_STATE_PENDING_REASSOCIATION = "pending-reassociation"
    OPER_STATE_PENDING_REBOOT = "pending-reboot"
    OPER_STATE_POWER_OFF = "power-off"
    OPER_STATE_POWER_PROBLEM = "power-problem"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_RESTART = "restart"
    OPER_STATE_TEST = "test"
    OPER_STATE_TEST_FAILED = "test-failed"
    OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    OPER_STATE_UNASSOCIATED = "unassociated"
    OPER_STATE_UNCONFIG = "unconfig"
    OPER_STATE_UNCONFIG_FAILED = "unconfig-failed"
    OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"


class ConfigServerFilter(ManagedObject):
    """This is ConfigServerFilter class."""

    consts = ConfigServerFilterConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigServerFilter", "configServerFilter", "server-filter", VersionMeta.Version131a, "InputOutput", 0xfffff, [], ["read-only"], [], [], [None])

    prop_meta = {
        "association": MoPropertyMeta("association", "association", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["associated", "establishing", "failed", "none", "removing", "throttled"], []), 
        "chassis_dn": MoPropertyMeta("chassis_dn", "chassisDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cpu_arch": MoPropertyMeta("cpu_arch", "cpuArch", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Dual-Core_Opteron", "Intel_P4_C", "Opteron", "Pentium_4", "Turion_64", "Xeon", "Xeon_MP", "Zen", "any"], []), 
        "decommissioned": MoPropertyMeta("decommissioned", "decommissioned", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []), 
        "discovery": MoPropertyMeta("discovery", "discovery", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["complete", "diagnostics-complete", "diagnostics-failed", "diagnostics-in-progress", "efidiagnostics-in-progress", "failed", "fru-identity-indeterminate", "fru-not-ready", "fru-state-indeterminate", "illegal-fru", "in-progress", "insufficiently-equipped", "invalid-adaptor-iocard", "malformed-fru-info", "retry", "throttled", "undiscovered", "user-acknowledged", "waiting-for-mgmt-ack", "waiting-for-user-ack"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "domain_dn": MoPropertyMeta("domain_dn", "domainDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "fw_oper_state": MoPropertyMeta("fw_oper_state", "fwOperState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating", "upgrading"], []), 
        "fw_version": MoPropertyMeta("fw_version", "fwVersion", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2000, 0, 510, None, [], []), 
        "num_of_adaptors": MoPropertyMeta("num_of_adaptors", "numOfAdaptors", "byte", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, [], []), 
        "num_of_cores": MoPropertyMeta("num_of_cores", "numOfCores", "ushort", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["bios-restore", "cmos-reset", "compute-failed", "compute-mismatch", "config", "config-failure", "decomissioning", "degraded", "diagnostics", "diagnostics-failed", "disabled", "discovery", "discovery-failed", "inaccessible", "indeterminate", "inoperable", "maintenance", "maintenance-failed", "ok", "pending-reassociation", "pending-reboot", "power-off", "power-problem", "removed", "restart", "test", "test-failed", "thermal-problem", "unassociated", "unconfig", "unconfig-failed", "voltage-problem"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x20000, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "total_memory": MoPropertyMeta("total_memory", "totalMemory", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, [], []), 
    }

    prop_map = {
        "association": "association", 
        "chassisDn": "chassis_dn", 
        "childAction": "child_action", 
        "cpuArch": "cpu_arch", 
        "decommissioned": "decommissioned", 
        "discovery": "discovery", 
        "dn": "dn", 
        "domainDn": "domain_dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainName": "domain_name", 
        "faultLevel": "fault_level", 
        "fwOperState": "fw_oper_state", 
        "fwVersion": "fw_version", 
        "model": "model", 
        "numOfAdaptors": "num_of_adaptors", 
        "numOfCores": "num_of_cores", 
        "operState": "oper_state", 
        "rn": "rn", 
        "status": "status", 
        "totalMemory": "total_memory", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.association = None
        self.chassis_dn = None
        self.child_action = None
        self.cpu_arch = None
        self.decommissioned = None
        self.discovery = None
        self.domain_dn = None
        self.domain_group_dn = None
        self.domain_name = None
        self.fault_level = None
        self.fw_oper_state = None
        self.fw_version = None
        self.model = None
        self.num_of_adaptors = None
        self.num_of_cores = None
        self.oper_state = None
        self.status = None
        self.total_memory = None

        ManagedObject.__init__(self, "ConfigServerFilter", parent_mo_or_dn, **kwargs)

