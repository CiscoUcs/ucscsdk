"""This module contains the general information for LsmaintMaintPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsmaintMaintPolicyConsts():
    DATA_DISR_IMMEDIATE = "immediate"
    DATA_DISR_USER_ACK = "user-ack"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    SOFT_SHUTDOWN_TIMER_150_SECS = "150-secs"
    SOFT_SHUTDOWN_TIMER_300_SECS = "300-secs"
    SOFT_SHUTDOWN_TIMER_600_SECS = "600-secs"
    SOFT_SHUTDOWN_TIMER_NEVER = "never"
    UPTIME_DISR_IMMEDIATE = "immediate"
    UPTIME_DISR_TIMER_AUTOMATIC = "timer-automatic"
    UPTIME_DISR_USER_ACK = "user-ack"


class LsmaintMaintPolicy(ManagedObject):
    """This is LsmaintMaintPolicy class."""

    consts = LsmaintMaintPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("LsmaintMaintPolicy", "lsmaintMaintPolicy", "maint-[name]", VersionMeta.Version101a, "InputOutput", 0x7ff, [], ["read-only"], ['orgDomainGroup', 'orgOrg'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "data_disr": MoPropertyMeta("data_disr", "dataDisr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["immediate", "user-ack"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_sched_name": MoPropertyMeta("oper_sched_name", "operSchedName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "sched_name": MoPropertyMeta("sched_name", "schedName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "soft_shutdown_timer": MoPropertyMeta("soft_shutdown_timer", "softShutdownTimer", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""(([1-9]*[0-9]{2}:)|)([0-1][0-9]||[2][0-3]):([0-5][0-9]):([0-5][0-9])||(([0-5][0-9]):|)([0-5][0-9])""", ["150-secs", "300-secs", "600-secs", "never"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_config": MoPropertyMeta("trigger_config", "triggerConfig", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((defaultValue|none|on-next-boot),){0,2}(defaultValue|none|on-next-boot){0,1}""", [], []), 
        "uptime_disr": MoPropertyMeta("uptime_disr", "uptimeDisr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["immediate", "timer-automatic", "user-ack"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dataDisr": "data_disr", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "operSchedName": "oper_sched_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "schedName": "sched_name", 
        "softShutdownTimer": "soft_shutdown_timer", 
        "status": "status", 
        "triggerConfig": "trigger_config", 
        "uptimeDisr": "uptime_disr", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.data_disr = None
        self.descr = None
        self.int_id = None
        self.oper_sched_name = None
        self.policy_level = None
        self.policy_owner = None
        self.sched_name = None
        self.soft_shutdown_timer = None
        self.status = None
        self.trigger_config = None
        self.uptime_disr = None

        ManagedObject.__init__(self, "LsmaintMaintPolicy", parent_mo_or_dn, **kwargs)

