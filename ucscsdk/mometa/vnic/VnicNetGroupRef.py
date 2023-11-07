"""This module contains the general information for VnicNetGroupRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicNetGroupRefConsts():
    pass


class VnicNetGroupRef(ManagedObject):
    """This is VnicNetGroupRef class."""

    consts = VnicNetGroupRefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicNetGroupRef", "vnicNetGroupRef", "ngref-[name]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["admin"], ['vnicNetGroup'], ['vnicEther'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x4, 1, 1024, None, [], []), 
        "oper_net_group_ref_dn": MoPropertyMeta("oper_net_group_ref_dn", "operNetGroupRefDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "operNetGroupRefDn": "oper_net_group_ref_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.oper_net_group_ref_dn = None
        self.status = None

        ManagedObject.__init__(self, "VnicNetGroupRef", parent_mo_or_dn, **kwargs)

