"""This module contains the meta information of OrgGetImpactedDomains ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("OrgGetImpactedDomains", "orgGetImpactedDomains", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_config": MethodPropertyMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
    "in_domain_group_dn": MethodPropertyMeta("InDomainGroupDn", "inDomainGroupDn", "ReferenceObject", "Version142b", "Input", False),
    "in_domain_type": MethodPropertyMeta("InDomainType", "inDomainType", "Xs:string", "Version142b", "Input", False),
    "in_dynamic": MethodPropertyMeta("InDynamic", "inDynamic", "Xs:string", "Version142b", "Input", False),
    "in_firmware_type": MethodPropertyMeta("InFirmwareType", "inFirmwareType", "Xs:string", "Version142b", "Input", False),
    "in_maint_tag": MethodPropertyMeta("InMaintTag", "inMaintTag", "Xs:string", "Version142b", "Input", False),
    "in_profile_name": MethodPropertyMeta("InProfileName", "inProfileName", "Xs:string", "Version142b", "Input", False),
    "out_domains": MethodPropertyMeta("OutDomains", "outDomains", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inConfig": "in_config",
    "inDomainGroupDn": "in_domain_group_dn",
    "inDomainType": "in_domain_type",
    "inDynamic": "in_dynamic",
    "inFirmwareType": "in_firmware_type",
    "inMaintTag": "in_maint_tag",
    "inProfileName": "in_profile_name",
    "outDomains": "out_domains",
}

