"""This module contains the general information for StorageItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageItemConsts():
    HIGH_SPEED_NOT_APPLICABLE = "not-applicable"
    LOW_SPEED_NOT_APPLICABLE = "not-applicable"
    NORMAL_SPEED_NOT_APPLICABLE = "not-applicable"
    READ_SPEED_NOT_APPLICABLE = "not-applicable"
    SIZE_NOTHING = "nothing"
    USED_EMPTY = "empty"
    USED_FULL = "full"
    USED_NOT_APPLICABLE = "not-applicable"


class StorageItem(ManagedObject):
    """This is StorageItem class."""

    consts = StorageItemConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("StorageItem", "storageItem", "stor-part-[name]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["read-only"], ['networkElement', 'nfsExportDef'], ['faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "high_speed": MoPropertyMeta("high_speed", "highSpeed", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "low_speed": MoPropertyMeta("low_speed", "lowSpeed", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "normal_speed": MoPropertyMeta("normal_speed", "normalSpeed", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "read_speed": MoPropertyMeta("read_speed", "readSpeed", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["nothing"], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "system_name": MoPropertyMeta("system_name", "systemName", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "used": MoPropertyMeta("used", "used", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "full", "not-applicable"], ["0-101"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "highSpeed": "high_speed", 
        "lowSpeed": "low_speed", 
        "name": "name", 
        "normalSpeed": "normal_speed", 
        "readSpeed": "read_speed", 
        "rn": "rn", 
        "size": "size", 
        "status": "status", 
        "systemName": "system_name", 
        "used": "used", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.high_speed = None
        self.low_speed = None
        self.normal_speed = None
        self.read_speed = None
        self.size = None
        self.status = None
        self.system_name = None
        self.used = None

        ManagedObject.__init__(self, "StorageItem", parent_mo_or_dn, **kwargs)

