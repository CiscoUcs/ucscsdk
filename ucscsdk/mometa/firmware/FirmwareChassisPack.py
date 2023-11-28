"""This module contains the general information for FirmwareChassisPack ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareChassisPackConsts():
    FORCE_DEPLOY_FALSE = "false"
    FORCE_DEPLOY_NO = "no"
    FORCE_DEPLOY_TRUE = "true"
    FORCE_DEPLOY_YES = "yes"
    INT_ID_NONE = "none"
    OVERRIDE_DEFAULT_EXCLUSION_FALSE = "false"
    OVERRIDE_DEFAULT_EXCLUSION_NO = "no"
    OVERRIDE_DEFAULT_EXCLUSION_TRUE = "true"
    OVERRIDE_DEFAULT_EXCLUSION_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    UPDATE_TRIGGER_IMMEDIATE = "immediate"


class FirmwareChassisPack(ManagedObject):
    """This is FirmwareChassisPack class."""

    consts = FirmwareChassisPackConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FirmwareChassisPack", "firmwareChassisPack", "fw-chassis-pack-[name]", VersionMeta.Version151a, "InputOutput", 0x1fff, [], ["read-only"], ['orgDomainGroup', 'orgOrg'], ['firmwareExcludeChassisComponent'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "chassis_bundle_name": MoPropertyMeta("chassis_bundle_name", "chassisBundleName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "chassis_bundle_version": MoPropertyMeta("chassis_bundle_version", "chassisBundleVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "force_deploy": MoPropertyMeta("force_deploy", "forceDeploy", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "override_default_exclusion": MoPropertyMeta("override_default_exclusion", "overrideDefaultExclusion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "no", "true", "yes"], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "service_pack_bundle_name": MoPropertyMeta("service_pack_bundle_name", "servicePackBundleName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "service_pack_bundle_version": MoPropertyMeta("service_pack_bundle_version", "servicePackBundleVersion", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], []), 
        "stage_size": MoPropertyMeta("stage_size", "stageSize", "ushort", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "update_trigger": MoPropertyMeta("update_trigger", "updateTrigger", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], []), 
    }

    prop_map = {
        "chassisBundleName": "chassis_bundle_name", 
        "chassisBundleVersion": "chassis_bundle_version", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "forceDeploy": "force_deploy", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "overrideDefaultExclusion": "override_default_exclusion", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "servicePackBundleName": "service_pack_bundle_name", 
        "servicePackBundleVersion": "service_pack_bundle_version", 
        "stageSize": "stage_size", 
        "status": "status", 
        "updateTrigger": "update_trigger", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.chassis_bundle_name = None
        self.chassis_bundle_version = None
        self.child_action = None
        self.descr = None
        self.force_deploy = None
        self.int_id = None
        self.mode = None
        self.override_default_exclusion = None
        self.policy_level = None
        self.policy_owner = None
        self.service_pack_bundle_name = None
        self.service_pack_bundle_version = None
        self.stage_size = None
        self.status = None
        self.update_trigger = None

        ManagedObject.__init__(self, "FirmwareChassisPack", parent_mo_or_dn, **kwargs)

