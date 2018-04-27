"""This module contains the meta information of AaaGetRemoteUserRoles ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaGetRemoteUserRoles", "aaaGetRemoteUserRoles", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_remote_user_name": MethodPropertyMeta("InRemoteUserName", "inRemoteUserName", "Xs:string", "Version142b", "Input", False),
    "out_remote_user_priv": MethodPropertyMeta("OutRemoteUserPriv", "outRemoteUserPriv", "Xs:string", "Version142b", "Output", False),
    "out_roles": MethodPropertyMeta("OutRoles", "outRoles", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inRemoteUserName": "in_remote_user_name",
    "outRemoteUserPriv": "out_remote_user_priv",
    "outRoles": "out_roles",
}

