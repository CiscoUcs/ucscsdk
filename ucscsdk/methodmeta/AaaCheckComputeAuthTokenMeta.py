"""This module contains the meta information of AaaCheckComputeAuthToken ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaCheckComputeAuthToken", "aaaCheckComputeAuthToken", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_token": MethodPropertyMeta("InToken", "inToken", "Xs:string", "Version142b", "Input", False),
    "in_user": MethodPropertyMeta("InUser", "inUser", "Xs:string", "Version142b", "Input", False),
    "out_allow": MethodPropertyMeta("OutAllow", "outAllow", "Xs:string", "Version142b", "Output", False),
    "out_auth_user": MethodPropertyMeta("OutAuthUser", "outAuthUser", "Xs:string", "Version142b", "Output", False),
    "out_locales": MethodPropertyMeta("OutLocales", "outLocales", "Xs:string", "Version142b", "Output", False),
    "out_priv": MethodPropertyMeta("OutPriv", "outPriv", "Xs:string", "Version142b", "Output", False),
    "out_remote": MethodPropertyMeta("OutRemote", "outRemote", "Xs:string", "Version142b", "Output", False),
    "out_role_list": MethodPropertyMeta("OutRoleList", "outRoleList", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inToken": "in_token",
    "inUser": "in_user",
    "outAllow": "out_allow",
    "outAuthUser": "out_auth_user",
    "outLocales": "out_locales",
    "outPriv": "out_priv",
    "outRemote": "out_remote",
    "outRoleList": "out_role_list",
}

