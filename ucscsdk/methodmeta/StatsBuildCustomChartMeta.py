"""This module contains the meta information of StatsBuildCustomChart ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("StatsBuildCustomChart", "statsBuildCustomChart", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_aggregate_by_dn": MethodPropertyMeta("InAggregateByDn", "inAggregateByDn", "Xs:string", "Version142b", "Input", False),
    "in_end_time": MethodPropertyMeta("InEndTime", "inEndTime", "Xs:unsignedLong", "Version142b", "Input", False),
    "in_overlay": MethodPropertyMeta("InOverlay", "inOverlay", "Xs:string", "Version142b", "Input", False),
    "in_resolve_dns": MethodPropertyMeta("InResolveDns", "inResolveDns", "DnSet", "Version142b", "Input", True),
    "in_start_time": MethodPropertyMeta("InStartTime", "inStartTime", "Xs:unsignedLong", "Version142b", "Input", False),
    "in_stats_types": MethodPropertyMeta("InStatsTypes", "inStatsTypes", "Xs:string", "Version142b", "Input", False),
    "out_stats_query_mo": MethodPropertyMeta("OutStatsQueryMo", "outStatsQueryMo", "ConfigConfig", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inAggregateByDn": "in_aggregate_by_dn",
    "inEndTime": "in_end_time",
    "inOverlay": "in_overlay",
    "inResolveDns": "in_resolve_dns",
    "inStartTime": "in_start_time",
    "inStatsTypes": "in_stats_types",
    "outStatsQueryMo": "out_stats_query_mo",
}

