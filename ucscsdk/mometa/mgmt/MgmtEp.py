"""This module contains the general information for MgmtEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtEpConsts():
    FW_CURRENT_UPDATE_STATE_FAILED = "failed"
    FW_CURRENT_UPDATE_STATE_IN_PROGRESS = "in-progress"
    FW_CURRENT_UPDATE_STATE_PENDING_USER_ACK = "pending-user-ack"
    FW_CURRENT_UPDATE_STATE_READY = "ready"
    FW_CURRENT_UPDATE_STATE_SCHEDULED = "scheduled"
    FW_CURRENT_UPDATE_STATE_START_PENDING_EXT_PERMISSION = "start-pending-ext-permission"


class MgmtEp(ManagedObject):
    """This is MgmtEp class."""

    consts = MgmtEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtEp", "mgmtEp", "mgmt-ep", VersionMeta.Version101a, "InputOutput", 0xf, [], ["admin"], ['topRoot'], ['mgmtSvc'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "fw_current_update_name": MoPropertyMeta("fw_current_update_name", "fwCurrentUpdateName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[a-zA-Z][a-zA-Z0-9@_.\-\\]{0,256}""", [], []), 
        "fw_current_update_state": MoPropertyMeta("fw_current_update_state", "fwCurrentUpdateState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "in-progress", "pending-user-ack", "ready", "scheduled", "start-pending-ext-permission"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fwCurrentUpdateName": "fw_current_update_name", 
        "fwCurrentUpdateState": "fw_current_update_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.fw_current_update_name = None
        self.fw_current_update_state = None
        self.status = None

        ManagedObject.__init__(self, "MgmtEp", **kwargs)

