"""This module contains the general information for FeatureEnvDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FeatureEnvDefConsts():
    pass


class FeatureEnvDef(ManagedObject):
    """This is FeatureEnvDef class."""

    consts = FeatureEnvDefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FeatureEnvDef", "featureEnvDef", "env-feature-[name]", VersionMeta.Version112a, "InputOutput", 0x1f, [], ["admin"], ['featureCatalogEp'], ['domainChassisParam', 'domainEnvironmentParam', 'domainNetworkParam', 'domainServerParam', 'domainStorageParam'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "feature_mask": MoPropertyMeta("feature_mask", "featureMask", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|domain_setting_feature_mask|remote_operation_feature_mask|ucs_registration_feature_mask|ucs_manager_context_launch_feature_mask|power_group_feature_mask|estimate_impact_on_reconnect_feature_mask|health_reporting_feature_mask|html5_kvm_client_feature_mask|sso_ucsm_cross_launch_feature_mask|dc_power_group_feature_mask),){0,11}(defaultValue|none|domain_setting_feature_mask|remote_operation_feature_mask|ucs_registration_feature_mask|ucs_manager_context_launch_feature_mask|power_group_feature_mask|estimate_impact_on_reconnect_feature_mask|health_reporting_feature_mask|html5_kvm_client_feature_mask|sso_ucsm_cross_launch_feature_mask|dc_power_group_feature_mask){0,1}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
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

        ManagedObject.__init__(self, "FeatureEnvDef", parent_mo_or_dn, **kwargs)

