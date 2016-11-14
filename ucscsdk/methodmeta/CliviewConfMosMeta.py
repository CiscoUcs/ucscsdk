"""This module contains the meta information of CliviewConfMos ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("CliviewConfMos", "cliviewConfMos", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_additional_methods": MethodPropertyMeta("InAdditionalMethods", "inAdditionalMethods", "MethodSet", "Version142b", "Input", True),
    "in_commit": MethodPropertyMeta("InCommit", "inCommit", "Xs:string", "Version142b", "Input", False),
    "in_configs": MethodPropertyMeta("InConfigs", "inConfigs", "ConfigMap", "Version142b", "Input", True),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigMap", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inAdditionalMethods": "in_additional_methods",
    "inCommit": "in_commit",
    "inConfigs": "in_configs",
    "inHierarchical": "in_hierarchical",
    "outConfigs": "out_configs",
}

