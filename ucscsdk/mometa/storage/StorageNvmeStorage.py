"""This module contains the general information for StorageNvmeStorage ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageNvmeStorageConsts():
    pass


class StorageNvmeStorage(ManagedObject):
    """This is StorageNvmeStorage class."""

    consts = StorageNvmeStorageConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageNvmeStorage", "storageNvmeStorage", "nvme-storage", VersionMeta.Version201b, "InputOutput", 0xf, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['storageController'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "performance_level": MoPropertyMeta("performance_level", "performanceLevel", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-100"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "performanceLevel": "performance_level", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.performance_level = None
        self.status = None

        ManagedObject.__init__(self, "StorageNvmeStorage", parent_mo_or_dn, **kwargs)

