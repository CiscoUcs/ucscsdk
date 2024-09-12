"""This module contains the general information for StorageInitiatorRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageInitiatorRefConsts():
    ID_UNSPECIFIED = "unspecified"


class StorageInitiatorRef(ManagedObject):
    """This is StorageInitiatorRef class."""

    consts = StorageInitiatorRefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("StorageInitiatorRef", "storageInitiatorRef", "lun-ref-[name]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['storageScsiLun'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "ls_dn": MoPropertyMeta("ls_dn", "lsDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "lsDn": "ls_dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.id = None
        self.ls_dn = None
        self.status = None

        ManagedObject.__init__(self, "StorageInitiatorRef", parent_mo_or_dn, **kwargs)

