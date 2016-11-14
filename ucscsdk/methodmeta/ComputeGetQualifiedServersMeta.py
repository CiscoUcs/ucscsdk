"""This module contains the meta information of ComputeGetQualifiedServers ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ComputeGetQualifiedServers", "computeGetQualifiedServers", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_qual_dn": MethodPropertyMeta("InQualDn", "inQualDn", "ReferenceObject", "Version142b", "Input", False),
    "in_return_pool_configs": MethodPropertyMeta("InReturnPoolConfigs", "inReturnPoolConfigs", "Xs:string", "Version142b", "Input", False),
    "in_return_server_configs": MethodPropertyMeta("InReturnServerConfigs", "inReturnServerConfigs", "Xs:string", "Version142b", "Input", False),
    "out_pools": MethodPropertyMeta("OutPools", "outPools", "ConfigSet", "Version142b", "Output", True),
    "out_servers": MethodPropertyMeta("OutServers", "outServers", "ConfigSet", "Version142b", "Output", True),
    "out_total_pools": MethodPropertyMeta("OutTotalPools", "outTotalPools", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_total_servers": MethodPropertyMeta("OutTotalServers", "outTotalServers", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inQualDn": "in_qual_dn",
    "inReturnPoolConfigs": "in_return_pool_configs",
    "inReturnServerConfigs": "in_return_server_configs",
    "outPools": "out_pools",
    "outServers": "out_servers",
    "outTotalPools": "out_total_pools",
    "outTotalServers": "out_total_servers",
}

