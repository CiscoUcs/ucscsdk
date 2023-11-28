"""This module contains the general information for EquipmentBeaconLed ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentBeaconLedConsts():
    ADMIN_STATE_BLINKING = "blinking"
    ADMIN_STATE_ETH = "eth"
    ADMIN_STATE_FC = "fc"
    ADMIN_STATE_OFF = "off"
    ADMIN_STATE_ON = "on"
    COLOR_AMBER = "amber"
    COLOR_BLUE = "blue"
    COLOR_GREEN = "green"
    COLOR_RED = "red"
    COLOR_UNKNOWN = "unknown"
    OPER_STATE_BLINKING = "blinking"
    OPER_STATE_ETH = "eth"
    OPER_STATE_FC = "fc"
    OPER_STATE_OFF = "off"
    OPER_STATE_ON = "on"
    OPER_STATE_UNKNOWN = "unknown"


class EquipmentBeaconLed(ManagedObject):
    """This is EquipmentBeaconLed class."""

    consts = EquipmentBeaconLedConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentBeaconLed", "equipmentBeaconLed", "beacon", VersionMeta.Version112a, "InputOutput", 0x7f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['computeBlade', 'computeRackUnit', 'computeServerUnit', 'equipmentChassis', 'equipmentFanModule', 'equipmentFex', 'equipmentIOCard', 'equipmentPsu'], [], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["blinking", "eth", "fc", "off", "on"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "color": MoPropertyMeta("color", "color", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["amber", "blue", "green", "red", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blinking", "eth", "fc", "off", "on", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "color": "color", 
        "dn": "dn", 
        "id": "id", 
        "name": "name", 
        "operState": "oper_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.color = None
        self.id = None
        self.name = None
        self.oper_state = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentBeaconLed", parent_mo_or_dn, **kwargs)

