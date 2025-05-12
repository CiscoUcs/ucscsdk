"""This module contains the general information for StorageFlexFlashController ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageFlexFlashControllerConsts():
    ADMIN_SLOT_NUMBER_1 = "1"
    ADMIN_SLOT_NUMBER_2 = "2"
    ADMIN_SLOT_NUMBER_NA = "NA"
    CONFIGURED_MODE_INDEPENDENT_DRIVES = "independent-drives"
    CONFIGURED_MODE_MIRROR = "mirror"
    CONFIGURED_MODE_UNKNOWN = "unknown"
    CONTROLLER_HEALTH_FFCH_ERROR_CARDS_ACCESS_ERROR = "FFCH_ERROR_CARDS_ACCESS_ERROR"
    CONTROLLER_HEALTH_FFCH_ERROR_CARD_SIZE_MISMATCH = "FFCH_ERROR_CARD_SIZE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_ERROR_INCONSISTANT_METADATA_IGNORED = "FFCH_ERROR_INCONSISTANT_METADATA_IGNORED"
    CONTROLLER_HEALTH_FFCH_ERROR_INVALID_SIZE = "FFCH_ERROR_INVALID_SIZE"
    CONTROLLER_HEALTH_FFCH_ERROR_MEDIA_WRITE_PROTECTED = "FFCH_ERROR_MEDIA_WRITE_PROTECTED"
    CONTROLLER_HEALTH_FFCH_ERROR_OLD_FIRMWARE_RUNNING = "FFCH_ERROR_OLD_FIRMWARE_RUNNING"
    CONTROLLER_HEALTH_FFCH_ERROR_REBOOTED_DURING_REBUILD = "FFCH_ERROR_REBOOTED_DURING_REBUILD"
    CONTROLLER_HEALTH_FFCH_ERROR_SD247_CARD_DETECTED = "FFCH_ERROR_SD247_CARD_DETECTED"
    CONTROLLER_HEALTH_FFCH_ERROR_SD253_WITH_UN_OR_SD247 = "FFCH_ERROR_SD253_WITH_UN_OR_SD247"
    CONTROLLER_HEALTH_FFCH_ERROR_SD_CARD_NOT_CONFIGURED = "FFCH_ERROR_SD_CARD_NOT_CONFIGURED"
    CONTROLLER_HEALTH_FFCH_ERROR_SECONDARY_UNHEALTHY_CARD = "FFCH_ERROR_SECONDARY_UNHEALTHY_CARD"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_IM_SD0_IGNORED_SD1 = "FFCH_FLEXD_ERROR_IM_SD0_IGNORED_SD1"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_IM_SD0_SD1_IGNORED = "FFCH_FLEXD_ERROR_IM_SD0_SD1_IGNORED"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_IM_SD_CARDS_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_IM_SD_CARDS_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_IM_SD_HEALTHY_SD_UN_IGNORED = "FFCH_FLEXD_ERROR_IM_SD_HEALTHY_SD_UN_IGNORED"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_IM_SD_UNHEALTHY_SD_UN_IGNORED = "FFCH_FLEXD_ERROR_IM_SD_UNHEALTHY_SD_UN_IGNORED"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_CARD0_HEALTHY_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_SD_CARD0_HEALTHY_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_CARD0_UNHEALTHY_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_SD_CARD0_UNHEALTHY_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_CARD1_HEALTHY_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_SD_CARD1_HEALTHY_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_CARD1_UNHEALTHY_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_SD_CARD1_UNHEALTHY_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_CARD_OP_MODE_MISMATCH = "FFCH_FLEXD_ERROR_SD_CARD_OP_MODE_MISMATCH"
    CONTROLLER_HEALTH_FFCH_FLEXD_ERROR_SD_OP_MODE_MISMATCH_WITH_UN = "FFCH_FLEXD_ERROR_SD_OP_MODE_MISMATCH_WITH_UN"
    CONTROLLER_HEALTH_FFCH_INCONSISTENT_METADATA = "FFCH_INCONSISTENT_METADATA"
    CONTROLLER_HEALTH_FFCH_METADATA_FAILURE = "FFCH_METADATA_FAILURE"
    CONTROLLER_HEALTH_FFCH_OK = "FFCH_OK"
    CONTROLLER_STATE_FFC_CONFIG = "FFC_CONFIG"
    CONTROLLER_STATE_FFC_FAILED = "FFC_FAILED"
    CONTROLLER_STATE_FFC_INIT = "FFC_INIT"
    CONTROLLER_STATE_FFC_REBUILDING = "FFC_REBUILDING"
    CONTROLLER_STATE_FFC_SOFTWARE_ERR = "FFC_SOFTWARE_ERR"
    CONTROLLER_STATE_FFC_UNINITALIZED = "FFC_UNINITALIZED"
    CONTROLLER_STATE_FFC_USB_CONNECTED = "FFC_USB_CONNECTED"
    CONTROLLER_STATE_FFC_USB_CONNECTING = "FFC_USB_CONNECTING"
    CONTROLLER_STATE_FFC_USB_DISCONNECTED = "FFC_USB_DISCONNECTED"
    CONTROLLER_STATE_FFC_USB_DISCONNECTING = "FFC_USB_DISCONNECTING"
    CONTROLLER_STATE_FFC_WAIT_USER = "FFC_WAIT_USER"
    FLEX_FLASH_TYPE_ASTORIA = "Astoria"
    FLEX_FLASH_TYPE_FX3_S = "FX3S"
    FLEX_FLASH_TYPE_UNKNOWN = "Unknown"
    HAS_ERROR_ERROR = "error"
    HAS_ERROR_NO_ERROR = "no_error"
    IS_CARD_MISMATCH_MATCH = "MATCH"
    IS_CARD_MISMATCH_MISMATCH = "MISMATCH"
    IS_CARD_MISMATCH_NA = "NA"
    IS_FORMAT_FSMRUNNING_NA = "NA"
    IS_FORMAT_FSMRUNNING_NO = "NO"
    IS_FORMAT_FSMRUNNING_YES = "YES"
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
    OPERATING_MODE_INDEPENDENT_DRIVES = "independent-drives"
    OPERATING_MODE_MIRROR = "mirror"
    OPERATING_MODE_UNKNOWN = "unknown"
    OPERATION_REQUEST_FORMAT = "format"
    OPERATION_REQUEST_PAIR = "pair"
    OPERATION_REQUEST_RESET = "reset"
    OPERATION_REQUEST_UNKNOWN = "unknown"
    OPERATION_REQUEST_UNPAIR = "unpair"
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
    RAID_SYNC_SUPPORT_NO = "no"
    RAID_SYNC_SUPPORT_YES = "yes"
    SUB_TYPE_NA = "NA"
    SUB_TYPE_NVME_FRONT = "NVME-FRONT"
    SUB_TYPE_NVME_HHHL = "NVME-HHHL"
    SUB_TYPE_NVME_M2 = "NVME-M2"
    SUB_TYPE_NVME_MEZZ = "NVME-MEZZ"
    SUB_TYPE_NVME_REAR = "NVME-REAR"
    SUB_TYPE_RDE = "RDE"
    THERMAL_LOWER_CRITICAL = "lower-critical"
    THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    THERMAL_NOT_SUPPORTED = "not-supported"
    THERMAL_OK = "ok"
    THERMAL_UNKNOWN = "unknown"
    THERMAL_UPPER_CRITICAL = "upper-critical"
    THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    TYPE_FLASH = "FLASH"
    TYPE_HBA = "HBA"
    TYPE_NVME = "NVME"
    TYPE_PCH = "PCH"
    TYPE_PT = "PT"
    TYPE_SAS = "SAS"
    TYPE_SATA = "SATA"
    TYPE_SD = "SD"
    TYPE_EXTERNAL = "external"
    TYPE_UNKNOWN = "unknown"
    VOLTAGE_LOWER_CRITICAL = "lower-critical"
    VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    VOLTAGE_NOT_SUPPORTED = "not-supported"
    VOLTAGE_OK = "ok"
    VOLTAGE_UNKNOWN = "unknown"
    VOLTAGE_UPPER_CRITICAL = "upper-critical"
    VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"


class StorageFlexFlashController(ManagedObject):
    """This is StorageFlexFlashController class."""

    consts = StorageFlexFlashControllerConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageFlexFlashController", "storageFlexFlashController", "storage-flexflash-[id]", VersionMeta.Version112a, "InputOutput", 0x7f, [], ["admin"], ['computeBoard'], ['firmwareRunning', 'storageFlexFlashCard', 'storageFlexFlashControllerOperation', 'storageFlexFlashVirtualDrive', 'storageLocalDiskConfigDef'], ["Get"])

    prop_meta = {
        "admin_slot_number": MoPropertyMeta("admin_slot_number", "adminSlotNumber", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["1", "2", "NA"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "configured_mode": MoPropertyMeta("configured_mode", "configuredMode", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["independent-drives", "mirror", "unknown"], []), 
        "controller_health": MoPropertyMeta("controller_health", "controllerHealth", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["FFCH_ERROR_CARDS_ACCESS_ERROR", "FFCH_ERROR_CARD_SIZE_MISMATCH", "FFCH_ERROR_INCONSISTANT_METADATA_IGNORED", "FFCH_ERROR_INVALID_SIZE", "FFCH_ERROR_MEDIA_WRITE_PROTECTED", "FFCH_ERROR_OLD_FIRMWARE_RUNNING", "FFCH_ERROR_REBOOTED_DURING_REBUILD", "FFCH_ERROR_SD247_CARD_DETECTED", "FFCH_ERROR_SD253_WITH_UN_OR_SD247", "FFCH_ERROR_SD_CARD_NOT_CONFIGURED", "FFCH_ERROR_SECONDARY_UNHEALTHY_CARD", "FFCH_FLEXD_ERROR_IM_SD0_IGNORED_SD1", "FFCH_FLEXD_ERROR_IM_SD0_SD1_IGNORED", "FFCH_FLEXD_ERROR_IM_SD_CARDS_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_IM_SD_HEALTHY_SD_UN_IGNORED", "FFCH_FLEXD_ERROR_IM_SD_UNHEALTHY_SD_UN_IGNORED", "FFCH_FLEXD_ERROR_SD_CARD0_HEALTHY_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_SD_CARD0_UNHEALTHY_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_SD_CARD1_HEALTHY_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_SD_CARD1_UNHEALTHY_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_SD_CARD_OP_MODE_MISMATCH", "FFCH_FLEXD_ERROR_SD_OP_MODE_MISMATCH_WITH_UN", "FFCH_INCONSISTENT_METADATA", "FFCH_METADATA_FAILURE", "FFCH_OK"], []), 
        "controller_state": MoPropertyMeta("controller_state", "controllerState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["FFC_CONFIG", "FFC_FAILED", "FFC_INIT", "FFC_REBUILDING", "FFC_SOFTWARE_ERR", "FFC_UNINITALIZED", "FFC_USB_CONNECTED", "FFC_USB_CONNECTING", "FFC_USB_DISCONNECTED", "FFC_USB_DISCONNECTING", "FFC_WAIT_USER"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "flex_flash_type": MoPropertyMeta("flex_flash_type", "flexFlashType", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Astoria", "FX3S", "Unknown"], []), 
        "has_error": MoPropertyMeta("has_error", "hasError", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["error", "no_error"], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-64"]), 
        "is_card_mismatch": MoPropertyMeta("is_card_mismatch", "isCardMismatch", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["MATCH", "MISMATCH", "NA"], []), 
        "is_format_fsm_running": MoPropertyMeta("is_format_fsm_running", "isFormatFSMRunning", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "NO", "YES"], []), 
        "location_dn": MoPropertyMeta("location_dn", "locationDn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "operating_mode": MoPropertyMeta("operating_mode", "operatingMode", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["independent-drives", "mirror", "unknown"], []), 
        "operation_request": MoPropertyMeta("operation_request", "operationRequest", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["format", "pair", "reset", "unknown", "unpair"], []), 
        "pci_addr": MoPropertyMeta("pci_addr", "pciAddr", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pci_slot": MoPropertyMeta("pci_slot", "pciSlot", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "perf": MoPropertyMeta("perf", "perf", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "physical_drive_count": MoPropertyMeta("physical_drive_count", "physicalDriveCount", "ushort", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "power": MoPropertyMeta("power", "power", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "failed", "not-supported", "off", "offduty", "offline", "ok", "on", "online", "power-save", "test", "unknown"], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "primary_slot_number": MoPropertyMeta("primary_slot_number", "primarySlotNumber", "ushort", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "raid_sync_support": MoPropertyMeta("raid_sync_support", "raidSyncSupport", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "read_error_threshold": MoPropertyMeta("read_error_threshold", "readErrorThreshold", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sub_type": MoPropertyMeta("sub_type", "subType", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "NVME-FRONT", "NVME-HHHL", "NVME-M2", "NVME-MEZZ", "NVME-REAR", "RDE"], []), 
        "thermal": MoPropertyMeta("thermal", "thermal", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["FLASH", "HBA", "NVME", "PCH", "PT", "SAS", "SATA", "SD", "external", "unknown"], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "virtual_drive_count": MoPropertyMeta("virtual_drive_count", "virtualDriveCount", "ushort", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "voltage": MoPropertyMeta("voltage", "voltage", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], []), 
        "write_error_threshold": MoPropertyMeta("write_error_threshold", "writeErrorThreshold", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "adminSlotNumber": "admin_slot_number", 
        "childAction": "child_action", 
        "configuredMode": "configured_mode", 
        "controllerHealth": "controller_health", 
        "controllerState": "controller_state", 
        "dn": "dn", 
        "firmwareVersion": "firmware_version", 
        "flexFlashType": "flex_flash_type", 
        "hasError": "has_error", 
        "id": "id", 
        "isCardMismatch": "is_card_mismatch", 
        "isFormatFSMRunning": "is_format_fsm_running", 
        "locationDn": "location_dn", 
        "model": "model", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "operatingMode": "operating_mode", 
        "operationRequest": "operation_request", 
        "pciAddr": "pci_addr", 
        "pciSlot": "pci_slot", 
        "perf": "perf", 
        "physicalDriveCount": "physical_drive_count", 
        "power": "power", 
        "presence": "presence", 
        "primarySlotNumber": "primary_slot_number", 
        "raidSyncSupport": "raid_sync_support", 
        "readErrorThreshold": "read_error_threshold", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "status": "status", 
        "subType": "sub_type", 
        "thermal": "thermal", 
        "type": "type", 
        "vendor": "vendor", 
        "virtualDriveCount": "virtual_drive_count", 
        "voltage": "voltage", 
        "writeErrorThreshold": "write_error_threshold", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_slot_number = None
        self.child_action = None
        self.configured_mode = None
        self.controller_health = None
        self.controller_state = None
        self.firmware_version = None
        self.flex_flash_type = None
        self.has_error = None
        self.is_card_mismatch = None
        self.is_format_fsm_running = None
        self.location_dn = None
        self.model = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.operating_mode = None
        self.operation_request = None
        self.pci_addr = None
        self.pci_slot = None
        self.perf = None
        self.physical_drive_count = None
        self.power = None
        self.presence = None
        self.primary_slot_number = None
        self.raid_sync_support = None
        self.read_error_threshold = None
        self.revision = None
        self.serial = None
        self.status = None
        self.sub_type = None
        self.thermal = None
        self.type = None
        self.vendor = None
        self.virtual_drive_count = None
        self.voltage = None
        self.write_error_threshold = None

        ManagedObject.__init__(self, "StorageFlexFlashController", parent_mo_or_dn, **kwargs)

