"""This module contains the general information for DupeChangeTracker ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class DupeChangeTrackerConsts():
    OPERATION_CREATE = "create"
    OPERATION_DELETE = "delete"


class DupeChangeTracker(ManagedObject):
    """This is DupeChangeTracker class."""

    consts = DupeChangeTrackerConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("DupeChangeTracker", "dupeChangeTracker", "changetracker-[id]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['dupeChangeTrackerEp'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "operation": MoPropertyMeta("operation", "operation", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["create", "delete"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "scope_dn": MoPropertyMeta("scope_dn", "scopeDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "update_time": MoPropertyMeta("update_time", "updateTime", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "operation": "operation", 
        "rn": "rn", 
        "scopeDn": "scope_dn", 
        "status": "status", 
        "updateTime": "update_time", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.operation = None
        self.scope_dn = None
        self.status = None
        self.update_time = None

        ManagedObject.__init__(self, "DupeChangeTracker", parent_mo_or_dn, **kwargs)

