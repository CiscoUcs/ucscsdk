"""This module contains the general information for StorageFcTargetEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageFcTargetEpConsts():
    PATH_A = "A"
    PATH_B = "B"
    PATH_NONE = "NONE"
    PATH_DUAL = "dual"
    PATH_MGMT = "mgmt"


class StorageFcTargetEp(ManagedObject):
    """This is StorageFcTargetEp class."""

    consts = StorageFcTargetEpConsts()
    naming_props = set(['targetwwpn'])

    mo_meta = MoMeta("StorageFcTargetEp", "storageFcTargetEp", "fc-target-ep-[targetwwpn]", VersionMeta.Version111a, "InputOutput", 0x7f, [], ["admin", "ext-san-config", "ext-san-policy", "ls-storage", "ls-storage-policy"], ['storageConnectionDef', 'storageConnectionPolicy'], ['storageVsanRef'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "path": MoPropertyMeta("path", "path", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["A", "B", "NONE", "dual", "mgmt"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "targetwwpn": MoPropertyMeta("targetwwpn", "targetwwpn", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x40, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "path": "path", 
        "rn": "rn", 
        "status": "status", 
        "targetwwpn": "targetwwpn", 
    }

    def __init__(self, parent_mo_or_dn, targetwwpn, **kwargs):
        self._dirty_mask = 0
        self.targetwwpn = targetwwpn
        self.child_action = None
        self.descr = None
        self.path = None
        self.status = None

        ManagedObject.__init__(self, "StorageFcTargetEp", parent_mo_or_dn, **kwargs)

