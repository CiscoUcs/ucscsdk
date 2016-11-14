"""This module contains the meta information of ConfigRemoteSearch ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigRemoteSearch", "configRemoteSearch", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_context": MethodPropertyMeta("InContext", "inContext", "Xs:string", "Version142b", "Input", False),
    "in_domain_id": MethodPropertyMeta("InDomainId", "inDomainId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_domain_name": MethodPropertyMeta("InDomainName", "inDomainName", "Xs:string", "Version142b", "Input", False),
    "in_fetch_size": MethodPropertyMeta("InFetchSize", "inFetchSize", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_name": MethodPropertyMeta("InName", "inName", "Xs:string", "Version142b", "Input", False),
    "in_object_type": MethodPropertyMeta("InObjectType", "inObjectType", "Xs:string", "Version142b", "Input", False),
    "in_policy_owner": MethodPropertyMeta("InPolicyOwner", "inPolicyOwner", "Xs:string", "Version142b", "Input", False),
    "in_recursive_context": MethodPropertyMeta("InRecursiveContext", "inRecursiveContext", "Xs:string", "Version142b", "Input", False),
    "in_recursive_domain_group": MethodPropertyMeta("InRecursiveDomainGroup", "inRecursiveDomainGroup", "Xs:string", "Version142b", "Input", False),
    "in_search_domain_group": MethodPropertyMeta("InSearchDomainGroup", "inSearchDomainGroup", "Xs:string", "Version142b", "Input", False),
    "in_search_type": MethodPropertyMeta("InSearchType", "inSearchType", "Xs:string", "Version142b", "Input", False),
    "out_has_more_results": MethodPropertyMeta("OutHasMoreResults", "outHasMoreResults", "Xs:string", "Version142b", "Output", False),
    "out_policies": MethodPropertyMeta("OutPolicies", "outPolicies", "ConfigSet", "Version142b", "Output", True),
    "out_result_set_size": MethodPropertyMeta("OutResultSetSize", "outResultSetSize", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inContext": "in_context",
    "inDomainId": "in_domain_id",
    "inDomainName": "in_domain_name",
    "inFetchSize": "in_fetch_size",
    "inName": "in_name",
    "inObjectType": "in_object_type",
    "inPolicyOwner": "in_policy_owner",
    "inRecursiveContext": "in_recursive_context",
    "inRecursiveDomainGroup": "in_recursive_domain_group",
    "inSearchDomainGroup": "in_search_domain_group",
    "inSearchType": "in_search_type",
    "outHasMoreResults": "out_has_more_results",
    "outPolicies": "out_policies",
    "outResultSetSize": "out_result_set_size",
}

