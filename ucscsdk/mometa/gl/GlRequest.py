"""This module contains the general information for GlRequest ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlRequestConsts():
    ADMIN_STATE_EVALUATE = "evaluate"
    ADMIN_STATE_GLOBALIZE = "globalize"
    ADMIN_STATE_REEVALUATE = "reevaluate"
    ADMIN_STATE_TERMINATE = "terminate"
    FSM_PREV_CREATE_GLOBAL_ID_POOL_BEGIN = "CreateGlobalIdPoolBegin"
    FSM_PREV_CREATE_GLOBAL_ID_POOL_CREATE_POLICIES = "CreateGlobalIdPoolCreatePolicies"
    FSM_PREV_CREATE_GLOBAL_ID_POOL_FAIL = "CreateGlobalIdPoolFail"
    FSM_PREV_CREATE_GLOBAL_ID_POOL_SUCCESS = "CreateGlobalIdPoolSuccess"
    FSM_PREV_CREATE_GLOBAL_POLICY_BEGIN = "CreateGlobalPolicyBegin"
    FSM_PREV_CREATE_GLOBAL_POLICY_CREATE_POLICIES = "CreateGlobalPolicyCreatePolicies"
    FSM_PREV_CREATE_GLOBAL_POLICY_FAIL = "CreateGlobalPolicyFail"
    FSM_PREV_CREATE_GLOBAL_POLICY_SUCCESS = "CreateGlobalPolicySuccess"
    FSM_PREV_EVALUATE_BEGIN = "EvaluateBegin"
    FSM_PREV_EVALUATE_EVALUATE = "EvaluateEvaluate"
    FSM_PREV_EVALUATE_FAIL = "EvaluateFail"
    FSM_PREV_EVALUATE_FETCH_DOMAIN_DATA = "EvaluateFetchDomainData"
    FSM_PREV_EVALUATE_SUCCESS = "EvaluateSuccess"
    FSM_PREV_EVALUATE_VALIDATE = "EvaluateValidate"
    FSM_PREV_GLOBALIZE_ADD_ID_TO_GLOBAL_POOL = "GlobalizeAddIdToGlobalPool"
    FSM_PREV_GLOBALIZE_ASSIGN_IDS = "GlobalizeAssignIds"
    FSM_PREV_GLOBALIZE_BEGIN = "GlobalizeBegin"
    FSM_PREV_GLOBALIZE_CREATE_GSP = "GlobalizeCreateGSP"
    FSM_PREV_GLOBALIZE_CREATE_ORG = "GlobalizeCreateOrg"
    FSM_PREV_GLOBALIZE_CREATE_POLICIES = "GlobalizeCreatePolicies"
    FSM_PREV_GLOBALIZE_CREATE_UPDATE_POLICY_SCOPE = "GlobalizeCreateUpdatePolicyScope"
    FSM_PREV_GLOBALIZE_CREATE_VLAN_ORG_PERMISSION = "GlobalizeCreateVlanOrgPermission"
    FSM_PREV_GLOBALIZE_FAIL = "GlobalizeFail"
    FSM_PREV_GLOBALIZE_REAPPLY_GSP = "GlobalizeReapplyGSP"
    FSM_PREV_GLOBALIZE_RESOLVE_GLOBAL_POOL_DN = "GlobalizeResolveGlobalPoolDn"
    FSM_PREV_GLOBALIZE_SUCCESS = "GlobalizeSuccess"
    FSM_PREV_GLOBALIZE_UNASSIGN_IDS = "GlobalizeUnassignIds"
    FSM_PREV_GLOBALIZE_UPDATE_DOMAIN_MOS = "GlobalizeUpdateDomainMos"
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
    FSM_STATUS_CREATE_GLOBAL_ID_POOL_BEGIN = "CreateGlobalIdPoolBegin"
    FSM_STATUS_CREATE_GLOBAL_ID_POOL_CREATE_POLICIES = "CreateGlobalIdPoolCreatePolicies"
    FSM_STATUS_CREATE_GLOBAL_ID_POOL_FAIL = "CreateGlobalIdPoolFail"
    FSM_STATUS_CREATE_GLOBAL_ID_POOL_SUCCESS = "CreateGlobalIdPoolSuccess"
    FSM_STATUS_CREATE_GLOBAL_POLICY_BEGIN = "CreateGlobalPolicyBegin"
    FSM_STATUS_CREATE_GLOBAL_POLICY_CREATE_POLICIES = "CreateGlobalPolicyCreatePolicies"
    FSM_STATUS_CREATE_GLOBAL_POLICY_FAIL = "CreateGlobalPolicyFail"
    FSM_STATUS_CREATE_GLOBAL_POLICY_SUCCESS = "CreateGlobalPolicySuccess"
    FSM_STATUS_EVALUATE_BEGIN = "EvaluateBegin"
    FSM_STATUS_EVALUATE_EVALUATE = "EvaluateEvaluate"
    FSM_STATUS_EVALUATE_FAIL = "EvaluateFail"
    FSM_STATUS_EVALUATE_FETCH_DOMAIN_DATA = "EvaluateFetchDomainData"
    FSM_STATUS_EVALUATE_SUCCESS = "EvaluateSuccess"
    FSM_STATUS_EVALUATE_VALIDATE = "EvaluateValidate"
    FSM_STATUS_GLOBALIZE_ADD_ID_TO_GLOBAL_POOL = "GlobalizeAddIdToGlobalPool"
    FSM_STATUS_GLOBALIZE_ASSIGN_IDS = "GlobalizeAssignIds"
    FSM_STATUS_GLOBALIZE_BEGIN = "GlobalizeBegin"
    FSM_STATUS_GLOBALIZE_CREATE_GSP = "GlobalizeCreateGSP"
    FSM_STATUS_GLOBALIZE_CREATE_ORG = "GlobalizeCreateOrg"
    FSM_STATUS_GLOBALIZE_CREATE_POLICIES = "GlobalizeCreatePolicies"
    FSM_STATUS_GLOBALIZE_CREATE_UPDATE_POLICY_SCOPE = "GlobalizeCreateUpdatePolicyScope"
    FSM_STATUS_GLOBALIZE_CREATE_VLAN_ORG_PERMISSION = "GlobalizeCreateVlanOrgPermission"
    FSM_STATUS_GLOBALIZE_FAIL = "GlobalizeFail"
    FSM_STATUS_GLOBALIZE_REAPPLY_GSP = "GlobalizeReapplyGSP"
    FSM_STATUS_GLOBALIZE_RESOLVE_GLOBAL_POOL_DN = "GlobalizeResolveGlobalPoolDn"
    FSM_STATUS_GLOBALIZE_SUCCESS = "GlobalizeSuccess"
    FSM_STATUS_GLOBALIZE_UNASSIGN_IDS = "GlobalizeUnassignIds"
    FSM_STATUS_GLOBALIZE_UPDATE_DOMAIN_MOS = "GlobalizeUpdateDomainMos"
    FSM_STATUS_NOP = "nop"
    GLOBALIZE_ADMIN_STATE_APPLY_RULE = "apply-rule"
    GLOBALIZE_ADMIN_STATE_CREATE_GLOBAL_ID_POOL = "create-global-id-pool"
    GLOBALIZE_ADMIN_STATE_CREATE_GLOBAL_POLICY = "create-global-policy"
    GLOBALIZE_ADMIN_STATE_CREATE_GLOBAL_SERVICE_PROFILE = "create-global-service-profile"
    GLOBALIZE_ADMIN_STATE_DEFAULT = "default"
    GLOBALIZE_ADMIN_STATE_GLOBALIZE_LSP = "globalize-lsp"
    GLOBALIZE_ADMIN_STATE_RESOLVE_CONFLICT = "resolve-conflict"
    GLOBALIZE_ADMIN_STATE_UNBIND_TEMPLATE = "unbind-template"
    IS_SERVER_POOL_ASSIGNED_FALSE = "false"
    IS_SERVER_POOL_ASSIGNED_NO = "no"
    IS_SERVER_POOL_ASSIGNED_TRUE = "true"
    IS_SERVER_POOL_ASSIGNED_YES = "yes"
    OPER_STATE_APPLYING_RULE_AND_EVALUATING = "ApplyingRuleAndEvaluating"
    OPER_STATE_EVALUATED_WITH_BLOCKING_ISSUE = "EvaluatedWithBlockingIssue"
    OPER_STATE_EVALUATED_WITH_CONFLICT = "EvaluatedWithConflict"
    OPER_STATE_EVALUATED_WITH_ERROR = "EvaluatedWithError"
    OPER_STATE_EVALUATED_WITH_SUCCESS = "EvaluatedWithSuccess"
    OPER_STATE_EVALUATING = "Evaluating"
    OPER_STATE_FETCHING_DATA_FROM_DOMAIN = "FetchingDataFromDomain"
    OPER_STATE_GLOBALIZED_WITH_ERROR = "GlobalizedWithError"
    OPER_STATE_GLOBALIZED_WITH_SUCCESS = "GlobalizedWithSuccess"
    OPER_STATE_GLOBALIZING = "Globalizing"
    OPER_STATE_NOT_EVALUATED = "NotEvaluated"
    SESSION_STATE_ACTIVE = "active"
    SESSION_STATE_TERMINATED = "terminated"
    SIM_IS_RESPONSED_FALSE = "false"
    SIM_IS_RESPONSED_NO = "no"
    SIM_IS_RESPONSED_TRUE = "true"
    SIM_IS_RESPONSED_YES = "yes"
    SIM_STATUS_FALSE = "false"
    SIM_STATUS_NO = "no"
    SIM_STATUS_TRUE = "true"
    SIM_STATUS_YES = "yes"


class GlRequest(ManagedObject):
    """This is GlRequest class."""

    consts = GlRequestConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("GlRequest", "glRequest", "req-[id]", VersionMeta.Version201b, "InputOutput", 0xff, [], ["admin"], ['glDomainEp'], ['eventInst', 'faultInst', 'glInventoryEp', 'glLsp', 'glOperationEp', 'glPathEp', 'glPolicyResolutionEp', 'glRequestFsm', 'glRequestFsmTask', 'glVnicTemplateEp', 'messageEp'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["evaluate", "globalize", "reevaluate", "terminate"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "domain_id": MoPropertyMeta("domain_id", "domainId", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, ["CreateGlobalIdPoolBegin", "CreateGlobalIdPoolCreatePolicies", "CreateGlobalIdPoolFail", "CreateGlobalIdPoolSuccess", "CreateGlobalPolicyBegin", "CreateGlobalPolicyCreatePolicies", "CreateGlobalPolicyFail", "CreateGlobalPolicySuccess", "EvaluateBegin", "EvaluateEvaluate", "EvaluateFail", "EvaluateFetchDomainData", "EvaluateSuccess", "EvaluateValidate", "GlobalizeAddIdToGlobalPool", "GlobalizeAssignIds", "GlobalizeBegin", "GlobalizeCreateGSP", "GlobalizeCreateOrg", "GlobalizeCreatePolicies", "GlobalizeCreateUpdatePolicyScope", "GlobalizeCreateVlanOrgPermission", "GlobalizeFail", "GlobalizeReapplyGSP", "GlobalizeResolveGlobalPoolDn", "GlobalizeSuccess", "GlobalizeUnassignIds", "GlobalizeUpdateDomainMos", "nop"], []), 
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]), 
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-error", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Digest-Validation-error", "ERR-Exec-Gen-Cert-error", "ERR-Exec-Get-CA-Cert-error", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-Get-CA-Cert-error", "ERR-Get-Cert-error", "ERR-Get-Out-Diget-Message-error", "ERR-HTTP-Request-error", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-Ipv6-addr-configured", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-Policy-resolution-in-progress", "ERR-TOKEN-request-denied", "ERR-Update-VM-IP-Mask-Gateway-error", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-create-chassispack-under-dg", "ERR-create-hfp-under-dg", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-estimate-impact-on-reconnect", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-nfs-down", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-role-set-error", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-password-strength-check", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-set-error", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "none"], ["0-4294967295"]), 
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []), 
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, ["CreateGlobalIdPoolBegin", "CreateGlobalIdPoolCreatePolicies", "CreateGlobalIdPoolFail", "CreateGlobalIdPoolSuccess", "CreateGlobalPolicyBegin", "CreateGlobalPolicyCreatePolicies", "CreateGlobalPolicyFail", "CreateGlobalPolicySuccess", "EvaluateBegin", "EvaluateEvaluate", "EvaluateFail", "EvaluateFetchDomainData", "EvaluateSuccess", "EvaluateValidate", "GlobalizeAddIdToGlobalPool", "GlobalizeAssignIds", "GlobalizeBegin", "GlobalizeCreateGSP", "GlobalizeCreateOrg", "GlobalizeCreatePolicies", "GlobalizeCreateUpdatePolicyScope", "GlobalizeCreateVlanOrgPermission", "GlobalizeFail", "GlobalizeReapplyGSP", "GlobalizeResolveGlobalPoolDn", "GlobalizeSuccess", "GlobalizeUnassignIds", "GlobalizeUpdateDomainMos", "nop"], []), 
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "globalize_admin_state": MoPropertyMeta("globalize_admin_state", "globalizeAdminState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["apply-rule", "create-global-id-pool", "create-global-policy", "create-global-service-profile", "default", "globalize-lsp", "resolve-conflict", "unbind-template"], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "is_server_pool_assigned": MoPropertyMeta("is_server_pool_assigned", "isServerPoolAssigned", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "num_of_blocks": MoPropertyMeta("num_of_blocks", "numOfBlocks", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_non_block_conflicts": MoPropertyMeta("num_of_non_block_conflicts", "numOfNonBlockConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ApplyingRuleAndEvaluating", "EvaluatedWithBlockingIssue", "EvaluatedWithConflict", "EvaluatedWithError", "EvaluatedWithSuccess", "Evaluating", "FetchingDataFromDomain", "GlobalizedWithError", "GlobalizedWithSuccess", "Globalizing", "NotEvaluated"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "rule_applied_counter": MoPropertyMeta("rule_applied_counter", "ruleAppliedCounter", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "session_state": MoPropertyMeta("session_state", "sessionState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "terminated"], []), 
        "sim_cookie": MoPropertyMeta("sim_cookie", "simCookie", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "sim_error_msg": MoPropertyMeta("sim_error_msg", "simErrorMsg", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "sim_fsm_stage_name": MoPropertyMeta("sim_fsm_stage_name", "simFsmStageName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "sim_is_responsed": MoPropertyMeta("sim_is_responsed", "simIsResponsed", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "sim_request_time": MoPropertyMeta("sim_request_time", "simRequestTime", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "sim_status": MoPropertyMeta("sim_status", "simStatus", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "domainId": "domain_id", 
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
        "globalizeAdminState": "globalize_admin_state", 
        "id": "id", 
        "index": "index", 
        "isServerPoolAssigned": "is_server_pool_assigned", 
        "numOfBlocks": "num_of_blocks", 
        "numOfNonBlockConflicts": "num_of_non_block_conflicts", 
        "operState": "oper_state", 
        "rn": "rn", 
        "ruleAppliedCounter": "rule_applied_counter", 
        "sessionState": "session_state", 
        "simCookie": "sim_cookie", 
        "simErrorMsg": "sim_error_msg", 
        "simFsmStageName": "sim_fsm_stage_name", 
        "simIsResponsed": "sim_is_responsed", 
        "simRequestTime": "sim_request_time", 
        "simStatus": "sim_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_state = None
        self.child_action = None
        self.domain_id = None
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
        self.globalize_admin_state = None
        self.index = None
        self.is_server_pool_assigned = None
        self.num_of_blocks = None
        self.num_of_non_block_conflicts = None
        self.oper_state = None
        self.rule_applied_counter = None
        self.session_state = None
        self.sim_cookie = None
        self.sim_error_msg = None
        self.sim_fsm_stage_name = None
        self.sim_is_responsed = None
        self.sim_request_time = None
        self.sim_status = None
        self.status = None

        ManagedObject.__init__(self, "GlRequest", parent_mo_or_dn, **kwargs)

