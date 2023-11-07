"""This module contains the general information for EquipmentStorageProcessorCap ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentStorageProcessorCapConsts():
    VIRTUALIZED_CESUPPORTED_FALSE = "false"
    VIRTUALIZED_CESUPPORTED_NO = "no"
    VIRTUALIZED_CESUPPORTED_TRUE = "true"
    VIRTUALIZED_CESUPPORTED_YES = "yes"


class EquipmentStorageProcessorCap(ManagedObject):
    """This is EquipmentStorageProcessorCap class."""

    consts = EquipmentStorageProcessorCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentStorageProcessorCap", "equipmentStorageProcessorCap", "storage-proc-cap", VersionMeta.Version131a, "InputOutput", 0xf, [], ["read-only"], ['equipmentBladeCapProvider', 'equipmentRackUnitCapProvider', 'equipmentServerUnitCapProvider'], ['equipmentImpliedStorageEnclosureDef'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "virtualized_ce_supported": MoPropertyMeta("virtualized_ce_supported", "virtualizedCESupported", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "virtualizedCESupported": "virtualized_ce_supported", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.virtualized_ce_supported = None

        ManagedObject.__init__(self, "EquipmentStorageProcessorCap", parent_mo_or_dn, **kwargs)

