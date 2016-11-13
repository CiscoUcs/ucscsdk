"""This module contains the meta information of ConfigGetTokenRequestors ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigGetTokenRequestors", "configGetTokenRequestors", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "out_catalog": MethodPropertyMeta("OutCatalog", "outCatalog", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "outCatalog": "out_catalog",
}

