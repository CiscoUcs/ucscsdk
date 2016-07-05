"""This module contains the general information for ConfigAppImpactResponse ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class ConfigAppImpactResponseConsts():
    STATE_COMPLETE = "complete"
    STATE_LOST_VISIBILITY = "lost-visibility"
    STATE_NOT_STARTED = "not-started"
    STATE_SUSPEND = "suspend"
    STATE_TIMED_OUT = "timed-out"
    STATE_WAITING = "waiting"


class ConfigAppImpactResponse(ManagedObject):
    """This is ConfigAppImpactResponse class."""

    consts = ConfigAppImpactResponseConsts()
    naming_props = set([u'appConnectorId', u'sourceConnectorId'])

    mo_meta = MoMeta("ConfigAppImpactResponse", "configAppImpactResponse", "app-id-[app_connector_id]src-id-[source_connector_id]", VersionMeta.Version111a, "InputOutput", 0xff, [], ["read-only"], [u'configImpactAnalyzer'], [u'configUCImpact'], [None])

    prop_meta = {
        "app_connector_id": MoPropertyMeta("app_connector_id", "appConnectorId", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x2, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "impact_analyzer_id": MoPropertyMeta("impact_analyzer_id", "impactAnalyzerId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "source_connector_id": MoPropertyMeta("source_connector_id", "sourceConnectorId", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["complete", "lost-visibility", "not-started", "suspend", "timed-out", "waiting"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "appConnectorId": "app_connector_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "impactAnalyzerId": "impact_analyzer_id", 
        "rn": "rn", 
        "sourceConnectorId": "source_connector_id", 
        "state": "state", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, app_connector_id, source_connector_id, **kwargs):
        self._dirty_mask = 0
        self.app_connector_id = app_connector_id
        self.source_connector_id = source_connector_id
        self.child_action = None
        self.impact_analyzer_id = None
        self.state = None
        self.status = None

        ManagedObject.__init__(self, "ConfigAppImpactResponse", parent_mo_or_dn, **kwargs)

