"""This module contains the general information for EquipmentSwitchIOCardCapProvider ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentSwitchIOCardCapProviderConsts():
    DEPRECATED_FALSE = "false"
    DEPRECATED_NO = "no"
    DEPRECATED_TRUE = "true"
    DEPRECATED_YES = "yes"


class EquipmentSwitchIOCardCapProvider(ManagedObject):
    """This is EquipmentSwitchIOCardCapProvider class."""

    consts = EquipmentSwitchIOCardCapProviderConsts()
    naming_props = set(['vendor', 'model', 'revision'])

    mo_meta = MoMeta("EquipmentSwitchIOCardCapProvider", "equipmentSwitchIOCardCapProvider", "manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version121a, "InputOutput", 0xff, [], ["admin"], ['capabilityCatalogue'], ['equipmentBreakoutCap', 'equipmentFanModulesDef', 'equipmentFruVariant', 'equipmentManufacturingDef', 'equipmentPicture', 'equipmentUnifiedPortCapProvider'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "deprecated": MoPropertyMeta("deprecated", "deprecated", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "gencount": MoPropertyMeta("gencount", "gencount", "uint", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mgmt_plane_ver": MoPropertyMeta("mgmt_plane_ver", "mgmtPlaneVer", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version121a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "prom_card_type": MoPropertyMeta("prom_card_type", "promCardType", "ushort", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version121a, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version121a, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "deprecated": "deprecated", 
        "dn": "dn", 
        "gencount": "gencount", 
        "mgmtPlaneVer": "mgmt_plane_ver", 
        "model": "model", 
        "promCardType": "prom_card_type", 
        "revision": "revision", 
        "rn": "rn", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, revision, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.revision = revision
        self.child_action = None
        self.deprecated = None
        self.gencount = None
        self.mgmt_plane_ver = None
        self.prom_card_type = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentSwitchIOCardCapProvider", parent_mo_or_dn, **kwargs)

