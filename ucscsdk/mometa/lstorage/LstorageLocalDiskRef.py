"""This module contains the general information for LstorageLocalDiskRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LstorageLocalDiskRefConsts():
    pass


class LstorageLocalDiskRef(ManagedObject):
    """This is LstorageLocalDiskRef class."""

    consts = LstorageLocalDiskRefConsts()
    naming_props = set(['enclosureId', 'slotId'])

    mo_meta = MoMeta("LstorageLocalDiskRef", "lstorageLocalDiskRef", "diskref-[enclosure_id]-slot-[slot_id]", VersionMeta.Version131a, "InputOutput", 0x3f, [], ["read-only"], [], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "enclosure_id": MoPropertyMeta("enclosure_id", "enclosureId", "uint", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "enclosureId": "enclosure_id", 
        "rn": "rn", 
        "slotId": "slot_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, enclosure_id, slot_id, **kwargs):
        self._dirty_mask = 0
        self.enclosure_id = enclosure_id
        self.slot_id = slot_id
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "LstorageLocalDiskRef", parent_mo_or_dn, **kwargs)

