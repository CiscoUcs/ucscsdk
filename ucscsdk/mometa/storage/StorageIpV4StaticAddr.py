"""This module contains the general information for StorageIpV4StaticAddr ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageIpV4StaticAddrConsts():
    pass


class StorageIpV4StaticAddr(ManagedObject):
    """This is StorageIpV4StaticAddr class."""

    consts = StorageIpV4StaticAddrConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageIpV4StaticAddr", "storageIpV4StaticAddr", "storage-ipv4-addr", VersionMeta.Version131a, "InputOutput", 0x1ff, [], ["admin", "ls-storage"], ['computeInstance', 'lsServer', 'mgmtVnet', 'vnicIPv4If', 'vnicMgmtIf'], [], ["Get"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
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

        ManagedObject.__init__(self, "StorageIpV4StaticAddr", parent_mo_or_dn, **kwargs)

