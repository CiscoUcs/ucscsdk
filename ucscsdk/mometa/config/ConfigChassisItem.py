"""This module contains the general information for ConfigChassisItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigChassisItemConsts():
    ADMIN_STATE_ACKNOWLEDGED = "acknowledged"
    ADMIN_STATE_AUTO_ACKNOWLEDGE = "auto-acknowledge"
    ADMIN_STATE_DECOMMISSION = "decommission"
    ADMIN_STATE_DISABLE_PORT_CHANNEL = "disable-port-channel"
    ADMIN_STATE_ENABLE_PORT_CHANNEL = "enable-port-channel"
    ADMIN_STATE_RE_ACKNOWLEDGE = "re-acknowledge"
    ADMIN_STATE_REMOVE = "remove"
    ASSOCIATION_ASSOCIATED = "associated"
    ASSOCIATION_ESTABLISHING = "establishing"
    ASSOCIATION_FAILED = "failed"
    ASSOCIATION_NONE = "none"
    ASSOCIATION_REMOVING = "removing"
    ASSOCIATION_THROTTLED = "throttled"
    CONFIG_STATE_ACK_IN_PROGRESS = "ack-in-progress"
    CONFIG_STATE_ACKNOWLEDGED = "acknowledged"
    CONFIG_STATE_AUTO_ACK = "auto-ack"
    CONFIG_STATE_EVALUATION = "evaluation"
    CONFIG_STATE_OK = "ok"
    CONFIG_STATE_REMOVING = "removing"
    CONFIG_STATE_UN_ACKNOWLEDGED = "un-acknowledged"
    CONFIG_STATE_UN_INITIALIZED = "un-initialized"
    CONFIG_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    DECOMMISSIONED_FALSE = "false"
    DECOMMISSIONED_NO = "no"
    DECOMMISSIONED_TRUE = "true"
    DECOMMISSIONED_YES = "yes"
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
    LOCATOR_LED_OPER_STATE_BLINKING = "blinking"
    LOCATOR_LED_OPER_STATE_ETH = "eth"
    LOCATOR_LED_OPER_STATE_FC = "fc"
    LOCATOR_LED_OPER_STATE_OFF = "off"
    LOCATOR_LED_OPER_STATE_ON = "on"
    LOCATOR_LED_OPER_STATE_UNKNOWN = "unknown"
    MANAGING_INST_A = "A"
    MANAGING_INST_B = "B"
    MANAGING_INST_NONE = "NONE"
    MANAGING_INST_MGMT = "mgmt"
    OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    OPER_STATE_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_DISCOVERY = "discovery"
    OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    OPER_STATE_EQUIPMENT_PROBLEM = "equipment-problem"
    OPER_STATE_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    OPER_STATE_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    OPER_STATE_IDENTIFY = "identify"
    OPER_STATE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    OPER_STATE_INOPERABLE = "inoperable"
    OPER_STATE_MALFORMED_FRU = "malformed-fru"
    OPER_STATE_NOT_SUPPORTED = "not-supported"
    OPER_STATE_OPERABLE = "operable"
    OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
    OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
    OPER_STATE_POST_FAILURE = "post-failure"
    OPER_STATE_POWER_PROBLEM = "power-problem"
    OPER_STATE_POWERED_OFF = "powered-off"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
    OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    POWER_FAILED = "failed"
    POWER_INPUT_DEGRADED = "input-degraded"
    POWER_INPUT_FAILED = "input-failed"
    POWER_OK = "ok"
    POWER_OUTPUT_DEGRADED = "output-degraded"
    POWER_OUTPUT_FAILED = "output-failed"
    POWER_REDUNDANCY_DEGRADED = "redundancy-degraded"
    POWER_REDUNDANCY_FAILED = "redundancy-failed"
    POWER_UNKNOWN = "unknown"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class ConfigChassisItem(ManagedObject):
    """This is ConfigChassisItem class."""

    consts = ConfigChassisItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigChassisItem", "configChassisItem", "chassis-item", VersionMeta.Version131a, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "chassis_profile": MoPropertyMeta("chassis_profile", "ChassisProfile", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["acknowledged", "auto-acknowledge", "decommission", "disable-port-channel", "enable-port-channel", "re-acknowledge", "remove"], []), 
        "association": MoPropertyMeta("association", "association", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["associated", "establishing", "failed", "none", "removing", "throttled"], []), 
        "chassis_dn": MoPropertyMeta("chassis_dn", "chassisDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ack-in-progress", "acknowledged", "auto-ack", "evaluation", "ok", "removing", "un-acknowledged", "un-initialized", "unsupported-connectivity"], []), 
        "decommissioned": MoPropertyMeta("decommissioned", "decommissioned", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_connection_state": MoPropertyMeta("domain_connection_state", "domainConnectionState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "lost-connectivity"], []), 
        "domain_dn": MoPropertyMeta("domain_dn", "domainDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "domain_oper_state": MoPropertyMeta("domain_oper_state", "domainOperState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "domain_suspend_state": MoPropertyMeta("domain_suspend_state", "domainSuspendState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "locator_led_oper_state": MoPropertyMeta("locator_led_oper_state", "locatorLedOperState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blinking", "eth", "fc", "off", "on", "unknown"], []), 
        "managing_inst": MoPropertyMeta("managing_inst", "managingInst", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "num_of_blades": MoPropertyMeta("num_of_blades", "numOfBlades", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_cartridges": MoPropertyMeta("num_of_cartridges", "numOfCartridges", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_storage_blades": MoPropertyMeta("num_of_storage_blades", "numOfStorageBlades", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oper_qualifier": MoPropertyMeta("oper_qualifier", "operQualifier", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|psu-voltage|iocard-voltage|fabric-unsupported-conn|chassis-post-failure|fan-power|compute-power|fan-inoperable|compute-inoperable|chassis-power|chassis-unsupported|chassis-thermal|psu-perf|iocard-perf|chassis-limit-exceeded|psu-thermal|iocard-thermal|iocard-inaccessible|chassis-inoperable|fan-voltage|removed|compute-voltage|backplane-port-problem|psu-power|iocard-power|chassis-vif-capacity-reduced|chassis-voltage|psu-inoperable|iocard-inoperable|fabric-conn-problem|config|fan-perf|compute-perf|fan-thermal|compute-thermal|chassis-port-channel-enabled|chassis-perf),){0,37}(defaultValue|not-applicable|psu-voltage|iocard-voltage|fabric-unsupported-conn|chassis-post-failure|fan-power|compute-power|fan-inoperable|compute-inoperable|chassis-power|chassis-unsupported|chassis-thermal|psu-perf|iocard-perf|chassis-limit-exceeded|psu-thermal|iocard-thermal|iocard-inaccessible|chassis-inoperable|fan-voltage|removed|compute-voltage|backplane-port-problem|psu-power|iocard-power|chassis-vif-capacity-reduced|chassis-voltage|psu-inoperable|iocard-inoperable|fabric-conn-problem|config|fan-perf|compute-perf|fan-thermal|compute-thermal|chassis-port-channel-enabled|chassis-perf){0,1}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "input-degraded", "input-failed", "ok", "output-degraded", "output-failed", "redundancy-degraded", "redundancy-failed", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
    }

    prop_map = {
        "ChassisProfile": "chassis_profile", 
        "adminState": "admin_state", 
        "association": "association", 
        "chassisDn": "chassis_dn", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "decommissioned": "decommissioned", 
        "dn": "dn", 
        "domainConnectionState": "domain_connection_state", 
        "domainDn": "domain_dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainName": "domain_name", 
        "domainOperState": "domain_oper_state", 
        "domainSuspendState": "domain_suspend_state", 
        "faultLevel": "fault_level", 
        "id": "id", 
        "locatorLedOperState": "locator_led_oper_state", 
        "managingInst": "managing_inst", 
        "model": "model", 
        "numOfBlades": "num_of_blades", 
        "numOfCartridges": "num_of_cartridges", 
        "numOfStorageBlades": "num_of_storage_blades", 
        "operQualifier": "oper_qualifier", 
        "operState": "oper_state", 
        "power": "power", 
        "rn": "rn", 
        "serial": "serial", 
        "status": "status", 
        "thermal": "thermal", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.chassis_profile = None
        self.admin_state = None
        self.association = None
        self.chassis_dn = None
        self.child_action = None
        self.config_state = None
        self.decommissioned = None
        self.domain_connection_state = None
        self.domain_dn = None
        self.domain_group_dn = None
        self.domain_name = None
        self.domain_oper_state = None
        self.domain_suspend_state = None
        self.fault_level = None
        self.id = None
        self.locator_led_oper_state = None
        self.managing_inst = None
        self.model = None
        self.num_of_blades = None
        self.num_of_cartridges = None
        self.num_of_storage_blades = None
        self.oper_qualifier = None
        self.oper_state = None
        self.power = None
        self.serial = None
        self.status = None
        self.thermal = None

        ManagedObject.__init__(self, "ConfigChassisItem", parent_mo_or_dn, **kwargs)

