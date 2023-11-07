"""This module contains the general information for SyntheticTime ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SyntheticTimeConsts():
    pass


class SyntheticTime(ManagedObject):
    """This is SyntheticTime class."""

    consts = SyntheticTimeConsts()
    naming_props = set(['ts'])

    mo_meta = MoMeta("SyntheticTime", "syntheticTime", "time-[ts]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin"], [], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "ts": MoPropertyMeta("ts", "ts", "ulong", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "ts": "ts", 
    }

    def __init__(self, parent_mo_or_dn, ts, **kwargs):
        self._dirty_mask = 0
        self.ts = ts
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "SyntheticTime", parent_mo_or_dn, **kwargs)

