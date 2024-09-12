"""This module contains the general information for FirmwareDistributable ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareDistributableConsts():
    ADMIN_DNLD_STATUS_IDLE = "idle"
    ADMIN_DNLD_STATUS_RESTART = "restart"
    ADMIN_STATE_ACTIVE = "active"
    ADMIN_STATE_DELETED = "deleted"
    COMPLETENESS_COMPLETE = "complete"
    COMPLETENESS_PARTIAL = "partial"
    FSM_PREV_DELETE_BEGIN = "DeleteBegin"
    FSM_PREV_DELETE_FAIL = "DeleteFail"
    FSM_PREV_DELETE_LOCAL = "DeleteLocal"
    FSM_PREV_DELETE_SUCCESS = "DeleteSuccess"
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
    FSM_STATUS_DELETE_BEGIN = "DeleteBegin"
    FSM_STATUS_DELETE_FAIL = "DeleteFail"
    FSM_STATUS_DELETE_LOCAL = "DeleteLocal"
    FSM_STATUS_DELETE_SUCCESS = "DeleteSuccess"
    FSM_STATUS_NOP = "nop"
    INT_ID_NONE = "none"
    IS_HIDDEN_FALSE = "false"
    IS_HIDDEN_NO = "no"
    IS_HIDDEN_TRUE = "true"
    IS_HIDDEN_YES = "yes"
    OPER_DNLD_STATUS_DELETING = "deleting"
    OPER_DNLD_STATUS_DOWNLOADED = "downloaded"
    OPER_DNLD_STATUS_DOWNLOADING = "downloading"
    OPER_DNLD_STATUS_EULA_ACCEPTANCE_REQUIRED = "eula-acceptance-required"
    OPER_DNLD_STATUS_FAILED = "failed"
    OPER_DNLD_STATUS_NOT_DOWNLOADED = "not-downloaded"
    OPER_DNLD_STATUS_TRIGGERED = "triggered"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    SOURCE_CISCO = "Cisco"
    SOURCE_LOCAL = "local"
    TRANSFER_STATE_DOWNLOADED = "downloaded"
    TRANSFER_STATE_DOWNLOADING = "downloading"
    TRANSFER_STATE_EULA_ACCEPTANCE_REQUIRED = "eula-acceptance-required"
    TRANSFER_STATE_FAILED = "failed"
    TRANSFER_STATE_INIT = "init"
    TYPE_B_SERIES_BUNDLE = "b-series-bundle"
    TYPE_C_SERIES_BUNDLE = "c-series-bundle"
    TYPE_CATALOG = "catalog"
    TYPE_CHASSIS_BUNDLE = "chassis-bundle"
    TYPE_FULL_BUNDLE = "full-bundle"
    TYPE_IMAGE = "image"
    TYPE_INFRASTRUCTURE_BUNDLE = "infrastructure-bundle"
    TYPE_M_SERIES_BUNDLE = "m-series-bundle"
    TYPE_PROVIDER_BUNDLE = "provider-bundle"
    TYPE_S_SERIES_BUNDLE = "s-series-bundle"
    TYPE_SERVICE_PACK_BUNDLE = "service-pack-bundle"
    TYPE_UNKNOWN = "unknown"


class FirmwareDistributable(ManagedObject):
    """This is FirmwareDistributable class."""

    consts = FirmwareDistributableConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FirmwareDistributable", "firmwareDistributable", "distrib-[name]", VersionMeta.Version101a, "InputOutput", 0x1ff, [], ["admin"], ['firmwareCatalogue', 'firmwareRemoteCatalogue'], ['eventInst', 'faultInst', 'firmwareDistImage', 'firmwareDistributableFsm', 'firmwareDistributableFsmTask'], ["Get", "Set"])

    prop_meta = {
        "admin_dnld_status": MoPropertyMeta("admin_dnld_status", "adminDnldStatus", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["idle", "restart"], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["active", "deleted"], []), 
        "bsd_checksum": MoPropertyMeta("bsd_checksum", "bsdChecksum", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "completeness": MoPropertyMeta("completeness", "completeness", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["complete", "partial"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "file_description": MoPropertyMeta("file_description", "fileDescription", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["DeleteBegin", "DeleteFail", "DeleteLocal", "DeleteSuccess", "nop"], []), 
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]), 
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-error", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Digest-Validation-error", "ERR-Exec-Gen-Cert-error", "ERR-Exec-Get-CA-Cert-error", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-Get-CA-Cert-error", "ERR-Get-Cert-error", "ERR-Get-Out-Diget-Message-error", "ERR-HTTP-Request-error", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-Ipv6-addr-configured", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-Policy-resolution-in-progress", "ERR-TOKEN-request-denied", "ERR-Update-VM-IP-Mask-Gateway-error", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-create-chassispack-under-dg", "ERR-create-hfp-under-dg", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-estimate-impact-on-reconnect", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-nfs-down", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-role-set-error", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-password-strength-check", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-set-error", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "none"], ["0-4294967295"]), 
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []), 
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["DeleteBegin", "DeleteFail", "DeleteLocal", "DeleteSuccess", "nop"], []), 
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "image_guid": MoPropertyMeta("image_guid", "imageGuid", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "image_page_index": MoPropertyMeta("image_page_index", "imagePageIndex", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "image_size": MoPropertyMeta("image_size", "imageSize", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "inv_tag": MoPropertyMeta("inv_tag", "invTag", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "ip_url": MoPropertyMeta("ip_url", "ipUrl", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "is_hidden": MoPropertyMeta("is_hidden", "isHidden", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []), 
        "md5_checksum": MoPropertyMeta("md5_checksum", "md5Checksum", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "mdf_id": MoPropertyMeta("mdf_id", "mdfId", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "meta_trans_id": MoPropertyMeta("meta_trans_id", "metaTransId", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x40, 1, 128, None, [], []), 
        "oauth_create_ts": MoPropertyMeta("oauth_create_ts", "oauthCreateTs", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "oauth_token_expiry": MoPropertyMeta("oauth_token_expiry", "oauthTokenExpiry", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oauth_token_type": MoPropertyMeta("oauth_token_type", "oauthTokenType", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oauth_token_val": MoPropertyMeta("oauth_token_val", "oauthTokenVal", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oper_dnld_status": MoPropertyMeta("oper_dnld_status", "operDnldStatus", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deleting", "downloaded", "downloading", "eula-acceptance-required", "failed", "not-downloaded", "triggered"], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "software_type_id": MoPropertyMeta("software_type_id", "softwareTypeId", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "source": MoPropertyMeta("source", "source", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Cisco", "local"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "transfer_state": MoPropertyMeta("transfer_state", "transferState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["downloaded", "downloading", "eula-acceptance-required", "failed", "init"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["b-series-bundle", "c-series-bundle", "catalog", "chassis-bundle", "full-bundle", "image", "infrastructure-bundle", "m-series-bundle", "provider-bundle", "s-series-bundle", "service-pack-bundle", "unknown"], []), 
        "url": MoPropertyMeta("url", "url", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminDnldStatus": "admin_dnld_status", 
        "adminState": "admin_state", 
        "bsdChecksum": "bsd_checksum", 
        "childAction": "child_action", 
        "completeness": "completeness", 
        "descr": "descr", 
        "dn": "dn", 
        "fileDescription": "file_description", 
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
        "imageGuid": "image_guid", 
        "imagePageIndex": "image_page_index", 
        "imageSize": "image_size", 
        "intId": "int_id", 
        "invTag": "inv_tag", 
        "ipUrl": "ip_url", 
        "isHidden": "is_hidden", 
        "md5Checksum": "md5_checksum", 
        "mdfId": "mdf_id", 
        "metaTransId": "meta_trans_id", 
        "model": "model", 
        "name": "name", 
        "oauthCreateTs": "oauth_create_ts", 
        "oauthTokenExpiry": "oauth_token_expiry", 
        "oauthTokenType": "oauth_token_type", 
        "oauthTokenVal": "oauth_token_val", 
        "operDnldStatus": "oper_dnld_status", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "softwareTypeId": "software_type_id", 
        "source": "source", 
        "status": "status", 
        "transferState": "transfer_state", 
        "type": "type", 
        "url": "url", 
        "vendor": "vendor", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_dnld_status = None
        self.admin_state = None
        self.bsd_checksum = None
        self.child_action = None
        self.completeness = None
        self.descr = None
        self.file_description = None
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
        self.image_guid = None
        self.image_page_index = None
        self.image_size = None
        self.int_id = None
        self.inv_tag = None
        self.ip_url = None
        self.is_hidden = None
        self.md5_checksum = None
        self.mdf_id = None
        self.meta_trans_id = None
        self.model = None
        self.oauth_create_ts = None
        self.oauth_token_expiry = None
        self.oauth_token_type = None
        self.oauth_token_val = None
        self.oper_dnld_status = None
        self.policy_level = None
        self.policy_owner = None
        self.software_type_id = None
        self.source = None
        self.status = None
        self.transfer_state = None
        self.type = None
        self.url = None
        self.vendor = None
        self.version = None

        ManagedObject.__init__(self, "FirmwareDistributable", parent_mo_or_dn, **kwargs)

