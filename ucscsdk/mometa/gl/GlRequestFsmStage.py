"""This module contains the general information for GlRequestFsmStage ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlRequestFsmStageConsts():
    LAST_UPDATE_TIME_ = ""
    NAME_CREATE_GLOBAL_ID_POOL_BEGIN = "CreateGlobalIdPoolBegin"
    NAME_CREATE_GLOBAL_ID_POOL_CREATE_POLICIES = "CreateGlobalIdPoolCreatePolicies"
    NAME_CREATE_GLOBAL_ID_POOL_FAIL = "CreateGlobalIdPoolFail"
    NAME_CREATE_GLOBAL_ID_POOL_SUCCESS = "CreateGlobalIdPoolSuccess"
    NAME_CREATE_GLOBAL_POLICY_BEGIN = "CreateGlobalPolicyBegin"
    NAME_CREATE_GLOBAL_POLICY_CREATE_POLICIES = "CreateGlobalPolicyCreatePolicies"
    NAME_CREATE_GLOBAL_POLICY_FAIL = "CreateGlobalPolicyFail"
    NAME_CREATE_GLOBAL_POLICY_SUCCESS = "CreateGlobalPolicySuccess"
    NAME_EVALUATE_BEGIN = "EvaluateBegin"
    NAME_EVALUATE_EVALUATE = "EvaluateEvaluate"
    NAME_EVALUATE_FAIL = "EvaluateFail"
    NAME_EVALUATE_FETCH_DOMAIN_DATA = "EvaluateFetchDomainData"
    NAME_EVALUATE_SUCCESS = "EvaluateSuccess"
    NAME_EVALUATE_VALIDATE = "EvaluateValidate"
    NAME_GLOBALIZE_ADD_ID_TO_GLOBAL_POOL = "GlobalizeAddIdToGlobalPool"
    NAME_GLOBALIZE_ASSIGN_IDS = "GlobalizeAssignIds"
    NAME_GLOBALIZE_BEGIN = "GlobalizeBegin"
    NAME_GLOBALIZE_CREATE_GSP = "GlobalizeCreateGSP"
    NAME_GLOBALIZE_CREATE_ORG = "GlobalizeCreateOrg"
    NAME_GLOBALIZE_CREATE_POLICIES = "GlobalizeCreatePolicies"
    NAME_GLOBALIZE_CREATE_UPDATE_POLICY_SCOPE = "GlobalizeCreateUpdatePolicyScope"
    NAME_GLOBALIZE_CREATE_VLAN_ORG_PERMISSION = "GlobalizeCreateVlanOrgPermission"
    NAME_GLOBALIZE_FAIL = "GlobalizeFail"
    NAME_GLOBALIZE_REAPPLY_GSP = "GlobalizeReapplyGSP"
    NAME_GLOBALIZE_RESOLVE_GLOBAL_POOL_DN = "GlobalizeResolveGlobalPoolDn"
    NAME_GLOBALIZE_SUCCESS = "GlobalizeSuccess"
    NAME_GLOBALIZE_UNASSIGN_IDS = "GlobalizeUnassignIds"
    NAME_GLOBALIZE_UPDATE_DOMAIN_MOS = "GlobalizeUpdateDomainMos"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class GlRequestFsmStage(ManagedObject):
    """This is GlRequestFsmStage class."""

    consts = GlRequestFsmStageConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("GlRequestFsmStage", "glRequestFsmStage", "stage-[name]", VersionMeta.Version201b, "OutputOnly", 0xf, [], [""], ['glRequestFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, None, None, None, None, ["CreateGlobalIdPoolBegin", "CreateGlobalIdPoolCreatePolicies", "CreateGlobalIdPoolFail", "CreateGlobalIdPoolSuccess", "CreateGlobalPolicyBegin", "CreateGlobalPolicyCreatePolicies", "CreateGlobalPolicyFail", "CreateGlobalPolicySuccess", "EvaluateBegin", "EvaluateEvaluate", "EvaluateFail", "EvaluateFetchDomainData", "EvaluateSuccess", "EvaluateValidate", "GlobalizeAddIdToGlobalPool", "GlobalizeAssignIds", "GlobalizeBegin", "GlobalizeCreateGSP", "GlobalizeCreateOrg", "GlobalizeCreatePolicies", "GlobalizeCreateUpdatePolicyScope", "GlobalizeCreateVlanOrgPermission", "GlobalizeFail", "GlobalizeReapplyGSP", "GlobalizeResolveGlobalPoolDn", "GlobalizeSuccess", "GlobalizeUnassignIds", "GlobalizeUpdateDomainMos", "nop"], []), 
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "lastUpdateTime": "last_update_time", 
        "name": "name", 
        "order": "order", 
        "retry": "retry", 
        "rn": "rn", 
        "stageStatus": "stage_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.last_update_time = None
        self.order = None
        self.retry = None
        self.stage_status = None
        self.status = None

        ManagedObject.__init__(self, "GlRequestFsmStage", parent_mo_or_dn, **kwargs)

