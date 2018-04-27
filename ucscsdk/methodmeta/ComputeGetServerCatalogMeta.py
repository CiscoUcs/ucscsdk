"""This module contains the meta information of ComputeGetServerCatalog ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ComputeGetServerCatalog", "computeGetServerCatalog", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_domain_group_list": MethodPropertyMeta("InDomainGroupList", "inDomainGroupList", "DnSet", "Version142b", "Input", True),
    "in_equipment_filter": MethodPropertyMeta("InEquipmentFilter", "inEquipmentFilter", "ConfigConfig", "Version142b", "Input", True),
    "in_exclude_total_result_size": MethodPropertyMeta("InExcludeTotalResultSize", "inExcludeTotalResultSize", "Xs:string", "Version142b", "Input", False),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
    "in_include_filter_list_only": MethodPropertyMeta("InIncludeFilterListOnly", "inIncludeFilterListOnly", "Xs:string", "Version142b", "Input", False),
    "in_include_props": MethodPropertyMeta("InIncludeProps", "inIncludeProps", "Xs:string", "Version142b", "Input", False),
    "in_limit": MethodPropertyMeta("InLimit", "inLimit", "Xs:unsignedShort", "Version142b", "Input", False),
    "in_offset": MethodPropertyMeta("InOffset", "inOffset", "Xs:unsignedShort", "Version142b", "Input", False),
    "in_recursive": MethodPropertyMeta("InRecursive", "inRecursive", "Xs:string", "Version142b", "Input", False),
    "in_return_count_only": MethodPropertyMeta("InReturnCountOnly", "inReturnCountOnly", "Xs:string", "Version142b", "Input", False),
    "out_catalog": MethodPropertyMeta("OutCatalog", "outCatalog", "ConfigSet", "Version142b", "Output", True),
    "out_filter_list": MethodPropertyMeta("OutFilterList", "outFilterList", "ConfigSet", "Version142b", "Output", True),
    "out_has_more_results": MethodPropertyMeta("OutHasMoreResults", "outHasMoreResults", "Xs:string", "Version142b", "Output", False),
    "out_result_set_size": MethodPropertyMeta("OutResultSetSize", "outResultSetSize", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_total_result_set_size": MethodPropertyMeta("OutTotalResultSetSize", "outTotalResultSetSize", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inDomainGroupList": "in_domain_group_list",
    "inEquipmentFilter": "in_equipment_filter",
    "inExcludeTotalResultSize": "in_exclude_total_result_size",
    "inFilter": "in_filter",
    "inIncludeFilterListOnly": "in_include_filter_list_only",
    "inIncludeProps": "in_include_props",
    "inLimit": "in_limit",
    "inOffset": "in_offset",
    "inRecursive": "in_recursive",
    "inReturnCountOnly": "in_return_count_only",
    "outCatalog": "out_catalog",
    "outFilterList": "out_filter_list",
    "outHasMoreResults": "out_has_more_results",
    "outResultSetSize": "out_result_set_size",
    "outTotalResultSetSize": "out_total_result_set_size",
}

