"""This module contains the general information for StorageLunCounters ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageLunCountersConsts():
    pass


class StorageLunCounters(ManagedObject):
    """This is StorageLunCounters class."""

    consts = StorageLunCountersConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageLunCounters", "storageLunCounters", "lun-counters", VersionMeta.Version131a, "InputOutput", 0xf, [], ["read-only"], ['storagePartition'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "lun_count_in_use": MoPropertyMeta("lun_count_in_use", "lunCountInUse", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lun_count_not_in_use": MoPropertyMeta("lun_count_not_in_use", "lunCountNotInUse", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lun_count_orphaned": MoPropertyMeta("lun_count_orphaned", "lunCountOrphaned", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lun_replica_count": MoPropertyMeta("lun_replica_count", "lunReplicaCount", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lun_snapshot_count": MoPropertyMeta("lun_snapshot_count", "lunSnapshotCount", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lunCountInUse": "lun_count_in_use", 
        "lunCountNotInUse": "lun_count_not_in_use", 
        "lunCountOrphaned": "lun_count_orphaned", 
        "lunReplicaCount": "lun_replica_count", 
        "lunSnapshotCount": "lun_snapshot_count", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.lun_count_in_use = None
        self.lun_count_not_in_use = None
        self.lun_count_orphaned = None
        self.lun_replica_count = None
        self.lun_snapshot_count = None
        self.status = None

        ManagedObject.__init__(self, "StorageLunCounters", parent_mo_or_dn, **kwargs)

