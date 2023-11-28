"""This module contains the general information for FabricFcEndpoint ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricFcEndpointConsts():
    pass


class FabricFcEndpoint(ManagedObject):
    """This is FabricFcEndpoint class."""

    consts = FabricFcEndpointConsts()
    naming_props = set(['wwpn'])

    mo_meta = MoMeta("FabricFcEndpoint", "fabricFcEndpoint", "endpoint-[wwpn]", VersionMeta.Version201b, "InputOutput", 0x3f, [], ["admin", "ext-san-config", "ext-san-policy"], ['fabricFcUserZone'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "wwpn": MoPropertyMeta("wwpn", "wwpn", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x20, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "wwpn": "wwpn", 
    }

    def __init__(self, parent_mo_or_dn, wwpn, **kwargs):
        self._dirty_mask = 0
        self.wwpn = wwpn
        self.child_action = None
        self.name = None
        self.status = None

        ManagedObject.__init__(self, "FabricFcEndpoint", parent_mo_or_dn, **kwargs)

