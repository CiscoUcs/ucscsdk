"""This module contains the general information for IdentpoolIPQual ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IdentpoolIPQualConsts():
    pass


class IdentpoolIPQual(ManagedObject):
    """This is IdentpoolIPQual class."""

    consts = IdentpoolIPQualConsts()
    naming_props = set(['addr'])

    mo_meta = MoMeta("IdentpoolIPQual", "identpoolIPQual", "ip-[addr]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin"], ['identpoolBlockQual'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, addr, **kwargs):
        self._dirty_mask = 0
        self.addr = addr
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "IdentpoolIPQual", parent_mo_or_dn, **kwargs)

