"""This module contains the general information for TrigMeta ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class TrigMetaConsts():
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGER_IMMEDIATE = "trigger-immediate"
    ADMIN_STATE_TRIGGERED = "triggered"
    ADMIN_STATE_UNTRIGGERED = "untriggered"
    ADMIN_STATE_USER_ACK = "user-ack"
    INT_ID_NONE = "none"
    OPER_STATE_CAP_REACHED = "cap-reached"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_IN_PROGRESS = "in-progress"
    OPER_STATE_PENDING = "pending"
    OPER_STATE_PENDING_ACK = "pending-ack"
    OPER_STATE_TRIGGERED = "triggered"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class TrigMeta(ManagedObject):
    """This is TrigMeta class."""

    consts = TrigMetaConsts()
    naming_props = set(['schedName'])

    mo_meta = MoMeta("TrigMeta", "trigMeta", "meta-trig-[sched_name]", VersionMeta.Version101a, "InputOutput", 0xff, [], ["read-only"], ['firmwareDomainInfraProfile', 'orgDomainGroup', 'storageCloud', 'topSystem'], ['trigServerToken', 'trigTokenRequestor', 'trigTriggered'], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "trigger-immediate", "triggered", "untriggered", "user-ack"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "job_count": MoPropertyMeta("job_count", "jobCount", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cap-reached", "failed", "in-progress", "pending", "pending-ack", "triggered"], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "sched_name": MoPropertyMeta("sched_name", "schedName", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,256}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trig_time": MoPropertyMeta("trig_time", "trigTime", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "window_dn": MoPropertyMeta("window_dn", "windowDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "jobCount": "job_count", 
        "name": "name", 
        "operState": "oper_state", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "schedName": "sched_name", 
        "status": "status", 
        "trigTime": "trig_time", 
        "windowDn": "window_dn", 
    }

    def __init__(self, parent_mo_or_dn, sched_name, **kwargs):
        self._dirty_mask = 0
        self.sched_name = sched_name
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.job_count = None
        self.name = None
        self.oper_state = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None
        self.trig_time = None
        self.window_dn = None

        ManagedObject.__init__(self, "TrigMeta", parent_mo_or_dn, **kwargs)

