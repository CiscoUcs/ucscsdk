"""This module contains the general information for GlIdentCtxResOp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlIdentCtxResOpConsts():
    ADMIN_STATE_DEFAULT = "default"
    ADMIN_STATE_EVALUATE = "evaluate"
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
    FSM_PREV_VALIDATE_ID_BEGIN = "ValidateIdBegin"
    FSM_PREV_VALIDATE_ID_FAIL = "ValidateIdFail"
    FSM_PREV_VALIDATE_ID_SUCCESS = "ValidateIdSuccess"
    FSM_PREV_VALIDATE_ID_VALIDATE = "ValidateIdValidate"
    FSM_PREV_NOP = "nop"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_CANCELLED = "ERR-DIAG-cancelled"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_FSM_RESTARTED = "ERR-DIAG-fsm-restarted"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_TEST_FAILED = "ERR-DIAG-test-failed"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_AUTHENTICATION_FAILURE = "ERR-DNLD-authentication-failure"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_ERROR = "ERR-DNLD-error"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_HOSTKEY_MISMATCH = "ERR-DNLD-hostkey-mismatch"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_INVALID_IMAGE = "ERR-DNLD-invalid-image"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_NO_FILE = "ERR-DNLD-no-file"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_NO_SPACE = "ERR-DNLD-no-space"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_DELETE_ERROR = "ERR-DNS-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_GET_ERROR = "ERR-DNS-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_SET_ERROR = "ERR-DNS-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_DIGEST_VALIDATION_ERROR = "ERR-Digest-Validation-error"
    FSM_RMT_INV_ERR_CODE_ERR_EXEC_GEN_CERT_ERROR = "ERR-Exec-Gen-Cert-error"
    FSM_RMT_INV_ERR_CODE_ERR_EXEC_GET_CA_CERT_ERROR = "ERR-Exec-Get-CA-Cert-error"
    FSM_RMT_INV_ERR_CODE_ERR_FILTER_ILLEGAL_FORMAT = "ERR-FILTER-illegal-format"
    FSM_RMT_INV_ERR_CODE_ERR_FSM_NO_SUCH_STATE = "ERR-FSM-no-such-state"
    FSM_RMT_INV_ERR_CODE_ERR_GET_CA_CERT_ERROR = "ERR-Get-CA-Cert-error"
    FSM_RMT_INV_ERR_CODE_ERR_GET_CERT_ERROR = "ERR-Get-Cert-error"
    FSM_RMT_INV_ERR_CODE_ERR_GET_OUT_DIGET_MESSAGE_ERROR = "ERR-Get-Out-Diget-Message-error"
    FSM_RMT_INV_ERR_CODE_ERR_HTTP_REQUEST_ERROR = "ERR-HTTP-Request-error"
    FSM_RMT_INV_ERR_CODE_ERR_HTTP_SET_ERROR = "ERR-HTTP-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_HTTPS_SET_ERROR = "ERR-HTTPS-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_IPV6_ADDR_CONFIGURED = "ERR-Ipv6-addr-configured"
    FSM_RMT_INV_ERR_CODE_ERR_MO_CONFIG_CHILD_OBJECT_CANT_BE_CONFIGURED = "ERR-MO-CONFIG-child-object-cant-be-configured"
    FSM_RMT_INV_ERR_CODE_ERR_MO_META_NO_SUCH_OBJECT_CLASS = "ERR-MO-META-no-such-object-class"
    FSM_RMT_INV_ERR_CODE_ERR_MO_PROPERTY_NO_SUCH_PROPERTY = "ERR-MO-PROPERTY-no-such-property"
    FSM_RMT_INV_ERR_CODE_ERR_MO_PROPERTY_VALUE_OUT_OF_RANGE = "ERR-MO-PROPERTY-value-out-of-range"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ACCESS_DENIED = "ERR-MO-access-denied"
    FSM_RMT_INV_ERR_CODE_ERR_MO_DELETION_RULE_VIOLATION = "ERR-MO-deletion-rule-violation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_DUPLICATE_OBJECT = "ERR-MO-duplicate-object"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_CONTAINMENT = "ERR-MO-illegal-containment"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_CREATION = "ERR-MO-illegal-creation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_ITERATOR_STATE = "ERR-MO-illegal-iterator-state"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_OBJECT_LIFECYCLE_TRANSITION = "ERR-MO-illegal-object-lifecycle-transition"
    FSM_RMT_INV_ERR_CODE_ERR_MO_NAMING_RULE_VIOLATION = "ERR-MO-naming-rule-violation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_OBJECT_NOT_FOUND = "ERR-MO-object-not-found"
    FSM_RMT_INV_ERR_CODE_ERR_MO_RESOURCE_ALLOCATION = "ERR-MO-resource-allocation"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_DELETE_ERROR = "ERR-NTP-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_GET_ERROR = "ERR-NTP-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_SET_ERROR = "ERR-NTP-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_POLICY_RESOLUTION_IN_PROGRESS = "ERR-Policy-resolution-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_TOKEN_REQUEST_DENIED = "ERR-TOKEN-request-denied"
    FSM_RMT_INV_ERR_CODE_ERR_UPDATE_VM_IP_MASK_GATEWAY_ERROR = "ERR-Update-VM-IP-Mask-Gateway-error"
    FSM_RMT_INV_ERR_CODE_ERR_AAA_CONFIG_MODIFY_ERROR = "ERR-aaa-config-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_ACCT_REALM_SET_ERROR = "ERR-acct-realm-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_ADMIN_PASSWD_SET = "ERR-admin-passwd-set"
    FSM_RMT_INV_ERR_CODE_ERR_AUTH_REALM_SET_ERROR = "ERR-auth-realm-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_AUTHENTICATION = "ERR-authentication"
    FSM_RMT_INV_ERR_CODE_ERR_AUTHORIZATION_REQUIRED = "ERR-authorization-required"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_CHASSISPACK_UNDER_DG = "ERR-create-chassispack-under-dg"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_HFP_UNDER_DG = "ERR-create-hfp-under-dg"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_KEYRING = "ERR-create-keyring"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_LOCALE = "ERR-create-locale"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_ROLE = "ERR-create-role"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_USER = "ERR-create-user"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_LOCALE = "ERR-delete-locale"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_ROLE = "ERR-delete-role"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_SESSION = "ERR-delete-session"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_USER = "ERR-delete-user"
    FSM_RMT_INV_ERR_CODE_ERR_ESTIMATE_IMPACT_ON_RECONNECT = "ERR-estimate-impact-on-reconnect"
    FSM_RMT_INV_ERR_CODE_ERR_GET_MAX_HTTP_USER_SESSIONS = "ERR-get-max-http-user-sessions"
    FSM_RMT_INV_ERR_CODE_ERR_HTTP_INITIALIZING = "ERR-http-initializing"
    FSM_RMT_INV_ERR_CODE_ERR_INTERNAL_ERROR = "ERR-internal-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_DELETE_ERROR = "ERR-ldap-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GET_ERROR = "ERR-ldap-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GROUP_MODIFY_ERROR = "ERR-ldap-group-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GROUP_SET_ERROR = "ERR-ldap-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_SET_ERROR = "ERR-ldap-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_LOCALE_SET_ERROR = "ERR-locale-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_MAX_USERID_SESSIONS_REACHED = "ERR-max-userid-sessions-reached"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_LOCALE = "ERR-modify-locale"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_ROLE = "ERR-modify-role"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER = "ERR-modify-user"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER_LOCALE = "ERR-modify-user-locale"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER_ROLE = "ERR-modify-user-role"
    FSM_RMT_INV_ERR_CODE_ERR_NFS_DOWN = "ERR-nfs-down"
    FSM_RMT_INV_ERR_CODE_ERR_PROVIDER_GROUP_MODIFY_ERROR = "ERR-provider-group-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_PROVIDER_GROUP_SET_ERROR = "ERR-provider-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_GLOBAL_SET_ERROR = "ERR-radius-global-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_GROUP_SET_ERROR = "ERR-radius-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_SET_ERROR = "ERR-radius-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_ROLE_SET_ERROR = "ERR-role-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_SERVICE_NOT_READY = "ERR-service-not-ready"
    FSM_RMT_INV_ERR_CODE_ERR_SESSION_CACHE_FULL = "ERR-session-cache-full"
    FSM_RMT_INV_ERR_CODE_ERR_SESSION_NOT_FOUND = "ERR-session-not-found"
    FSM_RMT_INV_ERR_CODE_ERR_SET_PASSWORD_STRENGTH_CHECK = "ERR-set-password-strength-check"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_ENABLE_ERROR = "ERR-tacacs-enable-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_GLOBAL_SET_ERROR = "ERR-tacacs-global-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_GROUP_SET_ERROR = "ERR-tacacs-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_SET_ERROR = "ERR-tacacs-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TIMEZONE_SET_ERROR = "ERR-timezone-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_USER_ACCOUNT_EXPIRED = "ERR-user-account-expired"
    FSM_RMT_INV_ERR_CODE_ERR_USER_SET_ERROR = "ERR-user-set-error"
    FSM_RMT_INV_ERR_CODE_NONE = "none"
    FSM_STAMP_NEVER = "never"
    FSM_STATUS_VALIDATE_ID_BEGIN = "ValidateIdBegin"
    FSM_STATUS_VALIDATE_ID_FAIL = "ValidateIdFail"
    FSM_STATUS_VALIDATE_ID_SUCCESS = "ValidateIdSuccess"
    FSM_STATUS_VALIDATE_ID_VALIDATE = "ValidateIdValidate"
    FSM_STATUS_NOP = "nop"
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
    USER_ACTION_NO_ACTION = "no-action"
    USER_ACTION_REFERENCE_GLOBAL = "reference-global"
    USER_ACTION_RENAME = "rename"


class GlIdentCtxResOp(ManagedObject):
    """This is GlIdentCtxResOp class."""

    consts = GlIdentCtxResOpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("GlIdentCtxResOp", "glIdentCtxResOp", "icrop-[id]", VersionMeta.Version201b, "InputOutput", 0x7ff, [], ["admin"], ['glIdentCtxEp'], ['eventInst', 'faultInst', 'glConflictEp', 'glIdentCtxResOpFsm', 'glIdentCtxResOpFsmTask', 'glRefsEp', 'glRequestorEp', 'messageEp'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["default", "evaluate"], []), 
        "assigned": MoPropertyMeta("assigned", "assigned", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "attr_name": MoPropertyMeta("attr_name", "attrName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "attr_value": MoPropertyMeta("attr_value", "attrValue", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "conflict": MoPropertyMeta("conflict", "conflict", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["has-conflict", "no-conflict"], []), 
        "cons_dn": MoPropertyMeta("cons_dn", "consDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "cons_type": MoPropertyMeta("cons_type", "consType", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis", "server", "vhba", "vm", "vmnic", "vnic"], []), 
        "defined_in_idm": MoPropertyMeta("defined_in_idm", "definedInIdm", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "evalution_state": MoPropertyMeta("evalution_state", "evalutionState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["evaluated", "evaluating", "not-evaluated"], []), 
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, ["ValidateIdBegin", "ValidateIdFail", "ValidateIdSuccess", "ValidateIdValidate", "nop"], []), 
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]), 
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-error", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Digest-Validation-error", "ERR-Exec-Gen-Cert-error", "ERR-Exec-Get-CA-Cert-error", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-Get-CA-Cert-error", "ERR-Get-Cert-error", "ERR-Get-Out-Diget-Message-error", "ERR-HTTP-Request-error", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-Ipv6-addr-configured", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-Policy-resolution-in-progress", "ERR-TOKEN-request-denied", "ERR-Update-VM-IP-Mask-Gateway-error", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-create-chassispack-under-dg", "ERR-create-hfp-under-dg", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-estimate-impact-on-reconnect", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-nfs-down", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-role-set-error", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-password-strength-check", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-set-error", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "none"], ["0-4294967295"]), 
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []), 
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, ["ValidateIdBegin", "ValidateIdFail", "ValidateIdSuccess", "ValidateIdValidate", "nop"], []), 
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "gl_action": MoPropertyMeta("gl_action", "glAction", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["change-default-to-global-default", "no-action", "policy-conflict"], []), 
        "gl_attr_value": MoPropertyMeta("gl_attr_value", "glAttrValue", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []), 
        "gl_oper_action": MoPropertyMeta("gl_oper_action", "glOperAction", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no-conflict", "policy-conflict"], []), 
        "gl_oper_attr_value": MoPropertyMeta("gl_oper_attr_value", "glOperAttrValue", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []), 
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "ident_type": MoPropertyMeta("ident_type", "identType", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipV4", "ipV6", "iqn", "mac", "uuid", "vlan", "wwnn", "wwpn"], []), 
        "intent": MoPropertyMeta("intent", "intent", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["add-pooled", "assign", "check-duplicate-id", "delete-pooled", "re-evaluate", "requisition", "sync", "unassign", "unassign-on-behalf-of-ucsm", "validate"], []), 
        "is_block": MoPropertyMeta("is_block", "isBlock", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_reference_global_pool": MoPropertyMeta("is_reference_global_pool", "isReferenceGlobalPool", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_src_template": MoPropertyMeta("is_src_template", "isSrcTemplate", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_static_id": MoPropertyMeta("is_static_id", "isStaticId", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_user_actionable": MoPropertyMeta("is_user_actionable", "isUserActionable", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "need_globalization": MoPropertyMeta("need_globalization", "needGlobalization", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "oper_attr_name": MoPropertyMeta("oper_attr_name", "operAttrName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_attr_value": MoPropertyMeta("oper_attr_value", "operAttrValue", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "pool_dn": MoPropertyMeta("pool_dn", "poolDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "pooled_id": MoPropertyMeta("pooled_id", "pooledId", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version201b, MoPropertyMeta.CREATE_ONLY, 0x20, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "src_mo_class_name": MoPropertyMeta("src_mo_class_name", "srcMoClassName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "src_mo_dn": MoPropertyMeta("src_mo_dn", "srcMoDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "src_mo_rn": MoPropertyMeta("src_mo_rn", "srcMoRn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "src_template_dn": MoPropertyMeta("src_template_dn", "srcTemplateDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suppl_id1": MoPropertyMeta("suppl_id1", "supplId1", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "suppl_id2": MoPropertyMeta("suppl_id2", "supplId2", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "suppl_id3": MoPropertyMeta("suppl_id3", "supplId3", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "suppl_id4": MoPropertyMeta("suppl_id4", "supplId4", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "user_action": MoPropertyMeta("user_action", "userAction", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["no-action", "reference-global", "rename"], []), 
        "user_input_name": MoPropertyMeta("user_input_name", "userInputName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "user_name_oper_attr": MoPropertyMeta("user_name_oper_attr", "userNameOperAttr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
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
        "fsmDescr": "fsm_descr", 
        "fsmPrev": "fsm_prev", 
        "fsmProgr": "fsm_progr", 
        "fsmRmtInvErrCode": "fsm_rmt_inv_err_code", 
        "fsmRmtInvErrDescr": "fsm_rmt_inv_err_descr", 
        "fsmRmtInvRslt": "fsm_rmt_inv_rslt", 
        "fsmStageDescr": "fsm_stage_descr", 
        "fsmStamp": "fsm_stamp", 
        "fsmStatus": "fsm_status", 
        "fsmTry": "fsm_try", 
        "glAction": "gl_action", 
        "glAttrValue": "gl_attr_value", 
        "glOperAction": "gl_oper_action", 
        "glOperAttrValue": "gl_oper_attr_value", 
        "id": "id", 
        "identPoolName": "ident_pool_name", 
        "identType": "ident_type", 
        "intent": "intent", 
        "isBlock": "is_block", 
        "isReferenceGlobalPool": "is_reference_global_pool", 
        "isSrcTemplate": "is_src_template", 
        "isStaticId": "is_static_id", 
        "isUserActionable": "is_user_actionable", 
        "needGlobalization": "need_globalization", 
        "operAttrName": "oper_attr_name", 
        "operAttrValue": "oper_attr_value", 
        "owner": "owner", 
        "poolDn": "pool_dn", 
        "pooledId": "pooled_id", 
        "purpose": "purpose", 
        "rn": "rn", 
        "srcMoClassName": "src_mo_class_name", 
        "srcMoDn": "src_mo_dn", 
        "srcMoRn": "src_mo_rn", 
        "srcTemplateDn": "src_template_dn", 
        "status": "status", 
        "supplId1": "suppl_id1", 
        "supplId2": "suppl_id2", 
        "supplId3": "suppl_id3", 
        "supplId4": "suppl_id4", 
        "userAction": "user_action", 
        "userInputName": "user_input_name", 
        "userNameOperAttr": "user_name_oper_attr", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_state = None
        self.assigned = None
        self.attr_name = None
        self.attr_value = None
        self.child_action = None
        self.conflict = None
        self.cons_dn = None
        self.cons_type = None
        self.defined_in_idm = None
        self.evalution_state = None
        self.fsm_descr = None
        self.fsm_prev = None
        self.fsm_progr = None
        self.fsm_rmt_inv_err_code = None
        self.fsm_rmt_inv_err_descr = None
        self.fsm_rmt_inv_rslt = None
        self.fsm_stage_descr = None
        self.fsm_stamp = None
        self.fsm_status = None
        self.fsm_try = None
        self.gl_action = None
        self.gl_attr_value = None
        self.gl_oper_action = None
        self.gl_oper_attr_value = None
        self.ident_pool_name = None
        self.ident_type = None
        self.intent = None
        self.is_block = None
        self.is_reference_global_pool = None
        self.is_src_template = None
        self.is_static_id = None
        self.is_user_actionable = None
        self.need_globalization = None
        self.oper_attr_name = None
        self.oper_attr_value = None
        self.owner = None
        self.pool_dn = None
        self.pooled_id = None
        self.purpose = None
        self.src_mo_class_name = None
        self.src_mo_dn = None
        self.src_mo_rn = None
        self.src_template_dn = None
        self.status = None
        self.suppl_id1 = None
        self.suppl_id2 = None
        self.suppl_id3 = None
        self.suppl_id4 = None
        self.user_action = None
        self.user_input_name = None
        self.user_name_oper_attr = None

        ManagedObject.__init__(self, "GlIdentCtxResOp", parent_mo_or_dn, **kwargs)

