"""This module contains the meta information of StatsBuildStandardChart ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("StatsBuildStandardChart", "statsBuildStandardChart", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_aggregation_property": MethodPropertyMeta("InAggregationProperty", "inAggregationProperty", "Xs:string", "Version142b", "Input", False),
    "in_context_class": MethodPropertyMeta("InContextClass", "inContextClass", "Xs:string", "Version142b", "Input", False),
    "in_count": MethodPropertyMeta("InCount", "inCount", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_end_time": MethodPropertyMeta("InEndTime", "inEndTime", "Xs:unsignedLong", "Version142b", "Input", False),
    "in_overlay": MethodPropertyMeta("InOverlay", "inOverlay", "Xs:string", "Version142b", "Input", False),
    "in_parent_dn": MethodPropertyMeta("InParentDn", "inParentDn", "Xs:string", "Version142b", "Input", False),
    "in_report_type": MethodPropertyMeta("InReportType", "inReportType", "Xs:string", "Version142b", "Input", False),
    "in_start_time": MethodPropertyMeta("InStartTime", "inStartTime", "Xs:unsignedLong", "Version142b", "Input", False),
    "in_stats_types": MethodPropertyMeta("InStatsTypes", "inStatsTypes", "Xs:string", "Version142b", "Input", False),
    "out_stats_query_mo": MethodPropertyMeta("OutStatsQueryMo", "outStatsQueryMo", "ConfigConfig", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inAggregationProperty": "in_aggregation_property",
    "inContextClass": "in_context_class",
    "inCount": "in_count",
    "inEndTime": "in_end_time",
    "inOverlay": "in_overlay",
    "inParentDn": "in_parent_dn",
    "inReportType": "in_report_type",
    "inStartTime": "in_start_time",
    "inStatsTypes": "in_stats_types",
    "outStatsQueryMo": "out_stats_query_mo",
}

