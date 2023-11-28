"""This module contains the general information for ComputeServerFeatMask ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeServerFeatMaskConsts():
    pass


class ComputeServerFeatMask(ManagedObject):
    """This is ComputeServerFeatMask class."""

    consts = ComputeServerFeatMaskConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeServerFeatMask", "computeServerFeatMask", "serv-feat-mask", VersionMeta.Version112a, "InputOutput", 0xf, [], ["read-only"], ['computeSystem', 'extpolDomain', 'lsServer'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "feat_mask": MoPropertyMeta("feat_mask", "featMask", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|populate_template_name_feature_mask|advanced_boot_order_feature_mask|policy_map_feature_mask|light_weight_patching_feature_mask|global_sp_feature_mask|maintenance_policy_feature_mask|in_band_mgmt_feature_mask|self_encrypting_drives_policy_feature_mask|exclude_firmware_component_feature_mask|health_policy_feature_mask),){0,11}(defaultValue|none|populate_template_name_feature_mask|advanced_boot_order_feature_mask|policy_map_feature_mask|light_weight_patching_feature_mask|global_sp_feature_mask|maintenance_policy_feature_mask|in_band_mgmt_feature_mask|self_encrypting_drives_policy_feature_mask|exclude_firmware_component_feature_mask|health_policy_feature_mask){0,1}""", [], []), 
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

        ManagedObject.__init__(self, "ComputeServerFeatMask", parent_mo_or_dn, **kwargs)

