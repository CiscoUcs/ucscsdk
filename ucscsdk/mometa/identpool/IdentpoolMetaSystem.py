"""This module contains the general information for IdentpoolMetaSystem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IdentpoolMetaSystemConsts():
    pass


class IdentpoolMetaSystem(ManagedObject):
    """This is IdentpoolMetaSystem class."""

    consts = IdentpoolMetaSystemConsts()
    naming_props = set(['sysId'])

    mo_meta = MoMeta("IdentpoolMetaSystem", "identpoolMetaSystem", "metasys-[sys_id]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["read-only"], ['identpoolMetaVerse'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "generation": MoPropertyMeta("generation", "generation", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sys_id": MoPropertyMeta("sys_id", "sysId", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "generation": "generation", 
        "rn": "rn", 
        "status": "status", 
        "sysId": "sys_id", 
    }

    def __init__(self, parent_mo_or_dn, sys_id, **kwargs):
        self._dirty_mask = 0
        self.sys_id = sys_id
        self.child_action = None
        self.generation = None
        self.status = None

        ManagedObject.__init__(self, "IdentpoolMetaSystem", parent_mo_or_dn, **kwargs)

