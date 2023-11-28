"""This module contains the general information for StatsDbMigrationStatus ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StatsDbMigrationStatusConsts():
    MIGRATE_STATUS_FAIL = "fail"
    MIGRATE_STATUS_IN_PROGRESS = "inProgress"
    MIGRATE_STATUS_PENDING = "pending"
    MIGRATE_STATUS_SKIP = "skip"
    MIGRATE_STATUS_SUCCESS = "success"


class StatsDbMigrationStatus(ManagedObject):
    """This is StatsDbMigrationStatus class."""

    consts = StatsDbMigrationStatusConsts()
    naming_props = set([])

    mo_meta = MoMeta("StatsDbMigrationStatus", "statsDbMigrationStatus", "dbMigrationStatus", VersionMeta.Version111b, "InputOutput", 0x3f, [], ["admin"], ['statsHolder'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "migrate_status": MoPropertyMeta("migrate_status", "migrateStatus", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["fail", "inProgress", "pending", "skip", "success"], []), 
        "percentage": MoPropertyMeta("percentage", "percentage", "uint", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "migrateStatus": "migrate_status", 
        "percentage": "percentage", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.migrate_status = None
        self.percentage = None
        self.status = None

        ManagedObject.__init__(self, "StatsDbMigrationStatus", parent_mo_or_dn, **kwargs)

