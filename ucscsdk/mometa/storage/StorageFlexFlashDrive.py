"""This module contains the general information for StorageFlexFlashDrive ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageFlexFlashDriveConsts():
    RWTYPE_READ_ONLY = "read_only"
    RWTYPE_READ_WRITE = "read_write"
    BLOCK_SIZE_512 = "512"
    BLOCK_SIZE_UNKNOWN = "unknown"
    CONNECTION_PROTOCOL_NVME = "NVME"
    CONNECTION_PROTOCOL_SAS = "SAS"
    CONNECTION_PROTOCOL_SATA = "SATA"
    CONNECTION_PROTOCOL_UNSPECIFIED = "unspecified"
    DRIVE_STATE_NONRAID = "NONRAID"
    DRIVE_STATE_RAID = "RAID"
    DRIVE_TYPE_DRIVERS = "Drivers"
    DRIVE_TYPE_HUU = "HUU"
    DRIVE_TYPE_HV = "HV"
    DRIVE_TYPE_SCU = "SCU"
    DRIVE_TYPE_UNKNOWN = "Unknown"
    LAST_OPERATION_PARTITION_MIRRORED = "PARTITION_MIRRORED"
    LAST_OPERATION_PARTITION_MIRRORED_ERASING = "PARTITION_MIRRORED_ERASING"
    LAST_OPERATION_PARTITION_MIRRORED_ERASING_FAIL = "PARTITION_MIRRORED_ERASING_FAIL"
    LAST_OPERATION_PARTITION_MIRRORED_ERASING_SUCCESS = "PARTITION_MIRRORED_ERASING_SUCCESS"
    LAST_OPERATION_PARTITION_MIRRORED_SYNCING = "PARTITION_MIRRORED_SYNCING"
    LAST_OPERATION_PARTITION_MIRRORED_SYNCING_FAIL = "PARTITION_MIRRORED_SYNCING_FAIL"
    LAST_OPERATION_PARTITION_MIRRORED_SYNCING_SUCCESS = "PARTITION_MIRRORED_SYNCING_SUCCESS"
    LAST_OPERATION_PARTITION_MIRRORED_UPDATING = "PARTITION_MIRRORED_UPDATING"
    LAST_OPERATION_PARTITION_MIRRORED_UPDATING_FAIL = "PARTITION_MIRRORED_UPDATING_FAIL"
    LAST_OPERATION_PARTITION_MIRRORED_UPDATING_SUCCESS = "PARTITION_MIRRORED_UPDATING_SUCCESS"
    LAST_OPERATION_PARTITION_NON_MIRRORED = "PARTITION_NON_MIRRORED"
    LAST_OPERATION_PARTITION_NON_MIRRORED_ERASING = "PARTITION_NON_MIRRORED_ERASING"
    LAST_OPERATION_PARTITION_NON_MIRRORED_ERASING_FAIL = "PARTITION_NON_MIRRORED_ERASING_FAIL"
    LAST_OPERATION_PARTITION_NON_MIRRORED_ERASING_SUCCESS = "PARTITION_NON_MIRRORED_ERASING_SUCCESS"
    LAST_OPERATION_PARTITION_NON_MIRRORED_UPDATING = "PARTITION_NON_MIRRORED_UPDATING"
    LAST_OPERATION_PARTITION_NON_MIRRORED_UPDATING_FAIL = "PARTITION_NON_MIRRORED_UPDATING_FAIL"
    LAST_OPERATION_PARTITION_NON_MIRRORED_UPDATING_SUCCESS = "PARTITION_NON_MIRRORED_UPDATING_SUCCESS"
    LAST_OPERATION_UNKNOWN = "unknown"
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
    OPERATION_STATE_PARTITION_MIRRORED = "PARTITION_MIRRORED"
    OPERATION_STATE_PARTITION_MIRRORED_ERASING = "PARTITION_MIRRORED_ERASING"
    OPERATION_STATE_PARTITION_MIRRORED_ERASING_FAIL = "PARTITION_MIRRORED_ERASING_FAIL"
    OPERATION_STATE_PARTITION_MIRRORED_ERASING_SUCCESS = "PARTITION_MIRRORED_ERASING_SUCCESS"
    OPERATION_STATE_PARTITION_MIRRORED_SYNCING = "PARTITION_MIRRORED_SYNCING"
    OPERATION_STATE_PARTITION_MIRRORED_SYNCING_FAIL = "PARTITION_MIRRORED_SYNCING_FAIL"
    OPERATION_STATE_PARTITION_MIRRORED_SYNCING_SUCCESS = "PARTITION_MIRRORED_SYNCING_SUCCESS"
    OPERATION_STATE_PARTITION_MIRRORED_UPDATING = "PARTITION_MIRRORED_UPDATING"
    OPERATION_STATE_PARTITION_MIRRORED_UPDATING_FAIL = "PARTITION_MIRRORED_UPDATING_FAIL"
    OPERATION_STATE_PARTITION_MIRRORED_UPDATING_SUCCESS = "PARTITION_MIRRORED_UPDATING_SUCCESS"
    OPERATION_STATE_PARTITION_NON_MIRRORED = "PARTITION_NON_MIRRORED"
    OPERATION_STATE_PARTITION_NON_MIRRORED_ERASING = "PARTITION_NON_MIRRORED_ERASING"
    OPERATION_STATE_PARTITION_NON_MIRRORED_ERASING_FAIL = "PARTITION_NON_MIRRORED_ERASING_FAIL"
    OPERATION_STATE_PARTITION_NON_MIRRORED_ERASING_SUCCESS = "PARTITION_NON_MIRRORED_ERASING_SUCCESS"
    OPERATION_STATE_PARTITION_NON_MIRRORED_UPDATING = "PARTITION_NON_MIRRORED_UPDATING"
    OPERATION_STATE_PARTITION_NON_MIRRORED_UPDATING_FAIL = "PARTITION_NON_MIRRORED_UPDATING_FAIL"
    OPERATION_STATE_PARTITION_NON_MIRRORED_UPDATING_SUCCESS = "PARTITION_NON_MIRRORED_UPDATING_SUCCESS"
    OPERATION_STATE_UNKNOWN = "unknown"
    PHYSICAL_BLOCK_SIZE_512 = "512"
    PHYSICAL_BLOCK_SIZE_UNKNOWN = "unknown"
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
    REMOVABLE_NA = "NA"
    REMOVABLE_NO = "no"
    REMOVABLE_YES = "yes"
    SIZE_NOT_APPLICABLE = "not-applicable"
    VISIBLE_NO = "no"
    VISIBLE_YES = "yes"


class StorageFlexFlashDrive(ManagedObject):
    """This is StorageFlexFlashDrive class."""

    consts = StorageFlexFlashDriveConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("StorageFlexFlashDrive", "storageFlexFlashDrive", "drive-[name]", VersionMeta.Version112a, "InputOutput", 0x3f, [], ["read-only"], ['storageFlexFlashCard'], [], ["Get"])

    prop_meta = {
        "rw_type": MoPropertyMeta("rw_type", "RWType", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["read_only", "read_write"], []), 
        "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "connection_protocol": MoPropertyMeta("connection_protocol", "connectionProtocol", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NVME", "SAS", "SATA", "unspecified"], []), 
        "controller_index": MoPropertyMeta("controller_index", "controllerIndex", "ushort", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "drive_state": MoPropertyMeta("drive_state", "driveState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NONRAID", "RAID"], []), 
        "drive_type": MoPropertyMeta("drive_type", "driveType", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Drivers", "HUU", "HV", "SCU", "Unknown"], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "last_operation": MoPropertyMeta("last_operation", "lastOperation", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["PARTITION_MIRRORED", "PARTITION_MIRRORED_ERASING", "PARTITION_MIRRORED_ERASING_FAIL", "PARTITION_MIRRORED_ERASING_SUCCESS", "PARTITION_MIRRORED_SYNCING", "PARTITION_MIRRORED_SYNCING_FAIL", "PARTITION_MIRRORED_SYNCING_SUCCESS", "PARTITION_MIRRORED_UPDATING", "PARTITION_MIRRORED_UPDATING_FAIL", "PARTITION_MIRRORED_UPDATING_SUCCESS", "PARTITION_NON_MIRRORED", "PARTITION_NON_MIRRORED_ERASING", "PARTITION_NON_MIRRORED_ERASING_FAIL", "PARTITION_NON_MIRRORED_ERASING_SUCCESS", "PARTITION_NON_MIRRORED_UPDATING", "PARTITION_NON_MIRRORED_UPDATING_FAIL", "PARTITION_NON_MIRRORED_UPDATING_SUCCESS", "unknown"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "operation_state": MoPropertyMeta("operation_state", "operationState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["PARTITION_MIRRORED", "PARTITION_MIRRORED_ERASING", "PARTITION_MIRRORED_ERASING_FAIL", "PARTITION_MIRRORED_ERASING_SUCCESS", "PARTITION_MIRRORED_SYNCING", "PARTITION_MIRRORED_SYNCING_FAIL", "PARTITION_MIRRORED_SYNCING_SUCCESS", "PARTITION_MIRRORED_UPDATING", "PARTITION_MIRRORED_UPDATING_FAIL", "PARTITION_MIRRORED_UPDATING_SUCCESS", "PARTITION_NON_MIRRORED", "PARTITION_NON_MIRRORED_ERASING", "PARTITION_NON_MIRRORED_ERASING_FAIL", "PARTITION_NON_MIRRORED_ERASING_SUCCESS", "PARTITION_NON_MIRRORED_UPDATING", "PARTITION_NON_MIRRORED_UPDATING_FAIL", "PARTITION_NON_MIRRORED_UPDATING_SUCCESS", "unknown"], []), 
        "physical_block_size": MoPropertyMeta("physical_block_size", "physicalBlockSize", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["512", "unknown"], ["0-4294967295"]), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "removable": MoPropertyMeta("removable", "removable", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA", "no", "yes"], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "slot_number": MoPropertyMeta("slot_number", "slotNumber", "ushort", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "visible": MoPropertyMeta("visible", "visible", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
    }

    prop_map = {
        "RWType": "rw_type", 
        "blockSize": "block_size", 
        "childAction": "child_action", 
        "connectionProtocol": "connection_protocol", 
        "controllerIndex": "controller_index", 
        "dn": "dn", 
        "driveState": "drive_state", 
        "driveType": "drive_type", 
        "id": "id", 
        "lastOperation": "last_operation", 
        "model": "model", 
        "name": "name", 
        "numberOfBlocks": "number_of_blocks", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operability": "operability", 
        "operationState": "operation_state", 
        "physicalBlockSize": "physical_block_size", 
        "presence": "presence", 
        "removable": "removable", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "size": "size", 
        "slotNumber": "slot_number", 
        "status": "status", 
        "vendor": "vendor", 
        "visible": "visible", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.rw_type = None
        self.block_size = None
        self.child_action = None
        self.connection_protocol = None
        self.controller_index = None
        self.drive_state = None
        self.drive_type = None
        self.id = None
        self.last_operation = None
        self.model = None
        self.number_of_blocks = None
        self.oper_qualifier_reason = None
        self.operability = None
        self.operation_state = None
        self.physical_block_size = None
        self.presence = None
        self.removable = None
        self.revision = None
        self.serial = None
        self.size = None
        self.slot_number = None
        self.status = None
        self.vendor = None
        self.visible = None

        ManagedObject.__init__(self, "StorageFlexFlashDrive", parent_mo_or_dn, **kwargs)

