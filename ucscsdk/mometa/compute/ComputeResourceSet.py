"""This module contains the general information for ComputeResourceSet ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeResourceSetConsts():
    STATE_INVENTORY_COMPLETE = "inventory-complete"
    STATE_INVENTORY_IN_PROGRESS = "inventory-in-progress"
    STATE_INVENTORY_PENDING = "inventory-pending"


class ComputeResourceSet(ManagedObject):
    """This is ComputeResourceSet class."""

    consts = ComputeResourceSetConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputeResourceSet", "computeResourceSet", "rsrc-set-[id]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin"], ['computeResourceSetManager'], ['computeResourceSetMember'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ushort", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "last_polled_ts": MoPropertyMeta("last_polled_ts", "lastPolledTs", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["inventory-complete", "inventory-in-progress", "inventory-pending"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "lastPolledTs": "last_polled_ts", 
        "rn": "rn", 
        "state": "state", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.last_polled_ts = None
        self.state = None
        self.status = None

        ManagedObject.__init__(self, "ComputeResourceSet", parent_mo_or_dn, **kwargs)

