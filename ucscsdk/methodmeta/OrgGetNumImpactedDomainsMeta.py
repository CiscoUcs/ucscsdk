"""This module contains the meta information of OrgGetNumImpactedDomains ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("OrgGetNumImpactedDomains", "orgGetNumImpactedDomains", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_config": MethodPropertyMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
    "in_domain_group_dn": MethodPropertyMeta("InDomainGroupDn", "inDomainGroupDn", "ReferenceObject", "Version142b", "Input", False),
    "in_dynamic": MethodPropertyMeta("InDynamic", "inDynamic", "Xs:string", "Version142b", "Input", False),
    "in_firmware_type": MethodPropertyMeta("InFirmwareType", "inFirmwareType", "Xs:string", "Version142b", "Input", False),
    "in_maint_tag": MethodPropertyMeta("InMaintTag", "inMaintTag", "Xs:string", "Version142b", "Input", False),
    "in_profile_name": MethodPropertyMeta("InProfileName", "inProfileName", "Xs:string", "Version142b", "Input", False),
    "out_num_domains_impacted": MethodPropertyMeta("OutNumDomainsImpacted", "outNumDomainsImpacted", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_num_domains_subscribed": MethodPropertyMeta("OutNumDomainsSubscribed", "outNumDomainsSubscribed", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_num_domains_unsubscribed": MethodPropertyMeta("OutNumDomainsUnsubscribed", "outNumDomainsUnsubscribed", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inConfig": "in_config",
    "inDomainGroupDn": "in_domain_group_dn",
    "inDynamic": "in_dynamic",
    "inFirmwareType": "in_firmware_type",
    "inMaintTag": "in_maint_tag",
    "inProfileName": "in_profile_name",
    "outNumDomainsImpacted": "out_num_domains_impacted",
    "outNumDomainsSubscribed": "out_num_domains_subscribed",
    "outNumDomainsUnsubscribed": "out_num_domains_unsubscribed",
}

