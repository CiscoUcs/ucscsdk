"""This module contains the general information for ConfigLunItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigLunItemConsts():
    BLOCK_SIZE_512 = "512"
    BLOCK_SIZE_UNKNOWN = "unknown"
    BOOTABLE_FALSE = "false"
    BOOTABLE_TRUE = "true"
    BOOTABLE_UNKNOWN = "unknown"
    CONFIG_STATE_N_A = "N/A"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLY_FAILED = "apply-failed"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_NOT_IN_USE = "not-in-use"
    CONFIG_STATE_ORPHANED = "orphaned"
    CONFIG_STATE_UNKNOWN = "unknown"
    DRIVE_STATE_CACHE_DEGRADED = "cache-degraded"
    DRIVE_STATE_DEGRADED = "degraded"
    DRIVE_STATE_OFFLINE = "offline"
    DRIVE_STATE_OPTIMAL = "optimal"
    DRIVE_STATE_PARTIALLY_DEGRADED = "partially-degraded"
    DRIVE_STATE_REBUILDING = "rebuilding"
    DRIVE_STATE_UNKNOWN = "unknown"
    EQUIPMENT_TYPE_CHASSIS = "chassis"
    EQUIPMENT_TYPE_FABRIC_INTERCONNECT = "fabricInterconnect"
    EQUIPMENT_TYPE_FEX = "fex"
    EQUIPMENT_TYPE_SERVER = "server"
    NUMBER_OF_BLOCKS_UNKNOWN = "unknown"
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


class ConfigLunItem(ManagedObject):
    """This is ConfigLunItem class."""

    consts = ConfigLunItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigLunItem", "configLunItem", "lun-item", VersionMeta.Version141a, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "affected_sp": MoPropertyMeta("affected_sp", "affectedSP", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]), 
        "bootable": MoPropertyMeta("bootable", "bootable", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "true", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "component_dn": MoPropertyMeta("component_dn", "componentDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A", "applied", "apply-failed", "applying", "not-applied", "not-in-use", "orphaned", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "drive_state": MoPropertyMeta("drive_state", "driveState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cache-degraded", "degraded", "offline", "optimal", "partially-degraded", "rebuilding", "unknown"], []), 
        "equipment_type": MoPropertyMeta("equipment_type", "equipmentType", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis", "fabricInterconnect", "fex", "server"], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "location": MoPropertyMeta("location", "location", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_profile": MoPropertyMeta("storage_profile", "storageProfile", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "affectedSP": "affected_sp", 
        "blockSize": "block_size", 
        "bootable": "bootable", 
        "childAction": "child_action", 
        "componentDn": "component_dn", 
        "configState": "config_state", 
        "dn": "dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainName": "domain_name", 
        "driveState": "drive_state", 
        "equipmentType": "equipment_type", 
        "id": "id", 
        "location": "location", 
        "name": "name", 
        "numberOfBlocks": "number_of_blocks", 
        "operState": "oper_state", 
        "presence": "presence", 
        "rn": "rn", 
        "size": "size", 
        "status": "status", 
        "storageProfile": "storage_profile", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.affected_sp = None
        self.block_size = None
        self.bootable = None
        self.child_action = None
        self.component_dn = None
        self.config_state = None
        self.domain_group_dn = None
        self.domain_name = None
        self.drive_state = None
        self.equipment_type = None
        self.id = None
        self.location = None
        self.name = None
        self.number_of_blocks = None
        self.oper_state = None
        self.presence = None
        self.size = None
        self.status = None
        self.storage_profile = None

        ManagedObject.__init__(self, "ConfigLunItem", parent_mo_or_dn, **kwargs)

