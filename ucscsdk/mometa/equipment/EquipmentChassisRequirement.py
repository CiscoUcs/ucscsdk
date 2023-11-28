"""This module contains the general information for EquipmentChassisRequirement ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentChassisRequirementConsts():
    INSTANTIATION_STATE_CHASSIS_FAILED = "chassis-failed"
    INSTANTIATION_STATE_CHASSIS_MISMATCH = "chassis-mismatch"
    INSTANTIATION_STATE_CONFIG = "config"
    INSTANTIATION_STATE_CONFIG_FAILURE = "config-failure"
    INSTANTIATION_STATE_DECOMISSIONING = "decomissioning"
    INSTANTIATION_STATE_DEGRADED = "degraded"
    INSTANTIATION_STATE_DIAGNOSTICS = "diagnostics"
    INSTANTIATION_STATE_DIAGNOSTICS_FAILED = "diagnostics-failed"
    INSTANTIATION_STATE_DISABLED = "disabled"
    INSTANTIATION_STATE_DISCOVERY = "discovery"
    INSTANTIATION_STATE_DISCOVERY_FAILED = "discovery-failed"
    INSTANTIATION_STATE_INACCESSIBLE = "inaccessible"
    INSTANTIATION_STATE_INDETERMINATE = "indeterminate"
    INSTANTIATION_STATE_INOPERABLE = "inoperable"
    INSTANTIATION_STATE_INSTANTIATED = "instantiated"
    INSTANTIATION_STATE_MAINTENANCE = "maintenance"
    INSTANTIATION_STATE_MAINTENANCE_FAILED = "maintenance-failed"
    INSTANTIATION_STATE_OK = "ok"
    INSTANTIATION_STATE_OPERABLE = "operable"
    INSTANTIATION_STATE_PENDING_REASSOCIATION = "pending-reassociation"
    INSTANTIATION_STATE_PENDING_REBOOT = "pending-reboot"
    INSTANTIATION_STATE_POWER_OFF = "power-off"
    INSTANTIATION_STATE_REMOVED = "removed"
    INSTANTIATION_STATE_RESTART = "restart"
    INSTANTIATION_STATE_TEST = "test"
    INSTANTIATION_STATE_TEST_FAILED = "test-failed"
    INSTANTIATION_STATE_UNASSOCIATED = "unassociated"
    INSTANTIATION_STATE_UNCONFIG = "unconfig"
    INSTANTIATION_STATE_UNCONFIG_FAILED = "unconfig-failed"
    INSTANTIATION_STATE_UNINSTANTIATED = "uninstantiated"
    INT_ID_NONE = "none"
    OPER_STATE_CHASSIS_FAILED = "chassis-failed"
    OPER_STATE_CHASSIS_MISMATCH = "chassis-mismatch"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_CONFIG_FAILURE = "config-failure"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_DIAGNOSTICS = "diagnostics"
    OPER_STATE_DIAGNOSTICS_FAILED = "diagnostics-failed"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_DISCOVERY = "discovery"
    OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    OPER_STATE_INACCESSIBLE = "inaccessible"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_INOPERABLE = "inoperable"
    OPER_STATE_MAINTENANCE = "maintenance"
    OPER_STATE_MAINTENANCE_FAILED = "maintenance-failed"
    OPER_STATE_OK = "ok"
    OPER_STATE_OPERABLE = "operable"
    OPER_STATE_PENDING_REASSOCIATION = "pending-reassociation"
    OPER_STATE_PENDING_REBOOT = "pending-reboot"
    OPER_STATE_POWER_OFF = "power-off"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_RESTART = "restart"
    OPER_STATE_TEST = "test"
    OPER_STATE_TEST_FAILED = "test-failed"
    OPER_STATE_UNASSOCIATED = "unassociated"
    OPER_STATE_UNCONFIG = "unconfig"
    OPER_STATE_UNCONFIG_FAILED = "unconfig-failed"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class EquipmentChassisRequirement(ManagedObject):
    """This is EquipmentChassisRequirement class."""

    consts = EquipmentChassisRequirementConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("EquipmentChassisRequirement", "equipmentChassisRequirement", "chassis-req-[name]", VersionMeta.Version151a, "InputOutput", 0x3f, [], ["read-only"], ['orgOrg'], ['equipmentInstance'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "instantiation_state": MoPropertyMeta("instantiation_state", "instantiationState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis-failed", "chassis-mismatch", "config", "config-failure", "decomissioning", "degraded", "diagnostics", "diagnostics-failed", "disabled", "discovery", "discovery-failed", "inaccessible", "indeterminate", "inoperable", "instantiated", "maintenance", "maintenance-failed", "ok", "operable", "pending-reassociation", "pending-reboot", "power-off", "removed", "restart", "test", "test-failed", "unassociated", "unconfig", "unconfig-failed", "uninstantiated"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "local_placement_ref_cnt": MoPropertyMeta("local_placement_ref_cnt", "localPlacementRefCnt", "ushort", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,128}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis-failed", "chassis-mismatch", "config", "config-failure", "decomissioning", "degraded", "diagnostics", "diagnostics-failed", "disabled", "discovery", "discovery-failed", "inaccessible", "indeterminate", "inoperable", "maintenance", "maintenance-failed", "ok", "operable", "pending-reassociation", "pending-reboot", "power-off", "removed", "restart", "test", "test-failed", "unassociated", "unconfig", "unconfig-failed"], []), 
        "placement_ref_cnt": MoPropertyMeta("placement_ref_cnt", "placementRefCnt", "ushort", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "instantiationState": "instantiation_state", 
        "intId": "int_id", 
        "localPlacementRefCnt": "local_placement_ref_cnt", 
        "name": "name", 
        "operState": "oper_state", 
        "placementRefCnt": "placement_ref_cnt", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.instantiation_state = None
        self.int_id = None
        self.local_placement_ref_cnt = None
        self.oper_state = None
        self.placement_ref_cnt = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentChassisRequirement", parent_mo_or_dn, **kwargs)

