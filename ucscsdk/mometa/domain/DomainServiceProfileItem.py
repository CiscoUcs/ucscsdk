"""This module contains the general information for DomainServiceProfileItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class DomainServiceProfileItemConsts():
    ASSOC_STATE_ASSOCIATED = "associated"
    ASSOC_STATE_ASSOCIATING = "associating"
    ASSOC_STATE_DISASSOCIATING = "disassociating"
    ASSOC_STATE_FAILED = "failed"
    ASSOC_STATE_UNASSOCIATED = "unassociated"
    DOMAIN_STATE_LOST_VISIBILITY = "lost-visibility"
    DOMAIN_STATE_REGISTERED = "registered"
    DOMAIN_STATE_REGISTERING = "registering"
    DOMAIN_STATE_SYNCHRONIZING = "synchronizing"
    DOMAIN_STATE_UNREGISTERED = "unregistered"
    DOMAIN_STATE_VERSION_MISMATCH = "version-mismatch"
    FAULT_LEVEL_CLEARED = "cleared"
    FAULT_LEVEL_CONDITION = "condition"
    FAULT_LEVEL_CRITICAL = "critical"
    FAULT_LEVEL_INFO = "info"
    FAULT_LEVEL_MAJOR = "major"
    FAULT_LEVEL_MINOR = "minor"
    FAULT_LEVEL_WARNING = "warning"
    OPER_STATE_BIOS_RESTORE = "bios-restore"
    OPER_STATE_CMOS_RESET = "cmos-reset"
    OPER_STATE_COMPUTE_FAILED = "compute-failed"
    OPER_STATE_COMPUTE_MISMATCH = "compute-mismatch"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_CONFIG_FAILURE = "config-failure"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_DIAGNOSTICS = "diagnostics"
    OPER_STATE_DIAGNOSTICS_FAILED = "diagnostics-failed"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_DISCOVERY = "discovery"
    OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    OPER_STATE_INACCESSIBLE = "inaccessible"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_INOPERABLE = "inoperable"
    OPER_STATE_MAINTENANCE = "maintenance"
    OPER_STATE_MAINTENANCE_FAILED = "maintenance-failed"
    OPER_STATE_OK = "ok"
    OPER_STATE_PENDING_REASSOCIATION = "pending-reassociation"
    OPER_STATE_PENDING_REBOOT = "pending-reboot"
    OPER_STATE_POWER_OFF = "power-off"
    OPER_STATE_POWER_PROBLEM = "power-problem"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_RESTART = "restart"
    OPER_STATE_TEST = "test"
    OPER_STATE_TEST_FAILED = "test-failed"
    OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    OPER_STATE_UNASSOCIATED = "unassociated"
    OPER_STATE_UNCONFIG = "unconfig"
    OPER_STATE_UNCONFIG_FAILED = "unconfig-failed"
    OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    SERVICE_PROFILE_OWNER_ALL = "all"
    SERVICE_PROFILE_OWNER_GLOBAL = "global"
    SERVICE_PROFILE_OWNER_LOCAL = "local"
    TEMPLATE_TYPE_INITIAL_TEMPLATE = "initial-template"
    TEMPLATE_TYPE_INSTANCE = "instance"
    TEMPLATE_TYPE_UPDATING_TEMPLATE = "updating-template"
    TYPE_INITIAL_TEMPLATE = "initial-template"
    TYPE_INSTANCE = "instance"
    TYPE_UPDATING_TEMPLATE = "updating-template"


class DomainServiceProfileItem(ManagedObject):
    """This is DomainServiceProfileItem class."""

    consts = DomainServiceProfileItemConsts()
    naming_props = set(['serviceProfileDn'])

    mo_meta = MoMeta("DomainServiceProfileItem", "domainServiceProfileItem", "SP[service_profile_dn]", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-server", "pn-equipment", "pn-maintenance", "pn-policy"], [], [], ["Get"])

    prop_meta = {
        "assoc_state": MoPropertyMeta("assoc_state", "assocState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["associated", "associating", "disassociating", "failed", "unassociated"], []), 
        "blade_dn": MoPropertyMeta("blade_dn", "bladeDn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_error_count": MoPropertyMeta("config_error_count", "configErrorCount", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_group": MoPropertyMeta("domain_group", "domainGroup", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "domain_id": MoPropertyMeta("domain_id", "domainId", "uint", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "domain_state": MoPropertyMeta("domain_state", "domainState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "num_running_instances": MoPropertyMeta("num_running_instances", "numRunningInstances", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oper_src_templ_name": MoPropertyMeta("oper_src_templ_name", "operSrcTemplName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bios-restore", "cmos-reset", "compute-failed", "compute-mismatch", "config", "config-failure", "decomissioning", "degraded", "diagnostics", "diagnostics-failed", "disabled", "discovery", "discovery-failed", "inaccessible", "indeterminate", "inoperable", "maintenance", "maintenance-failed", "ok", "pending-reassociation", "pending-reboot", "power-off", "power-problem", "removed", "restart", "test", "test-failed", "thermal-problem", "unassociated", "unconfig", "unconfig-failed", "voltage-problem"], []), 
        "org_dn": MoPropertyMeta("org_dn", "orgDn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "org_name": MoPropertyMeta("org_name", "orgName", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "server_dn": MoPropertyMeta("server_dn", "serverDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "server_id": MoPropertyMeta("server_id", "serverId", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "service_profile_dn": MoPropertyMeta("service_profile_dn", "serviceProfileDn", "string", VersionMeta.Version121a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "service_profile_name": MoPropertyMeta("service_profile_name", "serviceProfileName", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "service_profile_owner": MoPropertyMeta("service_profile_owner", "serviceProfileOwner", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "global", "local"], []), 
        "src_templ_name": MoPropertyMeta("src_templ_name", "srcTemplName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "template_type": MoPropertyMeta("template_type", "templateType", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["initial-template", "instance", "updating-template"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["initial-template", "instance", "updating-template"], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
    }

    prop_map = {
        "assocState": "assoc_state", 
        "bladeDn": "blade_dn", 
        "childAction": "child_action", 
        "configErrorCount": "config_error_count", 
        "dn": "dn", 
        "domainGroup": "domain_group", 
        "domainGroupDn": "domain_group_dn", 
        "domainId": "domain_id", 
        "domainName": "domain_name", 
        "domainState": "domain_state", 
        "faultLevel": "fault_level", 
        "numRunningInstances": "num_running_instances", 
        "operSrcTemplName": "oper_src_templ_name", 
        "operState": "oper_state", 
        "orgDn": "org_dn", 
        "orgName": "org_name", 
        "rn": "rn", 
        "serverDn": "server_dn", 
        "serverId": "server_id", 
        "serviceProfileDn": "service_profile_dn", 
        "serviceProfileName": "service_profile_name", 
        "serviceProfileOwner": "service_profile_owner", 
        "srcTemplName": "src_templ_name", 
        "status": "status", 
        "templateType": "template_type", 
        "type": "type", 
        "usrLbl": "usr_lbl", 
    }

    def __init__(self, parent_mo_or_dn, service_profile_dn, **kwargs):
        self._dirty_mask = 0
        self.service_profile_dn = service_profile_dn
        self.assoc_state = None
        self.blade_dn = None
        self.child_action = None
        self.config_error_count = None
        self.domain_group = None
        self.domain_group_dn = None
        self.domain_id = None
        self.domain_name = None
        self.domain_state = None
        self.fault_level = None
        self.num_running_instances = None
        self.oper_src_templ_name = None
        self.oper_state = None
        self.org_dn = None
        self.org_name = None
        self.server_dn = None
        self.server_id = None
        self.service_profile_name = None
        self.service_profile_owner = None
        self.src_templ_name = None
        self.status = None
        self.template_type = None
        self.type = None
        self.usr_lbl = None

        ManagedObject.__init__(self, "DomainServiceProfileItem", parent_mo_or_dn, **kwargs)

