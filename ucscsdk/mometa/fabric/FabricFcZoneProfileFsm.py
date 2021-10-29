"""This module contains the general information for FabricFcZoneProfileFsm ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricFcZoneProfileFsmConsts():
    COMPLETION_TIME_ = ""
    CURRENT_FSM_CONFIGURE = "Configure"
    CURRENT_FSM_NOP = "nop"
    FSM_STATUS_FAIL = "fail"
    FSM_STATUS_IN_PROGRESS = "inProgress"
    FSM_STATUS_NOP = "nop"
    FSM_STATUS_PENDING = "pending"
    FSM_STATUS_SKIP = "skip"
    FSM_STATUS_SUCCESS = "success"
    FSM_STATUS_THROTTLED = "throttled"
    RMT_ERR_CODE_ERR_DIAG_CANCELLED = "ERR-DIAG-cancelled"
    RMT_ERR_CODE_ERR_DIAG_FSM_RESTARTED = "ERR-DIAG-fsm-restarted"
    RMT_ERR_CODE_ERR_DIAG_TEST_FAILED = "ERR-DIAG-test-failed"
    RMT_ERR_CODE_ERR_DNLD_AUTHENTICATION_FAILURE = "ERR-DNLD-authentication-failure"
    RMT_ERR_CODE_ERR_DNLD_ERROR = "ERR-DNLD-error"
    RMT_ERR_CODE_ERR_DNLD_HOSTKEY_MISMATCH = "ERR-DNLD-hostkey-mismatch"
    RMT_ERR_CODE_ERR_DNLD_INVALID_IMAGE = "ERR-DNLD-invalid-image"
    RMT_ERR_CODE_ERR_DNLD_NO_FILE = "ERR-DNLD-no-file"
    RMT_ERR_CODE_ERR_DNLD_NO_SPACE = "ERR-DNLD-no-space"
    RMT_ERR_CODE_ERR_DNS_DELETE_ERROR = "ERR-DNS-delete-error"
    RMT_ERR_CODE_ERR_DNS_GET_ERROR = "ERR-DNS-get-error"
    RMT_ERR_CODE_ERR_DNS_SET_ERROR = "ERR-DNS-set-error"
    RMT_ERR_CODE_ERR_DIGEST_VALIDATION_ERROR = "ERR-Digest-Validation-error"
    RMT_ERR_CODE_ERR_EXEC_GEN_CERT_ERROR = "ERR-Exec-Gen-Cert-error"
    RMT_ERR_CODE_ERR_EXEC_GET_CA_CERT_ERROR = "ERR-Exec-Get-CA-Cert-error"
    RMT_ERR_CODE_ERR_FILTER_ILLEGAL_FORMAT = "ERR-FILTER-illegal-format"
    RMT_ERR_CODE_ERR_FSM_NO_SUCH_STATE = "ERR-FSM-no-such-state"
    RMT_ERR_CODE_ERR_GET_CA_CERT_ERROR = "ERR-Get-CA-Cert-error"
    RMT_ERR_CODE_ERR_GET_CERT_ERROR = "ERR-Get-Cert-error"
    RMT_ERR_CODE_ERR_GET_OUT_DIGET_MESSAGE_ERROR = "ERR-Get-Out-Diget-Message-error"
    RMT_ERR_CODE_ERR_HTTP_REQUEST_ERROR = "ERR-HTTP-Request-error"
    RMT_ERR_CODE_ERR_HTTP_SET_ERROR = "ERR-HTTP-set-error"
    RMT_ERR_CODE_ERR_HTTPS_SET_ERROR = "ERR-HTTPS-set-error"
    RMT_ERR_CODE_ERR_IPV6_ADDR_CONFIGURED = "ERR-Ipv6-addr-configured"
    RMT_ERR_CODE_ERR_MO_CONFIG_CHILD_OBJECT_CANT_BE_CONFIGURED = "ERR-MO-CONFIG-child-object-cant-be-configured"
    RMT_ERR_CODE_ERR_MO_META_NO_SUCH_OBJECT_CLASS = "ERR-MO-META-no-such-object-class"
    RMT_ERR_CODE_ERR_MO_PROPERTY_NO_SUCH_PROPERTY = "ERR-MO-PROPERTY-no-such-property"
    RMT_ERR_CODE_ERR_MO_PROPERTY_VALUE_OUT_OF_RANGE = "ERR-MO-PROPERTY-value-out-of-range"
    RMT_ERR_CODE_ERR_MO_ACCESS_DENIED = "ERR-MO-access-denied"
    RMT_ERR_CODE_ERR_MO_DELETION_RULE_VIOLATION = "ERR-MO-deletion-rule-violation"
    RMT_ERR_CODE_ERR_MO_DUPLICATE_OBJECT = "ERR-MO-duplicate-object"
    RMT_ERR_CODE_ERR_MO_ILLEGAL_CONTAINMENT = "ERR-MO-illegal-containment"
    RMT_ERR_CODE_ERR_MO_ILLEGAL_CREATION = "ERR-MO-illegal-creation"
    RMT_ERR_CODE_ERR_MO_ILLEGAL_ITERATOR_STATE = "ERR-MO-illegal-iterator-state"
    RMT_ERR_CODE_ERR_MO_ILLEGAL_OBJECT_LIFECYCLE_TRANSITION = "ERR-MO-illegal-object-lifecycle-transition"
    RMT_ERR_CODE_ERR_MO_NAMING_RULE_VIOLATION = "ERR-MO-naming-rule-violation"
    RMT_ERR_CODE_ERR_MO_OBJECT_NOT_FOUND = "ERR-MO-object-not-found"
    RMT_ERR_CODE_ERR_MO_RESOURCE_ALLOCATION = "ERR-MO-resource-allocation"
    RMT_ERR_CODE_ERR_NTP_DELETE_ERROR = "ERR-NTP-delete-error"
    RMT_ERR_CODE_ERR_NTP_GET_ERROR = "ERR-NTP-get-error"
    RMT_ERR_CODE_ERR_NTP_SET_ERROR = "ERR-NTP-set-error"
    RMT_ERR_CODE_ERR_POLICY_RESOLUTION_IN_PROGRESS = "ERR-Policy-resolution-in-progress"
    RMT_ERR_CODE_ERR_TOKEN_REQUEST_DENIED = "ERR-TOKEN-request-denied"
    RMT_ERR_CODE_ERR_UPDATE_VM_IP_MASK_GATEWAY_ERROR = "ERR-Update-VM-IP-Mask-Gateway-error"
    RMT_ERR_CODE_ERR_AAA_CONFIG_MODIFY_ERROR = "ERR-aaa-config-modify-error"
    RMT_ERR_CODE_ERR_ACCT_REALM_SET_ERROR = "ERR-acct-realm-set-error"
    RMT_ERR_CODE_ERR_ADMIN_PASSWD_SET = "ERR-admin-passwd-set"
    RMT_ERR_CODE_ERR_AUTH_REALM_SET_ERROR = "ERR-auth-realm-set-error"
    RMT_ERR_CODE_ERR_AUTHENTICATION = "ERR-authentication"
    RMT_ERR_CODE_ERR_AUTHORIZATION_REQUIRED = "ERR-authorization-required"
    RMT_ERR_CODE_ERR_CREATE_CHASSISPACK_UNDER_DG = "ERR-create-chassispack-under-dg"
    RMT_ERR_CODE_ERR_CREATE_HFP_UNDER_DG = "ERR-create-hfp-under-dg"
    RMT_ERR_CODE_ERR_CREATE_KEYRING = "ERR-create-keyring"
    RMT_ERR_CODE_ERR_CREATE_LOCALE = "ERR-create-locale"
    RMT_ERR_CODE_ERR_CREATE_ROLE = "ERR-create-role"
    RMT_ERR_CODE_ERR_CREATE_USER = "ERR-create-user"
    RMT_ERR_CODE_ERR_DELETE_LOCALE = "ERR-delete-locale"
    RMT_ERR_CODE_ERR_DELETE_ROLE = "ERR-delete-role"
    RMT_ERR_CODE_ERR_DELETE_SESSION = "ERR-delete-session"
    RMT_ERR_CODE_ERR_DELETE_USER = "ERR-delete-user"
    RMT_ERR_CODE_ERR_ESTIMATE_IMPACT_ON_RECONNECT = "ERR-estimate-impact-on-reconnect"
    RMT_ERR_CODE_ERR_GET_MAX_HTTP_USER_SESSIONS = "ERR-get-max-http-user-sessions"
    RMT_ERR_CODE_ERR_HTTP_INITIALIZING = "ERR-http-initializing"
    RMT_ERR_CODE_ERR_INTERNAL_ERROR = "ERR-internal-error"
    RMT_ERR_CODE_ERR_LDAP_DELETE_ERROR = "ERR-ldap-delete-error"
    RMT_ERR_CODE_ERR_LDAP_GET_ERROR = "ERR-ldap-get-error"
    RMT_ERR_CODE_ERR_LDAP_GROUP_MODIFY_ERROR = "ERR-ldap-group-modify-error"
    RMT_ERR_CODE_ERR_LDAP_GROUP_SET_ERROR = "ERR-ldap-group-set-error"
    RMT_ERR_CODE_ERR_LDAP_SET_ERROR = "ERR-ldap-set-error"
    RMT_ERR_CODE_ERR_LOCALE_SET_ERROR = "ERR-locale-set-error"
    RMT_ERR_CODE_ERR_MAX_USERID_SESSIONS_REACHED = "ERR-max-userid-sessions-reached"
    RMT_ERR_CODE_ERR_MODIFY_LOCALE = "ERR-modify-locale"
    RMT_ERR_CODE_ERR_MODIFY_ROLE = "ERR-modify-role"
    RMT_ERR_CODE_ERR_MODIFY_USER = "ERR-modify-user"
    RMT_ERR_CODE_ERR_MODIFY_USER_LOCALE = "ERR-modify-user-locale"
    RMT_ERR_CODE_ERR_MODIFY_USER_ROLE = "ERR-modify-user-role"
    RMT_ERR_CODE_ERR_NFS_DOWN = "ERR-nfs-down"
    RMT_ERR_CODE_ERR_PROVIDER_GROUP_MODIFY_ERROR = "ERR-provider-group-modify-error"
    RMT_ERR_CODE_ERR_PROVIDER_GROUP_SET_ERROR = "ERR-provider-group-set-error"
    RMT_ERR_CODE_ERR_RADIUS_GLOBAL_SET_ERROR = "ERR-radius-global-set-error"
    RMT_ERR_CODE_ERR_RADIUS_GROUP_SET_ERROR = "ERR-radius-group-set-error"
    RMT_ERR_CODE_ERR_RADIUS_SET_ERROR = "ERR-radius-set-error"
    RMT_ERR_CODE_ERR_ROLE_SET_ERROR = "ERR-role-set-error"
    RMT_ERR_CODE_ERR_SERVICE_NOT_READY = "ERR-service-not-ready"
    RMT_ERR_CODE_ERR_SESSION_CACHE_FULL = "ERR-session-cache-full"
    RMT_ERR_CODE_ERR_SESSION_NOT_FOUND = "ERR-session-not-found"
    RMT_ERR_CODE_ERR_SET_PASSWORD_STRENGTH_CHECK = "ERR-set-password-strength-check"
    RMT_ERR_CODE_ERR_TACACS_ENABLE_ERROR = "ERR-tacacs-enable-error"
    RMT_ERR_CODE_ERR_TACACS_GLOBAL_SET_ERROR = "ERR-tacacs-global-set-error"
    RMT_ERR_CODE_ERR_TACACS_GROUP_SET_ERROR = "ERR-tacacs-group-set-error"
    RMT_ERR_CODE_ERR_TACACS_SET_ERROR = "ERR-tacacs-set-error"
    RMT_ERR_CODE_ERR_TIMEZONE_SET_ERROR = "ERR-timezone-set-error"
    RMT_ERR_CODE_ERR_USER_ACCOUNT_EXPIRED = "ERR-user-account-expired"
    RMT_ERR_CODE_ERR_USER_SET_ERROR = "ERR-user-set-error"
    RMT_ERR_CODE_NONE = "none"


class FabricFcZoneProfileFsm(ManagedObject):
    """This is FabricFcZoneProfileFsm class."""

    consts = FabricFcZoneProfileFsmConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricFcZoneProfileFsm", "fabricFcZoneProfileFsm", "fsm", VersionMeta.Version201b, "OutputOnly", 0xf, [], [""], [u'fabricFcZoneProfile'], [u'fabricFcZoneProfileFsmStage'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "completion_time": MoPropertyMeta("completion_time", "completionTime", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
        "current_fsm": MoPropertyMeta("current_fsm", "currentFsm", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Configure", "nop"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fsm_instance_id": MoPropertyMeta("fsm_instance_id", "fsmInstanceId", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []), 
        "progress": MoPropertyMeta("progress", "progress", "byte", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-100"]), 
        "rmt_err_code": MoPropertyMeta("rmt_err_code", "rmtErrCode", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-error", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Digest-Validation-error", "ERR-Exec-Gen-Cert-error", "ERR-Exec-Get-CA-Cert-error", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-Get-CA-Cert-error", "ERR-Get-Cert-error", "ERR-Get-Out-Diget-Message-error", "ERR-HTTP-Request-error", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-Ipv6-addr-configured", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-Policy-resolution-in-progress", "ERR-TOKEN-request-denied", "ERR-Update-VM-IP-Mask-Gateway-error", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-create-chassispack-under-dg", "ERR-create-hfp-under-dg", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-estimate-impact-on-reconnect", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-nfs-down", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-role-set-error", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-password-strength-check", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-set-error", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "none"], ["0-4294967295"]), 
        "rmt_err_descr": MoPropertyMeta("rmt_err_descr", "rmtErrDescr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rmt_rslt": MoPropertyMeta("rmt_rslt", "rmtRslt", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "completionTime": "completion_time", 
        "currentFsm": "current_fsm", 
        "descr": "descr", 
        "dn": "dn", 
        "fsmInstanceId": "fsm_instance_id", 
        "fsmStatus": "fsm_status", 
        "progress": "progress", 
        "rmtErrCode": "rmt_err_code", 
        "rmtErrDescr": "rmt_err_descr", 
        "rmtRslt": "rmt_rslt", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.completion_time = None
        self.current_fsm = None
        self.descr = None
        self.fsm_instance_id = None
        self.fsm_status = None
        self.progress = None
        self.rmt_err_code = None
        self.rmt_err_descr = None
        self.rmt_rslt = None
        self.status = None

        ManagedObject.__init__(self, "FabricFcZoneProfileFsm", parent_mo_or_dn, **kwargs)

