"""This module contains the general information for EquipmentManufacturingDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentManufacturingDefConsts():
    pass


class EquipmentManufacturingDef(ManagedObject):
    """This is EquipmentManufacturingDef class."""

    consts = EquipmentManufacturingDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentManufacturingDef", "equipmentManufacturingDef", "manufacturing", VersionMeta.Version101a, "InputOutput", 0xf, [], [""], ['adaptorFruCapProvider', 'diagSrvCapProvider', 'equipmentBladeCapProvider', 'equipmentChassisCapProvider', 'equipmentCrossFabricModuleCapProvider', 'equipmentFanModuleCapProvider', 'equipmentFexCapProvider', 'equipmentGemCapProvider', 'equipmentGraphicsCardCapProvider', 'equipmentHostIfCapProvider', 'equipmentIOCardCapProvider', 'equipmentLocalDiskCapProvider', 'equipmentLocalDiskControllerCapProvider', 'equipmentMemoryUnitCapProvider', 'equipmentPcieConnectorCapProvider', 'equipmentPcieNodeCapProvider', 'equipmentProcessorUnitCapProvider', 'equipmentPsuCapProvider', 'equipmentRackUnitCapProvider', 'equipmentServerUnitCapProvider', 'equipmentSwitchCapProvider', 'equipmentSwitchIOCardCapProvider', 'equipmentSystemFruCapProvider'], [], ["Get"])

    prop_meta = {
        "caption": MoPropertyMeta("caption", "caption", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "clei": MoPropertyMeta("clei", "clei", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fru_major_type": MoPropertyMeta("fru_major_type", "fruMajorType", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "fru_minor_type": MoPropertyMeta("fru_minor_type", "fruMinorType", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oem_name": MoPropertyMeta("oem_name", "oemName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oem_part_number": MoPropertyMeta("oem_part_number", "oemPartNumber", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "part_number": MoPropertyMeta("part_number", "partNumber", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pid": MoPropertyMeta("pid", "pid", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "series": MoPropertyMeta("series", "series", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "sku": MoPropertyMeta("sku", "sku", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor_equipment_type": MoPropertyMeta("vendor_equipment_type", "vendorEquipmentType", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "vid": MoPropertyMeta("vid", "vid", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "caption": "caption", 
        "childAction": "child_action", 
        "clei": "clei", 
        "description": "description", 
        "dn": "dn", 
        "fruMajorType": "fru_major_type", 
        "fruMinorType": "fru_minor_type", 
        "name": "name", 
        "oemName": "oem_name", 
        "oemPartNumber": "oem_part_number", 
        "partNumber": "part_number", 
        "pid": "pid", 
        "rn": "rn", 
        "series": "series", 
        "sku": "sku", 
        "status": "status", 
        "vendorEquipmentType": "vendor_equipment_type", 
        "vid": "vid", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.caption = None
        self.child_action = None
        self.clei = None
        self.description = None
        self.fru_major_type = None
        self.fru_minor_type = None
        self.name = None
        self.oem_name = None
        self.oem_part_number = None
        self.part_number = None
        self.pid = None
        self.series = None
        self.sku = None
        self.status = None
        self.vendor_equipment_type = None
        self.vid = None

        ManagedObject.__init__(self, "EquipmentManufacturingDef", parent_mo_or_dn, **kwargs)

