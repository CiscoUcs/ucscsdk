"""This module contains the meta information of AaaGetComputeAuthToken ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaGetComputeAuthToken", "aaaGetComputeAuthToken", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "out_token": MethodPropertyMeta("OutToken", "outToken", "Xs:string", "Version142b", "Output", False),
    "out_user": MethodPropertyMeta("OutUser", "outUser", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "outToken": "out_token",
    "outUser": "out_user",
}

