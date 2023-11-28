"""This module contains the general information for EquipmentSystemIOController ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentSystemIOControllerConsts():
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
    CHECK_POINT_DEEP_CHECKPOINT = "deep-checkpoint"
    CHECK_POINT_DISCOVERED = "discovered"
    CHECK_POINT_REMOVING = "removing"
    CHECK_POINT_SHALLOW_CHECKPOINT = "shallow-checkpoint"
    CHECK_POINT_UNKNOWN = "unknown"
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
    MANAGING_INSTANCE_A = "A"
    MANAGING_INSTANCE_B = "B"
    MANAGING_INSTANCE_NONE = "NONE"
    MANAGING_INSTANCE_MGMT = "mgmt"
    MFG_TIME_NOT_APPLICABLE = "not-applicable"
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
    ROLE_ACTIVE = "active"
    ROLE_STANDBY = "standby"
    ROLE_UNKNOWN = "unknown"
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


class EquipmentSystemIOController(ManagedObject):
    """This is EquipmentSystemIOController class."""

    consts = EquipmentSystemIOControllerConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EquipmentSystemIOController", "equipmentSystemIOController", "slot-[id]", VersionMeta.Version151a, "InputOutput", 0xff, [], ["admin", "ls-network", "ls-network-policy", "pn-equipment", "pn-maintenance", "pn-policy"], ['equipmentChassis'], ['computeBoardController', 'equipmentSharedIOModule', 'equipmentSystemIOControllerOperation', 'mgmtController'], ["Get"])

    prop_meta = {
        "admin_power_state": MoPropertyMeta("admin_power_state", "adminPowerState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["cycle-immediate", "cycle-wait", "policy"], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["acknowledged", "auto-acknowledge", "decommission", "disable-port-channel", "enable-port-channel", "re-acknowledge", "remove"], []), 
        "asset_tag": MoPropertyMeta("asset_tag", "assetTag", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]), 
        "check_point": MoPropertyMeta("check_point", "checkPoint", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deep-checkpoint", "discovered", "removing", "shallow-checkpoint", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ack-in-progress", "acknowledged", "auto-ack", "evaluation", "ok", "removing", "un-acknowledged", "un-initialized", "unsupported-connectivity"], []), 
        "conn_path": MoPropertyMeta("conn_path", "connPath", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "conn_status": MoPropertyMeta("conn_status", "connStatus", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "discovery": MoPropertyMeta("discovery", "discovery", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["auto-upgrading", "discovered", "offline", "online", "unknown", "unsupported-connectivity"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-2"]), 
        "lc_name": MoPropertyMeta("lc_name", "lcName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "lc_ts": MoPropertyMeta("lc_ts", "lcTs", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "managing_instance": MoPropertyMeta("managing_instance", "managingInstance", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "mfg_time": MoPropertyMeta("mfg_time", "mfgTime", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["not-applicable"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_qualifier": MoPropertyMeta("oper_qualifier", "operQualifier", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|thermal|inoperable|voltage|perf|power|removed|fabric-port-problem|post-failure|server-port-problem|fabricpc-link-auto-ack-blocked|backplane-port-problem),){0,12}(defaultValue|not-applicable|thermal|inoperable|voltage|perf|power|removed|fabric-port-problem|post-failure|server-port-problem|fabricpc-link-auto-ack-blocked|backplane-port-problem){0,1}""", [], []), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "perf": MoPropertyMeta("perf", "perf", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "reachability": MoPropertyMeta("reachability", "reachability", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|A|B|unmanaged),){0,3}(defaultValue|A|B|unmanaged){0,1}""", [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "role": MoPropertyMeta("role", "role", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "standby", "unknown"], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "vid": MoPropertyMeta("vid", "vid", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
    }

    prop_map = {
        "adminPowerState": "admin_power_state", 
        "adminState": "admin_state", 
        "assetTag": "asset_tag", 
        "chassisId": "chassis_id", 
        "checkPoint": "check_point", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "connPath": "conn_path", 
        "connStatus": "conn_status", 
        "discovery": "discovery", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "id": "id", 
        "lcName": "lc_name", 
        "lcTs": "lc_ts", 
        "managingInstance": "managing_instance", 
        "mfgTime": "mfg_time", 
        "model": "model", 
        "operQualifier": "oper_qualifier", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "partNumber": "part_number", 
        "perf": "perf", 
        "power": "power", 
        "presence": "presence", 
        "reachability": "reachability", 
        "revision": "revision", 
        "rn": "rn", 
        "role": "role", 
        "serial": "serial", 
        "status": "status", 
        "thermal": "thermal", 
        "usrLbl": "usr_lbl", 
        "vendor": "vendor", 
        "vid": "vid", 
        "voltage": "voltage", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_power_state = None
        self.admin_state = None
        self.asset_tag = None
        self.chassis_id = None
        self.check_point = None
        self.child_action = None
        self.config_state = None
        self.conn_path = None
        self.conn_status = None
        self.discovery = None
        self.flt_aggr = None
        self.lc_name = None
        self.lc_ts = None
        self.managing_instance = None
        self.mfg_time = None
        self.model = None
        self.oper_qualifier = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.part_number = None
        self.perf = None
        self.power = None
        self.presence = None
        self.reachability = None
        self.revision = None
        self.role = None
        self.serial = None
        self.status = None
        self.thermal = None
        self.usr_lbl = None
        self.vendor = None
        self.vid = None
        self.voltage = None

        ManagedObject.__init__(self, "EquipmentSystemIOController", parent_mo_or_dn, **kwargs)

