"""This module contains the general information for SmartlicenseAgent ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SmartlicenseAgentConsts():
    AGENT_STATE_AUTHORIZED = "authorized"
    AGENT_STATE_EXPIRED = "expired"
    AGENT_STATE_OUTOFCOMPLIANCE = "outofcompliance"
    AGENT_STATE_REGISTERED = "registered"
    AGENT_STATE_UNCONFIGURED = "unconfigured"
    AGENT_STATE_UNIDENTIFIED = "unidentified"
    AUTH_EXPIRED_FALSE = "false"
    AUTH_EXPIRED_NO = "no"
    AUTH_EXPIRED_TRUE = "true"
    AUTH_EXPIRED_YES = "yes"
    ENFORCEMENT_MODE_AUTHORIZATION_EXPIRED = "authorization-expired"
    ENFORCEMENT_MODE_COMPLIANCE = "compliance"
    ENFORCEMENT_MODE_DISABLED = "disabled"
    ENFORCEMENT_MODE_EVAL = "eval"
    ENFORCEMENT_MODE_EXPIRED = "expired"
    ENFORCEMENT_MODE_GRACE_PERIOD = "grace-period"
    ENFORCEMENT_MODE_GRACE_PERIOD_EXPIRED = "grace-period-expired"
    ENFORCEMENT_MODE_INIT = "init"
    ENFORCEMENT_MODE_INVALID = "invalid"
    ENFORCEMENT_MODE_INVALID_TAG = "invalid-tag"
    ENFORCEMENT_MODE_MAX = "max"
    ENFORCEMENT_MODE_OUT_OF_COMPLIANCE = "out-of-compliance"
    ENFORCEMENT_MODE_OVERAGE = "overage"
    ENFORCEMENT_MODE_WAITING = "waiting"
    EVAL_IN_USE_FALSE = "false"
    EVAL_IN_USE_NO = "no"
    EVAL_IN_USE_TRUE = "true"
    EVAL_IN_USE_YES = "yes"
    EXPORT_CONTROLLED_ALLOWED_FALSE = "false"
    EXPORT_CONTROLLED_ALLOWED_NO = "no"
    EXPORT_CONTROLLED_ALLOWED_TRUE = "true"
    EXPORT_CONTROLLED_ALLOWED_YES = "yes"
    FSM_PREV_CONFIGURE_BEGIN = "ConfigureBegin"
    FSM_PREV_CONFIGURE_CONFIG = "ConfigureConfig"
    FSM_PREV_CONFIGURE_FAIL = "ConfigureFail"
    FSM_PREV_CONFIGURE_SUCCESS = "ConfigureSuccess"
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
    FSM_STATUS_CONFIGURE_BEGIN = "ConfigureBegin"
    FSM_STATUS_CONFIGURE_CONFIG = "ConfigureConfig"
    FSM_STATUS_CONFIGURE_FAIL = "ConfigureFail"
    FSM_STATUS_CONFIGURE_SUCCESS = "ConfigureSuccess"
    FSM_STATUS_NOP = "nop"
    GCH_DEBUG_LEVEL_ALL = "all"
    GCH_DEBUG_LEVEL_DEBUG = "debug"
    GCH_DEBUG_LEVEL_ERROR = "error"
    GCH_DEBUG_LEVEL_TRACE = "trace"
    REGISTRATION_STATUS_NOT_REGISTERED = "not-registered"
    REGISTRATION_STATUS_REGISTRATION_COMPLETED = "registration-completed"
    REGISTRATION_STATUS_REGISTRATION_FAILED = "registration-failed"
    REGISTRATION_STATUS_REGISTRATION_IN_PROGRESS = "registration-in-progress"
    REGISTRATION_STATUS_REGISTRATION_RETRY_IN_PROGRESS = "registration-retry-in-progress"
    RENEW_ID_CERTIFICATE_FALSE = "false"
    RENEW_ID_CERTIFICATE_NO = "no"
    RENEW_ID_CERTIFICATE_TRUE = "true"
    RENEW_ID_CERTIFICATE_YES = "yes"
    RENEW_STATUS_FALSE = "false"
    RENEW_STATUS_NO = "no"
    RENEW_STATUS_TRUE = "true"
    RENEW_STATUS_YES = "yes"
    SHOW_AGENT_TECH_SUPPORT_FALSE = "false"
    SHOW_AGENT_TECH_SUPPORT_NO = "no"
    SHOW_AGENT_TECH_SUPPORT_TRUE = "true"
    SHOW_AGENT_TECH_SUPPORT_YES = "yes"


class SmartlicenseAgent(ManagedObject):
    """This is SmartlicenseAgent class."""

    consts = SmartlicenseAgentConsts()
    naming_props = set([])

    mo_meta = MoMeta("SmartlicenseAgent", "smartlicenseAgent", "Agent", VersionMeta.Version141a, "InputOutput", 0x7f, [], ["admin"], ['smartlicenseHolder'], ['eventInst', 'faultInst', 'smartlicenseAgentFsm', 'smartlicenseAgentFsmTask', 'smartlicenseTest'], ["Get"])

    prop_meta = {
        "agent_component_version": MoPropertyMeta("agent_component_version", "agentComponentVersion", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "agent_state": MoPropertyMeta("agent_state", "agentState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["authorized", "expired", "outofcompliance", "registered", "unconfigured", "unidentified"], []), 
        "agent_version": MoPropertyMeta("agent_version", "agentVersion", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 1, 64, None, [], []), 
        "auth_expire_time": MoPropertyMeta("auth_expire_time", "authExpireTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "auth_expired": MoPropertyMeta("auth_expired", "authExpired", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "enforcement_mode": MoPropertyMeta("enforcement_mode", "enforcementMode", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["authorization-expired", "compliance", "disabled", "eval", "expired", "grace-period", "grace-period-expired", "init", "invalid", "invalid-tag", "max", "out-of-compliance", "overage", "waiting"], []), 
        "eval_expired_time": MoPropertyMeta("eval_expired_time", "evalExpiredTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "eval_in_use": MoPropertyMeta("eval_in_use", "evalInUse", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "eval_period_left": MoPropertyMeta("eval_period_left", "evalPeriodLeft", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", [], []), 
        "expire_time": MoPropertyMeta("expire_time", "expireTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "export_controlled_allowed": MoPropertyMeta("export_controlled_allowed", "exportControlledAllowed", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, ["ConfigureBegin", "ConfigureConfig", "ConfigureFail", "ConfigureSuccess", "nop"], []), 
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]), 
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-error", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Digest-Validation-error", "ERR-Exec-Gen-Cert-error", "ERR-Exec-Get-CA-Cert-error", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-Get-CA-Cert-error", "ERR-Get-Cert-error", "ERR-Get-Out-Diget-Message-error", "ERR-HTTP-Request-error", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-Ipv6-addr-configured", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-Policy-resolution-in-progress", "ERR-TOKEN-request-denied", "ERR-Update-VM-IP-Mask-Gateway-error", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-create-chassispack-under-dg", "ERR-create-hfp-under-dg", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-estimate-impact-on-reconnect", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-nfs-down", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-role-set-error", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-password-strength-check", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-set-error", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "none"], ["0-4294967295"]), 
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []), 
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, ["ConfigureBegin", "ConfigureConfig", "ConfigureFail", "ConfigureSuccess", "nop"], []), 
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "gch_debug_level": MoPropertyMeta("gch_debug_level", "gchDebugLevel", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["all", "debug", "error", "trace"], []), 
        "idcertificate": MoPropertyMeta("idcertificate", "idcertificate", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 4096, None, [], []), 
        "last_id_certificate_renewed": MoPropertyMeta("last_id_certificate_renewed", "lastIdCertificateRenewed", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "license_tech_support_info": MoPropertyMeta("license_tech_support_info", "licenseTechSupportInfo", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "next_registration_time": MoPropertyMeta("next_registration_time", "nextRegistrationTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "out_of_compliance_start_time": MoPropertyMeta("out_of_compliance_start_time", "outOfComplianceStartTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "product_instance_name": MoPropertyMeta("product_instance_name", "productInstanceName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "register_initial_time": MoPropertyMeta("register_initial_time", "registerInitialTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "register_renew_initial_time": MoPropertyMeta("register_renew_initial_time", "registerRenewInitialTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "register_renew_next_time": MoPropertyMeta("register_renew_next_time", "registerRenewNextTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "registration_expire_time": MoPropertyMeta("registration_expire_time", "registrationExpireTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "registration_failure_string": MoPropertyMeta("registration_failure_string", "registrationFailureString", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "registration_status": MoPropertyMeta("registration_status", "registrationStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-registered", "registration-completed", "registration-failed", "registration-in-progress", "registration-retry-in-progress"], []), 
        "registration_status_string": MoPropertyMeta("registration_status_string", "registrationStatusString", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "renew_failure_string": MoPropertyMeta("renew_failure_string", "renewFailureString", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "renew_id_certificate": MoPropertyMeta("renew_id_certificate", "renewIdCertificate", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []), 
        "renew_initial_time": MoPropertyMeta("renew_initial_time", "renewInitialTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "renew_next_time": MoPropertyMeta("renew_next_time", "renewNextTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "renew_status": MoPropertyMeta("renew_status", "renewStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "show_agent_tech_support": MoPropertyMeta("show_agent_tech_support", "showAgentTechSupport", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []), 
        "smart_account": MoPropertyMeta("smart_account", "smartAccount", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "udi_host_identifier": MoPropertyMeta("udi_host_identifier", "udiHostIdentifier", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "udi_ip_address": MoPropertyMeta("udi_ip_address", "udiIpAddress", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "udi_mac_address": MoPropertyMeta("udi_mac_address", "udiMacAddress", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "udi_pid": MoPropertyMeta("udi_pid", "udiPid", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "udi_sn": MoPropertyMeta("udi_sn", "udiSn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "udi_suvi": MoPropertyMeta("udi_suvi", "udiSuvi", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "udi_uuid": MoPropertyMeta("udi_uuid", "udiUuid", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "udi_vid": MoPropertyMeta("udi_vid", "udiVid", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "virtual_account": MoPropertyMeta("virtual_account", "virtualAccount", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "agentComponentVersion": "agent_component_version", 
        "agentState": "agent_state", 
        "agentVersion": "agent_version", 
        "authExpireTime": "auth_expire_time", 
        "authExpired": "auth_expired", 
        "childAction": "child_action", 
        "dn": "dn", 
        "enforcementMode": "enforcement_mode", 
        "evalExpiredTime": "eval_expired_time", 
        "evalInUse": "eval_in_use", 
        "evalPeriodLeft": "eval_period_left", 
        "expireTime": "expire_time", 
        "exportControlledAllowed": "export_controlled_allowed", 
        "fltAggr": "flt_aggr", 
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
        "gchDebugLevel": "gch_debug_level", 
        "idcertificate": "idcertificate", 
        "lastIdCertificateRenewed": "last_id_certificate_renewed", 
        "licenseTechSupportInfo": "license_tech_support_info", 
        "nextRegistrationTime": "next_registration_time", 
        "outOfComplianceStartTime": "out_of_compliance_start_time", 
        "productInstanceName": "product_instance_name", 
        "registerInitialTime": "register_initial_time", 
        "registerRenewInitialTime": "register_renew_initial_time", 
        "registerRenewNextTime": "register_renew_next_time", 
        "registrationExpireTime": "registration_expire_time", 
        "registrationFailureString": "registration_failure_string", 
        "registrationStatus": "registration_status", 
        "registrationStatusString": "registration_status_string", 
        "renewFailureString": "renew_failure_string", 
        "renewIdCertificate": "renew_id_certificate", 
        "renewInitialTime": "renew_initial_time", 
        "renewNextTime": "renew_next_time", 
        "renewStatus": "renew_status", 
        "rn": "rn", 
        "showAgentTechSupport": "show_agent_tech_support", 
        "smartAccount": "smart_account", 
        "status": "status", 
        "udiHostIdentifier": "udi_host_identifier", 
        "udiIpAddress": "udi_ip_address", 
        "udiMacAddress": "udi_mac_address", 
        "udiPid": "udi_pid", 
        "udiSn": "udi_sn", 
        "udiSuvi": "udi_suvi", 
        "udiUuid": "udi_uuid", 
        "udiVid": "udi_vid", 
        "virtualAccount": "virtual_account", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.agent_component_version = None
        self.agent_state = None
        self.agent_version = None
        self.auth_expire_time = None
        self.auth_expired = None
        self.child_action = None
        self.enforcement_mode = None
        self.eval_expired_time = None
        self.eval_in_use = None
        self.eval_period_left = None
        self.expire_time = None
        self.export_controlled_allowed = None
        self.flt_aggr = None
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
        self.gch_debug_level = None
        self.idcertificate = None
        self.last_id_certificate_renewed = None
        self.license_tech_support_info = None
        self.next_registration_time = None
        self.out_of_compliance_start_time = None
        self.product_instance_name = None
        self.register_initial_time = None
        self.register_renew_initial_time = None
        self.register_renew_next_time = None
        self.registration_expire_time = None
        self.registration_failure_string = None
        self.registration_status = None
        self.registration_status_string = None
        self.renew_failure_string = None
        self.renew_id_certificate = None
        self.renew_initial_time = None
        self.renew_next_time = None
        self.renew_status = None
        self.show_agent_tech_support = None
        self.smart_account = None
        self.status = None
        self.udi_host_identifier = None
        self.udi_ip_address = None
        self.udi_mac_address = None
        self.udi_pid = None
        self.udi_sn = None
        self.udi_suvi = None
        self.udi_uuid = None
        self.udi_vid = None
        self.virtual_account = None

        ManagedObject.__init__(self, "SmartlicenseAgent", parent_mo_or_dn, **kwargs)

