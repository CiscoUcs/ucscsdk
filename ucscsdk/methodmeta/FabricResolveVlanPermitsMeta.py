"""This module contains the meta information of FabricResolveVlanPermits ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("FabricResolveVlanPermits", "fabricResolveVlanPermits", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_action": MethodPropertyMeta("InAction", "inAction", "Xs:string", "Version142b", "Input", False),
    "in_domain_group_list": MethodPropertyMeta("InDomainGroupList", "inDomainGroupList", "DnSet", "Version142b", "Input", True),
    "in_from": MethodPropertyMeta("InFrom", "inFrom", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "in_org_list": MethodPropertyMeta("InOrgList", "inOrgList", "DnSet", "Version142b", "Input", True),
    "in_pub_nw_name": MethodPropertyMeta("InPubNwName", "inPubNwName", "Xs:string", "Version142b", "Input", False),
    "in_to": MethodPropertyMeta("InTo", "inTo", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_vlan_list": MethodPropertyMeta("InVlanList", "inVlanList", "DnSet", "Version142b", "Input", True),
    "in_vlan_name": MethodPropertyMeta("InVlanName", "inVlanName", "Xs:string", "Version142b", "Input", False),
    "in_vlan_prefix": MethodPropertyMeta("InVlanPrefix", "inVlanPrefix", "Xs:string", "Version142b", "Input", False),
    "out_result_set": MethodPropertyMeta("OutResultSet", "outResultSet", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inAction": "in_action",
    "inDomainGroupList": "in_domain_group_list",
    "inFrom": "in_from",
    "inHierarchical": "in_hierarchical",
    "inOrgList": "in_org_list",
    "inPubNwName": "in_pub_nw_name",
    "inTo": "in_to",
    "inVlanList": "in_vlan_list",
    "inVlanName": "in_vlan_name",
    "inVlanPrefix": "in_vlan_prefix",
    "outResultSet": "out_result_set",
}

