"""This module contains the meta information of FirmwareInstallAll ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("FirmwareInstallAll", "firmwareInstallAll", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_concurrent_jobs": MethodPropertyMeta("InConcurrentJobs", "inConcurrentJobs", "Xs:unsignedShort", "Version142b", "Input", False),
    "in_group_dn": MethodPropertyMeta("InGroupDn", "inGroupDn", "ReferenceObject", "Version142b", "Input", False),
    "in_honor_ls_maint": MethodPropertyMeta("InHonorLsMaint", "inHonorLsMaint", "Xs:string", "Version142b", "Input", False),
    "in_ignore_comp_check": MethodPropertyMeta("InIgnoreCompCheck", "inIgnoreCompCheck", "Xs:string", "Version142b", "Input", False),
    "in_packages": MethodPropertyMeta("InPackages", "inPackages", "ConfigSet", "Version142b", "Input", True),
    "in_start_time": MethodPropertyMeta("InStartTime", "inStartTime", "Xs:string", "Version142b", "Input", False),
    "in_user_ack": MethodPropertyMeta("InUserAck", "inUserAck", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inConcurrentJobs": "in_concurrent_jobs",
    "inGroupDn": "in_group_dn",
    "inHonorLsMaint": "in_honor_ls_maint",
    "inIgnoreCompCheck": "in_ignore_comp_check",
    "inPackages": "in_packages",
    "inStartTime": "in_start_time",
    "inUserAck": "in_user_ack",
}

