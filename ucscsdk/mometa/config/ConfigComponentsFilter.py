"""This module contains the general information for ConfigComponentsFilter ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigComponentsFilterConsts():
    COMPONENT_NAME_ADAPTORS = "adaptors"
    COMPONENT_NAME_CARTRIDGES = "cartridges"
    COMPONENT_NAME_CONTROLLERS = "controllers"
    COMPONENT_NAME_CPUS = "cpus"
    COMPONENT_NAME_CRYPTO_CARDS = "cryptoCards"
    COMPONENT_NAME_FANS = "fans"
    COMPONENT_NAME_GRAPHICS_CARDS = "graphicsCards"
    COMPONENT_NAME_IOMS = "ioms"
    COMPONENT_NAME_LOCAL_DISKS = "localDisks"
    COMPONENT_NAME_LUNS = "luns"
    COMPONENT_NAME_MEMORY = "memory"
    COMPONENT_NAME_MOTHERBOARDS = "motherboards"
    COMPONENT_NAME_PCIE_NODES = "pcieNodes"
    COMPONENT_NAME_PORTS = "ports"
    COMPONENT_NAME_PSUS = "psus"
    COMPONENT_NAME_XFMS = "xfms"
    EQUIPMENT_NAME_CHASSIS = "chassis"
    EQUIPMENT_NAME_FABRIC_INTERCONNECT = "fabricInterconnect"
    EQUIPMENT_NAME_FEX = "fex"
    EQUIPMENT_NAME_SERVER = "server"
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


class ConfigComponentsFilter(ManagedObject):
    """This is ConfigComponentsFilter class."""

    consts = ConfigComponentsFilterConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigComponentsFilter", "configComponentsFilter", "components-filter", VersionMeta.Version141a, "InputOutput", 0xfff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "component_name": MoPropertyMeta("component_name", "componentName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["adaptors", "cartridges", "controllers", "cpus", "cryptoCards", "fans", "graphicsCards", "ioms", "localDisks", "luns", "memory", "motherboards", "pcieNodes", "ports", "psus", "xfms"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "domain_dn": MoPropertyMeta("domain_dn", "domainDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "equipment_name": MoPropertyMeta("equipment_name", "equipmentName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["chassis", "fabricInterconnect", "fex", "server"], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "componentName": "component_name", 
        "dn": "dn", 
        "domainDn": "domain_dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainName": "domain_name", 
        "equipmentName": "equipment_name", 
        "faultLevel": "fault_level", 
        "model": "model", 
        "operState": "oper_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.component_name = None
        self.domain_dn = None
        self.domain_group_dn = None
        self.domain_name = None
        self.equipment_name = None
        self.fault_level = None
        self.model = None
        self.oper_state = None
        self.status = None

        ManagedObject.__init__(self, "ConfigComponentsFilter", parent_mo_or_dn, **kwargs)

