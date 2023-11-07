"""This module contains the general information for ConfigImpactAnalyzer ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigImpactAnalyzerConsts():
    CONTEXT_DME = "dme"
    CONTEXT_IMPORT = "import"
    MODE_RELAY = "relay"
    MODE_STRAIGHT = "straight"
    REBOOT_REQUIRED_FALSE = "false"
    REBOOT_REQUIRED_NO = "no"
    REBOOT_REQUIRED_TRUE = "true"
    REBOOT_REQUIRED_YES = "yes"
    STATE_COMPLETE = "complete"
    STATE_NOT_STARTED = "not-started"
    STATE_TIMED_OUT = "timed-out"
    STATE_WATING = "wating"


class ConfigImpactAnalyzer(ManagedObject):
    """This is ConfigImpactAnalyzer class."""

    consts = ConfigImpactAnalyzerConsts()
    naming_props = set(['impactAnalyzerId'])

    mo_meta = MoMeta("ConfigImpactAnalyzer", "configImpactAnalyzer", "impact-analyzer-[impact_analyzer_id]", VersionMeta.Version111a, "InputOutput", 0x3ff, [], ["read-only"], ['configImpactAnalyzerEp'], ['configAppImpactResponse', 'configInputConfigSet', 'configManagedEpImpactResponse'], [None])

    prop_meta = {
        "ack_app_response_count": MoPropertyMeta("ack_app_response_count", "ackAppResponseCount", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "affected_chassis_cnt": MoPropertyMeta("affected_chassis_cnt", "affectedChassisCnt", "ushort", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "chassis_profile_affected": MoPropertyMeta("chassis_profile_affected", "chassisProfileAffected", "ushort", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "completion_timestamp": MoPropertyMeta("completion_timestamp", "completionTimestamp", "ulong", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []), 
        "context": MoPropertyMeta("context", "context", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["dme", "import"], []), 
        "creation_timestamp": MoPropertyMeta("creation_timestamp", "creationTimestamp", "ulong", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "impact_analyzer_id": MoPropertyMeta("impact_analyzer_id", "impactAnalyzerId", "ulong", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["relay", "straight"], []), 
        "reboot_required": MoPropertyMeta("reboot_required", "rebootRequired", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "relay_app_response_count": MoPropertyMeta("relay_app_response_count", "relayAppResponseCount", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "servers_affected": MoPropertyMeta("servers_affected", "serversAffected", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "service_profile_affected": MoPropertyMeta("service_profile_affected", "serviceProfileAffected", "ushort", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "service_profile_lost_visibility": MoPropertyMeta("service_profile_lost_visibility", "serviceProfileLostVisibility", "ushort", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "service_profile_suspend": MoPropertyMeta("service_profile_suspend", "serviceProfileSuspend", "ushort", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "service_profile_timed_out": MoPropertyMeta("service_profile_timed_out", "serviceProfileTimedOut", "ushort", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "source_connector_id": MoPropertyMeta("source_connector_id", "sourceConnectorId", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["complete", "not-started", "timed-out", "wating"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "uc_central_config_issues": MoPropertyMeta("uc_central_config_issues", "ucCentralConfigIssues", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uc_central_errors": MoPropertyMeta("uc_central_errors", "ucCentralErrors", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uc_central_overall_issues": MoPropertyMeta("uc_central_overall_issues", "ucCentralOverallIssues", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "uc_central_warnings": MoPropertyMeta("uc_central_warnings", "ucCentralWarnings", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ucs_domains_affected": MoPropertyMeta("ucs_domains_affected", "ucsDomainsAffected", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ucs_domains_analyzed": MoPropertyMeta("ucs_domains_analyzed", "ucsDomainsAnalyzed", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ucs_domains_in_suspend": MoPropertyMeta("ucs_domains_in_suspend", "ucsDomainsInSuspend", "ushort", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ucs_domains_lost_visibility": MoPropertyMeta("ucs_domains_lost_visibility", "ucsDomainsLostVisibility", "ushort", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ucs_domains_timed_out": MoPropertyMeta("ucs_domains_timed_out", "ucsDomainsTimedOut", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "ackAppResponseCount": "ack_app_response_count", 
        "affectedChassisCnt": "affected_chassis_cnt", 
        "chassisProfileAffected": "chassis_profile_affected", 
        "childAction": "child_action", 
        "completionTimestamp": "completion_timestamp", 
        "context": "context", 
        "creationTimestamp": "creation_timestamp", 
        "dn": "dn", 
        "impactAnalyzerId": "impact_analyzer_id", 
        "mode": "mode", 
        "rebootRequired": "reboot_required", 
        "relayAppResponseCount": "relay_app_response_count", 
        "rn": "rn", 
        "serversAffected": "servers_affected", 
        "serviceProfileAffected": "service_profile_affected", 
        "serviceProfileLostVisibility": "service_profile_lost_visibility", 
        "serviceProfileSuspend": "service_profile_suspend", 
        "serviceProfileTimedOut": "service_profile_timed_out", 
        "sourceConnectorId": "source_connector_id", 
        "state": "state", 
        "status": "status", 
        "ucCentralConfigIssues": "uc_central_config_issues", 
        "ucCentralErrors": "uc_central_errors", 
        "ucCentralOverallIssues": "uc_central_overall_issues", 
        "ucCentralWarnings": "uc_central_warnings", 
        "ucsDomainsAffected": "ucs_domains_affected", 
        "ucsDomainsAnalyzed": "ucs_domains_analyzed", 
        "ucsDomainsInSuspend": "ucs_domains_in_suspend", 
        "ucsDomainsLostVisibility": "ucs_domains_lost_visibility", 
        "ucsDomainsTimedOut": "ucs_domains_timed_out", 
    }

    def __init__(self, parent_mo_or_dn, impact_analyzer_id, **kwargs):
        self._dirty_mask = 0
        self.impact_analyzer_id = impact_analyzer_id
        self.ack_app_response_count = None
        self.affected_chassis_cnt = None
        self.chassis_profile_affected = None
        self.child_action = None
        self.completion_timestamp = None
        self.context = None
        self.creation_timestamp = None
        self.mode = None
        self.reboot_required = None
        self.relay_app_response_count = None
        self.servers_affected = None
        self.service_profile_affected = None
        self.service_profile_lost_visibility = None
        self.service_profile_suspend = None
        self.service_profile_timed_out = None
        self.source_connector_id = None
        self.state = None
        self.status = None
        self.uc_central_config_issues = None
        self.uc_central_errors = None
        self.uc_central_overall_issues = None
        self.uc_central_warnings = None
        self.ucs_domains_affected = None
        self.ucs_domains_analyzed = None
        self.ucs_domains_in_suspend = None
        self.ucs_domains_lost_visibility = None
        self.ucs_domains_timed_out = None

        ManagedObject.__init__(self, "ConfigImpactAnalyzer", parent_mo_or_dn, **kwargs)

