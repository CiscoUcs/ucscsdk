"""This module contains the general information for ComputeBoardConnector ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeBoardConnectorConsts():
    BOARD_CONNECTOR_TYPE_CONN_LINKED = "conn-linked"
    BOARD_CONNECTOR_TYPE_CONN_UNLINKED = "conn-unlinked"


class ComputeBoardConnector(ManagedObject):
    """This is ComputeBoardConnector class."""

    consts = ComputeBoardConnectorConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeBoardConnector", "computeBoardConnector", "board-conn", VersionMeta.Version121a, "InputOutput", 0xf, [], ["read-only"], ['computeBlade'], [], ["Get"])

    prop_meta = {
        "board_connector_type": MoPropertyMeta("board_connector_type", "boardConnectorType", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn-linked", "conn-unlinked"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "master_slot_id": MoPropertyMeta("master_slot_id", "masterSlotId", "uint", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "slave_slot_id": MoPropertyMeta("slave_slot_id", "slaveSlotId", "uint", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "boardConnectorType": "board_connector_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "masterSlotId": "master_slot_id", 
        "rn": "rn", 
        "slaveSlotId": "slave_slot_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.board_connector_type = None
        self.child_action = None
        self.master_slot_id = None
        self.slave_slot_id = None
        self.status = None

        ManagedObject.__init__(self, "ComputeBoardConnector", parent_mo_or_dn, **kwargs)

