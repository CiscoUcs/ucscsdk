"""This module contains the general information for FabricChassisEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricChassisEpConsts():
    CHASSIS_ID_N_A = "N/A"


class FabricChassisEp(ManagedObject):
    """This is FabricChassisEp class."""

    consts = FabricChassisEpConsts()
    naming_props = set(['chassisId'])

    mo_meta = MoMeta("FabricChassisEp", "fabricChassisEp", "chassis-[chassis_id]", VersionMeta.Version112a, "InputOutput", 0x1f, [], ["read-only"], ['fabricDceSrv'], ['fabricCartridgeSlotEp', 'fabricComputeSlotEp', 'fabricEnclosureSlotEp'], ["Get"])

    prop_meta = {
        "chassis_dn": MoPropertyMeta("chassis_dn", "chassisDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x2, None, None, None, ["N/A"], ["1-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "chassisDn": "chassis_dn", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, chassis_id, **kwargs):
        self._dirty_mask = 0
        self.chassis_id = chassis_id
        self.chassis_dn = None
        self.child_action = None
        self.model = None
        self.revision = None
        self.serial = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "FabricChassisEp", parent_mo_or_dn, **kwargs)

