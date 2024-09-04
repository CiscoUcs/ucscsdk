"""This module contains the general information for LstorageAck ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LstorageAckConsts():
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGER_IMMEDIATE = "trigger-immediate"
    ADMIN_STATE_TRIGGERED = "triggered"
    ADMIN_STATE_UNTRIGGERED = "untriggered"
    ADMIN_STATE_USER_ACK = "user-ack"
    AUTO_DELETE_FALSE = "false"
    AUTO_DELETE_NO = "no"
    AUTO_DELETE_TRUE = "true"
    AUTO_DELETE_YES = "yes"
    CHANGE_MODE_CONFIG = "config"
    CHANGE_MODE_FORCE_UNCONFIG = "force-unconfig"
    CHANGE_MODE_NO_CHANGE = "no-change"
    CHANGE_MODE_REMOVE_CONFIG = "remove-config"
    CHANGE_MODE_UNCONFIG = "unconfig"
    DEPLOYMENT_MODE_IMMEDIATE = "immediate"
    DEPLOYMENT_MODE_TIMER_AUTOMATIC = "timer-automatic"
    DEPLOYMENT_MODE_USER_ACK = "user-ack"
    IGNORE_CAP_FALSE = "false"
    IGNORE_CAP_NO = "no"
    IGNORE_CAP_TRUE = "true"
    IGNORE_CAP_YES = "yes"
    INT_ID_NONE = "none"
    OPER_STATE_ACTIVE = "active"
    OPER_STATE_APPLIED = "applied"
    OPER_STATE_APPLY_PENDING = "apply-pending"
    OPER_STATE_EVALUATED = "evaluated"
    OPER_STATE_EVALUATION_PENDING = "evaluation-pending"
    OPER_STATE_EXPIRED = "expired"
    OPER_STATE_NONE = "none"
    OPER_STATE_PENDING = "pending"
    OPER_STATE_UNTRIGGERED = "untriggered"
    OPER_STATE_WAITING_FOR_DEPENDENCY = "waiting-for-dependency"
    OPER_STATE_WAITING_FOR_MAINT_WINDOW = "waiting-for-maint-window"
    OPER_STATE_WAITING_FOR_USER = "waiting-for-user"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PREV_OPER_STATE_ACTIVE = "active"
    PREV_OPER_STATE_APPLIED = "applied"
    PREV_OPER_STATE_APPLY_PENDING = "apply-pending"
    PREV_OPER_STATE_EVALUATED = "evaluated"
    PREV_OPER_STATE_EVALUATION_PENDING = "evaluation-pending"
    PREV_OPER_STATE_EXPIRED = "expired"
    PREV_OPER_STATE_NONE = "none"
    PREV_OPER_STATE_PENDING = "pending"
    PREV_OPER_STATE_UNTRIGGERED = "untriggered"
    PREV_OPER_STATE_WAITING_FOR_DEPENDENCY = "waiting-for-dependency"
    PREV_OPER_STATE_WAITING_FOR_MAINT_WINDOW = "waiting-for-maint-window"
    PREV_OPER_STATE_WAITING_FOR_USER = "waiting-for-user"
    TRIGGER_CONFIG_STATE_NONE = "none"
    TRIGGER_CONFIG_STATE_WAITING_FOR_NEXT_BOOT = "waiting-for-next-boot"


class LstorageAck(ManagedObject):
    """This is LstorageAck class."""

    consts = LstorageAckConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageAck", "lstorageAck", "ack", VersionMeta.Version131a, "InputOutput", 0xff, [], ["admin", "ls-storage"], [], ['faultInst'], [None])

    prop_meta = {
        "acked": MoPropertyMeta("acked", "acked", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "acked_by": MoPropertyMeta("acked_by", "ackedBy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 32, None, [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "trigger-immediate", "triggered", "untriggered", "user-ack"], []), 
        "auto_delete": MoPropertyMeta("auto_delete", "autoDelete", "string", VersionMeta.Version131a, MoPropertyMeta.CREATE_ONLY, 0x4, None, None, None, ["false", "no", "true", "yes"], []), 
        "change_by": MoPropertyMeta("change_by", "changeBy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 32, None, [], []), 
        "change_details": MoPropertyMeta("change_details", "changeDetails", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|graphics-card-mode|storage-snic-config|oob-local-storage-config|storage-target-id|bootmode-config|host-eth-if-qos-host-control|checkpoint|pin|blade-identity|boot-local-storage|ip|disk-zoning-config|host-fcoe-if|host-virt-fc-if-pers-bind|local-disk-fw|adaptor-host-fw|host-eth-if-qos|local-disk-data-loss|activate-fw|fan-speed-config|remote-storage-config|secureboot-config|host-if-pcie|sol|agent-policy|boot-virt-pxe|boot-order|sas-exp-reg-fw|vif|bmc-update-bios-fw|host-nonvirt-fc-if-pers-bind|adaptor-nw-fw|host-eth-if-nw-ctrl|host-virt-eth-if|local-storage-security|storage-dev-bridge-fw|vmedia-config|flexflash-config|implicit-host-eth-if-profile-redeploy|implicit-host-fc-if-profile-redeploy|ep-auth|boot-nonvirt-pxe|boot-virt-vnic|config-server-sioc-conn-state|vlan|host-fc-if-profile|sas-expander-fw|host-virt-fc-if|mgmt-controller-fw|host-nonvirt-eth-if|asset-tag-config|powercap-config|storage-appliance-sw|flexflash-reboot|storage-path|bios-profile|local-disk-policy|boot-nonvirt-vnic|vsan|host-fc-if-qos|implicit-reboot|board-controller-fw|host-nonvirt-fc-if|host-eth-if-profile|binding|bios-fw|storage-controller-fw|graphics-card-fw),){0,68}(defaultValue|graphics-card-mode|storage-snic-config|oob-local-storage-config|storage-target-id|bootmode-config|host-eth-if-qos-host-control|checkpoint|pin|blade-identity|boot-local-storage|ip|disk-zoning-config|host-fcoe-if|host-virt-fc-if-pers-bind|local-disk-fw|adaptor-host-fw|host-eth-if-qos|local-disk-data-loss|activate-fw|fan-speed-config|remote-storage-config|secureboot-config|host-if-pcie|sol|agent-policy|boot-virt-pxe|boot-order|sas-exp-reg-fw|vif|bmc-update-bios-fw|host-nonvirt-fc-if-pers-bind|adaptor-nw-fw|host-eth-if-nw-ctrl|host-virt-eth-if|local-storage-security|storage-dev-bridge-fw|vmedia-config|flexflash-config|implicit-host-eth-if-profile-redeploy|implicit-host-fc-if-profile-redeploy|ep-auth|boot-nonvirt-pxe|boot-virt-vnic|config-server-sioc-conn-state|vlan|host-fc-if-profile|sas-expander-fw|host-virt-fc-if|mgmt-controller-fw|host-nonvirt-eth-if|asset-tag-config|powercap-config|storage-appliance-sw|flexflash-reboot|storage-path|bios-profile|local-disk-policy|boot-nonvirt-vnic|vsan|host-fc-if-qos|implicit-reboot|board-controller-fw|host-nonvirt-fc-if|host-eth-if-profile|binding|bios-fw|storage-controller-fw|graphics-card-fw){0,1}""", [], []), 
        "change_mode": MoPropertyMeta("change_mode", "changeMode", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["config", "force-unconfig", "no-change", "remove-config", "unconfig"], []), 
        "changes": MoPropertyMeta("changes", "changes", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|storage|boot-order|chassis-assignment|server-assignment|operational-policies|chassis-identity|local-storage|server-identity|networking|vnic-vhba-placement),){0,10}(defaultValue|storage|boot-order|chassis-assignment|server-assignment|operational-policies|chassis-identity|local-storage|server-identity|networking|vnic-vhba-placement){0,1}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "deployment_mode": MoPropertyMeta("deployment_mode", "deploymentMode", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["immediate", "timer-automatic", "user-ack"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "disr": MoPropertyMeta("disr", "disr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|ac-power-cycle|local-storage-config-deployment|storage-access|local-storage-config-deployment-immediate|storage-uptime|up-time),){0,6}(defaultValue|ac-power-cycle|local-storage-config-deployment|storage-access|local-storage-config-deployment-immediate|storage-uptime|up-time){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "ignore_cap": MoPropertyMeta("ignore_cap", "ignoreCap", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "modified": MoPropertyMeta("modified", "modified", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "old_pn_dn": MoPropertyMeta("old_pn_dn", "oldPnDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "old_proc_dn": MoPropertyMeta("old_proc_dn", "oldProcDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_scheduler": MoPropertyMeta("oper_scheduler", "operScheduler", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "applied", "apply-pending", "evaluated", "evaluation-pending", "expired", "none", "pending", "untriggered", "waiting-for-dependency", "waiting-for-maint-window", "waiting-for-user"], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "prev_oper_state": MoPropertyMeta("prev_oper_state", "prevOperState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "applied", "apply-pending", "evaluated", "evaluation-pending", "expired", "none", "pending", "untriggered", "waiting-for-dependency", "waiting-for-maint-window", "waiting-for-user"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "scheduler": MoPropertyMeta("scheduler", "scheduler", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_config_state": MoPropertyMeta("trigger_config_state", "triggerConfigState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "waiting-for-next-boot"], []), 
    }

    prop_map = {
        "acked": "acked", 
        "ackedBy": "acked_by", 
        "adminState": "admin_state", 
        "autoDelete": "auto_delete", 
        "changeBy": "change_by", 
        "changeDetails": "change_details", 
        "changeMode": "change_mode", 
        "changes": "changes", 
        "childAction": "child_action", 
        "deploymentMode": "deployment_mode", 
        "descr": "descr", 
        "disr": "disr", 
        "dn": "dn", 
        "ignoreCap": "ignore_cap", 
        "intId": "int_id", 
        "modified": "modified", 
        "name": "name", 
        "oldPnDn": "old_pn_dn", 
        "oldProcDn": "old_proc_dn", 
        "operScheduler": "oper_scheduler", 
        "operState": "oper_state", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "prevOperState": "prev_oper_state", 
        "rn": "rn", 
        "scheduler": "scheduler", 
        "status": "status", 
        "triggerConfigState": "trigger_config_state", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.acked = None
        self.acked_by = None
        self.admin_state = None
        self.auto_delete = None
        self.change_by = None
        self.change_details = None
        self.change_mode = None
        self.changes = None
        self.child_action = None
        self.deployment_mode = None
        self.descr = None
        self.disr = None
        self.ignore_cap = None
        self.int_id = None
        self.modified = None
        self.name = None
        self.old_pn_dn = None
        self.old_proc_dn = None
        self.oper_scheduler = None
        self.oper_state = None
        self.policy_level = None
        self.policy_owner = None
        self.prev_oper_state = None
        self.scheduler = None
        self.status = None
        self.trigger_config_state = None

        ManagedObject.__init__(self, "LstorageAck", parent_mo_or_dn, **kwargs)

