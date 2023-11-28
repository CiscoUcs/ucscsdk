"""This module contains the general information for VnicIpV4StaticAddr ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicIpV4StaticAddrConsts():
    pass


class VnicIpV4StaticAddr(ManagedObject):
    """This is VnicIpV4StaticAddr class."""

    consts = VnicIpV4StaticAddrConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIpV4StaticAddr", "vnicIpV4StaticAddr", "ipv4-static-addr", VersionMeta.Version101a, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], ['computeInstance', 'lsServer', 'lsbootLanImagePath', 'mgmtController', 'mgmtVnet', 'vnicIPv4If', 'vnicMgmtIf', 'vnicOutbandMgmtEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "primDns": "prim_dns", 
        "rn": "rn", 
        "secDns": "sec_dns", 
        "status": "status", 
        "subnet": "subnet", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.addr = None
        self.child_action = None
        self.def_gw = None
        self.prim_dns = None
        self.sec_dns = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "VnicIpV4StaticAddr", parent_mo_or_dn, **kwargs)

