"""This module contains the general information for StorageControllerRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageControllerRefConsts():
    CONTROLLER_TYPE_FLASH = "FLASH"
    CONTROLLER_TYPE_HBA = "HBA"
    CONTROLLER_TYPE_NVME = "NVME"
    CONTROLLER_TYPE_PCH = "PCH"
    CONTROLLER_TYPE_PT = "PT"
    CONTROLLER_TYPE_SAS = "SAS"
    CONTROLLER_TYPE_SATA = "SATA"
    CONTROLLER_TYPE_SD = "SD"
    CONTROLLER_TYPE_EXTERNAL = "external"
    CONTROLLER_TYPE_UNKNOWN = "unknown"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"


class StorageControllerRef(ManagedObject):
    """This is StorageControllerRef class."""

    consts = StorageControllerRefConsts()
    naming_props = set(['serverId', 'controllerType', 'controllerId'])

    mo_meta = MoMeta("StorageControllerRef", "storageControllerRef", "server-[server_id]-controller-[controller_type]-[controller_id]", VersionMeta.Version151a, "InputOutput", 0x7f, [], ["read-only"], ['storageEnclosureDiskSlotEp'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "controller_id": MoPropertyMeta("controller_id", "controllerId", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x2, None, None, None, [], []), 
        "controller_type": MoPropertyMeta("controller_type", "controllerType", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, None, None, None, ["FLASH", "HBA", "NVME", "PCH", "PT", "SAS", "SATA", "SD", "external", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "server_id": MoPropertyMeta("server_id", "serverId", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "controllerId": "controller_id", 
        "controllerType": "controller_type", 
        "dn": "dn", 
        "lc": "lc", 
        "rn": "rn", 
        "serverId": "server_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, server_id, controller_type, controller_id, **kwargs):
        self._dirty_mask = 0
        self.server_id = server_id
        self.controller_type = controller_type
        self.controller_id = controller_id
        self.child_action = None
        self.lc = None
        self.status = None

        ManagedObject.__init__(self, "StorageControllerRef", parent_mo_or_dn, **kwargs)

