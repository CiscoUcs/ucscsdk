"""This module contains the general information for HcReport ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class HcReportConsts():
    ADMIN_STATE_DISABLE = "disable"
    ADMIN_STATE_ENABLE = "enable"
    CONDITION_ALL = "all"
    CONDITION_CANNOT_DETERMINE = "cannot-determine"
    CONDITION_NOT_SUPPORTED = "not-supported"
    CONDITION_OK = "ok"
    REPORT_ALL_FALSE = "false"
    REPORT_ALL_NO = "no"
    REPORT_ALL_TRUE = "true"
    REPORT_ALL_YES = "yes"
    REPORT_ERROR_CODE_ADAPTER_FW_VERSION_NOT_FOUND = "adapter-fw-version-not-found"
    REPORT_ERROR_CODE_ADAPTER_NOT_TAGGED = "adapter-not-tagged"
    REPORT_ERROR_CODE_DN_NOT_SPECIFIED = "dn-not-specified"
    REPORT_ERROR_CODE_DN_NOT_SUPPORTED = "dn-not-supported"
    REPORT_ERROR_CODE_INVALID_INPUT = "invalid-input"
    REPORT_ERROR_CODE_MISSING_DATA_IN_CATALOG = "missing-data-in-catalog"
    REPORT_ERROR_CODE_NO_MATCHING_SERVERS_FOUND = "no-matching-servers-found"
    REPORT_ERROR_CODE_NONE = "none"
    REPORT_ERROR_CODE_OS_NOT_TAGGED = "os-not-tagged"
    REPORT_ERROR_CODE_RETRY = "retry"
    REPORT_ERROR_CODE_TARGET_FW_VERSION_INVALID = "target-fw-version-invalid"
    REPORT_ERROR_CODE_TARGET_FW_VERSION_NOT_SPECIFIED = "target-fw-version-not-specified"
    REPORT_ERROR_CODE_UCS_FW_VERSION_NOT_FOUND = "ucs-fw-version-not-found"
    REPORT_GENERATION_STATUS_FAILED = "failed"
    REPORT_GENERATION_STATUS_IN_PROGRESS = "in-progress"
    REPORT_GENERATION_STATUS_NOT_STARTED = "not-started"
    REPORT_GENERATION_STATUS_SUCCESS = "success"


class HcReport(ManagedObject):
    """This is HcReport class."""

    consts = HcReportConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("HcReport", "hcReport", "report-[name]", VersionMeta.Version151a, "InputOutput", 0x7fffff, [], ["admin"], ['hcHolder'], ['hcScopeDn', 'hcServerComponent'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disable", "enable"], []), 
        "catalog_updated_date": MoPropertyMeta("catalog_updated_date", "catalogUpdatedDate", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []), 
        "catalog_version": MoPropertyMeta("catalog_version", "catalogVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "condition": MoPropertyMeta("condition", "condition", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["all", "cannot-determine", "not-supported", "ok"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "domain_group_scope_dn_cnt": MoPropertyMeta("domain_group_scope_dn_cnt", "domainGroupScopeDnCnt", "ulong", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []), 
        "domain_scope_dn_cnt": MoPropertyMeta("domain_scope_dn_cnt", "domainScopeDnCnt", "ulong", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []), 
        "equipment_scope_dn_cnt": MoPropertyMeta("equipment_scope_dn_cnt", "equipmentScopeDnCnt", "ulong", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{2,16}""", [], []), 
        "profile_scope_dn_cnt": MoPropertyMeta("profile_scope_dn_cnt", "profileScopeDnCnt", "ulong", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []), 
        "report_all": MoPropertyMeta("report_all", "reportAll", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["false", "no", "true", "yes"], []), 
        "report_completion_time": MoPropertyMeta("report_completion_time", "reportCompletionTime", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "report_error_code": MoPropertyMeta("report_error_code", "reportErrorCode", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["adapter-fw-version-not-found", "adapter-not-tagged", "dn-not-specified", "dn-not-supported", "invalid-input", "missing-data-in-catalog", "no-matching-servers-found", "none", "os-not-tagged", "retry", "target-fw-version-invalid", "target-fw-version-not-specified", "ucs-fw-version-not-found"], []), 
        "report_generation_status": MoPropertyMeta("report_generation_status", "reportGenerationStatus", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["failed", "in-progress", "not-started", "success"], []), 
        "report_start_time": MoPropertyMeta("report_start_time", "reportStartTime", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10000, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "target_blade_firmware_version": MoPropertyMeta("target_blade_firmware_version", "targetBladeFirmwareVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40000, 0, 510, None, [], []), 
        "target_modular_firmware_version": MoPropertyMeta("target_modular_firmware_version", "targetModularFirmwareVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80000, 0, 510, None, [], []), 
        "target_rack_firmware_version": MoPropertyMeta("target_rack_firmware_version", "targetRackFirmwareVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x100000, 0, 510, None, [], []), 
        "target_ucs_firmware_version": MoPropertyMeta("target_ucs_firmware_version", "targetUCSFirmwareVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x200000, 0, 510, None, [], []), 
        "total_components": MoPropertyMeta("total_components", "totalComponents", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x400000, None, None, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "catalogUpdatedDate": "catalog_updated_date", 
        "catalogVersion": "catalog_version", 
        "childAction": "child_action", 
        "condition": "condition", 
        "dn": "dn", 
        "domainGroupScopeDnCnt": "domain_group_scope_dn_cnt", 
        "domainScopeDnCnt": "domain_scope_dn_cnt", 
        "equipmentScopeDnCnt": "equipment_scope_dn_cnt", 
        "name": "name", 
        "profileScopeDnCnt": "profile_scope_dn_cnt", 
        "reportAll": "report_all", 
        "reportCompletionTime": "report_completion_time", 
        "reportErrorCode": "report_error_code", 
        "reportGenerationStatus": "report_generation_status", 
        "reportStartTime": "report_start_time", 
        "rn": "rn", 
        "status": "status", 
        "targetBladeFirmwareVersion": "target_blade_firmware_version", 
        "targetModularFirmwareVersion": "target_modular_firmware_version", 
        "targetRackFirmwareVersion": "target_rack_firmware_version", 
        "targetUCSFirmwareVersion": "target_ucs_firmware_version", 
        "totalComponents": "total_components", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.catalog_updated_date = None
        self.catalog_version = None
        self.child_action = None
        self.condition = None
        self.domain_group_scope_dn_cnt = None
        self.domain_scope_dn_cnt = None
        self.equipment_scope_dn_cnt = None
        self.profile_scope_dn_cnt = None
        self.report_all = None
        self.report_completion_time = None
        self.report_error_code = None
        self.report_generation_status = None
        self.report_start_time = None
        self.status = None
        self.target_blade_firmware_version = None
        self.target_modular_firmware_version = None
        self.target_rack_firmware_version = None
        self.target_ucs_firmware_version = None
        self.total_components = None

        ManagedObject.__init__(self, "HcReport", parent_mo_or_dn, **kwargs)

