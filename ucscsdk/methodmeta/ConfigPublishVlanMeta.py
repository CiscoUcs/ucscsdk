"""This module contains the meta information of ConfigPublishVlan ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigPublishVlan", "configPublishVlan", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_domain": MethodPropertyMeta("InDomain", "inDomain", "ReferenceObject", "Version142b", "Input", False),
    "in_vlan_name": MethodPropertyMeta("InVlanName", "inVlanName", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inDomain": "in_domain",
    "inVlanName": "in_vlan_name",
}

