"""This module contains the general information for ComputePhysicalExtension ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputePhysicalExtensionConsts():
    HW_INVENTORY_STATUS_IN_PROGRESS = "in-progress"
    HW_INVENTORY_STATUS_OK = "ok"
    HW_INVENTORY_STATUS_THROTTLED = "throttled"


class ComputePhysicalExtension(ManagedObject):
    """This is ComputePhysicalExtension class."""

    consts = ComputePhysicalExtensionConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePhysicalExtension", "computePhysicalExtension", "phys-extension", VersionMeta.Version201b, "InputOutput", 0xf, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], [], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "hw_inventory_status": MoPropertyMeta("hw_inventory_status", "hwInventoryStatus", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["in-progress", "ok", "throttled"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "hwInventoryStatus": "hw_inventory_status", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.hw_inventory_status = None
        self.status = None

        ManagedObject.__init__(self, "ComputePhysicalExtension", parent_mo_or_dn, **kwargs)

