"""This module contains the meta information of ConfigGetPolicyDomainGroup ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigGetPolicyDomainGroup", "configGetPolicyDomainGroup", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_class_id": MethodPropertyMeta("InClassId", "inClassId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_domain_id": MethodPropertyMeta("InDomainId", "inDomainId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_policy_name": MethodPropertyMeta("InPolicyName", "inPolicyName", "Xs:string", "Version142b", "Input", False),
    "out_domain_groups": MethodPropertyMeta("OutDomainGroups", "outDomainGroups", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inClassId": "in_class_id",
    "inDomainId": "in_domain_id",
    "inPolicyName": "in_policy_name",
    "outDomainGroups": "out_domain_groups",
}

