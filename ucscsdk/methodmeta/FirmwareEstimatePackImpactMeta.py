"""This module contains the meta information of FirmwareEstimatePackImpact ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("FirmwareEstimatePackImpact", "firmwareEstimatePackImpact", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_group_dn": MethodPropertyMeta("InGroupDn", "inGroupDn", "ReferenceObject", "Version142b", "Input", False),
    "in_pack_configs": MethodPropertyMeta("InPackConfigs", "inPackConfigs", "ConfigSet", "Version142b", "Input", True),
    "out_config_set": MethodPropertyMeta("OutConfigSet", "outConfigSet", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inGroupDn": "in_group_dn",
    "inPackConfigs": "in_pack_configs",
    "outConfigSet": "out_config_set",
}

