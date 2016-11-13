"""This module contains the meta information of IdentGetIdUsage ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("IdentGetIdUsage", "identGetIdUsage", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_pool_dn": MethodPropertyMeta("InPoolDn", "inPoolDn", "ReferenceObject", "Version142b", "Input", False),
    "out_number_available": MethodPropertyMeta("OutNumberAvailable", "outNumberAvailable", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_number_used": MethodPropertyMeta("OutNumberUsed", "outNumberUsed", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inPoolDn": "in_pool_dn",
    "outNumberAvailable": "out_number_available",
    "outNumberUsed": "out_number_used",
}

