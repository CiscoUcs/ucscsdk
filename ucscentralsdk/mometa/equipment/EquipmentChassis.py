"""This module contains the general information for EquipmentChassis ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class EquipmentChassisConsts():
    ADMIN_STATE_ACKNOWLEDGED = "acknowledged"
    ADMIN_STATE_AUTO_ACKNOWLEDGE = "auto-acknowledge"
    ADMIN_STATE_DECOMMISSION = "decommission"
    ADMIN_STATE_DISABLE_PORT_CHANNEL = "disable-port-channel"
    ADMIN_STATE_ENABLE_PORT_CHANNEL = "enable-port-channel"
    ADMIN_STATE_RE_ACKNOWLEDGE = "re-acknowledge"
    ADMIN_STATE_REMOVE = "remove"
    CONFIG_STATE_ACK_IN_PROGRESS = "ack-in-progress"
    CONFIG_STATE_ACKNOWLEDGED = "acknowledged"
    CONFIG_STATE_AUTO_ACK = "auto-ack"
    CONFIG_STATE_EVALUATION = "evaluation"
    CONFIG_STATE_OK = "ok"
    CONFIG_STATE_REMOVING = "removing"
    CONFIG_STATE_UN_ACKNOWLEDGED = "un-acknowledged"
    CONFIG_STATE_UN_INITIALIZED = "un-initialized"
    CONFIG_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    MANAGING_INST_A = "A"
    MANAGING_INST_B = "B"
    MANAGING_INST_NONE = "NONE"
    MANAGING_INST_MGMT = "mgmt"
    OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
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
    POWER_FAILED = "failed"
    POWER_INPUT_DEGRADED = "input-degraded"
    POWER_INPUT_FAILED = "input-failed"
    POWER_OK = "ok"
    POWER_OUTPUT_DEGRADED = "output-degraded"
    POWER_OUTPUT_FAILED = "output-failed"
    POWER_REDUNDANCY_DEGRADED = "redundancy-degraded"
    POWER_REDUNDANCY_FAILED = "redundancy-failed"
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
    SEEPROM_OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    SEEPROM_OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    SEEPROM_OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    SEEPROM_OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    SEEPROM_OPER_STATE_CONFIG = "config"
    SEEPROM_OPER_STATE_DECOMISSIONING = "decomissioning"
    SEEPROM_OPER_STATE_DEGRADED = "degraded"
    SEEPROM_OPER_STATE_DISABLED = "disabled"
    SEEPROM_OPER_STATE_DISCOVERY = "discovery"
    SEEPROM_OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    SEEPROM_OPER_STATE_EQUIPMENT_PROBLEM = "equipment-problem"
    SEEPROM_OPER_STATE_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    SEEPROM_OPER_STATE_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    SEEPROM_OPER_STATE_IDENTIFY = "identify"
    SEEPROM_OPER_STATE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    SEEPROM_OPER_STATE_INOPERABLE = "inoperable"
    SEEPROM_OPER_STATE_MALFORMED_FRU = "malformed-fru"
    SEEPROM_OPER_STATE_NOT_SUPPORTED = "not-supported"
    SEEPROM_OPER_STATE_OPERABLE = "operable"
    SEEPROM_OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
    SEEPROM_OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
    SEEPROM_OPER_STATE_POST_FAILURE = "post-failure"
    SEEPROM_OPER_STATE_POWER_PROBLEM = "power-problem"
    SEEPROM_OPER_STATE_POWERED_OFF = "powered-off"
    SEEPROM_OPER_STATE_REMOVED = "removed"
    SEEPROM_OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    SEEPROM_OPER_STATE_UNKNOWN = "unknown"
    SEEPROM_OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
    SEEPROM_OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class EquipmentChassis(ManagedObject):
    """This is EquipmentChassis class."""

    consts = EquipmentChassisConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("EquipmentChassis", "equipmentChassis", "chassis-[id]", VersionMeta.Version101a, "InputOutput", 0x7f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], [u'computeSystem'], [u'computeBlade', u'computeCartridge', u'equipmentBeaconLed', u'equipmentChassisOperation', u'equipmentChassisStats', u'equipmentFanModule', u'equipmentHealthLed', u'equipmentIOCard', u'equipmentIndicatorLed', u'equipmentLocatorLed', u'equipmentPsu', u'equipmentSharedIOModule', u'equipmentSwitchIOCard', u'faultInst', u'mgmtController', u'storageBlade', u'storageController'], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["acknowledged", "auto-acknowledge", "decommission", "disable-port-channel", "enable-port-channel", "re-acknowledge", "remove"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ack-in-progress", "acknowledged", "auto-ack", "evaluation", "ok", "removing", "un-acknowledged", "un-initialized", "unsupported-connectivity"], []), 
        "conn_path": MoPropertyMeta("conn_path", "connPath", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "conn_status": MoPropertyMeta("conn_status", "connStatus", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-255"]), 
        "managing_inst": MoPropertyMeta("managing_inst", "managingInst", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_qualifier": MoPropertyMeta("oper_qualifier", "operQualifier", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|psu-voltage|iocard-voltage|fabric-unsupported-conn|chassis-post-failure|fan-power|compute-power|fan-inoperable|compute-inoperable|chassis-power|chassis-unsupported|chassis-thermal|psu-perf|iocard-perf|chassis-limit-exceeded|psu-thermal|iocard-thermal|iocard-inaccessible|chassis-inoperable|fan-voltage|removed|compute-voltage|psu-power|iocard-power|chassis-vif-capacity-reduced|chassis-voltage|psu-inoperable|iocard-inoperable|fabric-conn-problem|config|fan-perf|compute-perf|fan-thermal|compute-thermal|chassis-port-channel-enabled|chassis-perf),){0,36}(defaultValue|not-applicable|psu-voltage|iocard-voltage|fabric-unsupported-conn|chassis-post-failure|fan-power|compute-power|fan-inoperable|compute-inoperable|chassis-power|chassis-unsupported|chassis-thermal|psu-perf|iocard-perf|chassis-limit-exceeded|psu-thermal|iocard-thermal|iocard-inaccessible|chassis-inoperable|fan-voltage|removed|compute-voltage|psu-power|iocard-power|chassis-vif-capacity-reduced|chassis-voltage|psu-inoperable|iocard-inoperable|fabric-conn-problem|config|fan-perf|compute-perf|fan-thermal|compute-thermal|chassis-port-channel-enabled|chassis-perf){0,1}""", [], []), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "input-degraded", "input-failed", "ok", "output-degraded", "output-failed", "redundancy-degraded", "redundancy-failed", "unknown"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "seeprom_oper_state": MoPropertyMeta("seeprom_oper_state", "seepromOperState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "thermal_state_qualifier": MoPropertyMeta("thermal_state_qualifier", "thermalStateQualifier", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "connPath": "conn_path", 
        "connStatus": "conn_status", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "id": "id", 
        "managingInst": "managing_inst", 
        "model": "model", 
        "operQualifier": "oper_qualifier", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "power": "power", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "seepromOperState": "seeprom_oper_state", 
        "serial": "serial", 
        "status": "status", 
        "thermal": "thermal", 
        "thermalStateQualifier": "thermal_state_qualifier", 
        "usrLbl": "usr_lbl", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_state = None
        self.child_action = None
        self.config_state = None
        self.conn_path = None
        self.conn_status = None
        self.flt_aggr = None
        self.managing_inst = None
        self.model = None
        self.oper_qualifier = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.power = None
        self.presence = None
        self.revision = None
        self.seeprom_oper_state = None
        self.serial = None
        self.status = None
        self.thermal = None
        self.thermal_state_qualifier = None
        self.usr_lbl = None
        self.vendor = None

        ManagedObject.__init__(self, "EquipmentChassis", parent_mo_or_dn, **kwargs)

