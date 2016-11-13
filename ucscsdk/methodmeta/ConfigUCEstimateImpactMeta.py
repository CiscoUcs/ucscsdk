"""This module contains the meta information of ConfigUCEstimateImpact ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigUCEstimateImpact", "configUCEstimateImpact", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_configs": MethodPropertyMeta("InConfigs", "inConfigs", "ConfigMap", "Version142b", "Input", True),
    "in_impact_analyzer_id": MethodPropertyMeta("InImpactAnalyzerId", "inImpactAnalyzerId", "Xs:unsignedLong", "Version142b", "Input", False),
    "out_impact_analyzer_dn": MethodPropertyMeta("OutImpactAnalyzerDn", "outImpactAnalyzerDn", "ReferenceObject", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inConfigs": "in_configs",
    "inImpactAnalyzerId": "in_impact_analyzer_id",
    "outImpactAnalyzerDn": "out_impact_analyzer_dn",
}

