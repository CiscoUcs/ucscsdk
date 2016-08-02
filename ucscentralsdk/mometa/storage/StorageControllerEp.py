"""This module contains the general information for StorageControllerEp ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class StorageControllerEpConsts():
    pass


class StorageControllerEp(ManagedObject):
    """This is StorageControllerEp class."""

    consts = StorageControllerEpConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("StorageControllerEp", "storageControllerEp", "controller-ep-[id]", None, "InputOutput", 0x1f, [], ["read-only"], [u'storageLocalDisk', u'storageVirtualDrive'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "controller_dn": MoPropertyMeta("controller_dn", "controllerDn", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", None, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "controllerDn": "controller_dn", 
        "dn": "dn", 
        "id": "id", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.controller_dn = None
        self.status = None

        ManagedObject.__init__(self, "StorageControllerEp", parent_mo_or_dn, **kwargs)

