"""This module contains the general information for GlIdentCtxOp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlIdentCtxOpConsts():
    CONFLICT_HAS_CONFLICT = "has-conflict"
    CONFLICT_NO_CONFLICT = "no-conflict"
    CONS_TYPE_CHASSIS = "chassis"
    CONS_TYPE_SERVER = "server"
    CONS_TYPE_VHBA = "vhba"
    CONS_TYPE_VM = "vm"
    CONS_TYPE_VMNIC = "vmnic"
    CONS_TYPE_VNIC = "vnic"
    DEFINED_IN_IDM_NO = "no"
    DEFINED_IN_IDM_YES = "yes"
    EVALUTION_STATE_EVALUATED = "evaluated"
    EVALUTION_STATE_EVALUATING = "evaluating"
    EVALUTION_STATE_NOT_EVALUATED = "not-evaluated"
    GL_ACTION_CHANGE_DEFAULT_TO_GLOBAL_DEFAULT = "change-default-to-global-default"
    GL_ACTION_NO_ACTION = "no-action"
    GL_ACTION_POLICY_CONFLICT = "policy-conflict"
    GL_OPER_ACTION_NO_CONFLICT = "no-conflict"
    GL_OPER_ACTION_POLICY_CONFLICT = "policy-conflict"
    IDENT_TYPE_IP_V4 = "ipV4"
    IDENT_TYPE_IP_V6 = "ipV6"
    IDENT_TYPE_IQN = "iqn"
    IDENT_TYPE_MAC = "mac"
    IDENT_TYPE_UUID = "uuid"
    IDENT_TYPE_VLAN = "vlan"
    IDENT_TYPE_WWNN = "wwnn"
    IDENT_TYPE_WWPN = "wwpn"
    INTENT_ADD_POOLED = "add-pooled"
    INTENT_ASSIGN = "assign"
    INTENT_CHECK_DUPLICATE_ID = "check-duplicate-id"
    INTENT_DELETE_POOLED = "delete-pooled"
    INTENT_RE_EVALUATE = "re-evaluate"
    INTENT_REQUISITION = "requisition"
    INTENT_SYNC = "sync"
    INTENT_UNASSIGN = "unassign"
    INTENT_UNASSIGN_ON_BEHALF_OF_UCSM = "unassign-on-behalf-of-ucsm"
    INTENT_VALIDATE = "validate"
    IS_BLOCK_FALSE = "false"
    IS_BLOCK_NO = "no"
    IS_BLOCK_TRUE = "true"
    IS_BLOCK_YES = "yes"
    IS_REFERENCE_GLOBAL_POOL_FALSE = "false"
    IS_REFERENCE_GLOBAL_POOL_NO = "no"
    IS_REFERENCE_GLOBAL_POOL_TRUE = "true"
    IS_REFERENCE_GLOBAL_POOL_YES = "yes"
    IS_SRC_TEMPLATE_FALSE = "false"
    IS_SRC_TEMPLATE_NO = "no"
    IS_SRC_TEMPLATE_TRUE = "true"
    IS_SRC_TEMPLATE_YES = "yes"
    IS_STATIC_ID_FALSE = "false"
    IS_STATIC_ID_NO = "no"
    IS_STATIC_ID_TRUE = "true"
    IS_STATIC_ID_YES = "yes"
    IS_USER_ACTIONABLE_FALSE = "false"
    IS_USER_ACTIONABLE_NO = "no"
    IS_USER_ACTIONABLE_TRUE = "true"
    IS_USER_ACTIONABLE_YES = "yes"
    NEED_GLOBALIZATION_FALSE = "false"
    NEED_GLOBALIZATION_NO = "no"
    NEED_GLOBALIZATION_TRUE = "true"
    NEED_GLOBALIZATION_YES = "yes"
    OWNER_LOCAL = "local"
    OWNER_PENDING_POLICY = "pending-policy"
    OWNER_POLICY = "policy"
    OWNER_UNSPECIFIED = "unspecified"
    SKIP_VALIDATION_FALSE = "false"
    SKIP_VALIDATION_NO = "no"
    SKIP_VALIDATION_TRUE = "true"
    SKIP_VALIDATION_YES = "yes"
    USER_ACTION_NO_ACTION = "no-action"
    USER_ACTION_REFERENCE_GLOBAL = "reference-global"
    USER_ACTION_RENAME = "rename"


class GlIdentCtxOp(ManagedObject):
    """This is GlIdentCtxOp class."""

    consts = GlIdentCtxOpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("GlIdentCtxOp", "glIdentCtxOp", "icop-[id]", VersionMeta.Version201b, "InputOutput", 0x3ff, [], ["read-only"], ['glIdentCtxEp'], ['glConflictEp', 'glRequestorEp', 'messageEp'], [None])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "attr_name": MoPropertyMeta("attr_name", "attrName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "attr_value": MoPropertyMeta("attr_value", "attrValue", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "conflict": MoPropertyMeta("conflict", "conflict", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["has-conflict", "no-conflict"], []), 
        "cons_dn": MoPropertyMeta("cons_dn", "consDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "cons_type": MoPropertyMeta("cons_type", "consType", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis", "server", "vhba", "vm", "vmnic", "vnic"], []), 
        "defined_in_idm": MoPropertyMeta("defined_in_idm", "definedInIdm", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "evalution_state": MoPropertyMeta("evalution_state", "evalutionState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["evaluated", "evaluating", "not-evaluated"], []), 
        "gl_action": MoPropertyMeta("gl_action", "glAction", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["change-default-to-global-default", "no-action", "policy-conflict"], []), 
        "gl_attr_value": MoPropertyMeta("gl_attr_value", "glAttrValue", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []), 
        "gl_oper_action": MoPropertyMeta("gl_oper_action", "glOperAction", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no-conflict", "policy-conflict"], []), 
        "gl_oper_attr_value": MoPropertyMeta("gl_oper_attr_value", "glOperAttrValue", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "global_pool_dn": MoPropertyMeta("global_pool_dn", "globalPoolDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "ident_type": MoPropertyMeta("ident_type", "identType", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipV4", "ipV6", "iqn", "mac", "uuid", "vlan", "wwnn", "wwpn"], []), 
        "intent": MoPropertyMeta("intent", "intent", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["add-pooled", "assign", "check-duplicate-id", "delete-pooled", "re-evaluate", "requisition", "sync", "unassign", "unassign-on-behalf-of-ucsm", "validate"], []), 
        "is_block": MoPropertyMeta("is_block", "isBlock", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_reference_global_pool": MoPropertyMeta("is_reference_global_pool", "isReferenceGlobalPool", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_src_template": MoPropertyMeta("is_src_template", "isSrcTemplate", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_static_id": MoPropertyMeta("is_static_id", "isStaticId", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_user_actionable": MoPropertyMeta("is_user_actionable", "isUserActionable", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "max_derivable_wwpn": MoPropertyMeta("max_derivable_wwpn", "maxDerivableWWPN", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "need_globalization": MoPropertyMeta("need_globalization", "needGlobalization", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "oper_attr_name": MoPropertyMeta("oper_attr_name", "operAttrName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_attr_value": MoPropertyMeta("oper_attr_value", "operAttrValue", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "pool_dn": MoPropertyMeta("pool_dn", "poolDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "pooled_id": MoPropertyMeta("pooled_id", "pooledId", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version201b, MoPropertyMeta.CREATE_ONLY, 0x10, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "skip_validation": MoPropertyMeta("skip_validation", "skipValidation", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "src_mo_class_name": MoPropertyMeta("src_mo_class_name", "srcMoClassName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "src_mo_dn": MoPropertyMeta("src_mo_dn", "srcMoDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "src_mo_rn": MoPropertyMeta("src_mo_rn", "srcMoRn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "src_template_dn": MoPropertyMeta("src_template_dn", "srcTemplateDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suppl_id1": MoPropertyMeta("suppl_id1", "supplId1", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "suppl_id2": MoPropertyMeta("suppl_id2", "supplId2", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "suppl_id3": MoPropertyMeta("suppl_id3", "supplId3", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "suppl_id4": MoPropertyMeta("suppl_id4", "supplId4", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "ucsc_src_mo_dn": MoPropertyMeta("ucsc_src_mo_dn", "ucscSrcMoDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "user_action": MoPropertyMeta("user_action", "userAction", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["no-action", "reference-global", "rename"], []), 
        "user_input_name": MoPropertyMeta("user_input_name", "userInputName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "user_name_oper_attr": MoPropertyMeta("user_name_oper_attr", "userNameOperAttr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], []), 
    }

    prop_map = {
        "assigned": "assigned", 
        "attrName": "attr_name", 
        "attrValue": "attr_value", 
        "childAction": "child_action", 
        "conflict": "conflict", 
        "consDn": "cons_dn", 
        "consType": "cons_type", 
        "definedInIdm": "defined_in_idm", 
        "dn": "dn", 
        "evalutionState": "evalution_state", 
        "glAction": "gl_action", 
        "glAttrValue": "gl_attr_value", 
        "glOperAction": "gl_oper_action", 
        "glOperAttrValue": "gl_oper_attr_value", 
        "globalPoolDn": "global_pool_dn", 
        "id": "id", 
        "identPoolName": "ident_pool_name", 
        "identType": "ident_type", 
        "intent": "intent", 
        "isBlock": "is_block", 
        "isReferenceGlobalPool": "is_reference_global_pool", 
        "isSrcTemplate": "is_src_template", 
        "isStaticId": "is_static_id", 
        "isUserActionable": "is_user_actionable", 
        "maxDerivableWWPN": "max_derivable_wwpn", 
        "needGlobalization": "need_globalization", 
        "operAttrName": "oper_attr_name", 
        "operAttrValue": "oper_attr_value", 
        "owner": "owner", 
        "poolDn": "pool_dn", 
        "pooledId": "pooled_id", 
        "purpose": "purpose", 
        "rn": "rn", 
        "skipValidation": "skip_validation", 
        "srcMoClassName": "src_mo_class_name", 
        "srcMoDn": "src_mo_dn", 
        "srcMoRn": "src_mo_rn", 
        "srcTemplateDn": "src_template_dn", 
        "status": "status", 
        "supplId1": "suppl_id1", 
        "supplId2": "suppl_id2", 
        "supplId3": "suppl_id3", 
        "supplId4": "suppl_id4", 
        "ucscSrcMoDn": "ucsc_src_mo_dn", 
        "userAction": "user_action", 
        "userInputName": "user_input_name", 
        "userNameOperAttr": "user_name_oper_attr", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.assigned = None
        self.attr_name = None
        self.attr_value = None
        self.child_action = None
        self.conflict = None
        self.cons_dn = None
        self.cons_type = None
        self.defined_in_idm = None
        self.evalution_state = None
        self.gl_action = None
        self.gl_attr_value = None
        self.gl_oper_action = None
        self.gl_oper_attr_value = None
        self.global_pool_dn = None
        self.ident_pool_name = None
        self.ident_type = None
        self.intent = None
        self.is_block = None
        self.is_reference_global_pool = None
        self.is_src_template = None
        self.is_static_id = None
        self.is_user_actionable = None
        self.max_derivable_wwpn = None
        self.need_globalization = None
        self.oper_attr_name = None
        self.oper_attr_value = None
        self.owner = None
        self.pool_dn = None
        self.pooled_id = None
        self.purpose = None
        self.skip_validation = None
        self.src_mo_class_name = None
        self.src_mo_dn = None
        self.src_mo_rn = None
        self.src_template_dn = None
        self.status = None
        self.suppl_id1 = None
        self.suppl_id2 = None
        self.suppl_id3 = None
        self.suppl_id4 = None
        self.ucsc_src_mo_dn = None
        self.user_action = None
        self.user_input_name = None
        self.user_name_oper_attr = None

        ManagedObject.__init__(self, "GlIdentCtxOp", parent_mo_or_dn, **kwargs)

