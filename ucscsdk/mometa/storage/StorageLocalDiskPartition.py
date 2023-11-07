"""This module contains the general information for StorageLocalDiskPartition ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageLocalDiskPartitionConsts():
    BOOTABLE_FALSE = "false"
    BOOTABLE_TRUE = "true"
    BOOTABLE_UNKNOWN = "unknown"
    PARTITION_END_UNKNOWN = "unknown"
    PARTITION_START_UNKNOWN = "unknown"
    SIZE_UNKNOWN = "unknown"
    TYPE_EMPTY = "empty"
    TYPE_EXTENDED = "extended"
    TYPE_LINUX = "linux"
    TYPE_LINUX_LVM = "linux-lvm"
    TYPE_LINUX_SWAP = "linux-swap"


class StorageLocalDiskPartition(ManagedObject):
    """This is StorageLocalDiskPartition class."""

    consts = StorageLocalDiskPartitionConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("StorageLocalDiskPartition", "storageLocalDiskPartition", "partition-[id]", VersionMeta.Version131a, "InputOutput", 0x1ff, [], ["read-only"], ['storageLocalDisk', 'storageLocalDiskConfigDef', 'storageLocalDiskConfigPolicy'], [], ["Get"])

    prop_meta = {
        "bootable": MoPropertyMeta("bootable", "bootable", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "true", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "partition_end": MoPropertyMeta("partition_end", "partitionEnd", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "partition_start": MoPropertyMeta("partition_start", "partitionStart", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unknown"], ["0-4294967295"]), 
        "raw_type_desc": MoPropertyMeta("raw_type_desc", "rawTypeDesc", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["unknown"], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["empty", "extended", "linux", "linux-lvm", "linux-swap"], ["0-4294967295"]), 
    }

    prop_map = {
        "bootable": "bootable", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "name": "name", 
        "partitionEnd": "partition_end", 
        "partitionStart": "partition_start", 
        "rawTypeDesc": "raw_type_desc", 
        "rn": "rn", 
        "size": "size", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.bootable = None
        self.child_action = None
        self.name = None
        self.partition_end = None
        self.partition_start = None
        self.raw_type_desc = None
        self.size = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "StorageLocalDiskPartition", parent_mo_or_dn, **kwargs)

