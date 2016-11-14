"""This module contains the general information for ConfigMotherboardItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigMotherboardItemConsts():
    BIOS_FW_STATUS_ACTIVATING = "activating"
    BIOS_FW_STATUS_BAD_IMAGE = "bad-image"
    BIOS_FW_STATUS_FAILED = "failed"
    BIOS_FW_STATUS_PENDING_NEXT_BOOT = "pending-next-boot"
    BIOS_FW_STATUS_READY = "ready"
    BIOS_FW_STATUS_REBOOTING = "rebooting"
    BIOS_FW_STATUS_SCHEDULED = "scheduled"
    BIOS_FW_STATUS_SET_STARTUP = "set-startup"
    BIOS_FW_STATUS_THROTTLED = "throttled"
    BIOS_FW_STATUS_UPDATING = "updating"
    BIOS_FW_STATUS_UPGRADING = "upgrading"
    BOARD_CONTROLLER_FW_STATUS_ACTIVATING = "activating"
    BOARD_CONTROLLER_FW_STATUS_BAD_IMAGE = "bad-image"
    BOARD_CONTROLLER_FW_STATUS_FAILED = "failed"
    BOARD_CONTROLLER_FW_STATUS_PENDING_NEXT_BOOT = "pending-next-boot"
    BOARD_CONTROLLER_FW_STATUS_READY = "ready"
    BOARD_CONTROLLER_FW_STATUS_REBOOTING = "rebooting"
    BOARD_CONTROLLER_FW_STATUS_SCHEDULED = "scheduled"
    BOARD_CONTROLLER_FW_STATUS_SET_STARTUP = "set-startup"
    BOARD_CONTROLLER_FW_STATUS_THROTTLED = "throttled"
    BOARD_CONTROLLER_FW_STATUS_UPDATING = "updating"
    BOARD_CONTROLLER_FW_STATUS_UPGRADING = "upgrading"
    FAULT_LEVEL_CLEARED = "cleared"
    FAULT_LEVEL_CONDITION = "condition"
    FAULT_LEVEL_CRITICAL = "critical"
    FAULT_LEVEL_INFO = "info"
    FAULT_LEVEL_MAJOR = "major"
    FAULT_LEVEL_MINOR = "minor"
    FAULT_LEVEL_WARNING = "warning"
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
    POWER_DEGRADED = "degraded"
    POWER_ERROR = "error"
    POWER_FAILED = "failed"
    POWER_NOT_SUPPORTED = "not-supported"
    POWER_OFF = "off"
    POWER_OFFDUTY = "offduty"
    POWER_OFFLINE = "offline"
    POWER_OK = "ok"
    POWER_ON = "on"
    POWER_ONLINE = "online"
    POWER_POWER_SAVE = "power-save"
    POWER_TEST = "test"
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


class ConfigMotherboardItem(ManagedObject):
    """This is ConfigMotherboardItem class."""

    consts = ConfigMotherboardItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigMotherboardItem", "configMotherboardItem", "motherboard-item", VersionMeta.Version141a, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "bios_fw_status": MoPropertyMeta("bios_fw_status", "biosFwStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating", "upgrading"], []), 
        "bios_fw_version": MoPropertyMeta("bios_fw_version", "biosFwVersion", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "board_controller_fw_status": MoPropertyMeta("board_controller_fw_status", "boardControllerFwStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating", "upgrading"], []), 
        "board_controller_fw_version": MoPropertyMeta("board_controller_fw_version", "boardControllerFwVersion", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "component_dn": MoPropertyMeta("component_dn", "componentDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "location": MoPropertyMeta("location", "location", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
    }

    prop_map = {
        "biosFwStatus": "bios_fw_status", 
        "biosFwVersion": "bios_fw_version", 
        "boardControllerFwStatus": "board_controller_fw_status", 
        "boardControllerFwVersion": "board_controller_fw_version", 
        "childAction": "child_action", 
        "componentDn": "component_dn", 
        "dn": "dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainName": "domain_name", 
        "faultLevel": "fault_level", 
        "id": "id", 
        "location": "location", 
        "model": "model", 
        "operState": "oper_state", 
        "power": "power", 
        "rn": "rn", 
        "serial": "serial", 
        "status": "status", 
        "thermal": "thermal", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.bios_fw_status = None
        self.bios_fw_version = None
        self.board_controller_fw_status = None
        self.board_controller_fw_version = None
        self.child_action = None
        self.component_dn = None
        self.domain_group_dn = None
        self.domain_name = None
        self.fault_level = None
        self.id = None
        self.location = None
        self.model = None
        self.oper_state = None
        self.power = None
        self.serial = None
        self.status = None
        self.thermal = None

        ManagedObject.__init__(self, "ConfigMotherboardItem", parent_mo_or_dn, **kwargs)

