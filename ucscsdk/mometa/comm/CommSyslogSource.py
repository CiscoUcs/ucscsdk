"""This module contains the general information for CommSyslogSource ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class CommSyslogSourceConsts():
    AUDITS_DISABLED = "disabled"
    AUDITS_ENABLED = "enabled"
    EVENTS_DISABLED = "disabled"
    EVENTS_ENABLED = "enabled"
    FAULTS_DISABLED = "disabled"
    FAULTS_ENABLED = "enabled"


class CommSyslogSource(ManagedObject):
    """This is CommSyslogSource class."""

    consts = CommSyslogSourceConsts()
    naming_props = set([])

    mo_meta = MoMeta("CommSyslogSource", "commSyslogSource", "source", VersionMeta.Version101a, "InputOutput", 0x1ff, [], ["admin", "domain-group-management", "operations"], ['commSyslog'], [], ["Add", "Get", "Set"])

    prop_meta = {
        "audits": MoPropertyMeta("audits", "audits", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "events": MoPropertyMeta("events", "events", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled"], []), 
        "faults": MoPropertyMeta("faults", "faults", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "audits": "audits", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "events": "events", 
        "faults": "faults", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.audits = None
        self.child_action = None
        self.descr = None
        self.events = None
        self.faults = None
        self.name = None
        self.status = None

        ManagedObject.__init__(self, "CommSyslogSource", parent_mo_or_dn, **kwargs)

