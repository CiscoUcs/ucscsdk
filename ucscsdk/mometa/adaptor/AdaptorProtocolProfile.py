"""This module contains the general information for AdaptorProtocolProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorProtocolProfileConsts():
    BOOT_TO_TARGET_FALSE = "false"
    BOOT_TO_TARGET_NO = "no"
    BOOT_TO_TARGET_TRUE = "true"
    BOOT_TO_TARGET_YES = "yes"
    HBA_MODE_FALSE = "false"
    HBA_MODE_NO = "no"
    HBA_MODE_TRUE = "true"
    HBA_MODE_YES = "yes"
    TCP_TIME_STAMP_FALSE = "false"
    TCP_TIME_STAMP_NO = "no"
    TCP_TIME_STAMP_TRUE = "true"
    TCP_TIME_STAMP_YES = "yes"


class AdaptorProtocolProfile(ManagedObject):
    """This is AdaptorProtocolProfile class."""

    consts = AdaptorProtocolProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorProtocolProfile", "adaptorProtocolProfile", "iscsi-prot-profile", VersionMeta.Version111a, "InputOutput", 0x3ff, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], ['adaptorHostIscsiIfProfile'], [], ["Add", "Get", "Set"])

    prop_meta = {
        "boot_to_target": MoPropertyMeta("boot_to_target", "bootToTarget", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "connection_time_out": MoPropertyMeta("connection_time_out", "connectionTimeOut", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-255"]), 
        "dhcp_time_out": MoPropertyMeta("dhcp_time_out", "dhcpTimeOut", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["60-300"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "hba_mode": MoPropertyMeta("hba_mode", "hbaMode", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []), 
        "lun_busy_retry_count": MoPropertyMeta("lun_busy_retry_count", "lunBusyRetryCount", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-60"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tcp_time_stamp": MoPropertyMeta("tcp_time_stamp", "tcpTimeStamp", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "bootToTarget": "boot_to_target", 
        "childAction": "child_action", 
        "connectionTimeOut": "connection_time_out", 
        "dhcpTimeOut": "dhcp_time_out", 
        "dn": "dn", 
        "hbaMode": "hba_mode", 
        "lunBusyRetryCount": "lun_busy_retry_count", 
        "rn": "rn", 
        "status": "status", 
        "tcpTimeStamp": "tcp_time_stamp", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.boot_to_target = None
        self.child_action = None
        self.connection_time_out = None
        self.dhcp_time_out = None
        self.hba_mode = None
        self.lun_busy_retry_count = None
        self.status = None
        self.tcp_time_stamp = None

        ManagedObject.__init__(self, "AdaptorProtocolProfile", parent_mo_or_dn, **kwargs)

