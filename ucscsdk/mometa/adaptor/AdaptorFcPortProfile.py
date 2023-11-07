"""This module contains the general information for AdaptorFcPortProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorFcPortProfileConsts():
    pass


class AdaptorFcPortProfile(ManagedObject):
    """This is AdaptorFcPortProfile class."""

    consts = AdaptorFcPortProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcPortProfile", "adaptorFcPortProfile", "fc-port", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage"], ['adaptorHostFcIfProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "io_throttle_count": MoPropertyMeta("io_throttle_count", "ioThrottleCount", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["256-1024"]), 
        "luns_per_target": MoPropertyMeta("luns_per_target", "lunsPerTarget", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-4096"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ioThrottleCount": "io_throttle_count", 
        "lunsPerTarget": "luns_per_target", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.io_throttle_count = None
        self.luns_per_target = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorFcPortProfile", parent_mo_or_dn, **kwargs)

