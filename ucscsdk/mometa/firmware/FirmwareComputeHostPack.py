"""This module contains the general information for FirmwareComputeHostPack ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareComputeHostPackConsts():
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


class FirmwareComputeHostPack(ManagedObject):
    """This is FirmwareComputeHostPack class."""

    consts = FirmwareComputeHostPackConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FirmwareComputeHostPack", "firmwareComputeHostPack", "fw-host-pack-[name]", VersionMeta.Version101a, "InputOutput", 0x3fff, [], ["read-only"], ['orgDomainGroup', 'orgOrg'], ['firmwareExcludeServerComponent'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "blade_bundle_name": MoPropertyMeta("blade_bundle_name", "bladeBundleName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "blade_bundle_version": MoPropertyMeta("blade_bundle_version", "bladeBundleVersion", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "m_series_bundle_name": MoPropertyMeta("m_series_bundle_name", "mSeriesBundleName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "m_series_bundle_version": MoPropertyMeta("m_series_bundle_version", "mSeriesBundleVersion", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "override_default_exclusion": MoPropertyMeta("override_default_exclusion", "overrideDefaultExclusion", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "no", "true", "yes"], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rack_bundle_name": MoPropertyMeta("rack_bundle_name", "rackBundleName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rack_bundle_version": MoPropertyMeta("rack_bundle_version", "rackBundleVersion", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []), 
        "service_pack_bundle_name": MoPropertyMeta("service_pack_bundle_name", "servicePackBundleName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "service_pack_bundle_version": MoPropertyMeta("service_pack_bundle_version", "servicePackBundleVersion", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []), 
        "stage_size": MoPropertyMeta("stage_size", "stageSize", "ushort", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "update_trigger": MoPropertyMeta("update_trigger", "updateTrigger", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], []), 
    }

    prop_map = {
        "bladeBundleName": "blade_bundle_name", 
        "bladeBundleVersion": "blade_bundle_version", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "mSeriesBundleName": "m_series_bundle_name", 
        "mSeriesBundleVersion": "m_series_bundle_version", 
        "mode": "mode", 
        "name": "name", 
        "overrideDefaultExclusion": "override_default_exclusion", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rackBundleName": "rack_bundle_name", 
        "rackBundleVersion": "rack_bundle_version", 
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
        self.blade_bundle_name = None
        self.blade_bundle_version = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.m_series_bundle_name = None
        self.m_series_bundle_version = None
        self.mode = None
        self.override_default_exclusion = None
        self.policy_level = None
        self.policy_owner = None
        self.rack_bundle_name = None
        self.rack_bundle_version = None
        self.service_pack_bundle_name = None
        self.service_pack_bundle_version = None
        self.stage_size = None
        self.status = None
        self.update_trigger = None

        ManagedObject.__init__(self, "FirmwareComputeHostPack", parent_mo_or_dn, **kwargs)

