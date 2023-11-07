"""This module contains the general information for LstorageDiskSlot ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LstorageDiskSlotConsts():
    DRIVE_PATH_NONE = "NONE"
    DRIVE_PATH_PATH_0 = "PATH-0"
    DRIVE_PATH_PATH_1 = "PATH-1"
    DRIVE_PATH_PATH_BOTH = "PATH-BOTH"
    DRIVE_PATH_UNKNOWN = "UNKNOWN"
    OWNERSHIP_CHASSIS_DEDICATED_SPARE = "chassis-dedicated-spare"
    OWNERSHIP_CHASSIS_GLOBAL_SPARE = "chassis-global-spare"
    OWNERSHIP_DEDICATED = "dedicated"
    OWNERSHIP_SHARED = "shared"
    OWNERSHIP_UNASSIGNED = "unassigned"
    OWNERSHIP_UNKNOWN = "unknown"


class LstorageDiskSlot(ManagedObject):
    """This is LstorageDiskSlot class."""

    consts = LstorageDiskSlotConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("LstorageDiskSlot", "lstorageDiskSlot", "disk-slot-[id]", VersionMeta.Version151a, "InputOutput", 0x7f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['lstorageDiskZoningConfigDef', 'lstorageDiskZoningPolicy'], ['lstorageControllerRef'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "drive_path": MoPropertyMeta("drive_path", "drivePath", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["NONE", "PATH-0", "PATH-1", "PATH-BOTH", "UNKNOWN"], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-60"]), 
        "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["chassis-dedicated-spare", "chassis-global-spare", "dedicated", "shared", "unassigned", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "drivePath": "drive_path", 
        "id": "id", 
        "ownership": "ownership", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.drive_path = None
        self.ownership = None
        self.status = None

        ManagedObject.__init__(self, "LstorageDiskSlot", parent_mo_or_dn, **kwargs)

