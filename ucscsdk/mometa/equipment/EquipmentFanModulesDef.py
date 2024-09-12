"""This module contains the general information for EquipmentFanModulesDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentFanModulesDefConsts():
    pass


class EquipmentFanModulesDef(ManagedObject):
    """This is EquipmentFanModulesDef class."""

    consts = EquipmentFanModulesDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentFanModulesDef", "equipmentFanModulesDef", "fanmodules", VersionMeta.Version201t, "InputOutput", 0x1f, [], [""], ['equipmentCrossFabricModuleCapProvider', 'equipmentIOCardCapProvider', 'equipmentSwitchIOCardCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201t, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201t, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fan_module_capacity": MoPropertyMeta("fan_module_capacity", "fanModuleCapacity", "ushort", VersionMeta.Version201t, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version201t, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201t, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version201t, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201t, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201t, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version201t, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fanModuleCapacity": "fan_module_capacity", 
        "model": "model", 
        "name": "name", 
        "revision": "revision", 
        "rn": "rn", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.fan_module_capacity = None
        self.model = None
        self.name = None
        self.revision = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "EquipmentFanModulesDef", parent_mo_or_dn, **kwargs)

