"""This module contains the general information for ComputeNetworkFeatMask ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeNetworkFeatMaskConsts():
    pass


class ComputeNetworkFeatMask(ManagedObject):
    """This is ComputeNetworkFeatMask class."""

    consts = ComputeNetworkFeatMaskConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeNetworkFeatMask", "computeNetworkFeatMask", "net-feat-mask", VersionMeta.Version112a, "InputOutput", 0xf, [], ["read-only"], ['computeSystem', 'extpolDomain', 'lsServer'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "feat_mask": MoPropertyMeta("feat_mask", "featMask", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|pvlan_feature_mask|netflow_feature_mask|vlan_range_feature_mask|vnic_pairing_feature_mask|vlan_range_extended_feature_mask|usnic_vmq_feature_mask),){0,7}(defaultValue|none|pvlan_feature_mask|netflow_feature_mask|vlan_range_feature_mask|vnic_pairing_feature_mask|vlan_range_extended_feature_mask|usnic_vmq_feature_mask){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "featMask": "feat_mask", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.feat_mask = None
        self.status = None

        ManagedObject.__init__(self, "ComputeNetworkFeatMask", parent_mo_or_dn, **kwargs)

