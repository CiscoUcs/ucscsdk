"""This module contains the meta information of IdentGetBlockReport ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("IdentGetBlockReport", "identGetBlockReport", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_block": MethodPropertyMeta("InBlock", "inBlock", "ConfigConfig", "Version142b", "Input", True),
    "in_pool": MethodPropertyMeta("InPool", "inPool", "ConfigConfig", "Version142b", "Input", True),
    "out_number_assigned": MethodPropertyMeta("OutNumberAssigned", "outNumberAssigned", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_number_available": MethodPropertyMeta("OutNumberAvailable", "outNumberAvailable", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_number_duplicate": MethodPropertyMeta("OutNumberDuplicate", "outNumberDuplicate", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inBlock": "in_block",
    "inPool": "in_pool",
    "outNumberAssigned": "out_number_assigned",
    "outNumberAvailable": "out_number_available",
    "outNumberDuplicate": "out_number_duplicate",
}

