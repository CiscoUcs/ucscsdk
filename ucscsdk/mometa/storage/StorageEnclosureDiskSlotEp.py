"""This module contains the general information for StorageEnclosureDiskSlotEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageEnclosureDiskSlotEpConsts():
    AUTO_ZONE_CAUSE_HDD_TRAY_IN_LIEU_OF_SERVER2 = "hdd-tray-in-lieu-of-server2"
    AUTO_ZONE_CAUSE_HDDSLOT_UNASSIGNED = "hddslot-unassigned"
    AUTO_ZONE_CAUSE_HOTSPARE_UNSUPPORTED = "hotspare-unsupported"
    AUTO_ZONE_CAUSE_MEZZ_CONTROLLER_IN_IOEXPANDER = "mezz-controller-in-ioexpander"
    AUTO_ZONE_CAUSE_NONE = "none"
    AUTO_ZONE_CAUSE_SECOND_CONTROLLER_ABSENT = "second-controller-absent"
    AUTO_ZONE_CAUSE_SHARING_UNSUPPORTED = "sharing-unsupported"
    CONFIGURATION_NOT_SUPPORTED = "not-supported"
    CONFIGURATION_SUPPORTED = "supported"
    CONFIGURATION_UNKNOWN = "unknown"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
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
    OWNERSHIP_CHASSIS_DEDICATED_SPARE = "chassis-dedicated-spare"
    OWNERSHIP_CHASSIS_GLOBAL_SPARE = "chassis-global-spare"
    OWNERSHIP_DEDICATED = "dedicated"
    OWNERSHIP_SHARED = "shared"
    OWNERSHIP_UNASSIGNED = "unassigned"
    OWNERSHIP_UNKNOWN = "unknown"
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


class StorageEnclosureDiskSlotEp(ManagedObject):
    """This is StorageEnclosureDiskSlotEp class."""

    consts = StorageEnclosureDiskSlotEpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageEnclosureDiskSlotEp", "storageEnclosureDiskSlotEp", "disk-slot-[id]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['storageEnclosure'], ['storageControllerRef'], ["Get"])

    prop_meta = {
        "auto_zone_cause": MoPropertyMeta("auto_zone_cause", "autoZoneCause", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["hdd-tray-in-lieu-of-server2", "hddslot-unassigned", "hotspare-unsupported", "mezz-controller-in-ioexpander", "none", "second-controller-absent", "sharing-unsupported"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "configuration": MoPropertyMeta("configuration", "configuration", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-supported", "supported", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis-dedicated-spare", "chassis-global-spare", "dedicated", "shared", "unassigned", "unknown"], []), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "autoZoneCause": "auto_zone_cause", 
        "childAction": "child_action", 
        "configuration": "configuration", 
        "dn": "dn", 
        "id": "id", 
        "lc": "lc", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operability": "operability", 
        "ownership": "ownership", 
        "peerDn": "peer_dn", 
        "presence": "presence", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.auto_zone_cause = None
        self.child_action = None
        self.configuration = None
        self.lc = None
        self.oper_qualifier_reason = None
        self.operability = None
        self.ownership = None
        self.peer_dn = None
        self.presence = None
        self.status = None

        ManagedObject.__init__(self, "StorageEnclosureDiskSlotEp", parent_mo_or_dn, **kwargs)

