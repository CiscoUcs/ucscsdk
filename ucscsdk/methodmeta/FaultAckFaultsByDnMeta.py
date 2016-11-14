"""This module contains the meta information of FaultAckFaultsByDn ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("FaultAckFaultsByDn", "faultAckFaultsByDn", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_dns": MethodPropertyMeta("InDns", "inDns", "DnSet", "Version142b", "Input", True),
}

prop_map = {
    "cookie": "cookie",
    "inDns": "in_dns",
}

