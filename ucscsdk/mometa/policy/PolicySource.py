"""This module contains the general information for PolicySource ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicySourceConsts():
    OWNERSHIP_LOCAL = "local"
    OWNERSHIP_PENDING_POLICY = "pending-policy"
    OWNERSHIP_POLICY = "policy"
    OWNERSHIP_UNSPECIFIED = "unspecified"


class PolicySource(ManagedObject):
    """This is PolicySource class."""

    consts = PolicySourceConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("PolicySource", "policySource", "source-[id]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin"], ['policyCluster'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "ownership": MoPropertyMeta("ownership", "ownership", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "ownership": "ownership", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.ownership = None
        self.status = None

        ManagedObject.__init__(self, "PolicySource", parent_mo_or_dn, **kwargs)

