"""This module contains the general information for EtherErrStatsHist ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EtherErrStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EtherErrStatsHist(ManagedObject):
    """This is EtherErrStatsHist class."""

    consts = EtherErrStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EtherErrStatsHist", "etherErrStatsHist", "[id]", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["read-only"], ['etherErrStats'], [], [None])

    prop_meta = {
        "align": MoPropertyMeta("align", "align", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "align_delta": MoPropertyMeta("align_delta", "alignDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "align_delta_avg": MoPropertyMeta("align_delta_avg", "alignDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "align_delta_max": MoPropertyMeta("align_delta_max", "alignDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "align_delta_min": MoPropertyMeta("align_delta_min", "alignDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "deferred_tx": MoPropertyMeta("deferred_tx", "deferredTx", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "deferred_tx_delta": MoPropertyMeta("deferred_tx_delta", "deferredTxDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "deferred_tx_delta_avg": MoPropertyMeta("deferred_tx_delta_avg", "deferredTxDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "deferred_tx_delta_max": MoPropertyMeta("deferred_tx_delta_max", "deferredTxDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "deferred_tx_delta_min": MoPropertyMeta("deferred_tx_delta_min", "deferredTxDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fcs": MoPropertyMeta("fcs", "fcs", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "fcs_delta": MoPropertyMeta("fcs_delta", "fcsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "fcs_delta_avg": MoPropertyMeta("fcs_delta_avg", "fcsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "fcs_delta_max": MoPropertyMeta("fcs_delta_max", "fcsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "fcs_delta_min": MoPropertyMeta("fcs_delta_min", "fcsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111a, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "int_mac_rx": MoPropertyMeta("int_mac_rx", "intMacRx", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_mac_rx_delta": MoPropertyMeta("int_mac_rx_delta", "intMacRxDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_mac_rx_delta_avg": MoPropertyMeta("int_mac_rx_delta_avg", "intMacRxDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_mac_rx_delta_max": MoPropertyMeta("int_mac_rx_delta_max", "intMacRxDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_mac_rx_delta_min": MoPropertyMeta("int_mac_rx_delta_min", "intMacRxDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_mac_tx": MoPropertyMeta("int_mac_tx", "intMacTx", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_mac_tx_delta": MoPropertyMeta("int_mac_tx_delta", "intMacTxDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_mac_tx_delta_avg": MoPropertyMeta("int_mac_tx_delta_avg", "intMacTxDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_mac_tx_delta_max": MoPropertyMeta("int_mac_tx_delta_max", "intMacTxDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_mac_tx_delta_min": MoPropertyMeta("int_mac_tx_delta_min", "intMacTxDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "out_discard": MoPropertyMeta("out_discard", "outDiscard", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "out_discard_delta": MoPropertyMeta("out_discard_delta", "outDiscardDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "out_discard_delta_avg": MoPropertyMeta("out_discard_delta_avg", "outDiscardDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "out_discard_delta_max": MoPropertyMeta("out_discard_delta_max", "outDiscardDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "out_discard_delta_min": MoPropertyMeta("out_discard_delta_min", "outDiscardDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rcv": MoPropertyMeta("rcv", "rcv", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rcv_delta": MoPropertyMeta("rcv_delta", "rcvDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rcv_delta_avg": MoPropertyMeta("rcv_delta_avg", "rcvDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rcv_delta_max": MoPropertyMeta("rcv_delta_max", "rcvDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rcv_delta_min": MoPropertyMeta("rcv_delta_min", "rcvDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "under_size": MoPropertyMeta("under_size", "underSize", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "under_size_delta": MoPropertyMeta("under_size_delta", "underSizeDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "under_size_delta_avg": MoPropertyMeta("under_size_delta_avg", "underSizeDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "under_size_delta_max": MoPropertyMeta("under_size_delta_max", "underSizeDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "under_size_delta_min": MoPropertyMeta("under_size_delta_min", "underSizeDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "xmit": MoPropertyMeta("xmit", "xmit", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "xmit_delta": MoPropertyMeta("xmit_delta", "xmitDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "xmit_delta_avg": MoPropertyMeta("xmit_delta_avg", "xmitDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "xmit_delta_max": MoPropertyMeta("xmit_delta_max", "xmitDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "xmit_delta_min": MoPropertyMeta("xmit_delta_min", "xmitDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "align": "align", 
        "alignDelta": "align_delta", 
        "alignDeltaAvg": "align_delta_avg", 
        "alignDeltaMax": "align_delta_max", 
        "alignDeltaMin": "align_delta_min", 
        "childAction": "child_action", 
        "deferredTx": "deferred_tx", 
        "deferredTxDelta": "deferred_tx_delta", 
        "deferredTxDeltaAvg": "deferred_tx_delta_avg", 
        "deferredTxDeltaMax": "deferred_tx_delta_max", 
        "deferredTxDeltaMin": "deferred_tx_delta_min", 
        "dn": "dn", 
        "fcs": "fcs", 
        "fcsDelta": "fcs_delta", 
        "fcsDeltaAvg": "fcs_delta_avg", 
        "fcsDeltaMax": "fcs_delta_max", 
        "fcsDeltaMin": "fcs_delta_min", 
        "id": "id", 
        "intMacRx": "int_mac_rx", 
        "intMacRxDelta": "int_mac_rx_delta", 
        "intMacRxDeltaAvg": "int_mac_rx_delta_avg", 
        "intMacRxDeltaMax": "int_mac_rx_delta_max", 
        "intMacRxDeltaMin": "int_mac_rx_delta_min", 
        "intMacTx": "int_mac_tx", 
        "intMacTxDelta": "int_mac_tx_delta", 
        "intMacTxDeltaAvg": "int_mac_tx_delta_avg", 
        "intMacTxDeltaMax": "int_mac_tx_delta_max", 
        "intMacTxDeltaMin": "int_mac_tx_delta_min", 
        "mostRecent": "most_recent", 
        "outDiscard": "out_discard", 
        "outDiscardDelta": "out_discard_delta", 
        "outDiscardDeltaAvg": "out_discard_delta_avg", 
        "outDiscardDeltaMax": "out_discard_delta_max", 
        "outDiscardDeltaMin": "out_discard_delta_min", 
        "rcv": "rcv", 
        "rcvDelta": "rcv_delta", 
        "rcvDeltaAvg": "rcv_delta_avg", 
        "rcvDeltaMax": "rcv_delta_max", 
        "rcvDeltaMin": "rcv_delta_min", 
        "rn": "rn", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "underSize": "under_size", 
        "underSizeDelta": "under_size_delta", 
        "underSizeDeltaAvg": "under_size_delta_avg", 
        "underSizeDeltaMax": "under_size_delta_max", 
        "underSizeDeltaMin": "under_size_delta_min", 
        "xmit": "xmit", 
        "xmitDelta": "xmit_delta", 
        "xmitDeltaAvg": "xmit_delta_avg", 
        "xmitDeltaMax": "xmit_delta_max", 
        "xmitDeltaMin": "xmit_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.align = None
        self.align_delta = None
        self.align_delta_avg = None
        self.align_delta_max = None
        self.align_delta_min = None
        self.child_action = None
        self.deferred_tx = None
        self.deferred_tx_delta = None
        self.deferred_tx_delta_avg = None
        self.deferred_tx_delta_max = None
        self.deferred_tx_delta_min = None
        self.fcs = None
        self.fcs_delta = None
        self.fcs_delta_avg = None
        self.fcs_delta_max = None
        self.fcs_delta_min = None
        self.int_mac_rx = None
        self.int_mac_rx_delta = None
        self.int_mac_rx_delta_avg = None
        self.int_mac_rx_delta_max = None
        self.int_mac_rx_delta_min = None
        self.int_mac_tx = None
        self.int_mac_tx_delta = None
        self.int_mac_tx_delta_avg = None
        self.int_mac_tx_delta_max = None
        self.int_mac_tx_delta_min = None
        self.most_recent = None
        self.out_discard = None
        self.out_discard_delta = None
        self.out_discard_delta_avg = None
        self.out_discard_delta_max = None
        self.out_discard_delta_min = None
        self.rcv = None
        self.rcv_delta = None
        self.rcv_delta_avg = None
        self.rcv_delta_max = None
        self.rcv_delta_min = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.under_size = None
        self.under_size_delta = None
        self.under_size_delta_avg = None
        self.under_size_delta_max = None
        self.under_size_delta_min = None
        self.xmit = None
        self.xmit_delta = None
        self.xmit_delta_avg = None
        self.xmit_delta_max = None
        self.xmit_delta_min = None

        ManagedObject.__init__(self, "EtherErrStatsHist", parent_mo_or_dn, **kwargs)

