"""This module contains the general information for StorageScsiDeviceDescriptor ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageScsiDeviceDescriptorConsts():
    TYPE_EUI_64 = "eui-64"
    TYPE_MD5 = "md5"
    TYPE_NAA = "naa"
    TYPE_SCSI_NAME = "scsi-name"
    TYPE_T10 = "t10"


class StorageScsiDeviceDescriptor(ManagedObject):
    """This is StorageScsiDeviceDescriptor class."""

    consts = StorageScsiDeviceDescriptorConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("StorageScsiDeviceDescriptor", "storageScsiDeviceDescriptor", "scsi-descriptor-[type]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['storageScsiLun'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["eui-64", "md5", "naa", "scsi-name", "t10"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.id = None
        self.status = None

        ManagedObject.__init__(self, "StorageScsiDeviceDescriptor", parent_mo_or_dn, **kwargs)

