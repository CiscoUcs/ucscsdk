"""This module contains the general information for AdaptorEthOffloadProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorEthOffloadProfileConsts():
    pass


class AdaptorEthOffloadProfile(ManagedObject):
    """This is AdaptorEthOffloadProfile class."""

    consts = AdaptorEthOffloadProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorEthOffloadProfile", "adaptorEthOffloadProfile", "eth-offload", VersionMeta.Version111a, "InputOutput", 0xff, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], ['adaptorHostEthIfProfile', 'adaptorUsnicConnDef'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "large_receive": MoPropertyMeta("large_receive", "largeReceive", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tcp_rx_checksum": MoPropertyMeta("tcp_rx_checksum", "tcpRxChecksum", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
        "tcp_segment": MoPropertyMeta("tcp_segment", "tcpSegment", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []), 
        "tcp_tx_checksum": MoPropertyMeta("tcp_tx_checksum", "tcpTxChecksum", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "largeReceive": "large_receive", 
        "rn": "rn", 
        "status": "status", 
        "tcpRxChecksum": "tcp_rx_checksum", 
        "tcpSegment": "tcp_segment", 
        "tcpTxChecksum": "tcp_tx_checksum", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.large_receive = None
        self.status = None
        self.tcp_rx_checksum = None
        self.tcp_segment = None
        self.tcp_tx_checksum = None

        ManagedObject.__init__(self, "AdaptorEthOffloadProfile", parent_mo_or_dn, **kwargs)

