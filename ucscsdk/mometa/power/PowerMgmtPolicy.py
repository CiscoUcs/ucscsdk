"""This module contains the general information for PowerMgmtPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PowerMgmtPolicyConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PROFILING_FALSE = "false"
    PROFILING_NO = "no"
    PROFILING_TRUE = "true"
    PROFILING_YES = "yes"
    SKIP_POWER_CHECK_FALSE = "false"
    SKIP_POWER_CHECK_NO = "no"
    SKIP_POWER_CHECK_TRUE = "true"
    SKIP_POWER_CHECK_YES = "yes"
    SKIP_POWER_DEPLOY_CHECK_FALSE = "false"
    SKIP_POWER_DEPLOY_CHECK_NO = "no"
    SKIP_POWER_DEPLOY_CHECK_TRUE = "true"
    SKIP_POWER_DEPLOY_CHECK_YES = "yes"
    STYLE_INTELLIGENT_POLICY_DRIVEN = "intelligent-policy-driven"
    STYLE_MANUAL_PER_BLADE = "manual-per-blade"


class PowerMgmtPolicy(ManagedObject):
    """This is PowerMgmtPolicy class."""

    consts = PowerMgmtPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("PowerMgmtPolicy", "powerMgmtPolicy", "pwr-mgmt-policy", VersionMeta.Version101a, "InputOutput", 0x3ff, [], ["admin", "domain-group-management", "power-mgmt"], ['orgDomainGroup'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "profiling": MoPropertyMeta("profiling", "profiling", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "skip_power_check": MoPropertyMeta("skip_power_check", "skipPowerCheck", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []), 
        "skip_power_deploy_check": MoPropertyMeta("skip_power_deploy_check", "skipPowerDeployCheck", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "no", "true", "yes"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "style": MoPropertyMeta("style", "style", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["intelligent-policy-driven", "manual-per-blade"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "profiling": "profiling", 
        "rn": "rn", 
        "skipPowerCheck": "skip_power_check", 
        "skipPowerDeployCheck": "skip_power_deploy_check", 
        "status": "status", 
        "style": "style", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.profiling = None
        self.skip_power_check = None
        self.skip_power_deploy_check = None
        self.status = None
        self.style = None

        ManagedObject.__init__(self, "PowerMgmtPolicy", parent_mo_or_dn, **kwargs)

