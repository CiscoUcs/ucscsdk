"""This module contains the general information for StorageScsiLunInstRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageScsiLunInstRefConsts():
    ADMIN_STATE_OFFLINE = "offline"
    ADMIN_STATE_ONLINE = "online"
    ADMIN_STATE_UNDEPLOYED = "undeployed"
    AUTO_AQUIRED_FALSE = "false"
    AUTO_AQUIRED_NO = "no"
    AUTO_AQUIRED_TRUE = "true"
    AUTO_AQUIRED_YES = "yes"
    CONFIG_STATE_N_A = "N/A"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLY_FAILED = "apply-failed"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_NOT_IN_USE = "not-in-use"
    CONFIG_STATE_ORPHANED = "orphaned"
    CONFIG_STATE_UNKNOWN = "unknown"
    LUN_MASK_ID_UNASSIGNED = "unassigned"
    LUN_STATUS_OFFLINE = "offline"
    LUN_STATUS_ONLINE = "online"
    LUN_STATUS_UNDEFINED = "undefined"
    PREFERRED_LUN_MASK_ID_UNASSIGNED = "unassigned"
    SNAPSHOT_ADMIN_STATE_ABORT_REPLICATION = "abort-replication"
    SNAPSHOT_ADMIN_STATE_CREATE = "create"
    SNAPSHOT_ADMIN_STATE_CREATE_LUN_REPLICA = "create-lun-replica"
    SNAPSHOT_ADMIN_STATE_REPLICATION_RESTORE = "replication-restore"
    SNAPSHOT_ADMIN_STATE_SET_REPLICATION_OFFLINE = "set-replication-offline"
    SNAPSHOT_ADMIN_STATE_SET_REPLICATION_ONLINE = "set-replication-online"
    SNAPSHOT_ADMIN_STATE_UNDEFINED = "undefined"


class StorageScsiLunInstRef(ManagedObject):
    """This is StorageScsiLunInstRef class."""

    consts = StorageScsiLunInstRefConsts()
    naming_props = set(['lunItemName'])

    mo_meta = MoMeta("StorageScsiLunInstRef", "storageScsiLunInstRef", "lun-inst-ref-[lun_item_name]", VersionMeta.Version131a, "InputOutput", 0xfff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['lsServer'], [], [None])

    prop_meta = {
        "admin_name": MoPropertyMeta("admin_name", "adminName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,15}""", [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["offline", "online", "undeployed"], []), 
        "auto_aquired": MoPropertyMeta("auto_aquired", "autoAquired", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A", "applied", "apply-failed", "applying", "not-applied", "not-in-use", "orphaned", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "lun_dn": MoPropertyMeta("lun_dn", "lunDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, 0, 256, None, [], []), 
        "lun_item_dn": MoPropertyMeta("lun_item_dn", "lunItemDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "lun_item_name": MoPropertyMeta("lun_item_name", "lunItemName", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x40, 1, 32, None, [], []), 
        "lun_mask_id": MoPropertyMeta("lun_mask_id", "lunMaskId", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unassigned"], ["0-4294967295"]), 
        "lun_status": MoPropertyMeta("lun_status", "lunStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["offline", "online", "undefined"], []), 
        "preferred_lun_mask_id": MoPropertyMeta("preferred_lun_mask_id", "preferredLunMaskId", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["unassigned"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["1-10240"]), 
        "snapshot_admin_state": MoPropertyMeta("snapshot_admin_state", "snapshotAdminState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["abort-replication", "create", "create-lun-replica", "replication-restore", "set-replication-offline", "set-replication-online", "undefined"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "volume_dn": MoPropertyMeta("volume_dn", "volumeDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
    }

    prop_map = {
        "adminName": "admin_name", 
        "adminState": "admin_state", 
        "autoAquired": "auto_aquired", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "dn": "dn", 
        "lunDn": "lun_dn", 
        "lunItemDn": "lun_item_dn", 
        "lunItemName": "lun_item_name", 
        "lunMaskId": "lun_mask_id", 
        "lunStatus": "lun_status", 
        "preferredLunMaskId": "preferred_lun_mask_id", 
        "rn": "rn", 
        "size": "size", 
        "snapshotAdminState": "snapshot_admin_state", 
        "status": "status", 
        "volumeDn": "volume_dn", 
    }

    def __init__(self, parent_mo_or_dn, lun_item_name, **kwargs):
        self._dirty_mask = 0
        self.lun_item_name = lun_item_name
        self.admin_name = None
        self.admin_state = None
        self.auto_aquired = None
        self.child_action = None
        self.config_state = None
        self.lun_dn = None
        self.lun_item_dn = None
        self.lun_mask_id = None
        self.lun_status = None
        self.preferred_lun_mask_id = None
        self.size = None
        self.snapshot_admin_state = None
        self.status = None
        self.volume_dn = None

        ManagedObject.__init__(self, "StorageScsiLunInstRef", parent_mo_or_dn, **kwargs)

