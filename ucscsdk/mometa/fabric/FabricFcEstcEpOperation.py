"""This module contains the general information for FabricFcEstcEpOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricFcEstcEpOperationConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    ADMIN_STATE_REMOTE_TRIGGER = "remoteTrigger"
    ADMIN_STATE_REMOVE = "remove"
    FILL_PATTERN_ARBFF = "arbff"
    FILL_PATTERN_IDLE = "idle"
    FSM_PREV_FIPORT_BEGIN = "FIPortBegin"
    FSM_PREV_FIPORT_CLEAN_UP = "FIPortCleanUp"
    FSM_PREV_FIPORT_FAIL = "FIPortFail"
    FSM_PREV_FIPORT_PUSH_POLICIES = "FIPortPushPolicies"
    FSM_PREV_FIPORT_PUSH_VXAN = "FIPortPushVxan"
    FSM_PREV_FIPORT_ROLE_CONFIG = "FIPortRoleConfig"
    FSM_PREV_FIPORT_SUCCESS = "FIPortSuccess"
    FSM_PREV_FIPORT_VXAN_CONFIG = "FIPortVxanConfig"
    FSM_PREV_FIPORT_WAIT = "FIPortWait"
    FSM_PREV_FIPORT_WAIT_FOR_POLICIES = "FIPortWaitForPolicies"
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
    FSM_STATUS_FIPORT_BEGIN = "FIPortBegin"
    FSM_STATUS_FIPORT_CLEAN_UP = "FIPortCleanUp"
    FSM_STATUS_FIPORT_FAIL = "FIPortFail"
    FSM_STATUS_FIPORT_PUSH_POLICIES = "FIPortPushPolicies"
    FSM_STATUS_FIPORT_PUSH_VXAN = "FIPortPushVxan"
    FSM_STATUS_FIPORT_ROLE_CONFIG = "FIPortRoleConfig"
    FSM_STATUS_FIPORT_SUCCESS = "FIPortSuccess"
    FSM_STATUS_FIPORT_VXAN_CONFIG = "FIPortVxanConfig"
    FSM_STATUS_FIPORT_WAIT = "FIPortWait"
    FSM_STATUS_FIPORT_WAIT_FOR_POLICIES = "FIPortWaitForPolicies"
    FSM_STATUS_NOP = "nop"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class FabricFcEstcEpOperation(ManagedObject):
    """This is FabricFcEstcEpOperation class."""

    consts = FabricFcEstcEpOperationConsts()
    naming_props = set([u'slotId', u'portId'])

    mo_meta = MoMeta("FabricFcEstcEpOperation", "fabricFcEstcEpOperation", "remoper-phys-fc-slot-[slot_id]-port-[port_id]", VersionMeta.Version141a, "InputOutput", 0x7ff, [], ["admin", "ext-san-config", "ext-san-policy"], [u'fabricFcEstc'], [u'eventInst', u'fabricFIPortOperationFsm', u'fabricFIPortOperationFsmTask', u'fabricFcEstcEpOperationFsm', u'fabricFcMonSrcEpOperation', u'fabricFcPortOperationFsm', u'faultInst', u'messageEp', u'vnicFc', u'vnicMonSesFc'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled", "remoteTrigger", "remove"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "fill_pattern": MoPropertyMeta("fill_pattern", "fillPattern", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["arbff", "idle"], []), 
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, ["FIPortBegin", "FIPortCleanUp", "FIPortFail", "FIPortPushPolicies", "FIPortPushVxan", "FIPortRoleConfig", "FIPortSuccess", "FIPortVxanConfig", "FIPortWait", "FIPortWaitForPolicies", "nop"], []), 
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]), 
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-error", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Digest-Validation-error", "ERR-Exec-Gen-Cert-error", "ERR-Exec-Get-CA-Cert-error", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-Get-CA-Cert-error", "ERR-Get-Cert-error", "ERR-Get-Out-Diget-Message-error", "ERR-HTTP-Request-error", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-Ipv6-addr-configured", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-Policy-resolution-in-progress", "ERR-TOKEN-request-denied", "ERR-Update-VM-IP-Mask-Gateway-error", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-create-chassispack-under-dg", "ERR-create-hfp-under-dg", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-estimate-impact-on-reconnect", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-nfs-down", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-role-set-error", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-password-strength-check", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-set-error", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "none"], ["0-4294967295"]), 
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []), 
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, ["FIPortBegin", "FIPortCleanUp", "FIPortFail", "FIPortPushPolicies", "FIPortPushVxan", "FIPortRoleConfig", "FIPortSuccess", "FIPortVxanConfig", "FIPortWait", "FIPortWaitForPolicies", "nop"], []), 
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-108"]), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x40, None, None, None, [], ["1-5"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "vsan_name": MoPropertyMeta("vsan_name", "vsanName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "fillPattern": "fill_pattern", 
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
        "lastModified": "last_modified", 
        "portId": "port_id", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "rn": "rn", 
        "slotId": "slot_id", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
        "usrLbl": "usr_lbl", 
        "vsanName": "vsan_name", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, port_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.port_id = port_id
        self.admin_state = None
        self.child_action = None
        self.ep_dn = None
        self.fill_pattern = None
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
        self.last_modified = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None
        self.usr_lbl = None
        self.vsan_name = None

        ManagedObject.__init__(self, "FabricFcEstcEpOperation", parent_mo_or_dn, **kwargs)

