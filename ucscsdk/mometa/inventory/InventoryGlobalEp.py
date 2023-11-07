"""This module contains the general information for InventoryGlobalEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class InventoryGlobalEpConsts():
    INVENTORY_TRIG_STATE_OFF = "off"
    INVENTORY_TRIG_STATE_ON = "on"


class InventoryGlobalEp(ManagedObject):
    """This is InventoryGlobalEp class."""

    consts = InventoryGlobalEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("InventoryGlobalEp", "inventoryGlobalEp", "global-ep", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["admin", "operations"], ['inventoryHolder'], ['inventoryInventoryMoMeta'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "inventory_trig_state": MoPropertyMeta("inventory_trig_state", "inventoryTrigState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["off", "on"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "inventoryTrigState": "inventory_trig_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.inventory_trig_state = None
        self.status = None

        ManagedObject.__init__(self, "InventoryGlobalEp", parent_mo_or_dn, **kwargs)

