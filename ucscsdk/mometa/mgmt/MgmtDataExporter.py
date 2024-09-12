"""This module contains the general information for MgmtDataExporter ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtDataExporterConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    AT_VMLEVEL_FALSE = "false"
    AT_VMLEVEL_NO = "no"
    AT_VMLEVEL_TRUE = "true"
    AT_VMLEVEL_YES = "yes"
    FSM_PREV_EXPORT_DATA_BEGIN = "exportDataBegin"
    FSM_PREV_EXPORT_DATA_DME_DATA_EXPORT = "exportDataDmeDataExport"
    FSM_PREV_EXPORT_DATA_FAIL = "exportDataFail"
    FSM_PREV_EXPORT_DATA_SUCCESS = "exportDataSuccess"
    FSM_PREV_EXPORT_DATA_UPLOAD = "exportDataUpload"
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
    FSM_STATUS_EXPORT_DATA_BEGIN = "exportDataBegin"
    FSM_STATUS_EXPORT_DATA_DME_DATA_EXPORT = "exportDataDmeDataExport"
    FSM_STATUS_EXPORT_DATA_FAIL = "exportDataFail"
    FSM_STATUS_EXPORT_DATA_SUCCESS = "exportDataSuccess"
    FSM_STATUS_EXPORT_DATA_UPLOAD = "exportDataUpload"
    FSM_STATUS_NOP = "nop"
    INT_ID_NONE = "none"
    JOB_IMMEDIATE = "immediate"
    OP_STATUS_ALL_SUCCESS = "all-success"
    OP_STATUS_DOMAIN_SUSPENDED = "domain-suspended"
    OP_STATUS_FAILED = "failed"
    OP_STATUS_NOT_STARTED = "not-started"
    OP_STATUS_PARTIAL_FAILED = "partial-failed"
    OP_STATUS_WORK_IN_PROGRESS = "work-in-progress"
    OVER_ALL_STATUS_ALL_SUCCESS = "all-success"
    OVER_ALL_STATUS_DOMAIN_SUSPENDED = "domain-suspended"
    OVER_ALL_STATUS_FAILED = "failed"
    OVER_ALL_STATUS_NOT_STARTED = "not-started"
    OVER_ALL_STATUS_PARTIAL_FAILED = "partial-failed"
    OVER_ALL_STATUS_WORK_IN_PROGRESS = "work-in-progress"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PRESERVE_POOLED_VALUES_FALSE = "false"
    PRESERVE_POOLED_VALUES_NO = "no"
    PRESERVE_POOLED_VALUES_TRUE = "true"
    PRESERVE_POOLED_VALUES_YES = "yes"
    PROTO_FTP = "ftp"
    PROTO_HTTP = "http"
    PROTO_NFS_COPY = "nfs-copy"
    PROTO_NONE = "none"
    PROTO_SCP = "scp"
    PROTO_SFTP = "sftp"
    PROTO_TFTP = "tftp"
    TYPE_CONFIG_ALL = "config-all"
    TYPE_CONFIG_LOGICAL = "config-logical"
    TYPE_CONFIG_SYSTEM = "config-system"
    TYPE_FULL_STATE = "full-state"


class MgmtDataExporter(ManagedObject):
    """This is MgmtDataExporter class."""

    consts = MgmtDataExporterConsts()
    naming_props = set(['hostname'])

    mo_meta = MoMeta("MgmtDataExporter", "mgmtDataExporter", "exporter-[hostname]", VersionMeta.Version101a, "InputOutput", 0x7fff, [], ["admin"], ['topSystem'], ['eventInst', 'faultInst', 'mgmtDataExporterFsm', 'mgmtDataExporterFsmTask', 'mgmtDataItem'], ["Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "at_vm_level": MoPropertyMeta("at_vm_level", "atVMLevel", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "err_msg": MoPropertyMeta("err_msg", "errMsg", "string", VersionMeta.Version201v, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["exportDataBegin", "exportDataDmeDataExport", "exportDataFail", "exportDataSuccess", "exportDataUpload", "nop"], []), 
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]), 
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-error", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Digest-Validation-error", "ERR-Exec-Gen-Cert-error", "ERR-Exec-Get-CA-Cert-error", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-Get-CA-Cert-error", "ERR-Get-Cert-error", "ERR-Get-Out-Diget-Message-error", "ERR-HTTP-Request-error", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-Ipv6-addr-configured", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-Policy-resolution-in-progress", "ERR-TOKEN-request-denied", "ERR-Update-VM-IP-Mask-Gateway-error", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-create-chassispack-under-dg", "ERR-create-hfp-under-dg", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-estimate-impact-on-reconnect", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-nfs-down", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-role-set-error", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-password-strength-check", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-set-error", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "none"], ["0-4294967295"]), 
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []), 
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["exportDataBegin", "exportDataDmeDataExport", "exportDataFail", "exportDataSuccess", "exportDataUpload", "nop"], []), 
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "job": MoPropertyMeta("job", "job", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x40, None, None, None, ["immediate"], []), 
        "max_files": MoPropertyMeta("max_files", "maxFiles", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "num_of_pending": MoPropertyMeta("num_of_pending", "numOfPending", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "op_status": MoPropertyMeta("op_status", "opStatus", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all-success", "domain-suspended", "failed", "not-started", "partial-failed", "work-in-progress"], []), 
        "over_all_status": MoPropertyMeta("over_all_status", "overAllStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all-success", "domain-suspended", "failed", "not-started", "partial-failed", "work-in-progress"], []), 
        "owner_policy": MoPropertyMeta("owner_policy", "ownerPolicy", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "post_action": MoPropertyMeta("post_action", "postAction", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "preserve_pooled_values": MoPropertyMeta("preserve_pooled_values", "preservePooledValues", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "no", "true", "yes"], []), 
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["ftp", "http", "nfs-copy", "none", "scp", "sftp", "tftp"], []), 
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, 0, 64, None, [], []), 
        "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x400, 1, 128, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "status_report": MoPropertyMeta("status_report", "statusReport", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 512, None, [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["config-all", "config-logical", "config-system", "full-state"], []), 
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4000, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "atVMLevel": "at_vm_level", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "errMsg": "err_msg", 
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
        "hostname": "hostname", 
        "intId": "int_id", 
        "job": "job", 
        "maxFiles": "max_files", 
        "name": "name", 
        "numOfPending": "num_of_pending", 
        "opStatus": "op_status", 
        "overAllStatus": "over_all_status", 
        "ownerPolicy": "owner_policy", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "postAction": "post_action", 
        "preservePooledValues": "preserve_pooled_values", 
        "proto": "proto", 
        "pwd": "pwd", 
        "remoteFile": "remote_file", 
        "rn": "rn", 
        "status": "status", 
        "statusReport": "status_report", 
        "type": "type", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, hostname, **kwargs):
        self._dirty_mask = 0
        self.hostname = hostname
        self.admin_state = None
        self.at_vm_level = None
        self.child_action = None
        self.descr = None
        self.err_msg = None
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
        self.int_id = None
        self.job = None
        self.max_files = None
        self.name = None
        self.num_of_pending = None
        self.op_status = None
        self.over_all_status = None
        self.owner_policy = None
        self.policy_level = None
        self.policy_owner = None
        self.post_action = None
        self.preserve_pooled_values = None
        self.proto = None
        self.pwd = None
        self.remote_file = None
        self.status = None
        self.status_report = None
        self.type = None
        self.user = None

        ManagedObject.__init__(self, "MgmtDataExporter", parent_mo_or_dn, **kwargs)

