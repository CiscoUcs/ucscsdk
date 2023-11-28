"""This module contains the general information for ComputePooledSlot ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputePooledSlotConsts():
    ASSIGNED_FALSE = "false"
    ASSIGNED_NO = "no"
    ASSIGNED_TRUE = "true"
    ASSIGNED_YES = "yes"
    CHASSIS_ID_N_A = "N/A"
    CONS_CNT_ASSIGNED_TO_SINGLE = "assigned-to-single"
    CONS_CNT_AVAILABLE = "available"
    OWNER_MANAGEMENT = "management"
    OWNER_POLICY = "policy"


class ComputePooledSlot(ManagedObject):
    """This is ComputePooledSlot class."""

    consts = ComputePooledSlotConsts()
    naming_props = set(['systemId', 'chassisId', 'slotId'])

    mo_meta = MoMeta("ComputePooledSlot", "computePooledSlot", "system-[system_id]-blade-[chassis_id]-[slot_id]", VersionMeta.Version111a, "InputOutput", 0x7f, [], ["admin", "pn-policy"], ['computePool'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "block_dn": MoPropertyMeta("block_dn", "blockDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x2, None, None, None, ["N/A"], ["1-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cons_cnt": MoPropertyMeta("cons_cnt", "consCnt", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["assigned-to-single", "available"], ["0-4294967295"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "id_released_time": MoPropertyMeta("id_released_time", "idReleasedTime", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["management", "policy"], []), 
        "poolable_dn": MoPropertyMeta("poolable_dn", "poolableDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "prev_assigned_to_dn": MoPropertyMeta("prev_assigned_to_dn", "prevAssignedToDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-8"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "system_id": MoPropertyMeta("system_id", "systemId", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []), 
    }

    prop_map = {
        "assigned": "assigned", 
        "assignedToDn": "assigned_to_dn", 
        "blockDn": "block_dn", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "consCnt": "cons_cnt", 
        "dn": "dn", 
        "idReleasedTime": "id_released_time", 
        "owner": "owner", 
        "poolableDn": "poolable_dn", 
        "prevAssignedToDn": "prev_assigned_to_dn", 
        "rn": "rn", 
        "slotId": "slot_id", 
        "status": "status", 
        "systemId": "system_id", 
    }

    def __init__(self, parent_mo_or_dn, system_id, chassis_id, slot_id, **kwargs):
        self._dirty_mask = 0
        self.system_id = system_id
        self.chassis_id = chassis_id
        self.slot_id = slot_id
        self.assigned = None
        self.assigned_to_dn = None
        self.block_dn = None
        self.child_action = None
        self.cons_cnt = None
        self.id_released_time = None
        self.owner = None
        self.poolable_dn = None
        self.prev_assigned_to_dn = None
        self.status = None

        ManagedObject.__init__(self, "ComputePooledSlot", parent_mo_or_dn, **kwargs)

