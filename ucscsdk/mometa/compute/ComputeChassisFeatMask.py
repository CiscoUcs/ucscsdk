"""This module contains the general information for ComputeChassisFeatMask ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeChassisFeatMaskConsts():
    pass


class ComputeChassisFeatMask(ManagedObject):
    """This is ComputeChassisFeatMask class."""

    consts = ComputeChassisFeatMaskConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeChassisFeatMask", "computeChassisFeatMask", "chassis-feat-mask", VersionMeta.Version201b, "InputOutput", 0xf, [], ["read-only"], ['computeSystem', 'equipmentChassis', 'equipmentChassisProfile', 'extpolDomain'], [], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "feat_mask": MoPropertyMeta("feat_mask", "featMask", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|compute_conn_policy_feature_mask|light_weight_patching_feature_mask),){0,3}(defaultValue|none|compute_conn_policy_feature_mask|light_weight_patching_feature_mask){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
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

        ManagedObject.__init__(self, "ComputeChassisFeatMask", parent_mo_or_dn, **kwargs)

