"""This module contains the general information for CallhomeProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class CallhomeProfileConsts():
    FORMAT_FULL_TXT = "fullTxt"
    FORMAT_SHORT_TXT = "shortTxt"
    FORMAT_XML = "xml"
    LEVEL_CRITICAL = "critical"
    LEVEL_DEBUG = "debug"
    LEVEL_DISASTER = "disaster"
    LEVEL_FATAL = "fatal"
    LEVEL_MAJOR = "major"
    LEVEL_MINOR = "minor"
    LEVEL_NORMAL = "normal"
    LEVEL_NOTIFICATION = "notification"
    LEVEL_WARNING = "warning"


class CallhomeProfile(ManagedObject):
    """This is CallhomeProfile class."""

    consts = CallhomeProfileConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("CallhomeProfile", "callhomeProfile", "profile-[name]", VersionMeta.Version101a, "InputOutput", 0x3ff, [], ["admin", "operations"], ['callhomeEp'], ['callhomeDest'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "alert_groups": MoPropertyMeta("alert_groups", "alertGroups", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""((diagnostic|all|syslogPort|inventory|system|license|environmental|test|linecard|lifeCycle|ciscoTac|supervisor),){0,11}(diagnostic|all|syslogPort|inventory|system|license|environmental|test|linecard|lifeCycle|ciscoTac|supervisor){0,1}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "format": MoPropertyMeta("format", "format", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["fullTxt", "shortTxt", "xml"], []), 
        "level": MoPropertyMeta("level", "level", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["critical", "debug", "disaster", "fatal", "major", "minor", "normal", "notification", "warning"], []), 
        "max_size": MoPropertyMeta("max_size", "maxSize", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-5000000"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "alertGroups": "alert_groups", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "format": "format", 
        "level": "level", 
        "maxSize": "max_size", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.alert_groups = None
        self.child_action = None
        self.descr = None
        self.format = None
        self.level = None
        self.max_size = None
        self.status = None

        ManagedObject.__init__(self, "CallhomeProfile", parent_mo_or_dn, **kwargs)

