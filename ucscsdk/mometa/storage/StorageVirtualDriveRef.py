"""This module contains the general information for StorageVirtualDriveRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageVirtualDriveRefConsts():
    ADMIN_STATE_OFFLINE = "offline"
    ADMIN_STATE_ONLINE = "online"
    ADMIN_STATE_UNDEPLOYED = "undeployed"
    CONFIG_STATE_N_A = "N/A"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLY_FAILED = "apply-failed"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_NOT_IN_USE = "not-in-use"
    CONFIG_STATE_ORPHANED = "orphaned"
    CONFIG_STATE_UNKNOWN = "unknown"
    IS_BOOTABLE_DISABLED = "disabled"
    IS_BOOTABLE_ENABLED = "enabled"
    ORDER_NOT_APPLICABLE = "not-applicable"
    RAID_LEVEL_MIRROR = "mirror"
    RAID_LEVEL_MIRROR_STRIPE = "mirror-stripe"
    RAID_LEVEL_RAID = "raid"
    RAID_LEVEL_SIMPLE = "simple"
    RAID_LEVEL_STRIPE = "stripe"
    RAID_LEVEL_STRIPE_DUAL_PARITY = "stripe-dual-parity"
    RAID_LEVEL_STRIPE_DUAL_PARITY_STRIPE = "stripe-dual-parity-stripe"
    RAID_LEVEL_STRIPE_PARITY = "stripe-parity"
    RAID_LEVEL_STRIPE_PARITY_STRIPE = "stripe-parity-stripe"
    RAID_LEVEL_UNSPECIFIED = "unspecified"


class StorageVirtualDriveRef(ManagedObject):
    """This is StorageVirtualDriveRef class."""

    consts = StorageVirtualDriveRefConsts()
    naming_props = set(['lunItemName'])

    mo_meta = MoMeta("StorageVirtualDriveRef", "storageVirtualDriveRef", "vdrive-ref-[lun_item_name]", VersionMeta.Version131a, "InputOutput", 0xff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['computeInstance', 'lsServer'], ['lstorageDiskGroupConfigDef', 'storageLunResourceSelectionLog', 'storageVirtualDriveRefOperation'], ["Get"])

    prop_meta = {
        "admin_name": MoPropertyMeta("admin_name", "adminName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,15}""", [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["offline", "online", "undeployed"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A", "applied", "apply-failed", "applying", "not-applied", "not-in-use", "orphaned", "unknown"], []), 
        "disk_selection_order": MoPropertyMeta("disk_selection_order", "diskSelectionOrder", "ushort", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "disk_selection_ts": MoPropertyMeta("disk_selection_ts", "diskSelectionTs", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "is_bootable": MoPropertyMeta("is_bootable", "isBootable", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
        "lun_dn": MoPropertyMeta("lun_dn", "lunDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "lun_item_dn": MoPropertyMeta("lun_item_dn", "lunItemDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "lun_item_name": MoPropertyMeta("lun_item_name", "lunItemName", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x10, 1, 32, None, [], []), 
        "lun_name": MoPropertyMeta("lun_name", "lunName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,15}""", [], []), 
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-64"]), 
        "raid_level": MoPropertyMeta("raid_level", "raidLevel", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["mirror", "mirror-stripe", "raid", "simple", "stripe", "stripe-dual-parity", "stripe-dual-parity-stripe", "stripe-parity", "stripe-parity-stripe", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
        "vendor_uuid": MoPropertyMeta("vendor_uuid", "vendorUuid", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
    }

    prop_map = {
        "adminName": "admin_name", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "diskSelectionOrder": "disk_selection_order", 
        "diskSelectionTs": "disk_selection_ts", 
        "dn": "dn", 
        "isBootable": "is_bootable", 
        "lunDn": "lun_dn", 
        "lunItemDn": "lun_item_dn", 
        "lunItemName": "lun_item_name", 
        "lunName": "lun_name", 
        "order": "order", 
        "raidLevel": "raid_level", 
        "rn": "rn", 
        "size": "size", 
        "status": "status", 
        "uuid": "uuid", 
        "vendorUuid": "vendor_uuid", 
    }

    def __init__(self, parent_mo_or_dn, lun_item_name, **kwargs):
        self._dirty_mask = 0
        self.lun_item_name = lun_item_name
        self.admin_name = None
        self.admin_state = None
        self.child_action = None
        self.config_state = None
        self.disk_selection_order = None
        self.disk_selection_ts = None
        self.is_bootable = None
        self.lun_dn = None
        self.lun_item_dn = None
        self.lun_name = None
        self.order = None
        self.raid_level = None
        self.size = None
        self.status = None
        self.uuid = None
        self.vendor_uuid = None

        ManagedObject.__init__(self, "StorageVirtualDriveRef", parent_mo_or_dn, **kwargs)

