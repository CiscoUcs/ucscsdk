"""This module contains the general information for EquipmentBreakoutCap ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentBreakoutCapConsts():
    pass


class EquipmentBreakoutCap(ManagedObject):
    """This is EquipmentBreakoutCap class."""

    consts = EquipmentBreakoutCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentBreakoutCap", "equipmentBreakoutCap", "breakout-cap", VersionMeta.Version141a, "InputOutput", 0x1f, [], [""], [u'equipmentSwitchCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "phy_port_bitmask": MoPropertyMeta("phy_port_bitmask", "phyPortBitmask", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((p45|p41|p37|p33|p29|p25|p21|p17|p13|p9|p5|p1|p46|p42|p38|p34|p30|p26|p22|p18|p14|p10|p6|p2|p47|p43|p39|p35|p31|p27|p23|p19|p15|p11|p7|p3|p48|p44|p40|p36|p32|p28|p24|p20|p16|p12|p8|p4|all|defaultValue),){0,49}(p45|p41|p37|p33|p29|p25|p21|p17|p13|p9|p5|p1|p46|p42|p38|p34|p30|p26|p22|p18|p14|p10|p6|p2|p47|p43|p39|p35|p31|p27|p23|p19|p15|p11|p7|p3|p48|p44|p40|p36|p32|p28|p24|p20|p16|p12|p8|p4|all|defaultValue){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "phyPortBitmask": "phy_port_bitmask", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.name = None
        self.phy_port_bitmask = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentBreakoutCap", parent_mo_or_dn, **kwargs)

