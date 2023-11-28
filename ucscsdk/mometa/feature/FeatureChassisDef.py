"""This module contains the general information for FeatureChassisDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FeatureChassisDefConsts():
    pass


class FeatureChassisDef(ManagedObject):
    """This is FeatureChassisDef class."""

    consts = FeatureChassisDefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FeatureChassisDef", "featureChassisDef", "chassis-feature-[name]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["admin"], ['featureCatalogEp'], ['domainChassisParam', 'domainEnvironmentParam', 'domainNetworkParam', 'domainServerParam', 'domainStorageParam'], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "feature_mask": MoPropertyMeta("feature_mask", "featureMask", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|compute_conn_policy_feature_mask|light_weight_patching_feature_mask),){0,3}(defaultValue|none|compute_conn_policy_feature_mask|light_weight_patching_feature_mask){0,1}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "featureMask": "feature_mask", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.description = None
        self.feature_mask = None
        self.status = None
        self.version = None

        ManagedObject.__init__(self, "FeatureChassisDef", parent_mo_or_dn, **kwargs)

