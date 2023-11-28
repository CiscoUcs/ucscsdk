"""This module contains the general information for InventoryInventoryMoMeta ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class InventoryInventoryMoMetaConsts():
    pass


class InventoryInventoryMoMeta(ManagedObject):
    """This is InventoryInventoryMoMeta class."""

    consts = InventoryInventoryMoMetaConsts()
    naming_props = set(['instId'])

    mo_meta = MoMeta("InventoryInventoryMoMeta", "inventoryInventoryMoMeta", "mo-[inst_id]", VersionMeta.Version201b, "InputOutput", 0xff, [], ["admin", "operations"], ['inventoryDomainEp', 'inventoryGlobalEp'], [], [None])

    prop_meta = {
        "admin_prop_mod": MoPropertyMeta("admin_prop_mod", "adminPropMod", "ulong", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "inst_id": MoPropertyMeta("inst_id", "instId", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "latest_update_time": MoPropertyMeta("latest_update_time", "latestUpdateTime", "ulong", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "mo_dn": MoPropertyMeta("mo_dn", "moDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_prop_mod": MoPropertyMeta("oper_prop_mod", "operPropMod", "ulong", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminPropMod": "admin_prop_mod", 
        "childAction": "child_action", 
        "dn": "dn", 
        "instId": "inst_id", 
        "latestUpdateTime": "latest_update_time", 
        "moDn": "mo_dn", 
        "operPropMod": "oper_prop_mod", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, inst_id, **kwargs):
        self._dirty_mask = 0
        self.inst_id = inst_id
        self.admin_prop_mod = None
        self.child_action = None
        self.latest_update_time = None
        self.mo_dn = None
        self.oper_prop_mod = None
        self.status = None

        ManagedObject.__init__(self, "InventoryInventoryMoMeta", parent_mo_or_dn, **kwargs)

