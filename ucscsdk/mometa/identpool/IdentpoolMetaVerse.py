"""This module contains the general information for IdentpoolMetaVerse ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IdentpoolMetaVerseConsts():
    pass


class IdentpoolMetaVerse(ManagedObject):
    """This is IdentpoolMetaVerse class."""

    consts = IdentpoolMetaVerseConsts()
    naming_props = set([])

    mo_meta = MoMeta("IdentpoolMetaVerse", "identpoolMetaVerse", "metaverse", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["read-only"], ['topRoot'], ['identpoolMetaSystem'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "generation": MoPropertyMeta("generation", "generation", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "generation": "generation", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.generation = None
        self.status = None

        ManagedObject.__init__(self, "IdentpoolMetaVerse", **kwargs)

