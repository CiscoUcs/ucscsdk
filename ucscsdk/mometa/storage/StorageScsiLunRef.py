"""This module contains the general information for StorageScsiLunRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageScsiLunRefConsts():
    ID_UNSPECIFIED = "unspecified"


class StorageScsiLunRef(ManagedObject):
    """This is StorageScsiLunRef class."""

    consts = StorageScsiLunRefConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageScsiLunRef", "storageScsiLunRef", "scsi-lun-ref-[id]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['storageLunReplica', 'storageLunSnapshot', 'storageScsiLun', 'storageVirtualDrive'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "ls_dn": MoPropertyMeta("ls_dn", "lsDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "lun_name": MoPropertyMeta("lun_name", "lunName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "profile_dn": MoPropertyMeta("profile_dn", "profileDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "lsDn": "ls_dn", 
        "lunName": "lun_name", 
        "pnDn": "pn_dn", 
        "profileDn": "profile_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.ls_dn = None
        self.lun_name = None
        self.pn_dn = None
        self.profile_dn = None
        self.status = None

        ManagedObject.__init__(self, "StorageScsiLunRef", parent_mo_or_dn, **kwargs)

