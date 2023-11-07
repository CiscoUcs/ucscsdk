"""This module contains the general information for IdentpoolIPV6Qual ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IdentpoolIPV6QualConsts():
    pass


class IdentpoolIPV6Qual(ManagedObject):
    """This is IdentpoolIPV6Qual class."""

    consts = IdentpoolIPV6QualConsts()
    naming_props = set(['addr'])

    mo_meta = MoMeta("IdentpoolIPV6Qual", "identpoolIPV6Qual", "ipv6-[addr]", VersionMeta.Version112a, "InputOutput", 0x3f, [], ["admin"], ['identpoolBlockQual'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x2, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "expanded_addr": MoPropertyMeta("expanded_addr", "expandedAddr", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "dn": "dn", 
        "expandedAddr": "expanded_addr", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, addr, **kwargs):
        self._dirty_mask = 0
        self.addr = addr
        self.child_action = None
        self.expanded_addr = None
        self.status = None

        ManagedObject.__init__(self, "IdentpoolIPV6Qual", parent_mo_or_dn, **kwargs)

