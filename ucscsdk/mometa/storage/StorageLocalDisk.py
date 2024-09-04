"""This module contains the general information for StorageLocalDisk ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageLocalDiskConsts():
    ADMIN_ACTION_CLEAR_SECURE_DRIVE = "clear-secure-drive"
    ADMIN_ACTION_CLEAR_SECURE_FOREIGN_CONFIG_DRIVE = "clear-secure-foreign-config-drive"
    ADMIN_ACTION_DEDICATED_HOT_SPARE = "dedicated-hot-spare"
    ADMIN_ACTION_ENABLE_SECURITY = "enable-security"
    ADMIN_ACTION_GLOBAL_HOT_SPARE = "global-hot-spare"
    ADMIN_ACTION_JBOD = "jbod"
    ADMIN_ACTION_LED_OFF = "led-off"
    ADMIN_ACTION_LED_ON = "led-on"
    ADMIN_ACTION_PREPARE_FOR_REMOVAL = "prepare-for-removal"
    ADMIN_ACTION_REMOVE_HOT_SPARE = "remove-hot-spare"
    ADMIN_ACTION_UNCONFIGURED_GOOD = "unconfigured-good"
    ADMIN_ACTION_UNDO_PREPARE_FOR_REMOVAL = "undo-prepare-for-removal"
    ADMIN_ACTION_UNLOCK_FOREIGN_DRIVE = "unlock-foreign-drive"
    ADMIN_ACTION_UNSPECIFIED = "unspecified"
    ADMIN_ACTION_TRIGGER_CANCELED = "canceled"
    ADMIN_ACTION_TRIGGER_IDLE = "idle"
    ADMIN_ACTION_TRIGGER_TRIGGERED = "triggered"
    ADMIN_VIRTUAL_DRIVE_ID_UNSPECIFIED = "unspecified"
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
    CONNECTION_PROTOCOL_NVME = "NVME"
    CONNECTION_PROTOCOL_SAS = "SAS"
    CONNECTION_PROTOCOL_SATA = "SATA"
    CONNECTION_PROTOCOL_UNSPECIFIED = "unspecified"
    DEVICE_TYPE_HDD = "HDD"
    DEVICE_TYPE_NVME = "NVME"
    DEVICE_TYPE_SSD = "SSD"
    DEVICE_TYPE_UNSPECIFIED = "unspecified"
    DISCOVERED_PATH_DEFAULT = "default"
    DISCOVERED_PATH_IB = "ib"
    DISCOVERED_PATH_OOB = "oob"
    DISK_STATE_NA = "NA"
    DISK_STATE_BAD = "bad"
    DISK_STATE_COPYBACK = "copyback"
    DISK_STATE_DEDICATED_HOT_SPARE = "dedicated-hot-spare"
    DISK_STATE_DISABLED_FOR_REMOVAL = "disabled-for-removal"
    DISK_STATE_FAILED = "failed"
    DISK_STATE_FOREIGN_CONFIGURATION = "foreign-configuration"
    DISK_STATE_GLOBAL_HOT_SPARE = "global-hot-spare"
    DISK_STATE_GOOD = "good"
    DISK_STATE_JBOD = "jbod"
    DISK_STATE_LOCKED_FOREIGN_CONFIGURATION = "locked-foreign-configuration"
    DISK_STATE_OFFLINE = "offline"
    DISK_STATE_ONLINE = "online"
    DISK_STATE_PREDICTIVE_FAILURE = "predictive-failure"
    DISK_STATE_REBUILDING = "rebuilding"
    DISK_STATE_SELF_TEST_FAILED = "self-test-failed"
    DISK_STATE_UNCONFIGURED_BAD = "unconfigured-bad"
    DISK_STATE_UNCONFIGURED_GOOD = "unconfigured-good"
    DISK_STATE_UNKNOWN = "unknown"
    DISK_STATE_ZEROING = "zeroing"
    ENC_ASSOCIATION_DIRECT_ATTACHED = "direct-attached"
    ENC_ASSOCIATION_EXPANDER_ATTACHED = "expander-attached"
    ENC_ASSOCIATION_UNKNOWN = "unknown"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    LINK_SPEED_1_5_GBPS = "1-5-gbps"
    LINK_SPEED_12_GBPS = "12-gbps"
    LINK_SPEED_16_GTPS = "16-gtps"
    LINK_SPEED_2_5_GTPS = "2-5-gtps"
    LINK_SPEED_24_GBPS = "24-gbps"
    LINK_SPEED_3_GBPS = "3-gbps"
    LINK_SPEED_5_GTPS = "5-gtps"
    LINK_SPEED_6_GBPS = "6-gbps"
    LINK_SPEED_8_GTPS = "8-gtps"
    LINK_SPEED_NA = "NA"
    LINK_SPEED_DISABLED = "disabled"
    LINK_SPEED_DOWN = "down"
    LINK_SPEED_HOST_POWER_OFF = "host-power-off"
    LINK_SPEED_UNKNOWN = "unknown"
    LINK_SPEED_UNSUPPORTED_DEVICE = "unsupported-device"
    LINK_STATE_MISCONNECT = "misconnect"
    LINK_STATE_OPTIMAL = "optimal"
    LINK_STATE_SUB_OPTIMAL = "sub-optimal"
    LINK_STATE_UNKNOWN = "unknown"
    NUMBER_OF_BLOCKS_UNKNOWN = "unknown"
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
    PHYSICAL_BLOCK_SIZE_512 = "512"
    PHYSICAL_BLOCK_SIZE_UNKNOWN = "unknown"
    POWER_STATE_NA = "NA"
    POWER_STATE_ACTIVE = "active"
    POWER_STATE_OFF = "off"
    POWER_STATE_POWERSAVE = "powersave"
    POWER_STATE_TRANSITIONING = "transitioning"
    POWER_STATE_UNKNOWN = "unknown"
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
    RAW_SIZE_NOT_APPLICABLE = "not-applicable"
    SIZE_NOT_APPLICABLE = "not-applicable"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class StorageLocalDisk(ManagedObject):
    """This is StorageLocalDisk class."""

    consts = StorageLocalDiskConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageLocalDisk", "storageLocalDisk", "disk-[id]", VersionMeta.Version111a, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['storageController', 'storageEnclosure'], ['equipmentLocatorLed', 'faultInst', 'firmwareBootDefinition', 'firmwareRunning', 'storageControllerEp', 'storageDiskEnvStats', 'storageLocalDiskOperation', 'storageLocalDiskPartition', 'storageOperation', 'storageSasPort'], ["Get"])

    prop_meta = {
        "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["clear-secure-drive", "clear-secure-foreign-config-drive", "dedicated-hot-spare", "enable-security", "global-hot-spare", "jbod", "led-off", "led-on", "prepare-for-removal", "remove-hot-spare", "unconfigured-good", "undo-prepare-for-removal", "unlock-foreign-drive", "unspecified"], []), 
        "admin_action_trigger": MoPropertyMeta("admin_action_trigger", "adminActionTrigger", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["canceled", "idle", "triggered"], []), 
        "admin_security_key": MoPropertyMeta("admin_security_key", "adminSecurityKey", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []), 
        "admin_virtual_drive_id": MoPropertyMeta("admin_virtual_drive_id", "adminVirtualDriveId", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]), 
        "bootable": MoPropertyMeta("bootable", "bootable", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "true", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_check_point": MoPropertyMeta("config_check_point", "configCheckPoint", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|firmware-inventory-reported),){0,2}(defaultValue|unknown|firmware-inventory-reported){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A", "applied", "apply-failed", "applying", "not-applied", "not-in-use", "orphaned", "unknown"], []), 
        "connection_protocol": MoPropertyMeta("connection_protocol", "connectionProtocol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NVME", "SAS", "SATA", "unspecified"], []), 
        "device_type": MoPropertyMeta("device_type", "deviceType", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["HDD", "NVME", "SSD", "unspecified"], []), 
        "device_version": MoPropertyMeta("device_version", "deviceVersion", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "discovered_path": MoPropertyMeta("discovered_path", "discoveredPath", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "ib", "oob"], []), 
        "disk_state": MoPropertyMeta("disk_state", "diskState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "bad", "copyback", "dedicated-hot-spare", "disabled-for-removal", "failed", "foreign-configuration", "global-hot-spare", "good", "jbod", "locked-foreign-configuration", "offline", "online", "predictive-failure", "rebuilding", "self-test-failed", "unconfigured-bad", "unconfigured-good", "unknown", "zeroing"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "drive_state": MoPropertyMeta("drive_state", "driveState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|securityCapable|securityEnabled|secured|locked|foreignSecured),){0,6}(defaultValue|none|securityCapable|securityEnabled|secured|locked|foreignSecured){0,1}""", [], []), 
        "enc_association": MoPropertyMeta("enc_association", "encAssociation", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["direct-attached", "expander-attached", "unknown"], []), 
        "err_description": MoPropertyMeta("err_description", "errDescription", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 64, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "link_speed": MoPropertyMeta("link_speed", "linkSpeed", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1-5-gbps", "12-gbps", "16-gtps", "2-5-gtps", "24-gbps", "3-gbps", "5-gtps", "6-gbps", "8-gtps", "NA", "disabled", "down", "host-power-off", "unknown", "unsupported-device"], []), 
        "link_state": MoPropertyMeta("link_state", "linkState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["misconnect", "optimal", "sub-optimal", "unknown"], []), 
        "link_state_reason": MoPropertyMeta("link_state_reason", "linkStateReason", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "physical_block_size": MoPropertyMeta("physical_block_size", "physicalBlockSize", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]), 
        "power_state": MoPropertyMeta("power_state", "powerState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "active", "off", "powersave", "transitioning", "unknown"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "raw_size": MoPropertyMeta("raw_size", "rawSize", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "variant_type": MoPropertyMeta("variant_type", "variantType", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminAction": "admin_action", 
        "adminActionTrigger": "admin_action_trigger", 
        "adminSecurityKey": "admin_security_key", 
        "adminVirtualDriveId": "admin_virtual_drive_id", 
        "blockSize": "block_size", 
        "bootable": "bootable", 
        "childAction": "child_action", 
        "configCheckPoint": "config_check_point", 
        "configState": "config_state", 
        "connectionProtocol": "connection_protocol", 
        "deviceType": "device_type", 
        "deviceVersion": "device_version", 
        "discoveredPath": "discovered_path", 
        "diskState": "disk_state", 
        "dn": "dn", 
        "driveState": "drive_state", 
        "encAssociation": "enc_association", 
        "errDescription": "err_description", 
        "id": "id", 
        "lc": "lc", 
        "linkSpeed": "link_speed", 
        "linkState": "link_state", 
        "linkStateReason": "link_state_reason", 
        "model": "model", 
        "numberOfBlocks": "number_of_blocks", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operability": "operability", 
        "physicalBlockSize": "physical_block_size", 
        "powerState": "power_state", 
        "presence": "presence", 
        "rawSize": "raw_size", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "size": "size", 
        "status": "status", 
        "thermal": "thermal", 
        "variantType": "variant_type", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.admin_action_trigger = None
        self.admin_security_key = None
        self.admin_virtual_drive_id = None
        self.block_size = None
        self.bootable = None
        self.child_action = None
        self.config_check_point = None
        self.config_state = None
        self.connection_protocol = None
        self.device_type = None
        self.device_version = None
        self.discovered_path = None
        self.disk_state = None
        self.drive_state = None
        self.enc_association = None
        self.err_description = None
        self.lc = None
        self.link_speed = None
        self.link_state = None
        self.link_state_reason = None
        self.model = None
        self.number_of_blocks = None
        self.oper_qualifier_reason = None
        self.operability = None
        self.physical_block_size = None
        self.power_state = None
        self.presence = None
        self.raw_size = None
        self.revision = None
        self.serial = None
        self.size = None
        self.status = None
        self.thermal = None
        self.variant_type = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageLocalDisk", parent_mo_or_dn, **kwargs)

