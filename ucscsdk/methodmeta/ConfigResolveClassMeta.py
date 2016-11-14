"""This module contains the meta information of ConfigResolveClass ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveClass", "configResolveClass", "Version142b")

prop_meta = {
    "class_id": MethodPropertyMeta("ClassId", "classId", "NamingClassId", "Version142b", "InputOutput", False),
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_include_props": MethodPropertyMeta("InIncludeProps", "inIncludeProps", "Xs:string", "Version142b", "Input", False),
    "in_limit": MethodPropertyMeta("InLimit", "inLimit", "Xs:unsignedShort", "Version142b", "Input", False),
    "in_offset": MethodPropertyMeta("InOffset", "inOffset", "Xs:unsignedShort", "Version142b", "Input", False),
    "in_return_count_only": MethodPropertyMeta("InReturnCountOnly", "inReturnCountOnly", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
    "out_count": MethodPropertyMeta("OutCount", "outCount", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_total_count": MethodPropertyMeta("OutTotalCount", "outTotalCount", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "classId": "class_id",
    "cookie": "cookie",
    "inFilter": "in_filter",
    "inHierarchical": "in_hierarchical",
    "inIncludeProps": "in_include_props",
    "inLimit": "in_limit",
    "inOffset": "in_offset",
    "inReturnCountOnly": "in_return_count_only",
    "outConfigs": "out_configs",
    "outCount": "out_count",
    "outTotalCount": "out_total_count",
}

