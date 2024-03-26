"""This module contains the general information for PolicyControlEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyControlEpConsts():
    ACK_STATE_ACKED = "acked"
    ACK_STATE_NO_ACK = "no-ack"
    ACK_STATE_REMOTE_TRIGGER = "remoteTrigger"
    REGISTRATION_STATE_FAILED = "failed"
    REGISTRATION_STATE_INPROGRESS = "inprogress"
    REGISTRATION_STATE_LOST_VISIBILITY = "lost-visibility"
    REGISTRATION_STATE_REGISTERED = "registered"
    REGISTRATION_STATE_UNREGISTERED = "unregistered"
    SUSPEND_STATE_OFF = "off"
    SUSPEND_STATE_ON = "on"
    SUSPEND_STATE_REMOTE_TRIGGER = "remoteTrigger"
    TYPE_POLICY = "policy"


class PolicyControlEp(ManagedObject):
    """This is PolicyControlEp class."""

    consts = PolicyControlEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("PolicyControlEp", "policyControlEp", "control-ep-policy", VersionMeta.Version121a, "InputOutput", 0x1ff, [], ["admin"], ['computeSystem', 'fabricSystem'], ['policyCommunication', 'policyConfigBackup', 'policyControlEpOperation', 'policyDateTime', 'policyDestEp', 'policyDiscovery', 'policyDns', 'policyEquipment', 'policyFault', 'policyInfraFirmware', 'policyMEp', 'policyModularChassisFan', 'policyMonitoring', 'policyPortConfig', 'policyPowerExtended', 'policyPowerMgmt', 'policyPowerSave', 'policyPsu', 'policySecurity', 'policySourceApp', 'policyStorageAutoConfig'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "ack_state": MoPropertyMeta("ack_state", "ackState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["acked", "no-ack", "remoteTrigger"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "registration_state": MoPropertyMeta("registration_state", "registrationState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "inprogress", "lost-visibility", "registered", "unregistered"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "secret": MoPropertyMeta("secret", "secret", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,64}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspend_state": MoPropertyMeta("suspend_state", "suspendState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["off", "on", "remoteTrigger"], []), 
        "svc_reg_name": MoPropertyMeta("svc_reg_name", "svcRegName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""^[A-Za-z]([A-Za-z0-9_.-]*[A-Za-z0-9])?([A-Za-z]([A-Za-z0-9._-]*[A-Za-z0-9])?)*$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["policy"], []), 
    }

    prop_map = {
        "ackState": "ack_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "registrationState": "registration_state", 
        "rn": "rn", 
        "secret": "secret", 
        "status": "status", 
        "suspendState": "suspend_state", 
        "svcRegName": "svc_reg_name", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.ack_state = None
        self.child_action = None
        self.registration_state = None
        self.secret = None
        self.status = None
        self.suspend_state = None
        self.svc_reg_name = None
        self.type = None

        ManagedObject.__init__(self, "PolicyControlEp", parent_mo_or_dn, **kwargs)

