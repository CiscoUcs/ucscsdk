"""This module contains the general information for AdaptorEthAdvFilterProfile ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class AdaptorEthAdvFilterProfileConsts():
    pass


class AdaptorEthAdvFilterProfile(ManagedObject):
    """This is AdaptorEthAdvFilterProfile class."""

    consts = AdaptorEthAdvFilterProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorEthAdvFilterProfile", "adaptorEthAdvFilterProfile", "eth-adv-filter", None, "InputOutput", 0x1f, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], [u'adaptorHostEthIfProfile'], [], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", None, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorEthAdvFilterProfile", parent_mo_or_dn, **kwargs)

