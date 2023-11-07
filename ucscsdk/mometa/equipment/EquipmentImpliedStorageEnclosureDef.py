"""This module contains the general information for EquipmentImpliedStorageEnclosureDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentImpliedStorageEnclosureDefConsts():
    pass


class EquipmentImpliedStorageEnclosureDef(ManagedObject):
    """This is EquipmentImpliedStorageEnclosureDef class."""

    consts = EquipmentImpliedStorageEnclosureDefConsts()
    naming_props = set(['enclosureId'])

    mo_meta = MoMeta("EquipmentImpliedStorageEnclosureDef", "equipmentImpliedStorageEnclosureDef", "enclosure-def-[enclosure_id]", VersionMeta.Version131a, "InputOutput", 0x1f, [], [""], ['equipmentStorageProcessorCap'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "enclosure_id": MoPropertyMeta("enclosure_id", "enclosureId", "ushort", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "first_slot_idx": MoPropertyMeta("first_slot_idx", "firstSlotIdx", "ushort", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "num_slots": MoPropertyMeta("num_slots", "numSlots", "ushort", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "enclosureId": "enclosure_id", 
        "firstSlotIdx": "first_slot_idx", 
        "model": "model", 
        "numSlots": "num_slots", 
        "rn": "rn", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, enclosure_id, **kwargs):
        self._dirty_mask = 0
        self.enclosure_id = enclosure_id
        self.child_action = None
        self.description = None
        self.first_slot_idx = None
        self.model = None
        self.num_slots = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "EquipmentImpliedStorageEnclosureDef", parent_mo_or_dn, **kwargs)

