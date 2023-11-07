"""This module contains the general information for StorageSnapshotCtx ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageSnapshotCtxConsts():
    LUN_CFG_ACTION_DELETE = "delete"
    LUN_CFG_ACTION_OFFLINE = "offline"
    LUN_CFG_ACTION_ONLINE = "online"
    LUN_CFG_ACTION_RESTORE_SNAPSHOT = "restore-snapshot"
    LUN_CFG_ACTION_TRIGGERED = "triggered"
    TS_CREATED_ = ""


class StorageSnapshotCtx(ManagedObject):
    """This is StorageSnapshotCtx class."""

    consts = StorageSnapshotCtxConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageSnapshotCtx", "storageSnapshotCtx", "snap-ctx", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['storageScsiLun'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "lun_cfg_action": MoPropertyMeta("lun_cfg_action", "lunCfgAction", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["delete", "offline", "online", "restore-snapshot", "triggered"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "snap_percent": MoPropertyMeta("snap_percent", "snapPercent", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "src_lun_dn": MoPropertyMeta("src_lun_dn", "srcLunDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "src_lun_name": MoPropertyMeta("src_lun_name", "srcLunName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "ts_created": MoPropertyMeta("ts_created", "tsCreated", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lunCfgAction": "lun_cfg_action", 
        "rn": "rn", 
        "snapPercent": "snap_percent", 
        "srcLunDn": "src_lun_dn", 
        "srcLunName": "src_lun_name", 
        "status": "status", 
        "tsCreated": "ts_created", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.lun_cfg_action = None
        self.snap_percent = None
        self.src_lun_dn = None
        self.src_lun_name = None
        self.status = None
        self.ts_created = None

        ManagedObject.__init__(self, "StorageSnapshotCtx", parent_mo_or_dn, **kwargs)

