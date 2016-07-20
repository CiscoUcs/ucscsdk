"""This module contains the general information for ConfigAckItem ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class ConfigAckItemConsts():
    ADMIN_STATE_ACK_TRIGGER = "trigger"
    ADMIN_STATE_ACK_TRIGGER_IMMEDIATE = "trigger-immediate"
    ADMIN_STATE_ACK_TRIGGERED = "triggered"
    ADMIN_STATE_ACK_UNTRIGGERED = "untriggered"
    ADMIN_STATE_ACK_USER_ACK = "user-ack"
    ADMIN_STATE_REQUESTOR_AUTO_SCHED = "auto-sched"
    ADMIN_STATE_REQUESTOR_FORCE_ACK = "force-ack"
    ADMIN_STATE_REQUESTOR_SCHED_ACK = "sched-ack"
    DISR_TYPE_FABRIC_INTERCONNECT = "fabric-interconnect"
    DISR_TYPE_FIRMWARE_INFRA = "firmware-infra"
    DISR_TYPE_HOST = "host"
    OPER_STATE_ACK_APPLIED = "applied"
    OPER_STATE_ACK_APPLY_PENDING = "apply-pending"
    OPER_STATE_ACK_EVALUATED = "evaluated"
    OPER_STATE_ACK_EVALUATION_PENDING = "evaluation-pending"
    OPER_STATE_ACK_UNTRIGGERED = "untriggered"
    OPER_STATE_ACK_WAITING_FOR_DEPENDENCY = "waiting-for-dependency"
    OPER_STATE_ACK_WAITING_FOR_MAINT_WINDOW = "waiting-for-maint-window"
    OPER_STATE_ACK_WAITING_FOR_USER = "waiting-for-user"
    OPER_STATE_REQUESTOR_CAP_REACHED = "cap-reached"
    OPER_STATE_REQUESTOR_FAILED = "failed"
    OPER_STATE_REQUESTOR_IN_PROGRESS = "in-progress"
    OPER_STATE_REQUESTOR_PENDING = "pending"
    OPER_STATE_REQUESTOR_PENDING_ACK = "pending-ack"
    OPER_STATE_REQUESTOR_TRIGGERED = "triggered"


class ConfigAckItem(ManagedObject):
    """This is ConfigAckItem class."""

    consts = ConfigAckItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigAckItem", "configAckItem", "ack-item", VersionMeta.Version131a, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "ack_dn": MoPropertyMeta("ack_dn", "ackDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "admin_state_ack": MoPropertyMeta("admin_state_ack", "adminStateAck", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["trigger", "trigger-immediate", "triggered", "untriggered", "user-ack"], []), 
        "admin_state_requestor": MoPropertyMeta("admin_state_requestor", "adminStateRequestor", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["auto-sched", "force-ack", "sched-ack"], []), 
        "change_by": MoPropertyMeta("change_by", "changeBy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[a-zA-Z][a-zA-Z0-9_.@-]{0,31}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "disr_type": MoPropertyMeta("disr_type", "disrType", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fabric-interconnect", "firmware-infra", "host"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_dn": MoPropertyMeta("domain_dn", "domainDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_scheduler": MoPropertyMeta("oper_scheduler", "operScheduler", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_state_ack": MoPropertyMeta("oper_state_ack", "operStateAck", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "apply-pending", "evaluated", "evaluation-pending", "untriggered", "waiting-for-dependency", "waiting-for-maint-window", "waiting-for-user"], []), 
        "oper_state_requestor": MoPropertyMeta("oper_state_requestor", "operStateRequestor", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cap-reached", "failed", "in-progress", "pending", "pending-ack", "triggered"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "scheduler": MoPropertyMeta("scheduler", "scheduler", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "server_id": MoPropertyMeta("server_id", "serverId", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "service_profile_dn": MoPropertyMeta("service_profile_dn", "serviceProfileDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "service_profile_name": MoPropertyMeta("service_profile_name", "serviceProfileName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "ackDn": "ack_dn", 
        "adminStateAck": "admin_state_ack", 
        "adminStateRequestor": "admin_state_requestor", 
        "changeBy": "change_by", 
        "childAction": "child_action", 
        "disrType": "disr_type", 
        "dn": "dn", 
        "domainDn": "domain_dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainName": "domain_name", 
        "operScheduler": "oper_scheduler", 
        "operStateAck": "oper_state_ack", 
        "operStateRequestor": "oper_state_requestor", 
        "rn": "rn", 
        "scheduler": "scheduler", 
        "serverId": "server_id", 
        "serviceProfileDn": "service_profile_dn", 
        "serviceProfileName": "service_profile_name", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.ack_dn = None
        self.admin_state_ack = None
        self.admin_state_requestor = None
        self.change_by = None
        self.child_action = None
        self.disr_type = None
        self.domain_dn = None
        self.domain_group_dn = None
        self.domain_name = None
        self.oper_scheduler = None
        self.oper_state_ack = None
        self.oper_state_requestor = None
        self.scheduler = None
        self.server_id = None
        self.service_profile_dn = None
        self.service_profile_name = None
        self.status = None

        ManagedObject.__init__(self, "ConfigAckItem", parent_mo_or_dn, **kwargs)

