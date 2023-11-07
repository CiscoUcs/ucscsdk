"""This module contains the general information for SmartcallhomePeriodicSystemInventory ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SmartcallhomePeriodicSystemInventoryConsts():
    ADMIN_STATE_OFF = "off"
    ADMIN_STATE_ON = "on"
    SEND_NOW_FALSE = "false"
    SEND_NOW_NO = "no"
    SEND_NOW_TRUE = "true"
    SEND_NOW_YES = "yes"


class SmartcallhomePeriodicSystemInventory(ManagedObject):
    """This is SmartcallhomePeriodicSystemInventory class."""

    consts = SmartcallhomePeriodicSystemInventoryConsts()
    naming_props = set([])

    mo_meta = MoMeta("SmartcallhomePeriodicSystemInventory", "smartcallhomePeriodicSystemInventory", "smart-periodic-inventory", VersionMeta.Version141a, "InputOutput", 0x1fff, [], ["admin", "operations"], ['callhomeEp'], [], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["off", "on"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "interval_days": MoPropertyMeta("interval_days", "intervalDays", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-30"]), 
        "maximum_retry_count": MoPropertyMeta("maximum_retry_count", "maximumRetryCount", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-5"]), 
        "minimum_send_now_interval_seconds": MoPropertyMeta("minimum_send_now_interval_seconds", "minimumSendNowIntervalSeconds", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-2000000000"]), 
        "poll_interval_seconds": MoPropertyMeta("poll_interval_seconds", "pollIntervalSeconds", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["10-3600"]), 
        "retry_delay_minutes": MoPropertyMeta("retry_delay_minutes", "retryDelayMinutes", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["0-60"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "send_now": MoPropertyMeta("send_now", "sendNow", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["false", "no", "true", "yes"], []), 
        "send_now_request": MoPropertyMeta("send_now_request", "sendNowRequest", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "time_of_day_hour": MoPropertyMeta("time_of_day_hour", "timeOfDayHour", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], ["0-23"]), 
        "time_of_day_minute": MoPropertyMeta("time_of_day_minute", "timeOfDayMinute", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], ["0-59"]), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervalDays": "interval_days", 
        "maximumRetryCount": "maximum_retry_count", 
        "minimumSendNowIntervalSeconds": "minimum_send_now_interval_seconds", 
        "pollIntervalSeconds": "poll_interval_seconds", 
        "retryDelayMinutes": "retry_delay_minutes", 
        "rn": "rn", 
        "sendNow": "send_now", 
        "sendNowRequest": "send_now_request", 
        "status": "status", 
        "timeOfDayHour": "time_of_day_hour", 
        "timeOfDayMinute": "time_of_day_minute", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.interval_days = None
        self.maximum_retry_count = None
        self.minimum_send_now_interval_seconds = None
        self.poll_interval_seconds = None
        self.retry_delay_minutes = None
        self.send_now = None
        self.send_now_request = None
        self.status = None
        self.time_of_day_hour = None
        self.time_of_day_minute = None

        ManagedObject.__init__(self, "SmartcallhomePeriodicSystemInventory", parent_mo_or_dn, **kwargs)

