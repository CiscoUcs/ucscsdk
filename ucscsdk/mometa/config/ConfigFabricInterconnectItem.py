"""This module contains the general information for ConfigFabricInterconnectItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigFabricInterconnectItemConsts():
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
    ID_A = "A"
    ID_B = "B"
    ID_NONE = "NONE"
    ID_MGMT = "mgmt"
    LOCATOR_LED_OPER_STATE_BLINKING = "blinking"
    LOCATOR_LED_OPER_STATE_ETH = "eth"
    LOCATOR_LED_OPER_STATE_FC = "fc"
    LOCATOR_LED_OPER_STATE_OFF = "off"
    LOCATOR_LED_OPER_STATE_ON = "on"
    LOCATOR_LED_OPER_STATE_UNKNOWN = "unknown"


class ConfigFabricInterconnectItem(ManagedObject):
    """This is ConfigFabricInterconnectItem class."""

    consts = ConfigFabricInterconnectItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigFabricInterconnectItem", "configFabricInterconnectItem", "fabric-interconnect-item", VersionMeta.Version131a, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_connection_state": MoPropertyMeta("domain_connection_state", "domainConnectionState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "lost-connectivity"], []), 
        "domain_dn": MoPropertyMeta("domain_dn", "domainDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "domain_oper_state": MoPropertyMeta("domain_oper_state", "domainOperState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "domain_suspend_state": MoPropertyMeta("domain_suspend_state", "domainSuspendState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []), 
        "fabric_interconnect_dn": MoPropertyMeta("fabric_interconnect_dn", "fabricInterconnectDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "fw_oper_state": MoPropertyMeta("fw_oper_state", "fwOperState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating", "upgrading"], []), 
        "fw_service_pack_version": MoPropertyMeta("fw_service_pack_version", "fwServicePackVersion", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "fw_version": MoPropertyMeta("fw_version", "fwVersion", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "leadership": MoPropertyMeta("leadership", "leadership", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "locator_led_oper_state": MoPropertyMeta("locator_led_oper_state", "locatorLedOperState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blinking", "eth", "fc", "off", "on", "unknown"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "num_of_eth_ports": MoPropertyMeta("num_of_eth_ports", "numOfEthPorts", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_expansion_modules": MoPropertyMeta("num_of_expansion_modules", "numOfExpansionModules", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_fc_ports": MoPropertyMeta("num_of_fc_ports", "numOfFcPorts", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_fixed_modules": MoPropertyMeta("num_of_fixed_modules", "numOfFixedModules", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oob_if_ip": MoPropertyMeta("oob_if_ip", "oobIfIp", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "domainConnectionState": "domain_connection_state", 
        "domainDn": "domain_dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainName": "domain_name", 
        "domainOperState": "domain_oper_state", 
        "domainSuspendState": "domain_suspend_state", 
        "fabricInterconnectDn": "fabric_interconnect_dn", 
        "faultLevel": "fault_level", 
        "fwOperState": "fw_oper_state", 
        "fwServicePackVersion": "fw_service_pack_version", 
        "fwVersion": "fw_version", 
        "id": "id", 
        "leadership": "leadership", 
        "locatorLedOperState": "locator_led_oper_state", 
        "model": "model", 
        "numOfEthPorts": "num_of_eth_ports", 
        "numOfExpansionModules": "num_of_expansion_modules", 
        "numOfFcPorts": "num_of_fc_ports", 
        "numOfFixedModules": "num_of_fixed_modules", 
        "oobIfIp": "oob_if_ip", 
        "operability": "operability", 
        "rn": "rn", 
        "serial": "serial", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.domain_connection_state = None
        self.domain_dn = None
        self.domain_group_dn = None
        self.domain_name = None
        self.domain_oper_state = None
        self.domain_suspend_state = None
        self.fabric_interconnect_dn = None
        self.fault_level = None
        self.fw_oper_state = None
        self.fw_service_pack_version = None
        self.fw_version = None
        self.id = None
        self.leadership = None
        self.locator_led_oper_state = None
        self.model = None
        self.num_of_eth_ports = None
        self.num_of_expansion_modules = None
        self.num_of_fc_ports = None
        self.num_of_fixed_modules = None
        self.oob_if_ip = None
        self.operability = None
        self.serial = None
        self.status = None

        ManagedObject.__init__(self, "ConfigFabricInterconnectItem", parent_mo_or_dn, **kwargs)

