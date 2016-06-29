"""This module contains the general information for PolicyControlEp ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class PolicyControlEpConsts():
    ACK_STATE_ACKED = "acked"
    ACK_STATE_NO_ACK = "no-ack"
    ACK_STATE_REMOTE_TRIGGER = "remoteTrigger"
    SUSPEND_STATE_OFF = "off"
    SUSPEND_STATE_ON = "on"
    SUSPEND_STATE_REMOTE_TRIGGER = "remoteTrigger"


class PolicyControlEp(ManagedObject):
    """This is PolicyControlEp class."""

    consts = PolicyControlEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("PolicyControlEp", "policyControlEp", "control-ep-policy", VersionMeta.Version121a, "InputOutput", 0x3f, [], ["admin"], [u'computeSystem'], [u'policyCommunication', u'policyConfigBackup', u'policyControlEpOperation', u'policyDateTime', u'policyDiscovery', u'policyDns', u'policyEquipment', u'policyFault', u'policyInfraFirmware', u'policyMEp', u'policyMonitoring', u'policyPortConfig', u'policyPowerMgmt', u'policyPsu', u'policySecurity', u'policyStorageAutoConfig'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "ack_state": MoPropertyMeta("ack_state", "ackState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["acked", "no-ack", "remoteTrigger"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspend_state": MoPropertyMeta("suspend_state", "suspendState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["off", "on", "remoteTrigger"], []), 
    }

    prop_map = {
        "ackState": "ack_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "suspendState": "suspend_state", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.ack_state = None
        self.child_action = None
        self.status = None
        self.suspend_state = None

        ManagedObject.__init__(self, "PolicyControlEp", parent_mo_or_dn, **kwargs)

