"""This module contains the meta information of ConfigResolveDomainElements ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveDomainElements", "configResolveDomainElements", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_assoc_state": MethodPropertyMeta("InAssocState", "inAssocState", "Xs:string", "Version142b", "Input", False),
    "in_class_id": MethodPropertyMeta("InClassId", "inClassId", "NamingClassId", "Version142b", "Input", False),
    "in_domain_group_context": MethodPropertyMeta("InDomainGroupContext", "inDomainGroupContext", "Xs:string", "Version142b", "Input", False),
    "in_domain_id": MethodPropertyMeta("InDomainId", "inDomainId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_fetch_size": MethodPropertyMeta("InFetchSize", "inFetchSize", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
    "in_ignore_assoc_state": MethodPropertyMeta("InIgnoreAssocState", "inIgnoreAssocState", "Xs:string", "Version142b", "Input", False),
    "in_include_filter_list_only": MethodPropertyMeta("InIncludeFilterListOnly", "inIncludeFilterListOnly", "Xs:string", "Version142b", "Input", False),
    "in_include_props": MethodPropertyMeta("InIncludeProps", "inIncludeProps", "Xs:string", "Version142b", "Input", False),
    "in_instance_type": MethodPropertyMeta("InInstanceType", "inInstanceType", "Xs:string", "Version142b", "Input", False),
    "in_limit": MethodPropertyMeta("InLimit", "inLimit", "Xs:unsignedShort", "Version142b", "Input", False),
    "in_name": MethodPropertyMeta("InName", "inName", "Xs:string", "Version142b", "Input", False),
    "in_offset": MethodPropertyMeta("InOffset", "inOffset", "Xs:unsignedShort", "Version142b", "Input", False),
    "in_org_context": MethodPropertyMeta("InOrgContext", "inOrgContext", "Xs:string", "Version142b", "Input", False),
    "in_owner": MethodPropertyMeta("InOwner", "inOwner", "Xs:string", "Version142b", "Input", False),
    "in_recursive_domain_group": MethodPropertyMeta("InRecursiveDomainGroup", "inRecursiveDomainGroup", "Xs:string", "Version142b", "Input", False),
    "in_recursive_org_group": MethodPropertyMeta("InRecursiveOrgGroup", "inRecursiveOrgGroup", "Xs:string", "Version142b", "Input", False),
    "in_return_count_only": MethodPropertyMeta("InReturnCountOnly", "inReturnCountOnly", "Xs:string", "Version142b", "Input", False),
    "out_catalog": MethodPropertyMeta("OutCatalog", "outCatalog", "ConfigSet", "Version142b", "Output", True),
    "out_filter_list": MethodPropertyMeta("OutFilterList", "outFilterList", "ConfigSet", "Version142b", "Output", True),
    "out_has_more_results": MethodPropertyMeta("OutHasMoreResults", "outHasMoreResults", "Xs:string", "Version142b", "Output", False),
    "out_result_set_size": MethodPropertyMeta("OutResultSetSize", "outResultSetSize", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_total_result_set_size": MethodPropertyMeta("OutTotalResultSetSize", "outTotalResultSetSize", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inAssocState": "in_assoc_state",
    "inClassId": "in_class_id",
    "inDomainGroupContext": "in_domain_group_context",
    "inDomainId": "in_domain_id",
    "inFetchSize": "in_fetch_size",
    "inFilter": "in_filter",
    "inIgnoreAssocState": "in_ignore_assoc_state",
    "inIncludeFilterListOnly": "in_include_filter_list_only",
    "inIncludeProps": "in_include_props",
    "inInstanceType": "in_instance_type",
    "inLimit": "in_limit",
    "inName": "in_name",
    "inOffset": "in_offset",
    "inOrgContext": "in_org_context",
    "inOwner": "in_owner",
    "inRecursiveDomainGroup": "in_recursive_domain_group",
    "inRecursiveOrgGroup": "in_recursive_org_group",
    "inReturnCountOnly": "in_return_count_only",
    "outCatalog": "out_catalog",
    "outFilterList": "out_filter_list",
    "outHasMoreResults": "out_has_more_results",
    "outResultSetSize": "out_result_set_size",
    "outTotalResultSetSize": "out_total_result_set_size",
}

