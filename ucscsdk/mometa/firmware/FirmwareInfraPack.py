"""This module contains the general information for FirmwareInfraPack ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareInfraPackConsts():
    EVACUATE_FALSE = "false"
    EVACUATE_NO = "no"
    EVACUATE_TRUE = "true"
    EVACUATE_YES = "yes"
    FORCE_DEPLOY_FALSE = "false"
    FORCE_DEPLOY_NO = "no"
    FORCE_DEPLOY_TRUE = "true"
    FORCE_DEPLOY_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    UPDATE_TRIGGER_IMMEDIATE = "immediate"


class FirmwareInfraPack(ManagedObject):
    """This is FirmwareInfraPack class."""

    consts = FirmwareInfraPackConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FirmwareInfraPack", "firmwareInfraPack", "fw-infra-pack-[name]", VersionMeta.Version101a, "InputOutput", 0x1fff, [], ["admin", "operations"], ['firmwareProductFamily', 'orgDomainGroup', 'orgOrg'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "evacuate": MoPropertyMeta("evacuate", "evacuate", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []), 
        "force_deploy": MoPropertyMeta("force_deploy", "forceDeploy", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []), 
        "infra_bundle_name": MoPropertyMeta("infra_bundle_name", "infraBundleName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "infra_bundle_version": MoPropertyMeta("infra_bundle_version", "infraBundleVersion", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "service_pack_bundle_name": MoPropertyMeta("service_pack_bundle_name", "servicePackBundleName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "service_pack_bundle_version": MoPropertyMeta("service_pack_bundle_version", "servicePackBundleVersion", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], []), 
        "stage_size": MoPropertyMeta("stage_size", "stageSize", "ushort", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "update_trigger": MoPropertyMeta("update_trigger", "updateTrigger", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "evacuate": "evacuate", 
        "forceDeploy": "force_deploy", 
        "infraBundleName": "infra_bundle_name", 
        "infraBundleVersion": "infra_bundle_version", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
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
        self.child_action = None
        self.descr = None
        self.evacuate = None
        self.force_deploy = None
        self.infra_bundle_name = None
        self.infra_bundle_version = None
        self.int_id = None
        self.mode = None
        self.policy_level = None
        self.policy_owner = None
        self.service_pack_bundle_name = None
        self.service_pack_bundle_version = None
        self.stage_size = None
        self.status = None
        self.update_trigger = None

        ManagedObject.__init__(self, "FirmwareInfraPack", parent_mo_or_dn, **kwargs)

