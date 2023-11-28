"""This module contains the general information for PortGroup ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PortGroupConsts():
    TYPE_ADAPTOR_EXT = "adaptor-ext"
    TYPE_ADAPTOR_PC = "adaptor-pc"
    TYPE_FABRIC = "fabric"
    TYPE_FABRIC_PC = "fabric-pc"
    TYPE_HOST = "host"
    TYPE_HOST_PC = "host-pc"
    TYPE_SERVER_PC = "server-pc"
    TYPE_SWITCH_ETHER = "switch-ether"
    TYPE_SWITCH_FC = "switch-fc"


class PortGroup(ManagedObject):
    """This is PortGroup class."""

    consts = PortGroupConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("PortGroup", "portGroup", "[type]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['equipmentIOCard', 'equipmentSharedIOModule', 'equipmentSwitchCard', 'equipmentSwitchIOCard'], ['etherPIo', 'etherServerIntFIo', 'etherSwitchIntFIo', 'fcPIo', 'portSubGroup'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["adaptor-ext", "adaptor-pc", "fabric", "fabric-pc", "host", "host-pc", "server-pc", "switch-ether", "switch-fc"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "PortGroup", parent_mo_or_dn, **kwargs)

