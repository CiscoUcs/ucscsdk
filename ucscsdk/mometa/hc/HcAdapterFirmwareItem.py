"""This module contains the general information for HcAdapterFirmwareItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class HcAdapterFirmwareItemConsts():
    ITEM_ERROR_CODE_ADAPTER_FW_VERSION_NOT_FOUND = "adapter-fw-version-not-found"
    ITEM_ERROR_CODE_ADAPTER_NOT_TAGGED = "adapter-not-tagged"
    ITEM_ERROR_CODE_DN_NOT_SPECIFIED = "dn-not-specified"
    ITEM_ERROR_CODE_DN_NOT_SUPPORTED = "dn-not-supported"
    ITEM_ERROR_CODE_INVALID_INPUT = "invalid-input"
    ITEM_ERROR_CODE_MISSING_DATA_IN_CATALOG = "missing-data-in-catalog"
    ITEM_ERROR_CODE_NO_MATCHING_SERVERS_FOUND = "no-matching-servers-found"
    ITEM_ERROR_CODE_NONE = "none"
    ITEM_ERROR_CODE_OS_NOT_TAGGED = "os-not-tagged"
    ITEM_ERROR_CODE_RETRY = "retry"
    ITEM_ERROR_CODE_TARGET_FW_VERSION_INVALID = "target-fw-version-invalid"
    ITEM_ERROR_CODE_TARGET_FW_VERSION_NOT_SPECIFIED = "target-fw-version-not-specified"
    ITEM_ERROR_CODE_UCS_FW_VERSION_NOT_FOUND = "ucs-fw-version-not-found"
    ITEM_STATUS_CANNOT_DETERMINE = "cannot-determine"
    ITEM_STATUS_NOT_APPLICABLE = "not-applicable"
    ITEM_STATUS_NOT_SUPPORTED = "not-supported"
    ITEM_STATUS_OK = "ok"


class HcAdapterFirmwareItem(ManagedObject):
    """This is HcAdapterFirmwareItem class."""

    consts = HcAdapterFirmwareItemConsts()
    naming_props = set(['itemId'])

    mo_meta = MoMeta("HcAdapterFirmwareItem", "hcAdapterFirmwareItem", "adapter-firmware-[item_id]", VersionMeta.Version151a, "InputOutput", 0x1fff, [], ["admin"], ['hcServerComponent'], ['hcItemNote', 'hcSupportedAdapterFirmwareItem'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "item_error_code": MoPropertyMeta("item_error_code", "itemErrorCode", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["adapter-fw-version-not-found", "adapter-not-tagged", "dn-not-specified", "dn-not-supported", "invalid-input", "missing-data-in-catalog", "no-matching-servers-found", "none", "os-not-tagged", "retry", "target-fw-version-invalid", "target-fw-version-not-specified", "ucs-fw-version-not-found"], []), 
        "item_id": MoPropertyMeta("item_id", "itemId", "ulong", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "item_note": MoPropertyMeta("item_note", "itemNote", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []), 
        "item_ref_dn": MoPropertyMeta("item_ref_dn", "itemRefDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, 0, 256, None, [], []), 
        "item_ref_id": MoPropertyMeta("item_ref_id", "itemRefId", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, None, [], []), 
        "item_ref_model": MoPropertyMeta("item_ref_model", "itemRefModel", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []), 
        "item_status": MoPropertyMeta("item_status", "itemStatus", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["cannot-determine", "not-applicable", "not-supported", "ok"], []), 
        "item_vendor": MoPropertyMeta("item_vendor", "itemVendor", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], []), 
        "item_version": MoPropertyMeta("item_version", "itemVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "itemErrorCode": "item_error_code", 
        "itemId": "item_id", 
        "itemNote": "item_note", 
        "itemRefDn": "item_ref_dn", 
        "itemRefId": "item_ref_id", 
        "itemRefModel": "item_ref_model", 
        "itemStatus": "item_status", 
        "itemVendor": "item_vendor", 
        "itemVersion": "item_version", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, item_id, **kwargs):
        self._dirty_mask = 0
        self.item_id = item_id
        self.child_action = None
        self.item_error_code = None
        self.item_note = None
        self.item_ref_dn = None
        self.item_ref_id = None
        self.item_ref_model = None
        self.item_status = None
        self.item_vendor = None
        self.item_version = None
        self.status = None

        ManagedObject.__init__(self, "HcAdapterFirmwareItem", parent_mo_or_dn, **kwargs)

