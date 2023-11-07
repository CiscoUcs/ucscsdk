"""This module contains the general information for SmartcallhomeSource ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SmartcallhomeSourceConsts():
    URGENCY_ALERT = "alert"
    URGENCY_CRITICAL = "critical"
    URGENCY_DEBUG = "debug"
    URGENCY_EMERGENCY = "emergency"
    URGENCY_ERROR = "error"
    URGENCY_INFO = "info"
    URGENCY_NOTICE = "notice"
    URGENCY_WARNING = "warning"


class SmartcallhomeSource(ManagedObject):
    """This is SmartcallhomeSource class."""

    consts = SmartcallhomeSourceConsts()
    naming_props = set([])

    mo_meta = MoMeta("SmartcallhomeSource", "smartcallhomeSource", "sch-source", VersionMeta.Version141a, "InputOutput", 0x3fff, [], ["admin", "operations"], ['callhomeEp'], [], ["Get", "Set"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "contact": MoPropertyMeta("contact", "contact", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, 0, 64, r"""[^<>""'&]*""", [], []), 
        "contract": MoPropertyMeta("contract", "contract", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, 0, 64, None, [], []), 
        "customer": MoPropertyMeta("customer", "customer", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []), 
        "r_from": MoPropertyMeta("r_from", "from", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []), 
        "phone": MoPropertyMeta("phone", "phone", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], []), 
        "reply_to": MoPropertyMeta("reply_to", "replyTo", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []), 
        "site": MoPropertyMeta("site", "site", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "urgency": MoPropertyMeta("urgency", "urgency", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["alert", "critical", "debug", "emergency", "error", "info", "notice", "warning"], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "contact": "contact", 
        "contract": "contract", 
        "customer": "customer", 
        "dn": "dn", 
        "email": "email", 
        "from": "r_from", 
        "phone": "phone", 
        "replyTo": "reply_to", 
        "rn": "rn", 
        "site": "site", 
        "status": "status", 
        "urgency": "urgency", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.addr = None
        self.child_action = None
        self.contact = None
        self.contract = None
        self.customer = None
        self.email = None
        self.r_from = None
        self.phone = None
        self.reply_to = None
        self.site = None
        self.status = None
        self.urgency = None

        ManagedObject.__init__(self, "SmartcallhomeSource", parent_mo_or_dn, **kwargs)

