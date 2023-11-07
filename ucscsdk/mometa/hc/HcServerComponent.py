"""This module contains the general information for HcServerComponent ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class HcServerComponentConsts():
    ERROR_CODE_ADAPTER_FW_VERSION_NOT_FOUND = "adapter-fw-version-not-found"
    ERROR_CODE_ADAPTER_NOT_TAGGED = "adapter-not-tagged"
    ERROR_CODE_DN_NOT_SPECIFIED = "dn-not-specified"
    ERROR_CODE_DN_NOT_SUPPORTED = "dn-not-supported"
    ERROR_CODE_INVALID_INPUT = "invalid-input"
    ERROR_CODE_MISSING_DATA_IN_CATALOG = "missing-data-in-catalog"
    ERROR_CODE_NO_MATCHING_SERVERS_FOUND = "no-matching-servers-found"
    ERROR_CODE_NONE = "none"
    ERROR_CODE_OS_NOT_TAGGED = "os-not-tagged"
    ERROR_CODE_RETRY = "retry"
    ERROR_CODE_TARGET_FW_VERSION_INVALID = "target-fw-version-invalid"
    ERROR_CODE_TARGET_FW_VERSION_NOT_SPECIFIED = "target-fw-version-not-specified"
    ERROR_CODE_UCS_FW_VERSION_NOT_FOUND = "ucs-fw-version-not-found"
    OVERALL_STATUS_CANNOT_DETERMINE = "cannot-determine"
    OVERALL_STATUS_NOT_APPLICABLE = "not-applicable"
    OVERALL_STATUS_NOT_SUPPORTED = "not-supported"
    OVERALL_STATUS_OK = "ok"


class HcServerComponent(ManagedObject):
    """This is HcServerComponent class."""

    consts = HcServerComponentConsts()
    naming_props = set(['componentId'])

    mo_meta = MoMeta("HcServerComponent", "hcServerComponent", "server-[component_id]", VersionMeta.Version151a, "InputOutput", 0xfffff, [], ["admin"], ['hcReport'], ['hcAdapterFirmwareItem', 'hcAdapterItem', 'hcDriverItem', 'hcOsItem'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "component_dn": MoPropertyMeta("component_dn", "componentDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, None, [], []), 
        "component_id": MoPropertyMeta("component_id", "componentId", "ulong", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "current_firmware": MoPropertyMeta("current_firmware", "currentFirmware", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, None, [], []), 
        "error_code": MoPropertyMeta("error_code", "errorCode", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["adapter-fw-version-not-found", "adapter-not-tagged", "dn-not-specified", "dn-not-supported", "invalid-input", "missing-data-in-catalog", "no-matching-servers-found", "none", "os-not-tagged", "retry", "target-fw-version-invalid", "target-fw-version-not-specified", "ucs-fw-version-not-found"], []), 
        "generated_time": MoPropertyMeta("generated_time", "generatedTime", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "host_firmware_policy_dn": MoPropertyMeta("host_firmware_policy_dn", "hostFirmwarePolicyDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []), 
        "overall_status": MoPropertyMeta("overall_status", "overallStatus", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["cannot-determine", "not-applicable", "not-supported", "ok"], []), 
        "profile_dn": MoPropertyMeta("profile_dn", "profileDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, None, [], []), 
        "report_dn": MoPropertyMeta("report_dn", "reportDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2000, 0, 256, None, [], []), 
        "report_name": MoPropertyMeta("report_name", "reportName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""[\-\.:_a-zA-Z0-9]{2,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8000, 0, 256, None, [], []), 
        "server_location_id": MoPropertyMeta("server_location_id", "serverLocationId", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10000, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "target_firmware": MoPropertyMeta("target_firmware", "targetFirmware", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40000, 0, 510, None, [], []), 
        "ucs_firmware": MoPropertyMeta("ucs_firmware", "ucsFirmware", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80000, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "componentDn": "component_dn", 
        "componentId": "component_id", 
        "currentFirmware": "current_firmware", 
        "dn": "dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainName": "domain_name", 
        "errorCode": "error_code", 
        "generatedTime": "generated_time", 
        "hostFirmwarePolicyDn": "host_firmware_policy_dn", 
        "model": "model", 
        "overallStatus": "overall_status", 
        "profileDn": "profile_dn", 
        "reportDn": "report_dn", 
        "reportName": "report_name", 
        "rn": "rn", 
        "serverLocationId": "server_location_id", 
        "status": "status", 
        "targetFirmware": "target_firmware", 
        "ucsFirmware": "ucs_firmware", 
    }

    def __init__(self, parent_mo_or_dn, component_id, **kwargs):
        self._dirty_mask = 0
        self.component_id = component_id
        self.child_action = None
        self.component_dn = None
        self.current_firmware = None
        self.domain_group_dn = None
        self.domain_name = None
        self.error_code = None
        self.generated_time = None
        self.host_firmware_policy_dn = None
        self.model = None
        self.overall_status = None
        self.profile_dn = None
        self.report_dn = None
        self.report_name = None
        self.server_location_id = None
        self.status = None
        self.target_firmware = None
        self.ucs_firmware = None

        ManagedObject.__init__(self, "HcServerComponent", parent_mo_or_dn, **kwargs)

