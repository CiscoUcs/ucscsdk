"""This module contains the general information for FirmwarePolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwarePolicyConsts():
    DEPLOYMENT_MODE_IMMEDIATE = "immediate"
    DEPLOYMENT_MODE_MAINT_POLICY = "maint-policy"
    DEPLOYMENT_MODE_TIMER_AUTOMATIC = "timer-automatic"
    DEPLOYMENT_MODE_USER_ACK = "user-ack"
    HONOR_LS_MAINT_POLICY_FALSE = "false"
    HONOR_LS_MAINT_POLICY_NO = "no"
    HONOR_LS_MAINT_POLICY_TRUE = "true"
    HONOR_LS_MAINT_POLICY_YES = "yes"
    IGNORE_COMP_CHECK_FALSE = "false"
    IGNORE_COMP_CHECK_NO = "no"
    IGNORE_COMP_CHECK_TRUE = "true"
    IGNORE_COMP_CHECK_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class FirmwarePolicy(ManagedObject):
    """This is FirmwarePolicy class."""

    consts = FirmwarePolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwarePolicy", "firmwarePolicy", "fw-policy", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin", "operations"], ['orgDomainGroup'], [], [None])

    prop_meta = {
        "blade_version": MoPropertyMeta("blade_version", "bladeVersion", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "deployment_mode": MoPropertyMeta("deployment_mode", "deploymentMode", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["immediate", "maint-policy", "timer-automatic", "user-ack"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "honor_ls_maint_policy": MoPropertyMeta("honor_ls_maint_policy", "honorLsMaintPolicy", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "ignore_comp_check": MoPropertyMeta("ignore_comp_check", "ignoreCompCheck", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "infra_version": MoPropertyMeta("infra_version", "infraVersion", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rack_version": MoPropertyMeta("rack_version", "rackVersion", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "start_time": MoPropertyMeta("start_time", "startTime", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "bladeVersion": "blade_version", 
        "childAction": "child_action", 
        "deploymentMode": "deployment_mode", 
        "descr": "descr", 
        "dn": "dn", 
        "honorLsMaintPolicy": "honor_ls_maint_policy", 
        "ignoreCompCheck": "ignore_comp_check", 
        "infraVersion": "infra_version", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rackVersion": "rack_version", 
        "rn": "rn", 
        "startTime": "start_time", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.blade_version = None
        self.child_action = None
        self.deployment_mode = None
        self.descr = None
        self.honor_ls_maint_policy = None
        self.ignore_comp_check = None
        self.infra_version = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.rack_version = None
        self.start_time = None
        self.status = None

        ManagedObject.__init__(self, "FirmwarePolicy", parent_mo_or_dn, **kwargs)

