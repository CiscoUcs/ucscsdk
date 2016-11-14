"""This module contains the meta information of ConfigGetIdUniverseUsage ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigGetIdUniverseUsage", "configGetIdUniverseUsage", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_domain_group_dn": MethodPropertyMeta("InDomainGroupDn", "inDomainGroupDn", "ReferenceObject", "Version142b", "Input", False),
    "in_id_type": MethodPropertyMeta("InIdType", "inIdType", "Xs:string", "Version142b", "Input", False),
    "in_show_id_details": MethodPropertyMeta("InShowIdDetails", "inShowIdDetails", "Xs:string", "Version142b", "Input", False),
    "out_assigned": MethodPropertyMeta("OutAssigned", "outAssigned", "ConfigSet", "Version142b", "Output", True),
    "out_available": MethodPropertyMeta("OutAvailable", "outAvailable", "ConfigSet", "Version142b", "Output", True),
    "out_conflict": MethodPropertyMeta("OutConflict", "outConflict", "ConfigSet", "Version142b", "Output", True),
    "out_num_assigned": MethodPropertyMeta("OutNumAssigned", "outNumAssigned", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_num_available": MethodPropertyMeta("OutNumAvailable", "outNumAvailable", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_num_conflict": MethodPropertyMeta("OutNumConflict", "outNumConflict", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_num_total": MethodPropertyMeta("OutNumTotal", "outNumTotal", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_total": MethodPropertyMeta("OutTotal", "outTotal", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inDomainGroupDn": "in_domain_group_dn",
    "inIdType": "in_id_type",
    "inShowIdDetails": "in_show_id_details",
    "outAssigned": "out_assigned",
    "outAvailable": "out_available",
    "outConflict": "out_conflict",
    "outNumAssigned": "out_num_assigned",
    "outNumAvailable": "out_num_available",
    "outNumConflict": "out_num_conflict",
    "outNumTotal": "out_num_total",
    "outTotal": "out_total",
}

