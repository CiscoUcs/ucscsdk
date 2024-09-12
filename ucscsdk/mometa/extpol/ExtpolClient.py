"""This module contains the general information for ExtpolClient ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ExtpolClientConsts():
    CONN_PROTOCOL_IPV4 = "ipv4"
    CONN_PROTOCOL_IPV6 = "ipv6"
    CONN_PROTOCOL_UNKNOWN = "unknown"
    CONNECTION_STATE_CONNECTED = "connected"
    CONNECTION_STATE_LOST_CONNECTIVITY = "lost-connectivity"
    FSM_PREV_UPDATE_CONTEXT_FSM_BEGIN = "UpdateContextFsmBegin"
    FSM_PREV_UPDATE_CONTEXT_FSM_EXECUTE = "UpdateContextFsmExecute"
    FSM_PREV_UPDATE_CONTEXT_FSM_FAIL = "UpdateContextFsmFail"
    FSM_PREV_UPDATE_CONTEXT_FSM_SUCCESS = "UpdateContextFsmSuccess"
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
    FSM_STATUS_UPDATE_CONTEXT_FSM_BEGIN = "UpdateContextFsmBegin"
    FSM_STATUS_UPDATE_CONTEXT_FSM_EXECUTE = "UpdateContextFsmExecute"
    FSM_STATUS_UPDATE_CONTEXT_FSM_FAIL = "UpdateContextFsmFail"
    FSM_STATUS_UPDATE_CONTEXT_FSM_SUCCESS = "UpdateContextFsmSuccess"
    FSM_STATUS_NOP = "nop"
    LIC_STATE_LICENSE_EXPIRED = "license-expired"
    LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
    LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
    LIC_STATE_LICENSE_OK = "license-ok"
    LIC_STATE_NOT_APPLICABLE = "not-applicable"
    LIC_STATE_UNKNOWN = "unknown"
    LOSS_VISIBILITY_SOURCE_POLLING = "polling"
    LOSS_VISIBILITY_SOURCE_UNKNOWN = "unknown"
    OPER_STATE_LOST_VISIBILITY = "lost-visibility"
    OPER_STATE_REGISTERED = "registered"
    OPER_STATE_REGISTERING = "registering"
    OPER_STATE_SYNCHRONIZING = "synchronizing"
    OPER_STATE_UNREGISTERED = "unregistered"
    OPER_STATE_VERSION_MISMATCH = "version-mismatch"
    PRODUCT_FAMILY_UCS_CLASSIC = "ucs-classic"
    PRODUCT_FAMILY_UCS_CLASSIC_3GEN = "ucs-classic-3gen"
    PRODUCT_FAMILY_UCS_CLASSIC_4GEN = "ucs-classic-4gen"
    PRODUCT_FAMILY_UCS_CLASSIC_5GEN = "ucs-classic-5gen"
    PRODUCT_FAMILY_UCS_MINI = "ucs-mini"
    PRODUCT_FAMILY_UCS_X_SERIES_DIRECT = "ucs-x-series-direct"
    SUSPEND_STATE_OFF = "off"
    SUSPEND_STATE_ON = "on"
    TYPE_BOOT_MGR = "boot-mgr"
    TYPE_CENTRAL_MGR = "central-mgr"
    TYPE_IDENTIFIER_MGR = "identifier-mgr"
    TYPE_MANAGED_ENDPOINT = "managed-endpoint"
    TYPE_MGMT_CONTROLLER = "mgmt-controller"
    TYPE_OPERATION_MGR = "operation-mgr"
    TYPE_POLICY_MGR = "policy-mgr"
    TYPE_RESOURCE_AGGR = "resource-aggr"
    TYPE_RESOURCE_MGR = "resource-mgr"
    TYPE_SERVER_MGR = "server-mgr"
    TYPE_SERVICE_REG = "service-reg"
    TYPE_STATS_MGR = "stats-mgr"
    TYPE_STORAGE_BROKER = "storage-broker"
    TYPE_VIRTUAL_SWITCHING_MGR = "virtual-switching-mgr"
    TYPE_VM_MGR = "vm-mgr"
    VERSION_HOLDER_FALSE = "false"
    VERSION_HOLDER_NO = "no"
    VERSION_HOLDER_TRUE = "true"
    VERSION_HOLDER_YES = "yes"


class ExtpolClient(ManagedObject):
    """This is ExtpolClient class."""

    consts = ExtpolClientConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ExtpolClient", "extpolClient", "client-[id]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin"], ['extpolClientCont'], ['dupeEp', 'eventInst', 'extpolClientFsm', 'extpolClientFsmTask', 'fabricVnetEpSyncEp', 'faultInst', 'mgmtBackup', 'observeObserved', 'policyConfigError', 'policyPolicyScopeCont', 'statsInventoryMeta'], ["Get", "Remove"])

    prop_meta = {
        "capability": MoPropertyMeta("capability", "capability", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|server-mgr|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr),){0,29}(defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|server-mgr|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr){0,1}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "conn_protocol": MoPropertyMeta("conn_protocol", "connProtocol", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipv4", "ipv6", "unknown"], []), 
        "connection_state": MoPropertyMeta("connection_state", "connectionState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "lost-connectivity"], []), 
        "context": MoPropertyMeta("context", "context", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["UpdateContextFsmBegin", "UpdateContextFsmExecute", "UpdateContextFsmFail", "UpdateContextFsmSuccess", "nop"], []), 
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]), 
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-error", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Digest-Validation-error", "ERR-Exec-Gen-Cert-error", "ERR-Exec-Get-CA-Cert-error", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-Get-CA-Cert-error", "ERR-Get-Cert-error", "ERR-Get-Out-Diget-Message-error", "ERR-HTTP-Request-error", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-Ipv6-addr-configured", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-Policy-resolution-in-progress", "ERR-TOKEN-request-denied", "ERR-Update-VM-IP-Mask-Gateway-error", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-create-chassispack-under-dg", "ERR-create-hfp-under-dg", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-estimate-impact-on-reconnect", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-nfs-down", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-role-set-error", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-password-strength-check", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-set-error", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "none"], ["0-4294967295"]), 
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []), 
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["UpdateContextFsmBegin", "UpdateContextFsmExecute", "UpdateContextFsmFail", "UpdateContextFsmSuccess", "nop"], []), 
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "grace_period_used": MoPropertyMeta("grace_period_used", "gracePeriodUsed", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "host": MoPropertyMeta("host", "host", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?$|^[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?(\.[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?)*(\.[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?)$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$""", [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "interest": MoPropertyMeta("interest", "interest", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|server-mgr|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr),){0,29}(defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|server-mgr|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr){0,1}""", [], []), 
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "ipv6": MoPropertyMeta("ipv6", "ipv6", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "last_poll_ts": MoPropertyMeta("last_poll_ts", "lastPollTs", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []), 
        "loss_visibility_source": MoPropertyMeta("loss_visibility_source", "lossVisibilitySource", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["polling", "unknown"], []), 
        "maint_grp_tag": MoPropertyMeta("maint_grp_tag", "maintGrpTag", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 64, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?]+""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "product_family": MoPropertyMeta("product_family", "productFamily", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ucs-classic", "ucs-classic-3gen", "ucs-classic-4gen", "ucs-classic-5gen", "ucs-mini", "ucs-x-series-direct"], []), 
        "reg_count": MoPropertyMeta("reg_count", "regCount", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "site": MoPropertyMeta("site", "site", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspend_state": MoPropertyMeta("suspend_state", "suspendState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["off", "on"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["boot-mgr", "central-mgr", "identifier-mgr", "managed-endpoint", "mgmt-controller", "operation-mgr", "policy-mgr", "resource-aggr", "resource-mgr", "server-mgr", "service-reg", "stats-mgr", "storage-broker", "virtual-switching-mgr", "vm-mgr"], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "version_holder": MoPropertyMeta("version_holder", "versionHolder", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "capability": "capability", 
        "childAction": "child_action", 
        "connProtocol": "conn_protocol", 
        "connectionState": "connection_state", 
        "context": "context", 
        "descr": "descr", 
        "dn": "dn", 
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
        "gracePeriodUsed": "grace_period_used", 
        "guid": "guid", 
        "host": "host", 
        "id": "id", 
        "interest": "interest", 
        "ip": "ip", 
        "ipv6": "ipv6", 
        "lastPollTs": "last_poll_ts", 
        "licState": "lic_state", 
        "lossVisibilitySource": "loss_visibility_source", 
        "maintGrpTag": "maint_grp_tag", 
        "name": "name", 
        "operState": "oper_state", 
        "owner": "owner", 
        "productFamily": "product_family", 
        "regCount": "reg_count", 
        "rn": "rn", 
        "site": "site", 
        "status": "status", 
        "suspendState": "suspend_state", 
        "type": "type", 
        "version": "version", 
        "versionHolder": "version_holder", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.capability = None
        self.child_action = None
        self.conn_protocol = None
        self.connection_state = None
        self.context = None
        self.descr = None
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
        self.grace_period_used = None
        self.guid = None
        self.host = None
        self.interest = None
        self.ip = None
        self.ipv6 = None
        self.last_poll_ts = None
        self.lic_state = None
        self.loss_visibility_source = None
        self.maint_grp_tag = None
        self.name = None
        self.oper_state = None
        self.owner = None
        self.product_family = None
        self.reg_count = None
        self.site = None
        self.status = None
        self.suspend_state = None
        self.type = None
        self.version = None
        self.version_holder = None

        ManagedObject.__init__(self, "ExtpolClient", parent_mo_or_dn, **kwargs)

