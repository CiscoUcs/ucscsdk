"""This module contains the general information for LstorageControllerRef ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class LstorageControllerRefConsts():
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


class LstorageControllerRef(ManagedObject):
    """This is LstorageControllerRef class."""

    consts = LstorageControllerRefConsts()
    naming_props = set([u'serverId', u'controllerType', u'controllerId'])

    mo_meta = MoMeta("LstorageControllerRef", "lstorageControllerRef", "server-[server_id]-controller-[controller_type]-[controller_id]", None, "InputOutput", 0x7f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], [u'lstorageDiskSlot'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "controller_id": MoPropertyMeta("controller_id", "controllerId", "uint", None, MoPropertyMeta.NAMING, 0x2, None, None, None, [], ["1-1"]), 
        "controller_type": MoPropertyMeta("controller_type", "controllerType", "string", None, MoPropertyMeta.NAMING, 0x4, None, None, None, ["FLASH", "HBA", "NVME", "PCH", "PT", "SAS", "SATA", "SD", "external", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "server_id": MoPropertyMeta("server_id", "serverId", "uint", None, MoPropertyMeta.NAMING, 0x20, None, None, None, [], ["1-2"]), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "controllerId": "controller_id", 
        "controllerType": "controller_type", 
        "dn": "dn", 
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
        self.status = None

        ManagedObject.__init__(self, "LstorageControllerRef", parent_mo_or_dn, **kwargs)

