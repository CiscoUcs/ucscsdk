"""This module contains the meta information of ConfigResolveClasses ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveClasses", "configResolveClasses", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_ids": MethodPropertyMeta("InIds", "inIds", "ClassIdSet", "Version142b", "Input", True),
    "in_return_count_only": MethodPropertyMeta("InReturnCountOnly", "inReturnCountOnly", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
    "out_count": MethodPropertyMeta("OutCount", "outCount", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inHierarchical": "in_hierarchical",
    "inIds": "in_ids",
    "inReturnCountOnly": "in_return_count_only",
    "outConfigs": "out_configs",
    "outCount": "out_count",
}

