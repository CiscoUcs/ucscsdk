"""This module contains the meta information of ConfigGetNetRefs ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigGetNetRefs", "configGetNetRefs", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_org_dn": MethodPropertyMeta("InOrgDn", "inOrgDn", "ReferenceObject", "Version142b", "Input", False),
    "in_server_dn": MethodPropertyMeta("InServerDn", "inServerDn", "ReferenceObject", "Version142b", "Input", False),
    "in_type": MethodPropertyMeta("InType", "inType", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inOrgDn": "in_org_dn",
    "inServerDn": "in_server_dn",
    "inType": "in_type",
    "outConfigs": "out_configs",
}

