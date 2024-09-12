"""This module contains the general information for ComputeBlade ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeBladeConsts():
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
    ADMIN_STATE_IN_MAINTENANCE = "in-maintenance"
    ADMIN_STATE_IN_SERVICE = "in-service"
    ADMIN_STATE_OUT_OF_SERVICE = "out-of-service"
    ASSOCIATION_ASSOCIATED = "associated"
    ASSOCIATION_ESTABLISHING = "establishing"
    ASSOCIATION_FAILED = "failed"
    ASSOCIATION_NONE = "none"
    ASSOCIATION_REMOVING = "removing"
    ASSOCIATION_THROTTLED = "throttled"
    AVAILABILITY_AVAILABLE = "available"
    AVAILABILITY_UNAVAILABLE = "unavailable"
    CHASSIS_ID_N_A = "N/A"
    CHECK_POINT_DEEP_CHECKPOINT = "deep-checkpoint"
    CHECK_POINT_DISCOVERED = "discovered"
    CHECK_POINT_REMOVING = "removing"
    CHECK_POINT_SHALLOW_CHECKPOINT = "shallow-checkpoint"
    CHECK_POINT_UNKNOWN = "unknown"
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
    INT_ID_NONE = "none"
    KMIP_FAULT_FALSE = "false"
    KMIP_FAULT_NO = "no"
    KMIP_FAULT_TRUE = "true"
    KMIP_FAULT_YES = "yes"
    LC_DECOMMISSION = "decommission"
    LC_DISCOVERED = "discovered"
    LC_MIGRATE = "migrate"
    LC_REDISCOVER = "rediscover"
    LC_REMOVE = "remove"
    LC_RESET_TO_FACTORY = "resetToFactory"
    LC_UNDISCOVERED = "undiscovered"
    MANAGING_INST_A = "A"
    MANAGING_INST_B = "B"
    MANAGING_INST_NONE = "NONE"
    MANAGING_INST_MGMT = "mgmt"
    MEMORY_SPEED_NOT_APPLICABLE = "not-applicable"
    MEMORY_SPEED_UNSPECIFIED = "unspecified"
    MFG_TIME_NOT_APPLICABLE = "not-applicable"
    OPER_POWER_DEGRADED = "degraded"
    OPER_POWER_ERROR = "error"
    OPER_POWER_FAILED = "failed"
    OPER_POWER_NOT_SUPPORTED = "not-supported"
    OPER_POWER_OFF = "off"
    OPER_POWER_OFFDUTY = "offduty"
    OPER_POWER_OFFLINE = "offline"
    OPER_POWER_OK = "ok"
    OPER_POWER_ON = "on"
    OPER_POWER_ONLINE = "online"
    OPER_POWER_POWER_SAVE = "power-save"
    OPER_POWER_TEST = "test"
    OPER_POWER_UNKNOWN = "unknown"
    OPER_PWR_TRANS_SRC_SOFTWARE = "software"
    OPER_PWR_TRANS_SRC_SOFTWARE_MCSERVER = "software_mcserver"
    OPER_PWR_TRANS_SRC_UNKNOWN = "unknown"
    OPER_PWR_TRANS_SRC_USER_FP = "user-fp"
    OPER_PWR_TRANS_SRC_USER_UNKNOWN = "user-unknown"
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
    OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    OPERABILITY_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPERABILITY_CONFIG = "config"
    OPERABILITY_DECOMISSIONING = "decomissioning"
    OPERABILITY_DEGRADED = "degraded"
    OPERABILITY_DISABLED = "disabled"
    OPERABILITY_DISCOVERY = "discovery"
    OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPERABILITY_IDENTIFY = "identify"
    OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPERABILITY_INOPERABLE = "inoperable"
    OPERABILITY_MALFORMED_FRU = "malformed-fru"
    OPERABILITY_NOT_SUPPORTED = "not-supported"
    OPERABILITY_OPERABLE = "operable"
    OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    OPERABILITY_POST_FAILURE = "post-failure"
    OPERABILITY_POWER_PROBLEM = "power-problem"
    OPERABILITY_POWERED_OFF = "powered-off"
    OPERABILITY_REMOVED = "removed"
    OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    OPERABILITY_UNKNOWN = "unknown"
    OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    PCIE_NODE_CAPABLE_FALSE = "false"
    PCIE_NODE_CAPABLE_NO = "no"
    PCIE_NODE_CAPABLE_TRUE = "true"
    PCIE_NODE_CAPABLE_YES = "yes"
    PCIE_NODE_CONNECTED_FALSE = "false"
    PCIE_NODE_CONNECTED_NO = "no"
    PCIE_NODE_CONNECTED_TRUE = "true"
    PCIE_NODE_CONNECTED_YES = "yes"
    PCIE_NODE_DISCOVER_STATUS_COMPLETE = "complete"
    PCIE_NODE_DISCOVER_STATUS_DIAGNOSTICS_COMPLETE = "diagnostics-complete"
    PCIE_NODE_DISCOVER_STATUS_DIAGNOSTICS_FAILED = "diagnostics-failed"
    PCIE_NODE_DISCOVER_STATUS_DIAGNOSTICS_IN_PROGRESS = "diagnostics-in-progress"
    PCIE_NODE_DISCOVER_STATUS_EFIDIAGNOSTICS_IN_PROGRESS = "efidiagnostics-in-progress"
    PCIE_NODE_DISCOVER_STATUS_FAILED = "failed"
    PCIE_NODE_DISCOVER_STATUS_FRU_IDENTITY_INDETERMINATE = "fru-identity-indeterminate"
    PCIE_NODE_DISCOVER_STATUS_FRU_NOT_READY = "fru-not-ready"
    PCIE_NODE_DISCOVER_STATUS_FRU_STATE_INDETERMINATE = "fru-state-indeterminate"
    PCIE_NODE_DISCOVER_STATUS_ILLEGAL_FRU = "illegal-fru"
    PCIE_NODE_DISCOVER_STATUS_IN_PROGRESS = "in-progress"
    PCIE_NODE_DISCOVER_STATUS_INSUFFICIENTLY_EQUIPPED = "insufficiently-equipped"
    PCIE_NODE_DISCOVER_STATUS_INVALID_ADAPTOR_IOCARD = "invalid-adaptor-iocard"
    PCIE_NODE_DISCOVER_STATUS_MALFORMED_FRU_INFO = "malformed-fru-info"
    PCIE_NODE_DISCOVER_STATUS_RETRY = "retry"
    PCIE_NODE_DISCOVER_STATUS_THROTTLED = "throttled"
    PCIE_NODE_DISCOVER_STATUS_UNDISCOVERED = "undiscovered"
    PCIE_NODE_DISCOVER_STATUS_USER_ACKNOWLEDGED = "user-acknowledged"
    PCIE_NODE_DISCOVER_STATUS_WAITING_FOR_MGMT_ACK = "waiting-for-mgmt-ack"
    PCIE_NODE_DISCOVER_STATUS_WAITING_FOR_USER_ACK = "waiting-for-user-ack"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_SLAVE = "equipped-slave"
    PRESENCE_EQUIPPED_UNSUPPORTED = "equipped-unsupported"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISMATCH_SLAVE = "mismatch-slave"
    PRESENCE_MISSING = "missing"
    PRESENCE_MISSING_SLAVE = "missing-slave"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"
    SCALED_MODE_NONE = "none"
    SCALED_MODE_SCALED = "scaled"
    SCALED_MODE_SINGLE = "single"
    UPGRADE_SCENARIO_NOT_APPLICABLE = "not-applicable"
    UPGRADE_SCENARIO_NOT_UPGRADED = "not-upgraded"
    UPGRADE_SCENARIO_UPGRADED = "upgraded"


class ComputeBlade(ManagedObject):
    """This is ComputeBlade class."""

    consts = ComputeBladeConsts()
    naming_props = set(['slotId'])

    mo_meta = MoMeta("ComputeBlade", "computeBlade", "blade-[slot_id]", VersionMeta.Version101a, "InputOutput", 0x3ff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['equipmentChassis'], ['adaptorHostIfConfig', 'adaptorUnit', 'biosUnit', 'computeBoard', 'computeBoardConnector', 'computeBoardController', 'computeExtBoard', 'computeFactoryResetOp', 'computeFactoryResetOperation', 'computePhysicalExtension', 'computePhysicalOperation', 'computePoolable', 'computeRebootLog', 'diagSrvCtrl', 'equipmentBeaconLed', 'equipmentHealthLed', 'equipmentIndicatorLed', 'equipmentLocatorLed', 'equipmentPcieNode', 'faultInst', 'firmwareStatus', 'lsIdentityInfo', 'lsbootDef', 'memoryRuntime', 'mgmtController', 'mgmtSecurity', 'osInstance', 'processorRuntime', 'storageEnclosure', 'storageVirtualDriveContainer', 'sysdebugDiagnosticLog'], ["Get"])

    prop_meta = {
        "admin_power": MoPropertyMeta("admin_power", "adminPower", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["admin-down", "admin-up", "bmc-reset-immediate", "bmc-reset-wait", "cmos-reset-immediate", "cycle-immediate", "cycle-wait", "diagnostic-interrupt", "hard-reset-immediate", "hard-reset-wait", "ipmi-reset", "kvm-reset", "policy"], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["in-maintenance", "in-service", "out-of-service"], []), 
        "asset_tag": MoPropertyMeta("asset_tag", "assetTag", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "association": MoPropertyMeta("association", "association", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["associated", "establishing", "failed", "none", "removing", "throttled"], []), 
        "availability": MoPropertyMeta("availability", "availability", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "unavailable"], []), 
        "available_memory": MoPropertyMeta("available_memory", "availableMemory", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]), 
        "check_point": MoPropertyMeta("check_point", "checkPoint", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deep-checkpoint", "discovered", "removing", "shallow-checkpoint", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "conn_path": MoPropertyMeta("conn_path", "connPath", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "conn_status": MoPropertyMeta("conn_status", "connStatus", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "discovery": MoPropertyMeta("discovery", "discovery", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["complete", "diagnostics-complete", "diagnostics-failed", "diagnostics-in-progress", "efidiagnostics-in-progress", "failed", "fru-identity-indeterminate", "fru-not-ready", "fru-state-indeterminate", "illegal-fru", "in-progress", "insufficiently-equipped", "invalid-adaptor-iocard", "malformed-fru-info", "retry", "throttled", "undiscovered", "user-acknowledged", "waiting-for-mgmt-ack", "waiting-for-user-ack"], []), 
        "discovery_status": MoPropertyMeta("discovery_status", "discoveryStatus", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "dual_slot_peer_pcie_node_dn": MoPropertyMeta("dual_slot_peer_pcie_node_dn", "dualSlotPeerPcieNodeDn", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "kmip_fault": MoPropertyMeta("kmip_fault", "kmipFault", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "kmip_fault_description": MoPropertyMeta("kmip_fault_description", "kmipFaultDescription", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["decommission", "discovered", "migrate", "rediscover", "remove", "resetToFactory", "undiscovered"], []), 
        "lc_ts": MoPropertyMeta("lc_ts", "lcTs", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "local_id": MoPropertyMeta("local_id", "localId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "low_voltage_memory": MoPropertyMeta("low_voltage_memory", "lowVoltageMemory", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ls_dn": MoPropertyMeta("ls_dn", "lsDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "managing_inst": MoPropertyMeta("managing_inst", "managingInst", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "memory_speed": MoPropertyMeta("memory_speed", "memorySpeed", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable", "unspecified"], ["0-4294967295"]), 
        "mfg_time": MoPropertyMeta("mfg_time", "mfgTime", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["not-applicable"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "num_of40_g_adaptors_with_old_fw": MoPropertyMeta("num_of40_g_adaptors_with_old_fw", "numOf40GAdaptorsWithOldFw", "byte", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of40_g_adaptors_with_unknown_fw": MoPropertyMeta("num_of40_g_adaptors_with_unknown_fw", "numOf40GAdaptorsWithUnknownFw", "byte", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_adaptors": MoPropertyMeta("num_of_adaptors", "numOfAdaptors", "byte", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_cores": MoPropertyMeta("num_of_cores", "numOfCores", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_cores_enabled": MoPropertyMeta("num_of_cores_enabled", "numOfCoresEnabled", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_cpus": MoPropertyMeta("num_of_cpus", "numOfCpus", "byte", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_eth_host_ifs": MoPropertyMeta("num_of_eth_host_ifs", "numOfEthHostIfs", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_fc_host_ifs": MoPropertyMeta("num_of_fc_host_ifs", "numOfFcHostIfs", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_threads": MoPropertyMeta("num_of_threads", "numOfThreads", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oper_power": MoPropertyMeta("oper_power", "operPower", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []), 
        "oper_pwr_trans_src": MoPropertyMeta("oper_pwr_trans_src", "operPwrTransSrc", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["software", "software_mcserver", "unknown", "user-fp", "user-unknown"], []), 
        "oper_qualifier": MoPropertyMeta("oper_qualifier", "operQualifier", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|cpu-voltage|adaptor-voltage|hba-voltage|compute-post-failure|memory-power|nic-power|memory-inoperable|nic-inoperable|compute-power|power-inoperable|compute-thermal|cpu-perf|adaptor-perf|hba-perf|cpu-thermal|adaptor-thermal|hba-thermal|compute-inoperable|memory-voltage|removed|nic-voltage|network-misconfig|cpu-power|adaptor-power|hba-power|compute-voltage|cpu-inoperable|adaptor-inoperable|hba-inoperable|config|memory-perf|nic-perf|adaptor-mismatch|memory-thermal|nic-thermal|mismatch|compute-perf),){0,38}(defaultValue|not-applicable|cpu-voltage|adaptor-voltage|hba-voltage|compute-post-failure|memory-power|nic-power|memory-inoperable|nic-inoperable|compute-power|power-inoperable|compute-thermal|cpu-perf|adaptor-perf|hba-perf|cpu-thermal|adaptor-thermal|hba-thermal|compute-inoperable|memory-voltage|removed|nic-voltage|network-misconfig|cpu-power|adaptor-power|hba-power|compute-voltage|cpu-inoperable|adaptor-inoperable|hba-inoperable|config|memory-perf|nic-perf|adaptor-mismatch|memory-thermal|nic-thermal|mismatch|compute-perf){0,1}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bios-restore", "cmos-reset", "compute-failed", "compute-mismatch", "config", "config-failure", "decomissioning", "degraded", "diagnostics", "diagnostics-failed", "disabled", "discovery", "discovery-failed", "inaccessible", "indeterminate", "inoperable", "maintenance", "maintenance-failed", "ok", "pending-reassociation", "pending-reboot", "power-off", "power-problem", "removed", "restart", "test", "test-failed", "thermal-problem", "unassociated", "unconfig", "unconfig-failed", "voltage-problem"], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "original_uuid": MoPropertyMeta("original_uuid", "originalUuid", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
        "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pcie_node_capable": MoPropertyMeta("pcie_node_capable", "pcieNodeCapable", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "pcie_node_connected": MoPropertyMeta("pcie_node_connected", "pcieNodeConnected", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "pcie_node_discover_status": MoPropertyMeta("pcie_node_discover_status", "pcieNodeDiscoverStatus", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, ["complete", "diagnostics-complete", "diagnostics-failed", "diagnostics-in-progress", "efidiagnostics-in-progress", "failed", "fru-identity-indeterminate", "fru-not-ready", "fru-state-indeterminate", "illegal-fru", "in-progress", "insufficiently-equipped", "invalid-adaptor-iocard", "malformed-fru-info", "retry", "throttled", "undiscovered", "user-acknowledged", "waiting-for-mgmt-ack", "waiting-for-user-ack"], []), 
        "peer_pcie_node_dn": MoPropertyMeta("peer_pcie_node_dn", "peerPcieNodeDn", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "unauthorized", "unknown"], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "scaled_mode": MoPropertyMeta("scaled_mode", "scaledMode", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "scaled", "single"], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "server_id": MoPropertyMeta("server_id", "serverId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x80, None, None, None, [], ["1-8"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "total_memory": MoPropertyMeta("total_memory", "totalMemory", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "upgrade_scenario": MoPropertyMeta("upgrade_scenario", "upgradeScenario", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable", "not-upgraded", "upgraded"], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "vid": MoPropertyMeta("vid", "vid", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminPower": "admin_power", 
        "adminState": "admin_state", 
        "assetTag": "asset_tag", 
        "assignedToDn": "assigned_to_dn", 
        "association": "association", 
        "availability": "availability", 
        "availableMemory": "available_memory", 
        "chassisId": "chassis_id", 
        "checkPoint": "check_point", 
        "childAction": "child_action", 
        "connPath": "conn_path", 
        "connStatus": "conn_status", 
        "descr": "descr", 
        "discovery": "discovery", 
        "discoveryStatus": "discovery_status", 
        "dn": "dn", 
        "dualSlotPeerPcieNodeDn": "dual_slot_peer_pcie_node_dn", 
        "fltAggr": "flt_aggr", 
        "intId": "int_id", 
        "kmipFault": "kmip_fault", 
        "kmipFaultDescription": "kmip_fault_description", 
        "lc": "lc", 
        "lcTs": "lc_ts", 
        "localId": "local_id", 
        "lowVoltageMemory": "low_voltage_memory", 
        "lsDn": "ls_dn", 
        "managingInst": "managing_inst", 
        "memorySpeed": "memory_speed", 
        "mfgTime": "mfg_time", 
        "model": "model", 
        "name": "name", 
        "numOf40GAdaptorsWithOldFw": "num_of40_g_adaptors_with_old_fw", 
        "numOf40GAdaptorsWithUnknownFw": "num_of40_g_adaptors_with_unknown_fw", 
        "numOfAdaptors": "num_of_adaptors", 
        "numOfCores": "num_of_cores", 
        "numOfCoresEnabled": "num_of_cores_enabled", 
        "numOfCpus": "num_of_cpus", 
        "numOfEthHostIfs": "num_of_eth_host_ifs", 
        "numOfFcHostIfs": "num_of_fc_host_ifs", 
        "numOfThreads": "num_of_threads", 
        "operPower": "oper_power", 
        "operPwrTransSrc": "oper_pwr_trans_src", 
        "operQualifier": "oper_qualifier", 
        "operState": "oper_state", 
        "operability": "operability", 
        "originalUuid": "original_uuid", 
        "partNumber": "part_number", 
        "pcieNodeCapable": "pcie_node_capable", 
        "pcieNodeConnected": "pcie_node_connected", 
        "pcieNodeDiscoverStatus": "pcie_node_discover_status", 
        "peerPcieNodeDn": "peer_pcie_node_dn", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "scaledMode": "scaled_mode", 
        "serial": "serial", 
        "serverId": "server_id", 
        "slotId": "slot_id", 
        "status": "status", 
        "totalMemory": "total_memory", 
        "upgradeScenario": "upgrade_scenario", 
        "usrLbl": "usr_lbl", 
        "uuid": "uuid", 
        "vendor": "vendor", 
        "vid": "vid", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.admin_power = None
        self.admin_state = None
        self.asset_tag = None
        self.assigned_to_dn = None
        self.association = None
        self.availability = None
        self.available_memory = None
        self.chassis_id = None
        self.check_point = None
        self.child_action = None
        self.conn_path = None
        self.conn_status = None
        self.descr = None
        self.discovery = None
        self.discovery_status = None
        self.dual_slot_peer_pcie_node_dn = None
        self.flt_aggr = None
        self.int_id = None
        self.kmip_fault = None
        self.kmip_fault_description = None
        self.lc = None
        self.lc_ts = None
        self.local_id = None
        self.low_voltage_memory = None
        self.ls_dn = None
        self.managing_inst = None
        self.memory_speed = None
        self.mfg_time = None
        self.model = None
        self.name = None
        self.num_of40_g_adaptors_with_old_fw = None
        self.num_of40_g_adaptors_with_unknown_fw = None
        self.num_of_adaptors = None
        self.num_of_cores = None
        self.num_of_cores_enabled = None
        self.num_of_cpus = None
        self.num_of_eth_host_ifs = None
        self.num_of_fc_host_ifs = None
        self.num_of_threads = None
        self.oper_power = None
        self.oper_pwr_trans_src = None
        self.oper_qualifier = None
        self.oper_state = None
        self.operability = None
        self.original_uuid = None
        self.part_number = None
        self.pcie_node_capable = None
        self.pcie_node_connected = None
        self.pcie_node_discover_status = None
        self.peer_pcie_node_dn = None
        self.policy_level = None
        self.policy_owner = None
        self.presence = None
        self.revision = None
        self.scaled_mode = None
        self.serial = None
        self.server_id = None
        self.status = None
        self.total_memory = None
        self.upgrade_scenario = None
        self.usr_lbl = None
        self.uuid = None
        self.vendor = None
        self.vid = None

        ManagedObject.__init__(self, "ComputeBlade", parent_mo_or_dn, **kwargs)

