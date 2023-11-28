"""This module contains the general information for IpServiceIf ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IpServiceIfConsts():
    pass


class IpServiceIf(ManagedObject):
    """This is IpServiceIf class."""

    consts = IpServiceIfConsts()
    naming_props = set(['addr', 'port'])

    mo_meta = MoMeta("IpServiceIf", "ipServiceIf", "serv-ip-[addr]-port-[port]", VersionMeta.Version131a, "InputOutput", 0x7f, [], ["admin"], ['storageEtherIf'], [], [None])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-65535"]), 
        "pref": MoPropertyMeta("pref", "pref", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "port": "port", 
        "pref": "pref", 
        "rn": "rn", 
        "status": "status", 
        "subnet": "subnet", 
    }

    def __init__(self, parent_mo_or_dn, addr, port, **kwargs):
        self._dirty_mask = 0
        self.addr = addr
        self.port = port
        self.child_action = None
        self.def_gw = None
        self.pref = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "IpServiceIf", parent_mo_or_dn, **kwargs)

