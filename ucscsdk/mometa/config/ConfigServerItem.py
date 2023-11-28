"""This module contains the general information for ConfigServerItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigServerItemConsts():
    ASSOCIATION_ASSOCIATED = "associated"
    ASSOCIATION_ESTABLISHING = "establishing"
    ASSOCIATION_FAILED = "failed"
    ASSOCIATION_NONE = "none"
    ASSOCIATION_REMOVING = "removing"
    ASSOCIATION_THROTTLED = "throttled"
    DECOMMISSIONED_FALSE = "false"
    DECOMMISSIONED_NO = "no"
    DECOMMISSIONED_TRUE = "true"
    DECOMMISSIONED_YES = "yes"
    DIAG_OPER_STATE_CANCELLED = "cancelled"
    DIAG_OPER_STATE_COMPLETED = "completed"
    DIAG_OPER_STATE_FAILED = "failed"
    DIAG_OPER_STATE_IDLE = "idle"
    DIAG_OPER_STATE_IN_PROGRESS = "in-progress"
    DIAG_OPER_STATE_UNKNOWN = "unknown"
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
    DOMAIN_CONNECTION_STATE_CONNECTED = "connected"
    DOMAIN_CONNECTION_STATE_LOST_CONNECTIVITY = "lost-connectivity"
    DOMAIN_OPER_STATE_LOST_VISIBILITY = "lost-visibility"
    DOMAIN_OPER_STATE_REGISTERED = "registered"
    DOMAIN_OPER_STATE_REGISTERING = "registering"
    DOMAIN_OPER_STATE_SYNCHRONIZING = "synchronizing"
    DOMAIN_OPER_STATE_UNREGISTERED = "unregistered"
    DOMAIN_OPER_STATE_VERSION_MISMATCH = "version-mismatch"
    DOMAIN_SUSPEND_STATE_OFF = "off"
    DOMAIN_SUSPEND_STATE_ON = "on"
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
    LOCATOR_LED_OPER_STATE_BLINKING = "blinking"
    LOCATOR_LED_OPER_STATE_ETH = "eth"
    LOCATOR_LED_OPER_STATE_FC = "fc"
    LOCATOR_LED_OPER_STATE_OFF = "off"
    LOCATOR_LED_OPER_STATE_ON = "on"
    LOCATOR_LED_OPER_STATE_UNKNOWN = "unknown"
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


class ConfigServerItem(ManagedObject):
    """This is ConfigServerItem class."""

    consts = ConfigServerItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigServerItem", "configServerItem", "server-item", VersionMeta.Version131a, "InputOutput", 0xf, [], ["read-only"], [], ['configCpuInfo'], [None])

    prop_meta = {
        "association": MoPropertyMeta("association", "association", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["associated", "establishing", "failed", "none", "removing", "throttled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "decommissioned": MoPropertyMeta("decommissioned", "decommissioned", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "diag_oper_state": MoPropertyMeta("diag_oper_state", "diagOperState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cancelled", "completed", "failed", "idle", "in-progress", "unknown"], []), 
        "diag_overall_progress": MoPropertyMeta("diag_overall_progress", "diagOverallProgress", "byte", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-100"]), 
        "discovery": MoPropertyMeta("discovery", "discovery", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["complete", "diagnostics-complete", "diagnostics-failed", "diagnostics-in-progress", "efidiagnostics-in-progress", "failed", "fru-identity-indeterminate", "fru-not-ready", "fru-state-indeterminate", "illegal-fru", "in-progress", "insufficiently-equipped", "invalid-adaptor-iocard", "malformed-fru-info", "retry", "throttled", "undiscovered", "user-acknowledged", "waiting-for-mgmt-ack", "waiting-for-user-ack"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_connection_state": MoPropertyMeta("domain_connection_state", "domainConnectionState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "lost-connectivity"], []), 
        "domain_dn": MoPropertyMeta("domain_dn", "domainDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_ipv4": MoPropertyMeta("domain_ipv4", "domainIpv4", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "domain_ipv6": MoPropertyMeta("domain_ipv6", "domainIpv6", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "domain_oper_state": MoPropertyMeta("domain_oper_state", "domainOperState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "domain_suspend_state": MoPropertyMeta("domain_suspend_state", "domainSuspendState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "fw_oper_state": MoPropertyMeta("fw_oper_state", "fwOperState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating", "upgrading"], []), 
        "fw_version": MoPropertyMeta("fw_version", "fwVersion", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "locator_led_oper_state": MoPropertyMeta("locator_led_oper_state", "locatorLedOperState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blinking", "eth", "fc", "off", "on", "unknown"], []), 
        "mgmt_ip": MoPropertyMeta("mgmt_ip", "mgmtIp", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "num_of_adaptors": MoPropertyMeta("num_of_adaptors", "numOfAdaptors", "byte", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_cores": MoPropertyMeta("num_of_cores", "numOfCores", "ushort", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oper_power": MoPropertyMeta("oper_power", "operPower", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bios-restore", "cmos-reset", "compute-failed", "compute-mismatch", "config", "config-failure", "decomissioning", "degraded", "diagnostics", "diagnostics-failed", "disabled", "discovery", "discovery-failed", "inaccessible", "indeterminate", "inoperable", "maintenance", "maintenance-failed", "ok", "pending-reassociation", "pending-reboot", "power-off", "power-problem", "removed", "restart", "test", "test-failed", "thermal-problem", "unassociated", "unconfig", "unconfig-failed", "voltage-problem"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "server_dn": MoPropertyMeta("server_dn", "serverDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "server_id": MoPropertyMeta("server_id", "serverId", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "service_profile": MoPropertyMeta("service_profile", "serviceProfile", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "total_memory": MoPropertyMeta("total_memory", "totalMemory", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "association": "association", 
        "childAction": "child_action", 
        "decommissioned": "decommissioned", 
        "diagOperState": "diag_oper_state", 
        "diagOverallProgress": "diag_overall_progress", 
        "discovery": "discovery", 
        "dn": "dn", 
        "domainConnectionState": "domain_connection_state", 
        "domainDn": "domain_dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainIpv4": "domain_ipv4", 
        "domainIpv6": "domain_ipv6", 
        "domainName": "domain_name", 
        "domainOperState": "domain_oper_state", 
        "domainSuspendState": "domain_suspend_state", 
        "faultLevel": "fault_level", 
        "fwOperState": "fw_oper_state", 
        "fwVersion": "fw_version", 
        "locatorLedOperState": "locator_led_oper_state", 
        "mgmtIp": "mgmt_ip", 
        "model": "model", 
        "numOfAdaptors": "num_of_adaptors", 
        "numOfCores": "num_of_cores", 
        "operPower": "oper_power", 
        "operState": "oper_state", 
        "rn": "rn", 
        "serial": "serial", 
        "serverDn": "server_dn", 
        "serverId": "server_id", 
        "serviceProfile": "service_profile", 
        "status": "status", 
        "totalMemory": "total_memory", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.association = None
        self.child_action = None
        self.decommissioned = None
        self.diag_oper_state = None
        self.diag_overall_progress = None
        self.discovery = None
        self.domain_connection_state = None
        self.domain_dn = None
        self.domain_group_dn = None
        self.domain_ipv4 = None
        self.domain_ipv6 = None
        self.domain_name = None
        self.domain_oper_state = None
        self.domain_suspend_state = None
        self.fault_level = None
        self.fw_oper_state = None
        self.fw_version = None
        self.locator_led_oper_state = None
        self.mgmt_ip = None
        self.model = None
        self.num_of_adaptors = None
        self.num_of_cores = None
        self.oper_power = None
        self.oper_state = None
        self.serial = None
        self.server_dn = None
        self.server_id = None
        self.service_profile = None
        self.status = None
        self.total_memory = None

        ManagedObject.__init__(self, "ConfigServerItem", parent_mo_or_dn, **kwargs)

