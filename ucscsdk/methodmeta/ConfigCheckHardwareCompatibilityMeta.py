"""This module contains the meta information of ConfigCheckHardwareCompatibility ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigCheckHardwareCompatibility", "configCheckHardwareCompatibility", "Version142b")

prop_meta = {
    "class_id": MethodPropertyMeta("ClassId", "classId", "NamingClassId", "Version142b", "InputOutput", False),
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_target_blade_firmware_version": MethodPropertyMeta("InTargetBladeFirmwareVersion", "inTargetBladeFirmwareVersion", "Xs:string", "Version142b", "Input", False),
    "in_target_dn": MethodPropertyMeta("InTargetDn", "inTargetDn", "ReferenceObject", "Version142b", "Input", False),
    "in_target_modular_firmware_version": MethodPropertyMeta("InTargetModularFirmwareVersion", "inTargetModularFirmwareVersion", "Xs:string", "Version142b", "Input", False),
    "in_target_rack_firmware_version": MethodPropertyMeta("InTargetRackFirmwareVersion", "inTargetRackFirmwareVersion", "Xs:string", "Version142b", "Input", False),
    "in_target_ucs_firmware_version": MethodPropertyMeta("InTargetUCSFirmwareVersion", "inTargetUCSFirmwareVersion", "Xs:string", "Version142b", "Input", False),
    "out_cannot_determine_count": MethodPropertyMeta("OutCannotDetermineCount", "outCannotDetermineCount", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_catalog_updated_date": MethodPropertyMeta("OutCatalogUpdatedDate", "outCatalogUpdatedDate", "Xs:string", "Version142b", "Output", False),
    "out_catalog_version": MethodPropertyMeta("OutCatalogVersion", "outCatalogVersion", "Xs:string", "Version142b", "Output", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
    "out_hc_error_desc": MethodPropertyMeta("OutHcErrorDesc", "outHcErrorDesc", "Xs:string", "Version142b", "Output", False),
    "out_not_supported_count": MethodPropertyMeta("OutNotSupportedCount", "outNotSupportedCount", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_ok_count": MethodPropertyMeta("OutOkCount", "outOkCount", "Xs:unsignedInt", "Version142b", "Output", False),
    "out_total_count": MethodPropertyMeta("OutTotalCount", "outTotalCount", "Xs:unsignedInt", "Version142b", "Output", False),
}

prop_map = {
    "classId": "class_id",
    "cookie": "cookie",
    "inTargetBladeFirmwareVersion": "in_target_blade_firmware_version",
    "inTargetDn": "in_target_dn",
    "inTargetModularFirmwareVersion": "in_target_modular_firmware_version",
    "inTargetRackFirmwareVersion": "in_target_rack_firmware_version",
    "inTargetUCSFirmwareVersion": "in_target_ucs_firmware_version",
    "outCannotDetermineCount": "out_cannot_determine_count",
    "outCatalogUpdatedDate": "out_catalog_updated_date",
    "outCatalogVersion": "out_catalog_version",
    "outConfigs": "out_configs",
    "outHcErrorDesc": "out_hc_error_desc",
    "outNotSupportedCount": "out_not_supported_count",
    "outOkCount": "out_ok_count",
    "outTotalCount": "out_total_count",
}

