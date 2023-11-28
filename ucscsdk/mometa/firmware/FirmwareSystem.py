"""This module contains the general information for FirmwareSystem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareSystemConsts():
    OPER_STATE_FAILED = "failed"
    OPER_STATE_IN_PROGRESS = "in-progress"
    OPER_STATE_PENDING_USER_ACK = "pending-user-ack"
    OPER_STATE_READY = "ready"
    OPER_STATE_SCHEDULED = "scheduled"
    OPER_STATE_START_PENDING_EXT_PERMISSION = "start-pending-ext-permission"
    STATE_COMPATIBLE = "compatible"
    STATE_INCOMPATIBLE = "incompatible"
    STATE_MULTIPLE_RELEASES = "multiple-releases"
    STATE_SAME_RELEASE = "same-release"
    STATE_UNKNOWN = "unknown"


class FirmwareSystem(ManagedObject):
    """This is FirmwareSystem class."""

    consts = FirmwareSystemConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareSystem", "firmwareSystem", "fw-system", VersionMeta.Version101a, "InputOutput", 0xf, [], ["admin", "ls-config-policy", "ls-server-policy"], ['computeSystem', 'topSystem'], ['firmwareAck', 'firmwareInfra'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "in-progress", "pending-user-ack", "ready", "scheduled", "start-pending-ext-permission"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["compatible", "incompatible", "multiple-releases", "same-release", "unknown"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "operState": "oper_state", 
        "rn": "rn", 
        "state": "state", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.oper_state = None
        self.state = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareSystem", parent_mo_or_dn, **kwargs)

