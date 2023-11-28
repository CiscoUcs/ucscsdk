"""This module contains the general information for ConfigManagedEpImpactResponse ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigManagedEpImpactResponseConsts():
    PROFILE_TYPE_CHASSIS_PROFILE = "chassis-profile"
    PROFILE_TYPE_SERVICE_PROFILE = "service-profile"
    REBOOT_REQUIRED_FALSE = "false"
    REBOOT_REQUIRED_NO = "no"
    REBOOT_REQUIRED_TRUE = "true"
    REBOOT_REQUIRED_YES = "yes"
    STATE_COMPLETE = "complete"
    STATE_LOST_VISIBILITY = "lost-visibility"
    STATE_NOT_STARTED = "not-started"
    STATE_SUSPEND = "suspend"
    STATE_TIMED_OUT = "timed-out"
    STATE_WAITING = "waiting"


class ConfigManagedEpImpactResponse(ManagedObject):
    """This is ConfigManagedEpImpactResponse class."""

    consts = ConfigManagedEpImpactResponseConsts()
    naming_props = set(['appConnectorId', 'sourceConnectorId'])

    mo_meta = MoMeta("ConfigManagedEpImpactResponse", "configManagedEpImpactResponse", "ManagedEpapp-id-[app_connector_id]src-id-[source_connector_id]", VersionMeta.Version111a, "InputOutput", 0x1ff, [], ["read-only"], ['configImpactAnalyzer'], ['configImpact'], [None])

    prop_meta = {
        "affected_chassis_cnt": MoPropertyMeta("affected_chassis_cnt", "affectedChassisCnt", "ushort", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "affected_servers": MoPropertyMeta("affected_servers", "affectedServers", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "app_connector_id": MoPropertyMeta("app_connector_id", "appConnectorId", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x2, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "ep_name": MoPropertyMeta("ep_name", "epName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "impact_analyzer_id": MoPropertyMeta("impact_analyzer_id", "impactAnalyzerId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "profile_type": MoPropertyMeta("profile_type", "profileType", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["chassis-profile", "service-profile"], []), 
        "reboot_required": MoPropertyMeta("reboot_required", "rebootRequired", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "source_connector_id": MoPropertyMeta("source_connector_id", "sourceConnectorId", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["complete", "lost-visibility", "not-started", "suspend", "timed-out", "waiting"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "affectedChassisCnt": "affected_chassis_cnt", 
        "affectedServers": "affected_servers", 
        "appConnectorId": "app_connector_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "epName": "ep_name", 
        "impactAnalyzerId": "impact_analyzer_id", 
        "profileType": "profile_type", 
        "rebootRequired": "reboot_required", 
        "rn": "rn", 
        "sourceConnectorId": "source_connector_id", 
        "state": "state", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, app_connector_id, source_connector_id, **kwargs):
        self._dirty_mask = 0
        self.app_connector_id = app_connector_id
        self.source_connector_id = source_connector_id
        self.affected_chassis_cnt = None
        self.affected_servers = None
        self.child_action = None
        self.ep_dn = None
        self.ep_name = None
        self.impact_analyzer_id = None
        self.profile_type = None
        self.reboot_required = None
        self.state = None
        self.status = None

        ManagedObject.__init__(self, "ConfigManagedEpImpactResponse", parent_mo_or_dn, **kwargs)

