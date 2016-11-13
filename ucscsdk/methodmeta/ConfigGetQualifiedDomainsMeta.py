"""This module contains the meta information of ConfigGetQualifiedDomains ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigGetQualifiedDomains", "configGetQualifiedDomains", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_qual_dn": MethodPropertyMeta("InQualDn", "inQualDn", "ReferenceObject", "Version142b", "Input", False),
    "in_return_domain_configs": MethodPropertyMeta("InReturnDomainConfigs", "inReturnDomainConfigs", "Xs:string", "Version142b", "Input", False),
    "in_return_policy_configs": MethodPropertyMeta("InReturnPolicyConfigs", "inReturnPolicyConfigs", "Xs:string", "Version142b", "Input", False),
    "out_domains": MethodPropertyMeta("OutDomains", "outDomains", "ConfigSet", "Version142b", "Output", True),
    "out_policies": MethodPropertyMeta("OutPolicies", "outPolicies", "ConfigSet", "Version142b", "Output", True),
    "out_total_domains": MethodPropertyMeta("OutTotalDomains", "outTotalDomains", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_total_policies": MethodPropertyMeta("OutTotalPolicies", "outTotalPolicies", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inQualDn": "in_qual_dn",
    "inReturnDomainConfigs": "in_return_domain_configs",
    "inReturnPolicyConfigs": "in_return_policy_configs",
    "outDomains": "out_domains",
    "outPolicies": "out_policies",
    "outTotalDomains": "out_total_domains",
    "outTotalPolicies": "out_total_policies",
}

