"""This module contains the general information for StorageVirtualDriveEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageVirtualDriveEpConsts():
    BOOTABLE_FALSE = "false"
    BOOTABLE_TRUE = "true"
    BOOTABLE_UNKNOWN = "unknown"
    DRIVE_STATE_CACHE_DEGRADED = "cache-degraded"
    DRIVE_STATE_DEGRADED = "degraded"
    DRIVE_STATE_OFFLINE = "offline"
    DRIVE_STATE_OPTIMAL = "optimal"
    DRIVE_STATE_PARTIALLY_DEGRADED = "partially-degraded"
    DRIVE_STATE_REBUILDING = "rebuilding"
    DRIVE_STATE_UNKNOWN = "unknown"
    ID_UNSPECIFIED = "unspecified"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    OPER_DEVICE_ID_UNSPECIFIED = "unspecified"


class StorageVirtualDriveEp(ManagedObject):
    """This is StorageVirtualDriveEp class."""

    consts = StorageVirtualDriveEpConsts()
    naming_props = set(['containerId', 'id'])

    mo_meta = MoMeta("StorageVirtualDriveEp", "storageVirtualDriveEp", "vd-ep-[container_id]-id-[id]", VersionMeta.Version151a, "InputOutput", 0x3f, [], ["read-only"], ['storageController'], [], ["Get"])

    prop_meta = {
        "bootable": MoPropertyMeta("bootable", "bootable", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "true", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "container_id": MoPropertyMeta("container_id", "containerId", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x2, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "drive_state": MoPropertyMeta("drive_state", "driveState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cache-degraded", "degraded", "offline", "optimal", "partially-degraded", "rebuilding", "unknown"], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x8, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_device_id": MoPropertyMeta("oper_device_id", "operDeviceId", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
        "vd_dn": MoPropertyMeta("vd_dn", "vdDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "vendor_uuid": MoPropertyMeta("vendor_uuid", "vendorUuid", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
    }

    prop_map = {
        "bootable": "bootable", 
        "childAction": "child_action", 
        "containerId": "container_id", 
        "dn": "dn", 
        "driveState": "drive_state", 
        "id": "id", 
        "lc": "lc", 
        "name": "name", 
        "operDeviceId": "oper_device_id", 
        "rn": "rn", 
        "status": "status", 
        "uuid": "uuid", 
        "vdDn": "vd_dn", 
        "vendorUuid": "vendor_uuid", 
    }

    def __init__(self, parent_mo_or_dn, container_id, id, **kwargs):
        self._dirty_mask = 0
        self.container_id = container_id
        self.id = id
        self.bootable = None
        self.child_action = None
        self.drive_state = None
        self.lc = None
        self.name = None
        self.oper_device_id = None
        self.status = None
        self.uuid = None
        self.vd_dn = None
        self.vendor_uuid = None

        ManagedObject.__init__(self, "StorageVirtualDriveEp", parent_mo_or_dn, **kwargs)

