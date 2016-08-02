"""This module contains the general information for EquipmentChassisQual ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class EquipmentChassisQualConsts():
    pass


class EquipmentChassisQual(ManagedObject):
    """This is EquipmentChassisQual class."""

    consts = EquipmentChassisQualConsts()
    naming_props = set([u'minId', u'maxId'])

    mo_meta = MoMeta("EquipmentChassisQual", "equipmentChassisQual", "chassis-from-[min_id]-to-[max_id]", None, "InputOutput", 0x3f, [], ["admin", "pn-policy"], [u'equipmentQual'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "max_id": MoPropertyMeta("max_id", "maxId", "uint", None, MoPropertyMeta.NAMING, 0x4, None, None, None, [], ["1-255"]), 
        "min_id": MoPropertyMeta("min_id", "minId", "uint", None, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-255"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maxId": "max_id", 
        "minId": "min_id", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, min_id, max_id, **kwargs):
        self._dirty_mask = 0
        self.min_id = min_id
        self.max_id = max_id
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentChassisQual", parent_mo_or_dn, **kwargs)

