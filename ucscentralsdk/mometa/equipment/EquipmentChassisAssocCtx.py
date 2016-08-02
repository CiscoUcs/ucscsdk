"""This module contains the general information for EquipmentChassisAssocCtx ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class EquipmentChassisAssocCtxConsts():
    pass


class EquipmentChassisAssocCtx(ManagedObject):
    """This is EquipmentChassisAssocCtx class."""

    consts = EquipmentChassisAssocCtxConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentChassisAssocCtx", "equipmentChassisAssocCtx", "cp-assoc-ctx", None, "InputOutput", 0xf, [], ["read-only"], [u'equipmentChassisProfileAssocCtx'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fru_cap_dn": MoPropertyMeta("fru_cap_dn", "fruCapDn", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fruCapDn": "fru_cap_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.fru_cap_dn = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentChassisAssocCtx", parent_mo_or_dn, **kwargs)

