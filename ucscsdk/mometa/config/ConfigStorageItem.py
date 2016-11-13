"""This module contains the general information for ConfigStorageItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigStorageItemConsts():
    BLADE_OPER_STATE_BIOS_RESTORE = "bios-restore"
    BLADE_OPER_STATE_CMOS_RESET = "cmos-reset"
    BLADE_OPER_STATE_COMPUTE_FAILED = "compute-failed"
    BLADE_OPER_STATE_COMPUTE_MISMATCH = "compute-mismatch"
    BLADE_OPER_STATE_CONFIG = "config"
    BLADE_OPER_STATE_CONFIG_FAILURE = "config-failure"
    BLADE_OPER_STATE_DECOMISSIONING = "decomissioning"
    BLADE_OPER_STATE_DEGRADED = "degraded"
    BLADE_OPER_STATE_DIAGNOSTICS = "diagnostics"
    BLADE_OPER_STATE_DIAGNOSTICS_FAILED = "diagnostics-failed"
    BLADE_OPER_STATE_DISABLED = "disabled"
    BLADE_OPER_STATE_DISCOVERY = "discovery"
    BLADE_OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    BLADE_OPER_STATE_INACCESSIBLE = "inaccessible"
    BLADE_OPER_STATE_INDETERMINATE = "indeterminate"
    BLADE_OPER_STATE_INOPERABLE = "inoperable"
    BLADE_OPER_STATE_MAINTENANCE = "maintenance"
    BLADE_OPER_STATE_MAINTENANCE_FAILED = "maintenance-failed"
    BLADE_OPER_STATE_OK = "ok"
    BLADE_OPER_STATE_PENDING_REASSOCIATION = "pending-reassociation"
    BLADE_OPER_STATE_PENDING_REBOOT = "pending-reboot"
    BLADE_OPER_STATE_POWER_OFF = "power-off"
    BLADE_OPER_STATE_POWER_PROBLEM = "power-problem"
    BLADE_OPER_STATE_REMOVED = "removed"
    BLADE_OPER_STATE_RESTART = "restart"
    BLADE_OPER_STATE_TEST = "test"
    BLADE_OPER_STATE_TEST_FAILED = "test-failed"
    BLADE_OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    BLADE_OPER_STATE_UNASSOCIATED = "unassociated"
    BLADE_OPER_STATE_UNCONFIG = "unconfig"
    BLADE_OPER_STATE_UNCONFIG_FAILED = "unconfig-failed"
    BLADE_OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    CARTRIDGE_OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    CARTRIDGE_OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    CARTRIDGE_OPER_STATE_BACKPLANE_PORT_PROBLEM = "backplane-port-problem"
    CARTRIDGE_OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    CARTRIDGE_OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    CARTRIDGE_OPER_STATE_CONFIG = "config"
    CARTRIDGE_OPER_STATE_DECOMISSIONING = "decomissioning"
    CARTRIDGE_OPER_STATE_DEGRADED = "degraded"
    CARTRIDGE_OPER_STATE_DISABLED = "disabled"
    CARTRIDGE_OPER_STATE_DISCOVERY = "discovery"
    CARTRIDGE_OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    CARTRIDGE_OPER_STATE_EQUIPMENT_PROBLEM = "equipment-problem"
    CARTRIDGE_OPER_STATE_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    CARTRIDGE_OPER_STATE_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    CARTRIDGE_OPER_STATE_IDENTIFY = "identify"
    CARTRIDGE_OPER_STATE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CARTRIDGE_OPER_STATE_INOPERABLE = "inoperable"
    CARTRIDGE_OPER_STATE_MALFORMED_FRU = "malformed-fru"
    CARTRIDGE_OPER_STATE_NOT_SUPPORTED = "not-supported"
    CARTRIDGE_OPER_STATE_OPERABLE = "operable"
    CARTRIDGE_OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
    CARTRIDGE_OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
    CARTRIDGE_OPER_STATE_POST_FAILURE = "post-failure"
    CARTRIDGE_OPER_STATE_POWER_PROBLEM = "power-problem"
    CARTRIDGE_OPER_STATE_POWERED_OFF = "powered-off"
    CARTRIDGE_OPER_STATE_REMOVED = "removed"
    CARTRIDGE_OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    CARTRIDGE_OPER_STATE_UNKNOWN = "unknown"
    CARTRIDGE_OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
    CARTRIDGE_OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    CHASSIS_ID_N_A = "N/A"
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
    STORAGE_TYPE_CARTRIDGE = "cartridge"
    STORAGE_TYPE_STORAGE_BLADE = "storageBlade"


class ConfigStorageItem(ManagedObject):
    """This is ConfigStorageItem class."""

    consts = ConfigStorageItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigStorageItem", "configStorageItem", "storage-item", VersionMeta.Version141a, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "blade_oper_state": MoPropertyMeta("blade_oper_state", "bladeOperState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bios-restore", "cmos-reset", "compute-failed", "compute-mismatch", "config", "config-failure", "decomissioning", "degraded", "diagnostics", "diagnostics-failed", "disabled", "discovery", "discovery-failed", "inaccessible", "indeterminate", "inoperable", "maintenance", "maintenance-failed", "ok", "pending-reassociation", "pending-reboot", "power-off", "power-problem", "removed", "restart", "test", "test-failed", "thermal-problem", "unassociated", "unconfig", "unconfig-failed", "voltage-problem"], []), 
        "cartridge_oper_state": MoPropertyMeta("cartridge_oper_state", "cartridgeOperState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "decommissioned": MoPropertyMeta("decommissioned", "decommissioned", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_connection_state": MoPropertyMeta("domain_connection_state", "domainConnectionState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "lost-connectivity"], []), 
        "domain_dn": MoPropertyMeta("domain_dn", "domainDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_ipv4": MoPropertyMeta("domain_ipv4", "domainIpv4", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "domain_ipv6": MoPropertyMeta("domain_ipv6", "domainIpv6", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "domain_oper_state": MoPropertyMeta("domain_oper_state", "domainOperState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "domain_suspend_state": MoPropertyMeta("domain_suspend_state", "domainSuspendState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "num_of_controllers": MoPropertyMeta("num_of_controllers", "numOfControllers", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_enclosures": MoPropertyMeta("num_of_enclosures", "numOfEnclosures", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_server_units": MoPropertyMeta("num_of_server_units", "numOfServerUnits", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_dn": MoPropertyMeta("storage_dn", "storageDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "storage_type": MoPropertyMeta("storage_type", "storageType", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cartridge", "storageBlade"], []), 
    }

    prop_map = {
        "assignedToDn": "assigned_to_dn", 
        "bladeOperState": "blade_oper_state", 
        "cartridgeOperState": "cartridge_oper_state", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "decommissioned": "decommissioned", 
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
        "numOfControllers": "num_of_controllers", 
        "numOfEnclosures": "num_of_enclosures", 
        "numOfServerUnits": "num_of_server_units", 
        "rn": "rn", 
        "serial": "serial", 
        "slotId": "slot_id", 
        "status": "status", 
        "storageDn": "storage_dn", 
        "storageType": "storage_type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.assigned_to_dn = None
        self.blade_oper_state = None
        self.cartridge_oper_state = None
        self.chassis_id = None
        self.child_action = None
        self.decommissioned = None
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
        self.num_of_controllers = None
        self.num_of_enclosures = None
        self.num_of_server_units = None
        self.serial = None
        self.slot_id = None
        self.status = None
        self.storage_dn = None
        self.storage_type = None

        ManagedObject.__init__(self, "ConfigStorageItem", parent_mo_or_dn, **kwargs)

