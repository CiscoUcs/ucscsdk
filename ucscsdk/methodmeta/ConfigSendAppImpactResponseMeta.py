"""This module contains the meta information of ConfigSendAppImpactResponse ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigSendAppImpactResponse", "configSendAppImpactResponse", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_app_impact_response_set": MethodPropertyMeta("InAppImpactResponseSet", "inAppImpactResponseSet", "ConfigSet", "Version142b", "Input", True),
}

prop_map = {
    "cookie": "cookie",
    "inAppImpactResponseSet": "in_app_impact_response_set",
}

