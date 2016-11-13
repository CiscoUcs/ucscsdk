"""This module contains the meta information of StatsBuildChartResult ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("StatsBuildChartResult", "statsBuildChartResult", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "out_stats_mos": MethodPropertyMeta("OutStatsMos", "outStatsMos", "ConfigSet", "Version142b", "Output", True),
    "out_step": MethodPropertyMeta("OutStep", "outStep", "Xs:long", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "outStatsMos": "out_stats_mos",
    "outStep": "out_step",
}

