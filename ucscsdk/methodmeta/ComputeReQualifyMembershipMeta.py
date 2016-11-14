"""This module contains the meta information of ComputeReQualifyMembership ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ComputeReQualifyMembership", "computeReQualifyMembership", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
}

