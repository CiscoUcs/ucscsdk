"""This module contains the meta information of ConfigResolveSpotLightIdx ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveSpotLightIdx", "configResolveSpotLightIdx", "Version142b")

prop_meta = {
    "class_id": MethodPropertyMeta("ClassId", "classId", "NamingClassId", "Version142b", "InputOutput", False),
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_class": MethodPropertyMeta("InClass", "inClass", "Xs:string", "Version142b", "Input", False),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
    "in_include_facet": MethodPropertyMeta("InIncludeFacet", "inIncludeFacet", "Xs:string", "Version142b", "Input", False),
    "in_include_prop": MethodPropertyMeta("InIncludeProp", "inIncludeProp", "Xs:string", "Version142b", "Input", False),
    "in_limit": MethodPropertyMeta("InLimit", "inLimit", "Xs:unsignedShort", "Version142b", "Input", False),
    "in_offset": MethodPropertyMeta("InOffset", "inOffset", "Xs:unsignedShort", "Version142b", "Input", False),
    "in_query": MethodPropertyMeta("InQuery", "inQuery", "Xs:string", "Version142b", "Input", False),
    "in_sort_str": MethodPropertyMeta("InSortStr", "inSortStr", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
    "out_facets": MethodPropertyMeta("OutFacets", "outFacets", "ConfigSet", "Version142b", "Output", True),
    "out_total_count": MethodPropertyMeta("OutTotalCount", "outTotalCount", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "classId": "class_id",
    "cookie": "cookie",
    "inClass": "in_class",
    "inFilter": "in_filter",
    "inIncludeFacet": "in_include_facet",
    "inIncludeProp": "in_include_prop",
    "inLimit": "in_limit",
    "inOffset": "in_offset",
    "inQuery": "in_query",
    "inSortStr": "in_sort_str",
    "outConfigs": "out_configs",
    "outFacets": "out_facets",
    "outTotalCount": "out_total_count",
}

