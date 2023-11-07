"""This module contains the general information for TrigTriggered ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class TrigTriggeredConsts():
    OPER_STATE_FAILED = "failed"
    OPER_STATE_IN_PROGRESS = "in-progress"
    OPER_STATE_PENDING = "pending"
    OPER_STATE_TRIGGERED = "triggered"


class TrigTriggered(ManagedObject):
    """This is TrigTriggered class."""

    consts = TrigTriggeredConsts()
    naming_props = set(['trId'])

    mo_meta = MoMeta("TrigTriggered", "trigTriggered", "trig-[tr_id]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["read-only"], ['trigMeta'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "job_count": MoPropertyMeta("job_count", "jobCount", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "in-progress", "pending", "triggered"], []), 
        "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tr_dn": MoPropertyMeta("tr_dn", "trDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "tr_id": MoPropertyMeta("tr_id", "trId", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "jobCount": "job_count", 
        "operState": "oper_state", 
        "order": "order", 
        "rn": "rn", 
        "status": "status", 
        "trDn": "tr_dn", 
        "trId": "tr_id", 
    }

    def __init__(self, parent_mo_or_dn, tr_id, **kwargs):
        self._dirty_mask = 0
        self.tr_id = tr_id
        self.child_action = None
        self.job_count = None
        self.oper_state = None
        self.order = None
        self.status = None
        self.tr_dn = None

        ManagedObject.__init__(self, "TrigTriggered", parent_mo_or_dn, **kwargs)

