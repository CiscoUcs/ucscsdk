"""This module contains the meta information of SnmpFindVar ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("SnmpFindVar", "snmpFindVar", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_is_exact": MethodPropertyMeta("InIsExact", "inIsExact", "Xs:string", "Version142b", "Input", False),
    "in_oid": MethodPropertyMeta("InOid", "inOid", "Xs:string", "Version142b", "Input", False),
    "out_initial_oid": MethodPropertyMeta("OutInitialOid", "outInitialOid", "Xs:string", "Version142b", "Output", False),
    "out_marshaling_mode": MethodPropertyMeta("OutMarshalingMode", "outMarshalingMode", "Xs:string", "Version142b", "Output", False),
    "out_oid": MethodPropertyMeta("OutOid", "outOid", "Xs:string", "Version142b", "Output", False),
    "out_var": MethodPropertyMeta("OutVar", "outVar", "Xs:string", "Version142b", "Output", False),
    "out_var_type": MethodPropertyMeta("OutVarType", "outVarType", "Xs:unsignedByte", "Version142b", "Output", False),
    "out_was_found": MethodPropertyMeta("OutWasFound", "outWasFound", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inIsExact": "in_is_exact",
    "inOid": "in_oid",
    "outInitialOid": "out_initial_oid",
    "outMarshalingMode": "out_marshaling_mode",
    "outOid": "out_oid",
    "outVar": "out_var",
    "outVarType": "out_var_type",
    "outWasFound": "out_was_found",
}

