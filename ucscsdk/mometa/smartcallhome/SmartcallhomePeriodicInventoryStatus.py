"""This module contains the general information for SmartcallhomePeriodicInventoryStatus ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SmartcallhomePeriodicInventoryStatusConsts():
    NEXT_DEADLINE_NEVER = "never"
    TIME_OF_LAST_SUCCESS_NEVER = "never"


class SmartcallhomePeriodicInventoryStatus(ManagedObject):
    """This is SmartcallhomePeriodicInventoryStatus class."""

    consts = SmartcallhomePeriodicInventoryStatusConsts()
    naming_props = set([])

    mo_meta = MoMeta("SmartcallhomePeriodicInventoryStatus", "smartcallhomePeriodicInventoryStatus", "inventory-status", VersionMeta.Version141a, "InputOutput", 0xf, [], ["read-only"], ['callhomeHolder'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "last_deadline": MoPropertyMeta("last_deadline", "lastDeadline", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "next_deadline": MoPropertyMeta("next_deadline", "nextDeadline", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "retry_count": MoPropertyMeta("retry_count", "retryCount", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "time_of_last_attempt": MoPropertyMeta("time_of_last_attempt", "timeOfLastAttempt", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "time_of_last_success": MoPropertyMeta("time_of_last_success", "timeOfLastSuccess", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lastDeadline": "last_deadline", 
        "nextDeadline": "next_deadline", 
        "retryCount": "retry_count", 
        "rn": "rn", 
        "status": "status", 
        "timeOfLastAttempt": "time_of_last_attempt", 
        "timeOfLastSuccess": "time_of_last_success", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.last_deadline = None
        self.next_deadline = None
        self.retry_count = None
        self.status = None
        self.time_of_last_attempt = None
        self.time_of_last_success = None

        ManagedObject.__init__(self, "SmartcallhomePeriodicInventoryStatus", parent_mo_or_dn, **kwargs)

