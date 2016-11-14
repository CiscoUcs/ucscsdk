"""This module contains the meta information of ConfigResolveClassDB ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveClassDB", "configResolveClassDB", "Version142b")

prop_meta = {
    "class_id": MethodPropertyMeta("ClassId", "classId", "NamingClassId", "Version142b", "InputOutput", False),
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_include_prop": MethodPropertyMeta("InIncludeProp", "inIncludeProp", "Xs:string", "Version142b", "Input", False),
    "in_key": MethodPropertyMeta("InKey", "inKey", "Xs:string", "Version142b", "Input", False),
    "in_limit": MethodPropertyMeta("InLimit", "inLimit", "Xs:unsignedShort", "Version142b", "Input", False),
    "in_offset": MethodPropertyMeta("InOffset", "inOffset", "Xs:unsignedShort", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "classId": "class_id",
    "cookie": "cookie",
    "inFilter": "in_filter",
    "inHierarchical": "in_hierarchical",
    "inIncludeProp": "in_include_prop",
    "inKey": "in_key",
    "inLimit": "in_limit",
    "inOffset": "in_offset",
    "outConfigs": "out_configs",
}

