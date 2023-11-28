"""This module contains the general information for LsbootEmbeddedLocalDiskImagePath ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsbootEmbeddedLocalDiskImagePathConsts():
    pass


class LsbootEmbeddedLocalDiskImagePath(ManagedObject):
    """This is LsbootEmbeddedLocalDiskImagePath class."""

    consts = LsbootEmbeddedLocalDiskImagePathConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("LsbootEmbeddedLocalDiskImagePath", "lsbootEmbeddedLocalDiskImagePath", "diskimgpath-[type]", VersionMeta.Version141a, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['lsbootEmbeddedLocalDiskImage'], ['lsbootUEFIBootParam'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "slot_number": MoPropertyMeta("slot_number", "slotNumber", "ushort", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-254"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "slotNumber": "slot_number", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.slot_number = None
        self.status = None

        ManagedObject.__init__(self, "LsbootEmbeddedLocalDiskImagePath", parent_mo_or_dn, **kwargs)

