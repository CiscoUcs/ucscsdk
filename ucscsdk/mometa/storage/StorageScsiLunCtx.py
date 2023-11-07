"""This module contains the general information for StorageScsiLunCtx ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageScsiLunCtxConsts():
    CLONE_STATUS_NOT_APPLICABLE = "not-applicable"
    CLONE_STATUS_UNKNOWN = "unknown"
    LUN_CFG_ACTION_ABORT_REPLICATION = "abort-replication"
    LUN_CFG_ACTION_CREATE_REPLICATION = "create-replication"
    LUN_CFG_ACTION_CREATE_SNAPSHOT = "create-snapshot"
    LUN_CFG_ACTION_DELETE = "delete"
    LUN_CFG_ACTION_DISABLE_REPLICATION = "disable-replication"
    LUN_CFG_ACTION_ENABLE_REPLICATION = "enable-replication"
    LUN_CFG_ACTION_OFFLINE = "offline"
    LUN_CFG_ACTION_ONLINE = "online"
    LUN_CFG_ACTION_RESTORE = "restore"
    LUN_CFG_ACTION_TRIGGERED = "triggered"


class StorageScsiLunCtx(ManagedObject):
    """This is StorageScsiLunCtx class."""

    consts = StorageScsiLunCtxConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageScsiLunCtx", "storageScsiLunCtx", "lun-ctx", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['storageScsiLun'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "clone_status": MoPropertyMeta("clone_status", "cloneStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable", "unknown"], ["0-101"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "last_snapshot_id": MoPropertyMeta("last_snapshot_id", "lastSnapshotId", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lun_cfg_action": MoPropertyMeta("lun_cfg_action", "lunCfgAction", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["abort-replication", "create-replication", "create-snapshot", "delete", "disable-replication", "enable-replication", "offline", "online", "restore", "triggered"], []), 
        "parent_lun_name": MoPropertyMeta("parent_lun_name", "parentLunName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "cloneStatus": "clone_status", 
        "dn": "dn", 
        "lastSnapshotId": "last_snapshot_id", 
        "lunCfgAction": "lun_cfg_action", 
        "parentLunName": "parent_lun_name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.clone_status = None
        self.last_snapshot_id = None
        self.lun_cfg_action = None
        self.parent_lun_name = None
        self.status = None

        ManagedObject.__init__(self, "StorageScsiLunCtx", parent_mo_or_dn, **kwargs)

