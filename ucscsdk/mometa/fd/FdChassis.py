"""This module contains the general information for FdChassis ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FdChassisConsts():
    CHASSIS_ID_N_A = "N/A"


class FdChassis(ManagedObject):
    """This is FdChassis class."""

    consts = FdChassisConsts()
    naming_props = set(['chassisId'])

    mo_meta = MoMeta("FdChassis", "fdChassis", "chassis-[chassis_id]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricSystem'], ['fdBlade', 'messageEp'], ["get"])

    prop_meta = {
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x2, None, None, None, ["N/A"], ["0-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, chassis_id, **kwargs):
        self._dirty_mask = 0
        self.chassis_id = chassis_id
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "FdChassis", parent_mo_or_dn, **kwargs)

