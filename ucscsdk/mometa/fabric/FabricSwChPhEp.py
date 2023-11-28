"""This module contains the general information for FabricSwChPhEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricSwChPhEpConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    ADMIN_STATE_REMOVE = "remove"
    CHASSIS_ID_N_A = "N/A"
    EQ_TYPE_BLADE = "blade"
    EQ_TYPE_CARTRIDGE = "cartridge"
    EQ_TYPE_CHASSIS = "chassis"
    EQ_TYPE_FEX = "fex"
    EQ_TYPE_RACK_UNIT = "rack-unit"
    EQ_TYPE_SERVER_UNIT = "server-unit"
    EQ_TYPE_UNKNOWN = "unknown"
    LC_IN_SERVICE = "in-service"
    LC_OUT_OF_SERVICE = "out-of-service"


class FabricSwChPhEp(ManagedObject):
    """This is FabricSwChPhEp class."""

    consts = FabricSwChPhEpConsts()
    naming_props = set(['vendor', 'model', 'serial'])

    mo_meta = MoMeta("FabricSwChPhEp", "fabricSwChPhEp", "chassis-ep-ven-[vendor]-mod[model]-ser-[serial]", VersionMeta.Version112a, "InputOutput", 0x3ff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['fabricDceSrv'], ['fabricSwChPhEpOperation'], ["Get", "Set"])

    prop_meta = {
        "address": MoPropertyMeta("address", "address", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled", "remove"], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["N/A"], ["1-40"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "eq_type": MoPropertyMeta("eq_type", "eqType", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blade", "cartridge", "chassis", "fex", "rack-unit", "server-unit", "unknown"], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["in-service", "out-of-service"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, 1, 32, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x200, 1, 510, None, [], []), 
    }

    prop_map = {
        "address": "address", 
        "adminState": "admin_state", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "eqType": "eq_type", 
        "lc": "lc", 
        "model": "model", 
        "name": "name", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, serial, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.serial = serial
        self.address = None
        self.admin_state = None
        self.chassis_id = None
        self.child_action = None
        self.eq_type = None
        self.lc = None
        self.name = None
        self.revision = None
        self.status = None

        ManagedObject.__init__(self, "FabricSwChPhEp", parent_mo_or_dn, **kwargs)

