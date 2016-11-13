"""This module contains the meta information of ConfigFindPolicyUsage ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigFindPolicyUsage", "configFindPolicyUsage", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_policy_dn": MethodPropertyMeta("InPolicyDn", "inPolicyDn", "ReferenceObject", "Version142b", "Input", False),
    "in_policy_usage": MethodPropertyMeta("InPolicyUsage", "inPolicyUsage", "Xs:string", "Version142b", "Input", False),
    "in_return_configs": MethodPropertyMeta("InReturnConfigs", "inReturnConfigs", "Xs:string", "Version142b", "Input", False),
    "out_associated": MethodPropertyMeta("OutAssociated", "outAssociated", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_config_error": MethodPropertyMeta("OutConfigError", "outConfigError", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_consumers": MethodPropertyMeta("OutConsumers", "outConsumers", "ConfigSet", "Version142b", "Output", True),
    "out_count": MethodPropertyMeta("OutCount", "outCount", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_running": MethodPropertyMeta("OutRunning", "outRunning", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_service_profiles": MethodPropertyMeta("OutServiceProfiles", "outServiceProfiles", "ConfigSet", "Version142b", "Output", True),
    "out_unassociated": MethodPropertyMeta("OutUnassociated", "outUnassociated", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inPolicyDn": "in_policy_dn",
    "inPolicyUsage": "in_policy_usage",
    "inReturnConfigs": "in_return_configs",
    "outAssociated": "out_associated",
    "outConfigError": "out_config_error",
    "outConsumers": "out_consumers",
    "outCount": "out_count",
    "outRunning": "out_running",
    "outServiceProfiles": "out_service_profiles",
    "outUnassociated": "out_unassociated",
}

