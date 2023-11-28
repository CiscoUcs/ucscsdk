"""This module contains the general information for PolicyPortConfig ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyPortConfigConsts():
    SOURCE_LOCAL = "local"
    SOURCE_PENDING_POLICY = "pending-policy"
    SOURCE_POLICY = "policy"
    SOURCE_UNSPECIFIED = "unspecified"


class PolicyPortConfig(ManagedObject):
    """This is PolicyPortConfig class."""

    consts = PolicyPortConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("PolicyPortConfig", "policyPortConfig", "portconfig-ctrl", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["admin", "pn-equipment", "pn-policy"], ['policyControlEp'], ['policyControlledInstance', 'policyControlledType'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "source": MoPropertyMeta("source", "source", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "source": "source", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.source = None
        self.status = None

        ManagedObject.__init__(self, "PolicyPortConfig", parent_mo_or_dn, **kwargs)

