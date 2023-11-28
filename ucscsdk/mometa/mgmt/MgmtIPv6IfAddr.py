"""This module contains the general information for MgmtIPv6IfAddr ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtIPv6IfAddrConsts():
    pass


class MgmtIPv6IfAddr(ManagedObject):
    """This is MgmtIPv6IfAddr class."""

    consts = MgmtIPv6IfAddrConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtIPv6IfAddr", "mgmtIPv6IfAddr", "if-ipv6", VersionMeta.Version112a, "InputOutput", 0x7f, [], ["admin", "ext-lan-config"], ['mgmtIPv6IfConfig', 'networkElement'], [], ["Get", "Set"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "prefix": MoPropertyMeta("prefix", "prefix", "byte", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-127"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "prefix": "prefix", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.addr = None
        self.child_action = None
        self.def_gw = None
        self.prefix = None
        self.status = None

        ManagedObject.__init__(self, "MgmtIPv6IfAddr", parent_mo_or_dn, **kwargs)

