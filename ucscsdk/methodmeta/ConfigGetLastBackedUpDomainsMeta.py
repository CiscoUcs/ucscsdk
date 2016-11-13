"""This module contains the meta information of ConfigGetLastBackedUpDomains ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigGetLastBackedUpDomains", "configGetLastBackedUpDomains", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_backup_type": MethodPropertyMeta("InBackupType", "inBackupType", "Xs:string", "Version142b", "Input", False),
    "in_domains": MethodPropertyMeta("InDomains", "inDomains", "DnSet", "Version142b", "Input", True),
    "out_config_backup": MethodPropertyMeta("OutConfigBackup", "outConfigBackup", "ConfigSet", "Version142b", "Output", True),
    "out_empty_backup_clients": MethodPropertyMeta("OutEmptyBackupClients", "outEmptyBackupClients", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inBackupType": "in_backup_type",
    "inDomains": "in_domains",
    "outConfigBackup": "out_config_backup",
    "outEmptyBackupClients": "out_empty_backup_clients",
}

