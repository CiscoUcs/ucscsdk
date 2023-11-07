"""This module contains the general information for EquipmentServerFeatureCap ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentServerFeatureCapConsts():
    CMOS_RESET_SUPPORTED_FALSE = "false"
    CMOS_RESET_SUPPORTED_NO = "no"
    CMOS_RESET_SUPPORTED_TRUE = "true"
    CMOS_RESET_SUPPORTED_YES = "yes"
    STORAGE_JBOD_MODE_SUPPORTED_FALSE = "false"
    STORAGE_JBOD_MODE_SUPPORTED_NO = "no"
    STORAGE_JBOD_MODE_SUPPORTED_TRUE = "true"
    STORAGE_JBOD_MODE_SUPPORTED_YES = "yes"


class EquipmentServerFeatureCap(ManagedObject):
    """This is EquipmentServerFeatureCap class."""

    consts = EquipmentServerFeatureCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentServerFeatureCap", "equipmentServerFeatureCap", "server-feature-cap", VersionMeta.Version141a, "InputOutput", 0xf, [], ["read-only"], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider', 'equipmentServerUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "adaptor_model": MoPropertyMeta("adaptor_model", "adaptorModel", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cmos_reset_supported": MoPropertyMeta("cmos_reset_supported", "cmosResetSupported", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "max_virtual_drives_per_server": MoPropertyMeta("max_virtual_drives_per_server", "maxVirtualDrivesPerServer", "ushort", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "max_virtual_eth_if_per_server": MoPropertyMeta("max_virtual_eth_if_per_server", "maxVirtualEthIfPerServer", "ushort", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "number_of_server_units": MoPropertyMeta("number_of_server_units", "numberOfServerUnits", "ushort", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_jbod_mode_supported": MoPropertyMeta("storage_jbod_mode_supported", "storageJbodModeSupported", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "adaptorModel": "adaptor_model", 
        "childAction": "child_action", 
        "cmosResetSupported": "cmos_reset_supported", 
        "dn": "dn", 
        "maxVirtualDrivesPerServer": "max_virtual_drives_per_server", 
        "maxVirtualEthIfPerServer": "max_virtual_eth_if_per_server", 
        "numberOfServerUnits": "number_of_server_units", 
        "rn": "rn", 
        "status": "status", 
        "storageJbodModeSupported": "storage_jbod_mode_supported", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.adaptor_model = None
        self.child_action = None
        self.cmos_reset_supported = None
        self.max_virtual_drives_per_server = None
        self.max_virtual_eth_if_per_server = None
        self.number_of_server_units = None
        self.status = None
        self.storage_jbod_mode_supported = None

        ManagedObject.__init__(self, "EquipmentServerFeatureCap", parent_mo_or_dn, **kwargs)

