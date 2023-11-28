"""This module contains the general information for InventoryDomainEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class InventoryDomainEpConsts():
    INVENTORY_TRIG_STATE_OFF = "off"
    INVENTORY_TRIG_STATE_ON = "on"
    TRIG_FULL_INVENTORY_OFF = "off"
    TRIG_FULL_INVENTORY_ON = "on"


class InventoryDomainEp(ManagedObject):
    """This is InventoryDomainEp class."""

    consts = InventoryDomainEpConsts()
    naming_props = set(['sysId'])

    mo_meta = MoMeta("InventoryDomainEp", "inventoryDomainEp", "domain-[sys_id]", VersionMeta.Version201b, "InputOutput", 0xff, [], ["admin", "operations"], ['inventoryHolder'], ['inventoryInventoryMoMeta'], ["get", "set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "inventory_trig_state": MoPropertyMeta("inventory_trig_state", "inventoryTrigState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["off", "on"], []), 
        "latest_update_time": MoPropertyMeta("latest_update_time", "latestUpdateTime", "ulong", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sys_id": MoPropertyMeta("sys_id", "sysId", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []), 
        "trig_full_inventory": MoPropertyMeta("trig_full_inventory", "trigFullInventory", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["off", "on"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "inventoryTrigState": "inventory_trig_state", 
        "latestUpdateTime": "latest_update_time", 
        "rn": "rn", 
        "status": "status", 
        "sysId": "sys_id", 
        "trigFullInventory": "trig_full_inventory", 
    }

    def __init__(self, parent_mo_or_dn, sys_id, **kwargs):
        self._dirty_mask = 0
        self.sys_id = sys_id
        self.child_action = None
        self.inventory_trig_state = None
        self.latest_update_time = None
        self.status = None
        self.trig_full_inventory = None

        ManagedObject.__init__(self, "InventoryDomainEp", parent_mo_or_dn, **kwargs)

