"""This module contains the general information for GlVnetInvHolder ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlVnetInvHolderConsts():
    pass


class GlVnetInvHolder(ManagedObject):
    """This is GlVnetInvHolder class."""

    consts = GlVnetInvHolderConsts()
    naming_props = set([])

    mo_meta = MoMeta("GlVnetInvHolder", "glVnetInvHolder", "vnet", VersionMeta.Version201b, "InputOutput", 0xf, [], ["read-only"], ['glRequestVnetEpDomainEp'], ['glMcastPolicy', 'glVlan', 'glVsan'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_policy": MoPropertyMeta("num_of_policy", "numOfPolicy", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_policy_conflict_resolved": MoPropertyMeta("num_of_policy_conflict_resolved", "numOfPolicyConflictResolved", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_policy_conflicts": MoPropertyMeta("num_of_policy_conflicts", "numOfPolicyConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_policy_no_conflicts": MoPropertyMeta("num_of_policy_no_conflicts", "numOfPolicyNoConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_vlan_conflict_resolved": MoPropertyMeta("num_of_vlan_conflict_resolved", "numOfVlanConflictResolved", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_vlan_conflicts": MoPropertyMeta("num_of_vlan_conflicts", "numOfVlanConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_vlan_no_conflicts": MoPropertyMeta("num_of_vlan_no_conflicts", "numOfVlanNoConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_vlans": MoPropertyMeta("num_of_vlans", "numOfVlans", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_vsan_conflict_resolved": MoPropertyMeta("num_of_vsan_conflict_resolved", "numOfVsanConflictResolved", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_vsan_conflicts": MoPropertyMeta("num_of_vsan_conflicts", "numOfVsanConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_vsan_no_conflicts": MoPropertyMeta("num_of_vsan_no_conflicts", "numOfVsanNoConflicts", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_vsans": MoPropertyMeta("num_of_vsans", "numOfVsans", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "index": "index", 
        "numOfPolicy": "num_of_policy", 
        "numOfPolicyConflictResolved": "num_of_policy_conflict_resolved", 
        "numOfPolicyConflicts": "num_of_policy_conflicts", 
        "numOfPolicyNoConflicts": "num_of_policy_no_conflicts", 
        "numOfVlanConflictResolved": "num_of_vlan_conflict_resolved", 
        "numOfVlanConflicts": "num_of_vlan_conflicts", 
        "numOfVlanNoConflicts": "num_of_vlan_no_conflicts", 
        "numOfVlans": "num_of_vlans", 
        "numOfVsanConflictResolved": "num_of_vsan_conflict_resolved", 
        "numOfVsanConflicts": "num_of_vsan_conflicts", 
        "numOfVsanNoConflicts": "num_of_vsan_no_conflicts", 
        "numOfVsans": "num_of_vsans", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.index = None
        self.num_of_policy = None
        self.num_of_policy_conflict_resolved = None
        self.num_of_policy_conflicts = None
        self.num_of_policy_no_conflicts = None
        self.num_of_vlan_conflict_resolved = None
        self.num_of_vlan_conflicts = None
        self.num_of_vlan_no_conflicts = None
        self.num_of_vlans = None
        self.num_of_vsan_conflict_resolved = None
        self.num_of_vsan_conflicts = None
        self.num_of_vsan_no_conflicts = None
        self.num_of_vsans = None
        self.status = None

        ManagedObject.__init__(self, "GlVnetInvHolder", parent_mo_or_dn, **kwargs)

