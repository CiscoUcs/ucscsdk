"""This module contains the meta information of FabricVnetIdEpOverlapCheck ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("FabricVnetIdEpOverlapCheck", "fabricVnetIdEpOverlapCheck", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_class_id": MethodPropertyMeta("InClassId", "inClassId", "NamingClassId", "Version142b", "Input", False),
    "in_delimiter": MethodPropertyMeta("InDelimiter", "inDelimiter", "Xs:string", "Version142b", "Input", False),
    "in_id_type": MethodPropertyMeta("InIdType", "inIdType", "Xs:string", "Version142b", "Input", False),
    "in_ids_to_check": MethodPropertyMeta("InIdsToCheck", "inIdsToCheck", "Xs:string", "Version142b", "Input", False),
    "in_should_return_overlapping_vnets": MethodPropertyMeta("InShouldReturnOverlappingVnets", "inShouldReturnOverlappingVnets", "Xs:string", "Version142b", "Input", False),
    "out_overlap_exists": MethodPropertyMeta("OutOverlapExists", "outOverlapExists", "Xs:string", "Version142b", "Output", False),
    "out_overlapping_vnet_eps": MethodPropertyMeta("OutOverlappingVnetEps", "outOverlappingVnetEps", "DnSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inClassId": "in_class_id",
    "inDelimiter": "in_delimiter",
    "inIdType": "in_id_type",
    "inIdsToCheck": "in_ids_to_check",
    "inShouldReturnOverlappingVnets": "in_should_return_overlapping_vnets",
    "outOverlapExists": "out_overlap_exists",
    "outOverlappingVnetEps": "out_overlapping_vnet_eps",
}

