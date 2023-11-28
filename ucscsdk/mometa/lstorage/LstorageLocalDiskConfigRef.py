"""This module contains the general information for LstorageLocalDiskConfigRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LstorageLocalDiskConfigRefConsts():
    ROLE_DED_HOT_SPARE = "ded-hot-spare"
    ROLE_GLOB_HOT_SPARE = "glob-hot-spare"
    ROLE_NORMAL = "normal"
    ROLE_UNKNOWN = "unknown"
    SPAN_ID_UNSPECIFIED = "unspecified"


class LstorageLocalDiskConfigRef(ManagedObject):
    """This is LstorageLocalDiskConfigRef class."""

    consts = LstorageLocalDiskConfigRefConsts()
    naming_props = set(['slotNum'])

    mo_meta = MoMeta("LstorageLocalDiskConfigRef", "lstorageLocalDiskConfigRef", "slot-[slot_num]", VersionMeta.Version131a, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], ['lstorageDiskGroupConfigDef', 'lstorageDiskGroupConfigPolicy'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "role": MoPropertyMeta("role", "role", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["ded-hot-spare", "glob-hot-spare", "normal", "unknown"], []), 
        "slot_num": MoPropertyMeta("slot_num", "slotNum", "ushort", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-254"]), 
        "span_id": MoPropertyMeta("span_id", "spanId", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["unspecified"], ["0-8"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "role": "role", 
        "slotNum": "slot_num", 
        "spanId": "span_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, slot_num, **kwargs):
        self._dirty_mask = 0
        self.slot_num = slot_num
        self.child_action = None
        self.role = None
        self.span_id = None
        self.status = None

        ManagedObject.__init__(self, "LstorageLocalDiskConfigRef", parent_mo_or_dn, **kwargs)

