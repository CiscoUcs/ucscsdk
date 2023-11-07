"""This module contains the general information for FabricLanPinTarget ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricLanPinTargetConsts():
    FABRIC_ID_A = "A"
    FABRIC_ID_B = "B"
    FABRIC_ID_NONE = "NONE"
    FABRIC_ID_DUAL = "dual"
    FABRIC_ID_MGMT = "mgmt"
    TARGET_STATUS_INVALID = "invalid"
    TARGET_STATUS_VALID = "valid"


class FabricLanPinTarget(ManagedObject):
    """This is FabricLanPinTarget class."""

    consts = FabricLanPinTargetConsts()
    naming_props = set(['fabricId'])

    mo_meta = MoMeta("FabricLanPinTarget", "fabricLanPinTarget", "target-[fabric_id]", VersionMeta.Version141a, "InputOutput", 0x1ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricLanPinGroup'], [], ["Get"])

    prop_meta = {
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-108"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []), 
        "fabric_id": MoPropertyMeta("fabric_id", "fabricId", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["A", "B", "NONE", "dual", "mgmt"], []), 
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-20"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1-2"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "target_status": MoPropertyMeta("target_status", "targetStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["invalid", "valid"], []), 
    }

    prop_map = {
        "aggrPortId": "aggr_port_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "fabricId": "fabric_id", 
        "portId": "port_id", 
        "rn": "rn", 
        "slotId": "slot_id", 
        "status": "status", 
        "targetStatus": "target_status", 
    }

    def __init__(self, parent_mo_or_dn, fabric_id, **kwargs):
        self._dirty_mask = 0
        self.fabric_id = fabric_id
        self.aggr_port_id = None
        self.child_action = None
        self.ep_dn = None
        self.port_id = None
        self.slot_id = None
        self.status = None
        self.target_status = None

        ManagedObject.__init__(self, "FabricLanPinTarget", parent_mo_or_dn, **kwargs)

