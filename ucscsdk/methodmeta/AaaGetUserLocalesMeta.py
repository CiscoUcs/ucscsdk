"""This module contains the meta information of AaaGetUserLocales ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaGetUserLocales", "aaaGetUserLocales", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_is_user_remote": MethodPropertyMeta("InIsUserRemote", "inIsUserRemote", "Xs:string", "Version142b", "Input", False),
    "in_user_name": MethodPropertyMeta("InUserName", "inUserName", "Xs:string", "Version142b", "Input", False),
    "out_user_locales": MethodPropertyMeta("OutUserLocales", "outUserLocales", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inIsUserRemote": "in_is_user_remote",
    "inUserName": "in_user_name",
    "outUserLocales": "out_user_locales",
}

