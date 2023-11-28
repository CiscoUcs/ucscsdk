"""This module contains the general information for PolicyCluster ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyClusterConsts():
    pass


class PolicyCluster(ManagedObject):
    """This is PolicyCluster class."""

    consts = PolicyClusterConsts()
    naming_props = set(['convertedDn'])

    mo_meta = MoMeta("PolicyCluster", "policyCluster", "cluster-[converted_dn]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin"], ['policyUniverse'], ['policySource'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "class_type": MoPropertyMeta("class_type", "classType", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "converted_dn": MoPropertyMeta("converted_dn", "convertedDn", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x2, 1, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "policy_dn": MoPropertyMeta("policy_dn", "policyDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "classType": "class_type", 
        "convertedDn": "converted_dn", 
        "dn": "dn", 
        "name": "name", 
        "policyDn": "policy_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, converted_dn, **kwargs):
        self._dirty_mask = 0
        self.converted_dn = converted_dn
        self.child_action = None
        self.class_type = None
        self.name = None
        self.policy_dn = None
        self.status = None

        ManagedObject.__init__(self, "PolicyCluster", parent_mo_or_dn, **kwargs)

