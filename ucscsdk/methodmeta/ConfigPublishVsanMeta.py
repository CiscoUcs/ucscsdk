"""This module contains the meta information of ConfigPublishVsan ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigPublishVsan", "configPublishVsan", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_domain": MethodPropertyMeta("InDomain", "inDomain", "ReferenceObject", "Version142b", "Input", False),
    "in_switch_id": MethodPropertyMeta("InSwitchId", "inSwitchId", "Xs:string", "Version142b", "Input", False),
    "in_vsan_name": MethodPropertyMeta("InVsanName", "inVsanName", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inDomain": "in_domain",
    "inSwitchId": "in_switch_id",
    "inVsanName": "in_vsan_name",
}

