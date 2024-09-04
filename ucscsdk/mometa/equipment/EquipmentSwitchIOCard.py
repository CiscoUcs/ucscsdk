"""This module contains the general information for EquipmentSwitchIOCard ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentSwitchIOCardConsts():
    ADMIN_PEER_POWER_STATE_CYCLE_IMMEDIATE = "cycle-immediate"
    ADMIN_PEER_POWER_STATE_CYCLE_WAIT = "cycle-wait"
    ADMIN_PEER_POWER_STATE_POLICY = "policy"
    ADMIN_POWER_STATE_CYCLE_IMMEDIATE = "cycle-immediate"
    ADMIN_POWER_STATE_CYCLE_WAIT = "cycle-wait"
    ADMIN_POWER_STATE_POLICY = "policy"
    ADMIN_STATE_ACKNOWLEDGED = "acknowledged"
    ADMIN_STATE_AUTO_ACKNOWLEDGE = "auto-acknowledge"
    ADMIN_STATE_DECOMMISSION = "decommission"
    ADMIN_STATE_DISABLE_PORT_CHANNEL = "disable-port-channel"
    ADMIN_STATE_ENABLE_PORT_CHANNEL = "enable-port-channel"
    ADMIN_STATE_RE_ACKNOWLEDGE = "re-acknowledge"
    ADMIN_STATE_REMOVE = "remove"
    CHASSIS_ID_N_A = "N/A"
    CONFIG_STATE_ACK_IN_PROGRESS = "ack-in-progress"
    CONFIG_STATE_ACKNOWLEDGED = "acknowledged"
    CONFIG_STATE_AUTO_ACK = "auto-ack"
    CONFIG_STATE_EVALUATION = "evaluation"
    CONFIG_STATE_OK = "ok"
    CONFIG_STATE_REMOVING = "removing"
    CONFIG_STATE_UN_ACKNOWLEDGED = "un-acknowledged"
    CONFIG_STATE_UN_INITIALIZED = "un-initialized"
    CONFIG_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    DISCOVERY_AUTO_UPGRADING = "auto-upgrading"
    DISCOVERY_DISCOVERED = "discovered"
    DISCOVERY_OFFLINE = "offline"
    DISCOVERY_ONLINE = "online"
    DISCOVERY_UNKNOWN = "unknown"
    DISCOVERY_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    FE_OFFLINE_TS_NEVER = "never"
    FE_READY_TS_NEVER = "never"
    MFG_TIME_NOT_APPLICABLE = "not-applicable"
    OPER_EVAC_STATE_DRAIN = "drain"
    OPER_EVAC_STATE_FILL = "fill"
    OPER_EVAC_STATE_UNKNOWN = "unknown"
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
    PEER_COMM_STATUS_CONNECTED = "connected"
    PEER_COMM_STATUS_DISCONNECTED = "disconnected"
    PEER_COMM_STATUS_UNKNOWN = "unknown"
    PERF_LOWER_CRITICAL = "lower-critical"
    PERF_LOWER_NON_CRITICAL = "lower-non-critical"
    PERF_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    PERF_NOT_SUPPORTED = "not-supported"
    PERF_OK = "ok"
    PERF_UNKNOWN = "unknown"
    PERF_UPPER_CRITICAL = "upper-critical"
    PERF_UPPER_NON_CRITICAL = "upper-non-critical"
    PERF_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
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
    PRESENCE_NOT_SUPPORTED = "not-supported"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"
    PROCESSOR_THERMAL_STATE_LOWER_CRITICAL = "lower-critical"
    PROCESSOR_THERMAL_STATE_LOWER_NON_CRITICAL = "lower-non-critical"
    PROCESSOR_THERMAL_STATE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    PROCESSOR_THERMAL_STATE_NOT_SUPPORTED = "not-supported"
    PROCESSOR_THERMAL_STATE_OK = "ok"
    PROCESSOR_THERMAL_STATE_UNKNOWN = "unknown"
    PROCESSOR_THERMAL_STATE_UPPER_CRITICAL = "upper-critical"
    PROCESSOR_THERMAL_STATE_UPPER_NON_CRITICAL = "upper-non-critical"
    PROCESSOR_THERMAL_STATE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    SIDE_LEFT = "left"
    SIDE_RIGHT = "right"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    VOLTAGE_LOWER_CRITICAL = "lower-critical"
    VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    VOLTAGE_NOT_SUPPORTED = "not-supported"
    VOLTAGE_OK = "ok"
    VOLTAGE_UNKNOWN = "unknown"
    VOLTAGE_UPPER_CRITICAL = "upper-critical"
    VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class EquipmentSwitchIOCard(ManagedObject):
    """This is EquipmentSwitchIOCard class."""

    consts = EquipmentSwitchIOCardConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EquipmentSwitchIOCard", "equipmentSwitchIOCard", "sw-slot-[id]", VersionMeta.Version121a, "InputOutput", 0x1ff, [], ["admin", "ls-network", "ls-network-policy", "pn-equipment", "pn-maintenance", "pn-policy"], ['equipmentChassis'], ['equipmentFanModule', 'mgmtController', 'portGroup'], ["Get"])

    prop_meta = {
        "admin_peer_power_state": MoPropertyMeta("admin_peer_power_state", "adminPeerPowerState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["cycle-immediate", "cycle-wait", "policy"], []), 
        "admin_power_state": MoPropertyMeta("admin_power_state", "adminPowerState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["cycle-immediate", "cycle-wait", "policy"], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["acknowledged", "auto-acknowledge", "decommission", "disable-port-channel", "enable-port-channel", "re-acknowledge", "remove"], []), 
        "base_addr": MoPropertyMeta("base_addr", "baseAddr", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ack-in-progress", "acknowledged", "auto-ack", "evaluation", "ok", "removing", "un-acknowledged", "un-initialized", "unsupported-connectivity"], []), 
        "discovery": MoPropertyMeta("discovery", "discovery", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["auto-upgrading", "discovered", "offline", "online", "unknown", "unsupported-connectivity"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "fe_offline_ts": MoPropertyMeta("fe_offline_ts", "feOfflineTs", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["never"], ["0-4294967295"]), 
        "fe_ready_ts": MoPropertyMeta("fe_ready_ts", "feReadyTs", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["never"], ["0-4294967295"]), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version121a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], ["1-2"]), 
        "lc_name": MoPropertyMeta("lc_name", "lcName", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "lc_ts": MoPropertyMeta("lc_ts", "lcTs", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "mfg_time": MoPropertyMeta("mfg_time", "mfgTime", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["not-applicable"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_evac_state": MoPropertyMeta("oper_evac_state", "operEvacState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["drain", "fill", "unknown"], []), 
        "oper_qualifier": MoPropertyMeta("oper_qualifier", "operQualifier", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|thermal|inoperable|voltage|perf|power|removed|fabric-port-problem|post-failure|server-port-problem|fabricpc-link-auto-ack-blocked|backplane-port-problem),){0,12}(defaultValue|not-applicable|thermal|inoperable|voltage|perf|power|removed|fabric-port-problem|post-failure|server-port-problem|fabricpc-link-auto-ack-blocked|backplane-port-problem){0,1}""", [], []), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "peer_comm_status": MoPropertyMeta("peer_comm_status", "peerCommStatus", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "disconnected", "unknown"], []), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "perf": MoPropertyMeta("perf", "perf", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "processor_thermal_state": MoPropertyMeta("processor_thermal_state", "processorThermalState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "side": MoPropertyMeta("side", "side", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["left", "right"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "upgrade_status": MoPropertyMeta("upgrade_status", "upgradeStatus", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unasserted|hw-change-detected|fw-change-detected|hw-incompatible|fw-incompatible|unsupported-hw-version|unsupported-fw-version|hw-change-success|fw-change-success),){0,9}(defaultValue|unasserted|hw-change-detected|fw-change-detected|hw-incompatible|fw-incompatible|unsupported-hw-version|unsupported-fw-version|hw-change-success|fw-change-success){0,1}""", [], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
    }

    prop_map = {
        "adminPeerPowerState": "admin_peer_power_state", 
        "adminPowerState": "admin_power_state", 
        "adminState": "admin_state", 
        "baseAddr": "base_addr", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "discovery": "discovery", 
        "dn": "dn", 
        "feOfflineTs": "fe_offline_ts", 
        "feReadyTs": "fe_ready_ts", 
        "fltAggr": "flt_aggr", 
        "id": "id", 
        "lcName": "lc_name", 
        "lcTs": "lc_ts", 
        "mfgTime": "mfg_time", 
        "model": "model", 
        "operEvacState": "oper_evac_state", 
        "operQualifier": "oper_qualifier", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "peerCommStatus": "peer_comm_status", 
        "peerDn": "peer_dn", 
        "perf": "perf", 
        "power": "power", 
        "presence": "presence", 
        "processorThermalState": "processor_thermal_state", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "side": "side", 
        "status": "status", 
        "switchId": "switch_id", 
        "thermal": "thermal", 
        "upgradeStatus": "upgrade_status", 
        "usrLbl": "usr_lbl", 
        "vendor": "vendor", 
        "voltage": "voltage", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_peer_power_state = None
        self.admin_power_state = None
        self.admin_state = None
        self.base_addr = None
        self.chassis_id = None
        self.child_action = None
        self.config_state = None
        self.discovery = None
        self.fe_offline_ts = None
        self.fe_ready_ts = None
        self.flt_aggr = None
        self.lc_name = None
        self.lc_ts = None
        self.mfg_time = None
        self.model = None
        self.oper_evac_state = None
        self.oper_qualifier = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.peer_comm_status = None
        self.peer_dn = None
        self.perf = None
        self.power = None
        self.presence = None
        self.processor_thermal_state = None
        self.revision = None
        self.serial = None
        self.side = None
        self.status = None
        self.switch_id = None
        self.thermal = None
        self.upgrade_status = None
        self.usr_lbl = None
        self.vendor = None
        self.voltage = None

        ManagedObject.__init__(self, "EquipmentSwitchIOCard", parent_mo_or_dn, **kwargs)

