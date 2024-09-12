"""This module contains the general information for EquipmentFruVariant ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentFruVariantConsts():
    pass


class EquipmentFruVariant(ManagedObject):
    """This is EquipmentFruVariant class."""

    consts = EquipmentFruVariantConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("EquipmentFruVariant", "equipmentFruVariant", "fruVariant-[type]", VersionMeta.Version201b, "InputOutput", 0x1f, [], [""], ['adaptorFruCapProvider', 'diagSrvCapProvider', 'equipmentBladeCapProvider', 'equipmentChassisCapProvider', 'equipmentCrossFabricModuleCapProvider', 'equipmentFanModuleCapProvider', 'equipmentFexCapProvider', 'equipmentGemCapProvider', 'equipmentGraphicsCardCapProvider', 'equipmentHostIfCapProvider', 'equipmentIOCardCapProvider', 'equipmentLocalDiskCapProvider', 'equipmentLocalDiskControllerCapProvider', 'equipmentMemoryUnitCapProvider', 'equipmentPcieConnectorCapProvider', 'equipmentPcieNodeCapProvider', 'equipmentProcessorUnitCapProvider', 'equipmentPsuCapProvider', 'equipmentRackUnitCapProvider', 'equipmentServerUnitCapProvider', 'equipmentSwitchCapProvider', 'equipmentSwitchIOCardCapProvider', 'equipmentSystemFruCapProvider'], [], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "pid": "pid", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.description = None
        self.pid = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentFruVariant", parent_mo_or_dn, **kwargs)

