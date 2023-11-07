"""This module contains the general information for EquipmentAdvancedBootOrder ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentAdvancedBootOrderConsts():
    IS_SUPPORTED_FALSE = "false"
    IS_SUPPORTED_NO = "no"
    IS_SUPPORTED_TRUE = "true"
    IS_SUPPORTED_YES = "yes"


class EquipmentAdvancedBootOrder(ManagedObject):
    """This is EquipmentAdvancedBootOrder class."""

    consts = EquipmentAdvancedBootOrderConsts()
    naming_props = set(['isSupported'])

    mo_meta = MoMeta("EquipmentAdvancedBootOrder", "equipmentAdvancedBootOrder", "advbootordsupp-[is_supported]", VersionMeta.Version121a, "InputOutput", 0x3f, [], [""], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider', 'equipmentServerUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "is_supported": MoPropertyMeta("is_supported", "isSupported", "string", VersionMeta.Version121a, MoPropertyMeta.NAMING, 0x4, None, None, None, ["false", "no", "true", "yes"], []), 
        "min_bios_version": MoPropertyMeta("min_bios_version", "minBiosVersion", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "min_cimc_version": MoPropertyMeta("min_cimc_version", "minCimcVersion", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isSupported": "is_supported", 
        "minBiosVersion": "min_bios_version", 
        "minCimcVersion": "min_cimc_version", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, is_supported, **kwargs):
        self._dirty_mask = 0
        self.is_supported = is_supported
        self.child_action = None
        self.min_bios_version = None
        self.min_cimc_version = None
        self.name = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentAdvancedBootOrder", parent_mo_or_dn, **kwargs)

