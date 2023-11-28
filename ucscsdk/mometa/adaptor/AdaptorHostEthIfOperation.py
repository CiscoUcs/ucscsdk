"""This module contains the general information for AdaptorHostEthIfOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorHostEthIfOperationConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_DISABLED_ACTIVE = "disabled-active"
    ADMIN_STATE_DISABLED_PASSIVE = "disabled-passive"
    ADMIN_STATE_ENABLED = "enabled"
    ADMIN_STATE_ENABLED_ACTIVE = "enabled-active"
    ADMIN_STATE_ENABLED_PASSIVE = "enabled-passive"
    ADMIN_STATE_REMOTE_TRIGGER = "remoteTrigger"
    ADMIN_STATE_RESET_CONNECTIVITY = "reset-connectivity"
    ADMIN_STATE_RESET_CONNECTIVITY_ACTIVE = "reset-connectivity-active"
    ADMIN_STATE_RESET_CONNECTIVITY_PASSIVE = "reset-connectivity-passive"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class AdaptorHostEthIfOperation(ManagedObject):
    """This is AdaptorHostEthIfOperation class."""

    consts = AdaptorHostEthIfOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorHostEthIfOperation", "adaptorHostEthIfOperation", "remote-oper", VersionMeta.Version201b, "InputOutput", 0x3f, [], ["admin", "ext-lan-config", "ext-lan-policy", "pn-equipment", "pn-maintenance"], ['adaptorHostEthIf'], ['faultInst'], ["get", "set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "disabled-active", "disabled-passive", "enabled", "enabled-active", "enabled-passive", "remoteTrigger", "reset-connectivity", "reset-connectivity-active", "reset-connectivity-passive"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "lastModified": "last_modified", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "rn": "rn", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.last_modified = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "AdaptorHostEthIfOperation", parent_mo_or_dn, **kwargs)

