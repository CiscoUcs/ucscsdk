"""This module contains the meta information of FabricPermitsForExistingVlanNames ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("FabricPermitsForExistingVlanNames", "fabricPermitsForExistingVlanNames", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_org_dn": MethodPropertyMeta("InOrgDn", "inOrgDn", "ReferenceObject", "Version142b", "Input", False),
    "out_vlan_permits": MethodPropertyMeta("OutVlanPermits", "outVlanPermits", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inOrgDn": "in_org_dn",
    "outVlanPermits": "out_vlan_permits",
}

