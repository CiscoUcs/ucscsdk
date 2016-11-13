"""This module contains the meta information of ConfigGetConnectedEndpoints ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigGetConnectedEndpoints", "configGetConnectedEndpoints", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_equipment_dn": MethodPropertyMeta("InEquipmentDn", "inEquipmentDn", "ReferenceObject", "Version142b", "Input", False),
    "in_equpiment_id_filter": MethodPropertyMeta("InEqupimentIdFilter", "inEqupimentIdFilter", "NamingClassId", "Version142b", "Input", False),
    "out_endpoints": MethodPropertyMeta("OutEndpoints", "outEndpoints", "ConfigSet", "Version142b", "Output", True),
    "out_num_endpoints": MethodPropertyMeta("OutNumEndpoints", "outNumEndpoints", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inEquipmentDn": "in_equipment_dn",
    "inEqupimentIdFilter": "in_equpiment_id_filter",
    "outEndpoints": "out_endpoints",
    "outNumEndpoints": "out_num_endpoints",
}

