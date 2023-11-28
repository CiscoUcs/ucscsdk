"""This module contains the general information for ComputeChassisConnPolicyOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeChassisConnPolicyOperationConsts():
    ADMIN_STATE_GLOBAL = "global"
    ADMIN_STATE_NONE = "none"
    ADMIN_STATE_PORT_CHANNEL = "port-channel"
    ADMIN_STATE_UNSPECIFIED = "unspecified"
    BACKPLANE_SPEED_PREF_40_G = "40G"
    BACKPLANE_SPEED_PREF_4X10_G = "4x10G"
    BACKPLANE_SPEED_PREF_GLOBAL = "global"
    BACKPLANE_SPEED_PREF_UNSPECIFIED = "unspecified"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class ComputeChassisConnPolicyOperation(ManagedObject):
    """This is ComputeChassisConnPolicyOperation class."""

    consts = ComputeChassisConnPolicyOperationConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeChassisConnPolicyOperation", "computeChassisConnPolicyOperation", "remote-oper", VersionMeta.Version151a, "InputOutput", 0x7f, [], ["admin", "pn-policy"], ['computeChassisConnPolicy'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["global", "none", "port-channel", "unspecified"], []), 
        "backplane_speed_pref": MoPropertyMeta("backplane_speed_pref", "backplaneSpeedPref", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["40G", "4x10G", "global", "unspecified"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "backplaneSpeedPref": "backplane_speed_pref", 
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
        self.backplane_speed_pref = None
        self.child_action = None
        self.last_modified = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "ComputeChassisConnPolicyOperation", parent_mo_or_dn, **kwargs)

