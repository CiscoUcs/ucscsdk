"""This module contains the meta information of ConfigScope ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigScope", "configScope", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_class": MethodPropertyMeta("InClass", "inClass", "NamingClassId", "Version142b", "Input", False),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_recursive": MethodPropertyMeta("InRecursive", "inRecursive", "Xs:string", "Version142b", "Input", False),
    "in_return_count_only": MethodPropertyMeta("InReturnCountOnly", "inReturnCountOnly", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
    "out_count": MethodPropertyMeta("OutCount", "outCount", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inClass": "in_class",
    "inFilter": "in_filter",
    "inHierarchical": "in_hierarchical",
    "inRecursive": "in_recursive",
    "inReturnCountOnly": "in_return_count_only",
    "outConfigs": "out_configs",
    "outCount": "out_count",
}

