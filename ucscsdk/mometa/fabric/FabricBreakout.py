"""This module contains the general information for FabricBreakout ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricBreakoutConsts():
    BREAKOUT_TYPE_10G_4X = "10g-4x"
    BREAKOUT_TYPE_25G_4X = "25g-4x"
    BREAKOUT_TYPE_UNKNOWN = "unknown"


class FabricBreakout(ManagedObject):
    """This is FabricBreakout class."""

    consts = FabricBreakoutConsts()
    naming_props = set(['slotId', 'portId'])

    mo_meta = MoMeta("FabricBreakout", "fabricBreakout", "breakout-slot-[slot_id]-port-[port_id]", VersionMeta.Version141a, "InputOutput", 0x7f, [], ["admin", "ext-lan-config", "ext-lan-policy", "ext-san-config", "ext-san-policy"], ['fabricCablingSw'], [], ["Get"])

    prop_meta = {
        "breakout_type": MoPropertyMeta("breakout_type", "breakoutType", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["10g-4x", "25g-4x", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-108"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], ["1-2"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "breakoutType": "breakout_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "portId": "port_id", 
        "rn": "rn", 
        "slotId": "slot_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, port_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.port_id = port_id
        self.breakout_type = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "FabricBreakout", parent_mo_or_dn, **kwargs)

