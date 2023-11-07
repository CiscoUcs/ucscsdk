"""This module contains the general information for AdaptorEthGENEVEProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorEthGENEVEProfileConsts():
    pass


class AdaptorEthGENEVEProfile(ManagedObject):
    """This is AdaptorEthGENEVEProfile class."""

    consts = AdaptorEthGENEVEProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorEthGENEVEProfile", "adaptorEthGENEVEProfile", "eth-geneve", VersionMeta.Version201m, "InputOutput", 0x1f, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], ['adaptorHostEthIfProfile'], [], [None])

    prop_meta = {
        "offload": MoPropertyMeta("offload", "Offload", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "Offload": "offload", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.offload = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorEthGENEVEProfile", parent_mo_or_dn, **kwargs)

