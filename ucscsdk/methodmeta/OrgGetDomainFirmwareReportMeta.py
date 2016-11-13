"""This module contains the meta information of OrgGetDomainFirmwareReport ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("OrgGetDomainFirmwareReport", "orgGetDomainFirmwareReport", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_domain_group_dn": MethodPropertyMeta("InDomainGroupDn", "inDomainGroupDn", "ReferenceObject", "Version142b", "Input", False),
    "in_domain_list": MethodPropertyMeta("InDomainList", "inDomainList", "ConfigSet", "Version142b", "Input", True),
    "in_firmware_type": MethodPropertyMeta("InFirmwareType", "inFirmwareType", "Xs:string", "Version142b", "Input", False),
    "in_maint_tag": MethodPropertyMeta("InMaintTag", "inMaintTag", "Xs:string", "Version142b", "Input", False),
    "out_firmware_oper_state": MethodPropertyMeta("OutFirmwareOperState", "outFirmwareOperState", "Xs:string", "Version142b", "Output", False),
    "out_firmware_report_set": MethodPropertyMeta("OutFirmwareReportSet", "outFirmwareReportSet", "ConfigSet", "Version142b", "Output", True),
    "out_firmware_version_set": MethodPropertyMeta("OutFirmwareVersionSet", "outFirmwareVersionSet", "DnSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inDomainGroupDn": "in_domain_group_dn",
    "inDomainList": "in_domain_list",
    "inFirmwareType": "in_firmware_type",
    "inMaintTag": "in_maint_tag",
    "outFirmwareOperState": "out_firmware_oper_state",
    "outFirmwareReportSet": "out_firmware_report_set",
    "outFirmwareVersionSet": "out_firmware_version_set",
}

