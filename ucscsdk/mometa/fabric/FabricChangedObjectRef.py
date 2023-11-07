"""This module contains the general information for FabricChangedObjectRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricChangedObjectRefConsts():
    CENTRAL_RANGE_CHECK_CONFIG_STATE_DEPLOYMENT_ERROR = "deployment-error"
    CENTRAL_RANGE_CHECK_CONFIG_STATE_NOT_DEPLOYED_YET = "not-deployed-yet"
    REF_OBJ_STATUS_CREATED = "created"
    REF_OBJ_STATUS_DELETED = "deleted"
    REF_OBJ_STATUS_INTENT_DELETION = "intent-deletion"
    REF_OBJ_STATUS_MODIFIED = "modified"
    UCSM_DEPLOYMENT_CONFIG_STATE_DEPLOYMENT_ERROR = "deployment-error"
    UCSM_DEPLOYMENT_CONFIG_STATE_NOT_DEPLOYED_YET = "not-deployed-yet"


class FabricChangedObjectRef(ManagedObject):
    """This is FabricChangedObjectRef class."""

    consts = FabricChangedObjectRefConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FabricChangedObjectRef", "fabricChangedObjectRef", "ChangedObjectRef[id]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['fabricVnetEpSyncEp'], ['faultInst'], [None])

    prop_meta = {
        "central_range_check_config_state": MoPropertyMeta("central_range_check_config_state", "centralRangeCheckConfigState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deployment-error", "not-deployed-yet"], []), 
        "centrale_vnet_ep_dn": MoPropertyMeta("centrale_vnet_ep_dn", "centraleVnetEpDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_range_message": MoPropertyMeta("config_range_message", "configRangeMessage", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "old_centrale_vnet_ep_dn": MoPropertyMeta("old_centrale_vnet_ep_dn", "oldCentraleVnetEpDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "ref_obj_status": MoPropertyMeta("ref_obj_status", "refObjStatus", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["created", "deleted", "intent-deletion", "modified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "ucsm_config_message": MoPropertyMeta("ucsm_config_message", "ucsmConfigMessage", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "ucsm_deployment_config_state": MoPropertyMeta("ucsm_deployment_config_state", "ucsmDeploymentConfigState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deployment-error", "not-deployed-yet"], []), 
        "ucsm_vnet_ep_dn": MoPropertyMeta("ucsm_vnet_ep_dn", "ucsmVnetEpDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
    }

    prop_map = {
        "centralRangeCheckConfigState": "central_range_check_config_state", 
        "centraleVnetEpDn": "centrale_vnet_ep_dn", 
        "childAction": "child_action", 
        "configRangeMessage": "config_range_message", 
        "dn": "dn", 
        "id": "id", 
        "oldCentraleVnetEpDn": "old_centrale_vnet_ep_dn", 
        "refObjStatus": "ref_obj_status", 
        "rn": "rn", 
        "status": "status", 
        "ucsmConfigMessage": "ucsm_config_message", 
        "ucsmDeploymentConfigState": "ucsm_deployment_config_state", 
        "ucsmVnetEpDn": "ucsm_vnet_ep_dn", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.central_range_check_config_state = None
        self.centrale_vnet_ep_dn = None
        self.child_action = None
        self.config_range_message = None
        self.old_centrale_vnet_ep_dn = None
        self.ref_obj_status = None
        self.status = None
        self.ucsm_config_message = None
        self.ucsm_deployment_config_state = None
        self.ucsm_vnet_ep_dn = None

        ManagedObject.__init__(self, "FabricChangedObjectRef", parent_mo_or_dn, **kwargs)

