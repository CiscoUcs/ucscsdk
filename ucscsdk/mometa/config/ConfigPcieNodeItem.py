"""This module contains the general information for ConfigPcieNodeItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigPcieNodeItemConsts():
    CHASSIS_ID_N_A = "N/A"
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


class ConfigPcieNodeItem(ManagedObject):
    """This is ConfigPcieNodeItem class."""

    consts = ConfigPcieNodeItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigPcieNodeItem", "configPcieNodeItem", "pcie-node-item", VersionMeta.Version201v, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201v, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_connection_state": MoPropertyMeta("domain_connection_state", "domainConnectionState", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "lost-connectivity"], []), 
        "domain_dn": MoPropertyMeta("domain_dn", "domainDn", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_ipv4": MoPropertyMeta("domain_ipv4", "domainIpv4", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "domain_ipv6": MoPropertyMeta("domain_ipv6", "domainIpv6", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "domain_oper_state": MoPropertyMeta("domain_oper_state", "domainOperState", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "domain_suspend_state": MoPropertyMeta("domain_suspend_state", "domainSuspendState", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "pcie_node_dn": MoPropertyMeta("pcie_node_dn", "pcieNodeDn", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "serial_number": MoPropertyMeta("serial_number", "serialNumber", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201v, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
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
        "model": "model", 
        "operState": "oper_state", 
        "pcieNodeDn": "pcie_node_dn", 
        "peerDn": "peer_dn", 
        "presence": "presence", 
        "rn": "rn", 
        "serialNumber": "serial_number", 
        "slotId": "slot_id", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.chassis_id = None
        self.child_action = None
        self.domain_connection_state = None
        self.domain_dn = None
        self.domain_group_dn = None
        self.domain_ipv4 = None
        self.domain_ipv6 = None
        self.domain_name = None
        self.domain_oper_state = None
        self.domain_suspend_state = None
        self.fault_level = None
        self.model = None
        self.oper_state = None
        self.pcie_node_dn = None
        self.peer_dn = None
        self.presence = None
        self.serial_number = None
        self.slot_id = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "ConfigPcieNodeItem", parent_mo_or_dn, **kwargs)

