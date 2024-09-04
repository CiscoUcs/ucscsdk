"""This module contains the general information for EquipmentPicture ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentPictureConsts():
    TYPE_BACK = "back"
    TYPE_BOTTOM = "bottom"
    TYPE_FRONT = "front"
    TYPE_LEFT = "left"
    TYPE_RIGHT = "right"
    TYPE_TOP = "top"
    TYPE_UNKNOWN = "unknown"


class EquipmentPicture(ManagedObject):
    """This is EquipmentPicture class."""

    consts = EquipmentPictureConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("EquipmentPicture", "equipmentPicture", "picture-[type]", VersionMeta.Version101a, "InputOutput", 0x1f, [], [""], ['adaptorFruCapProvider', 'diagSrvCapProvider', 'equipmentBladeCapProvider', 'equipmentChassisCapProvider', 'equipmentCrossFabricModuleCapProvider', 'equipmentFanModuleCapProvider', 'equipmentFexCapProvider', 'equipmentGemCapProvider', 'equipmentGraphicsCardCapProvider', 'equipmentHostIfCapProvider', 'equipmentIOCardCapProvider', 'equipmentLocalDiskCapProvider', 'equipmentLocalDiskControllerCapProvider', 'equipmentMemoryUnitCapProvider', 'equipmentPcieConnectorCapProvider', 'equipmentPcieNodeCapProvider', 'equipmentProcessorUnitCapProvider', 'equipmentPsuCapProvider', 'equipmentRackUnitCapProvider', 'equipmentServerUnitCapProvider', 'equipmentSwitchCapProvider', 'equipmentSwitchIOCardCapProvider', 'equipmentSystemFruCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "file_name": MoPropertyMeta("file_name", "fileName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["back", "bottom", "front", "left", "right", "top", "unknown"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fileName": "file_name", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.file_name = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPicture", parent_mo_or_dn, **kwargs)

