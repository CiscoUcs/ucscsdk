"""This module contains the meta information of EventSubscribeApps ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EventSubscribeApps", "eventSubscribeApps", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_app_list": MethodPropertyMeta("InAppList", "inAppList", "ConfigSet", "Version142b", "Input", True),
    "in_filter": MethodPropertyMeta("InFilter", "inFilter", "FilterFilter", "Version142b", "Input", True),
}

prop_map = {
    "cookie": "cookie",
    "inAppList": "in_app_list",
    "inFilter": "in_filter",
}

