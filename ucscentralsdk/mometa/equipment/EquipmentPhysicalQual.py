"""This module contains the general information for EquipmentPhysicalQual ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class EquipmentPhysicalQualConsts():
    pass


class EquipmentPhysicalQual(ManagedObject):
    """This is EquipmentPhysicalQual class."""

    consts = EquipmentPhysicalQualConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentPhysicalQual", "equipmentPhysicalQual", "physicalqual", None, "InputOutput", 0x1f, [], ["admin", "pn-policy"], [u'equipmentQual'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", None, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%\(\)\*\+,\-\./:;\?@\[\\\]\^_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "model": "model", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.model = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPhysicalQual", parent_mo_or_dn, **kwargs)

