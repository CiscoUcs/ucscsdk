"""This module contains the general information for GlBlockOp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlBlockOpConsts():
    CATEGORY_VXAN = "Vxan"
    CATEGORY_DEFAULT = "default"
    CONFLICT_HAS_CONFLICT = "has-conflict"
    CONFLICT_NO_CONFLICT = "no-conflict"
    EVALUTION_STATE_EVALUATED = "evaluated"
    EVALUTION_STATE_EVALUATING = "evaluating"
    EVALUTION_STATE_NOT_EVALUATED = "not-evaluated"
    GL_ACTION_CHANGE_DEFAULT_TO_GLOBAL_DEFAULT = "change-default-to-global-default"
    GL_ACTION_NO_ACTION = "no-action"
    GL_ACTION_POLICY_CONFLICT = "policy-conflict"
    GL_OPER_ACTION_NO_CONFLICT = "no-conflict"
    GL_OPER_ACTION_POLICY_CONFLICT = "policy-conflict"
    IS_BLOCK_FALSE = "false"
    IS_BLOCK_NO = "no"
    IS_BLOCK_TRUE = "true"
    IS_BLOCK_YES = "yes"
    IS_SRC_TEMPLATE_FALSE = "false"
    IS_SRC_TEMPLATE_NO = "no"
    IS_SRC_TEMPLATE_TRUE = "true"
    IS_SRC_TEMPLATE_YES = "yes"
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
    USER_ACTION_NO_ACTION = "no-action"
    USER_ACTION_REFERENCE_GLOBAL = "reference-global"
    USER_ACTION_RENAME = "rename"


class GlBlockOp(ManagedObject):
    """This is GlBlockOp class."""

    consts = GlBlockOpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("GlBlockOp", "glBlockOp", "block-[id]", VersionMeta.Version201b, "InputOutput", 0x1ff, [], ["read-only"], ['glBlockEp'], ['glConflictEp', 'glRequestorEp', 'messageEp'], [None])

    prop_meta = {
        "category": MoPropertyMeta("category", "category", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Vxan", "default"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "conflict": MoPropertyMeta("conflict", "conflict", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["has-conflict", "no-conflict"], []), 
        "create_from_dn": MoPropertyMeta("create_from_dn", "createFromDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "evalution_state": MoPropertyMeta("evalution_state", "evalutionState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["evaluated", "evaluating", "not-evaluated"], []), 
        "gl_action": MoPropertyMeta("gl_action", "glAction", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["change-default-to-global-default", "no-action", "policy-conflict"], []), 
        "gl_attr_value": MoPropertyMeta("gl_attr_value", "glAttrValue", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []), 
        "gl_oper_action": MoPropertyMeta("gl_oper_action", "glOperAction", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no-conflict", "policy-conflict"], []), 
        "gl_oper_attr_value": MoPropertyMeta("gl_oper_attr_value", "glOperAttrValue", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "is_block": MoPropertyMeta("is_block", "isBlock", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_src_template": MoPropertyMeta("is_src_template", "isSrcTemplate", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_user_actionable": MoPropertyMeta("is_user_actionable", "isUserActionable", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "need_globalization": MoPropertyMeta("need_globalization", "needGlobalization", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "src_mo_class_name": MoPropertyMeta("src_mo_class_name", "srcMoClassName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "src_mo_dn": MoPropertyMeta("src_mo_dn", "srcMoDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "src_mo_rn": MoPropertyMeta("src_mo_rn", "srcMoRn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "src_template_dn": MoPropertyMeta("src_template_dn", "srcTemplateDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "user_action": MoPropertyMeta("user_action", "userAction", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["no-action", "reference-global", "rename"], []), 
        "user_input_name": MoPropertyMeta("user_input_name", "userInputName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "user_name_oper_attr": MoPropertyMeta("user_name_oper_attr", "userNameOperAttr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], []), 
    }

    prop_map = {
        "category": "category", 
        "childAction": "child_action", 
        "conflict": "conflict", 
        "createFromDn": "create_from_dn", 
        "dn": "dn", 
        "evalutionState": "evalution_state", 
        "glAction": "gl_action", 
        "glAttrValue": "gl_attr_value", 
        "glOperAction": "gl_oper_action", 
        "glOperAttrValue": "gl_oper_attr_value", 
        "id": "id", 
        "isBlock": "is_block", 
        "isSrcTemplate": "is_src_template", 
        "isUserActionable": "is_user_actionable", 
        "needGlobalization": "need_globalization", 
        "owner": "owner", 
        "rn": "rn", 
        "srcMoClassName": "src_mo_class_name", 
        "srcMoDn": "src_mo_dn", 
        "srcMoRn": "src_mo_rn", 
        "srcTemplateDn": "src_template_dn", 
        "status": "status", 
        "userAction": "user_action", 
        "userInputName": "user_input_name", 
        "userNameOperAttr": "user_name_oper_attr", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.category = None
        self.child_action = None
        self.conflict = None
        self.create_from_dn = None
        self.evalution_state = None
        self.gl_action = None
        self.gl_attr_value = None
        self.gl_oper_action = None
        self.gl_oper_attr_value = None
        self.is_block = None
        self.is_src_template = None
        self.is_user_actionable = None
        self.need_globalization = None
        self.owner = None
        self.src_mo_class_name = None
        self.src_mo_dn = None
        self.src_mo_rn = None
        self.src_template_dn = None
        self.status = None
        self.user_action = None
        self.user_input_name = None
        self.user_name_oper_attr = None

        ManagedObject.__init__(self, "GlBlockOp", parent_mo_or_dn, **kwargs)

