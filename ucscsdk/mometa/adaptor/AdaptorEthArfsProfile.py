"""This module contains the general information for AdaptorEthArfsProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorEthArfsProfileConsts():
    pass


class AdaptorEthArfsProfile(ManagedObject):
    """This is AdaptorEthArfsProfile class."""

    consts = AdaptorEthArfsProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorEthArfsProfile", "adaptorEthArfsProfile", "eth-arfs", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], ['adaptorHostEthIfProfile'], [], ["Get", "Set"])

    prop_meta = {
        "accelarated_rfs": MoPropertyMeta("accelarated_rfs", "accelaratedRFS", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "accelaratedRFS": "accelarated_rfs", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.accelarated_rfs = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorEthArfsProfile", parent_mo_or_dn, **kwargs)

