"""This module contains the general information for PolicyUniverse ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyUniverseConsts():
    TYPE_CLIENT = "client"
    TYPE_SERVER = "server"


class PolicyUniverse(ManagedObject):
    """This is PolicyUniverse class."""

    consts = PolicyUniverseConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("PolicyUniverse", "policyUniverse", "universe-[type]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin"], ['topRoot'], ['policyCluster'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["client", "server"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "PolicyUniverse", **kwargs)

