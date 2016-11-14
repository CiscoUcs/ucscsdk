"""This module contains the meta information of IdentGetSortedIds ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("IdentGetSortedIds", "identGetSortedIds", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_block": MethodPropertyMeta("InBlock", "inBlock", "ConfigConfig", "Version142b", "Input", True),
    "in_pool": MethodPropertyMeta("InPool", "inPool", "ConfigConfig", "Version142b", "Input", True),
    "out_assigned_ids": MethodPropertyMeta("OutAssignedIds", "outAssignedIds", "ConfigSet", "Version142b", "Output", True),
    "out_available_ids": MethodPropertyMeta("OutAvailableIds", "outAvailableIds", "ConfigSet", "Version142b", "Output", True),
    "out_duplicate_ids": MethodPropertyMeta("OutDuplicateIds", "outDuplicateIds", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inBlock": "in_block",
    "inPool": "in_pool",
    "outAssignedIds": "out_assigned_ids",
    "outAvailableIds": "out_available_ids",
    "outDuplicateIds": "out_duplicate_ids",
}

