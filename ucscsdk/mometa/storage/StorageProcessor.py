"""This module contains the general information for StorageProcessor ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageProcessorConsts():
    ADMIN_LEADERSHIP_ACTIVE = "active"
    ADMIN_LEADERSHIP_PASSIVE = "passive"
    ADMIN_LEADERSHIP_UNKNOWN = "unknown"
    ADMIN_STATE_FULL_MAINTENANCE = "full-maintenance"
    ADMIN_STATE_IN_MAINTENANCE = "in-maintenance"
    ADMIN_STATE_IN_SERVICE = "in-service"
    CIMC_BACKUP_TRIGGER_STATUS_DISABLED = "disabled"
    CIMC_BACKUP_TRIGGER_STATUS_ENABLED = "enabled"
    CIMC_BACKUP_TRIGGER_STATUS_UNKNOWN = "unknown"
    CIMC_HEARTBEAT_STATUS_DISABLED = "disabled"
    CIMC_HEARTBEAT_STATUS_RUNNING = "running"
    CIMC_HEARTBEAT_STATUS_TIMED_OUT = "timed-out"
    CIMC_HEARTBEAT_STATUS_UNKNOWN = "unknown"
    CLUSTER_STATE_DEGRADED = "degraded"
    CLUSTER_STATE_OK = "ok"
    CLUSTER_STATE_UNKNOWN = "unknown"
    CONFIG_STATE_DISRUPTIVE = "disruptive"
    CONFIG_STATE_OK = "ok"
    CONFIG_STATE_UNKNOWN = "unknown"
    DEPLOY_ACTION_ABORT_REPLICATION = "abort-replication"
    DEPLOY_ACTION_CREATE = "create"
    DEPLOY_ACTION_DELETE = "delete"
    DEPLOY_ACTION_MODIFY = "modify"
    DEPLOY_ACTION_NO_ACTION = "no-action"
    DEPLOY_ACTION_REPLACE = "replace"
    DEPLOY_ACTION_RESTORE = "restore"
    DEPLOY_ACTION_SET_OFFLINE = "set-offline"
    DEPLOY_ACTION_SET_ONLINE = "set-online"
    HA_STATE_DEGRADED = "degraded"
    HA_STATE_ELECTION_FAILED = "election-failed"
    HA_STATE_FAILOVER_IN_PROGRESS = "failover-in-progress"
    HA_STATE_NOT_READY = "not-ready"
    HA_STATE_OFFLINE = "offline"
    HA_STATE_READY = "ready"
    HA_STATE_UNKNOWN = "unknown"
    LEADERSHIP_ACTIVE = "active"
    LEADERSHIP_PASSIVE = "passive"
    LEADERSHIP_UNKNOWN = "unknown"
    MANAGING_INST_A = "A"
    MANAGING_INST_B = "B"
    MANAGING_INST_NONE = "NONE"
    MANAGING_INST_MGMT = "mgmt"
    OPER_STATE_COMPUTE_DEGRADED = "compute-degraded"
    OPER_STATE_COMPUTE_INOPERABLE = "compute-inoperable"
    OPER_STATE_FULL_MAINTENANCE = "full-maintenance"
    OPER_STATE_IN_MAINTENANCE = "in-maintenance"
    OPER_STATE_OFFLINE = "offline"
    OPER_STATE_ONLINE = "online"
    OPER_STATE_UNDEFINED = "undefined"
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


class StorageProcessor(ManagedObject):
    """This is StorageProcessor class."""

    consts = StorageProcessorConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("StorageProcessor", "storageProcessor", "processor-[name]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['storageArray'], ['commLocale', 'osController', 'storageEthLif', 'storageProcessorRuntime'], ["Get"])

    prop_meta = {
        "admin_leadership": MoPropertyMeta("admin_leadership", "adminLeadership", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "passive", "unknown"], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["full-maintenance", "in-maintenance", "in-service"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cimc_backup_trigger_status": MoPropertyMeta("cimc_backup_trigger_status", "cimcBackupTriggerStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled", "unknown"], []), 
        "cimc_heartbeat_status": MoPropertyMeta("cimc_heartbeat_status", "cimcHeartbeatStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "running", "timed-out", "unknown"], []), 
        "cluster_state": MoPropertyMeta("cluster_state", "clusterState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "ok", "unknown"], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disruptive", "ok", "unknown"], []), 
        "conn_path": MoPropertyMeta("conn_path", "connPath", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "conn_status": MoPropertyMeta("conn_status", "connStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "deploy_action": MoPropertyMeta("deploy_action", "deployAction", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["abort-replication", "create", "delete", "modify", "no-action", "replace", "restore", "set-offline", "set-online"], []), 
        "discovery_status": MoPropertyMeta("discovery_status", "discoveryStatus", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "ha_peer_dn": MoPropertyMeta("ha_peer_dn", "haPeerDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "ha_state": MoPropertyMeta("ha_state", "haState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "election-failed", "failover-in-progress", "not-ready", "offline", "ready", "unknown"], []), 
        "ha_state_reason": MoPropertyMeta("ha_state_reason", "haStateReason", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "leadership": MoPropertyMeta("leadership", "leadership", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "passive", "unknown"], []), 
        "ls_dn": MoPropertyMeta("ls_dn", "lsDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "managing_inst": MoPropertyMeta("managing_inst", "managingInst", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_config_issues": MoPropertyMeta("oper_config_issues", "operConfigIssues", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|invalid-config|invicta-uptime-out-of-sync),){0,3}(defaultValue|not-applicable|invalid-config|invicta-uptime-out-of-sync){0,1}""", [], []), 
        "oper_qualifier_reason": MoPropertyMeta("oper_qualifier_reason", "operQualifierReason", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["compute-degraded", "compute-inoperable", "full-maintenance", "in-maintenance", "offline", "online", "undefined"], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "backplane-port-problem", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], []), 
        "orig_iqn": MoPropertyMeta("orig_iqn", "origIqn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "not-supported", "unauthorized", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminLeadership": "admin_leadership", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "cimcBackupTriggerStatus": "cimc_backup_trigger_status", 
        "cimcHeartbeatStatus": "cimc_heartbeat_status", 
        "clusterState": "cluster_state", 
        "configState": "config_state", 
        "connPath": "conn_path", 
        "connStatus": "conn_status", 
        "deployAction": "deploy_action", 
        "discoveryStatus": "discovery_status", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "haPeerDn": "ha_peer_dn", 
        "haState": "ha_state", 
        "haStateReason": "ha_state_reason", 
        "id": "id", 
        "leadership": "leadership", 
        "lsDn": "ls_dn", 
        "managingInst": "managing_inst", 
        "name": "name", 
        "operConfigIssues": "oper_config_issues", 
        "operQualifierReason": "oper_qualifier_reason", 
        "operState": "oper_state", 
        "operability": "operability", 
        "origIqn": "orig_iqn", 
        "pnDn": "pn_dn", 
        "presence": "presence", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_leadership = None
        self.admin_state = None
        self.child_action = None
        self.cimc_backup_trigger_status = None
        self.cimc_heartbeat_status = None
        self.cluster_state = None
        self.config_state = None
        self.conn_path = None
        self.conn_status = None
        self.deploy_action = None
        self.discovery_status = None
        self.flt_aggr = None
        self.ha_peer_dn = None
        self.ha_state = None
        self.ha_state_reason = None
        self.id = None
        self.leadership = None
        self.ls_dn = None
        self.managing_inst = None
        self.oper_config_issues = None
        self.oper_qualifier_reason = None
        self.oper_state = None
        self.operability = None
        self.orig_iqn = None
        self.pn_dn = None
        self.presence = None
        self.status = None

        ManagedObject.__init__(self, "StorageProcessor", parent_mo_or_dn, **kwargs)

