"""This module contains the general information for AdaptorFcCdbWorkQueueProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorFcCdbWorkQueueProfileConsts():
    pass


class AdaptorFcCdbWorkQueueProfile(ManagedObject):
    """This is AdaptorFcCdbWorkQueueProfile class."""

    consts = AdaptorFcCdbWorkQueueProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcCdbWorkQueueProfile", "adaptorFcCdbWorkQueueProfile", "fc-cdb-work-q", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage"], ['adaptorHostFcIfProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "count": MoPropertyMeta("count", "count", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-8"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "ring_size": MoPropertyMeta("ring_size", "ringSize", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["64-512"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "count": "count", 
        "dn": "dn", 
        "ringSize": "ring_size", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.count = None
        self.ring_size = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorFcCdbWorkQueueProfile", parent_mo_or_dn, **kwargs)

