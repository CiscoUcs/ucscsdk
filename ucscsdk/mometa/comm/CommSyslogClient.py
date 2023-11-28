"""This module contains the general information for CommSyslogClient ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class CommSyslogClientConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    FORWARDING_FACILITY_AUTH = "auth"
    FORWARDING_FACILITY_AUTHPRIV = "authpriv"
    FORWARDING_FACILITY_CRON = "cron"
    FORWARDING_FACILITY_DAEMON = "daemon"
    FORWARDING_FACILITY_FTP = "ftp"
    FORWARDING_FACILITY_KERNEL = "kernel"
    FORWARDING_FACILITY_LOCAL0 = "local0"
    FORWARDING_FACILITY_LOCAL1 = "local1"
    FORWARDING_FACILITY_LOCAL2 = "local2"
    FORWARDING_FACILITY_LOCAL3 = "local3"
    FORWARDING_FACILITY_LOCAL4 = "local4"
    FORWARDING_FACILITY_LOCAL5 = "local5"
    FORWARDING_FACILITY_LOCAL6 = "local6"
    FORWARDING_FACILITY_LOCAL7 = "local7"
    FORWARDING_FACILITY_LPR = "lpr"
    FORWARDING_FACILITY_MAIL = "mail"
    FORWARDING_FACILITY_NEWS = "news"
    FORWARDING_FACILITY_SYSLOG = "syslog"
    FORWARDING_FACILITY_USER = "user"
    FORWARDING_FACILITY_UUCP = "uucp"
    NAME_PRIMARY = "primary"
    NAME_SECONDARY = "secondary"
    NAME_TERTIARY = "tertiary"
    SEVERITY_ALERTS = "alerts"
    SEVERITY_CRITICAL = "critical"
    SEVERITY_DEBUGGING = "debugging"
    SEVERITY_EMERGENCIES = "emergencies"
    SEVERITY_ERRORS = "errors"
    SEVERITY_INFORMATION = "information"
    SEVERITY_NOTIFICATIONS = "notifications"
    SEVERITY_WARNINGS = "warnings"


class CommSyslogClient(ManagedObject):
    """This is CommSyslogClient class."""

    consts = CommSyslogClientConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("CommSyslogClient", "commSyslogClient", "client-[name]", VersionMeta.Version101a, "InputOutput", 0x1ff, [], ["admin", "operations"], ['commSyslog'], [], ["Add", "Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "forwarding_facility": MoPropertyMeta("forwarding_facility", "forwardingFacility", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["auth", "authpriv", "cron", "daemon", "ftp", "kernel", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7", "lpr", "mail", "news", "syslog", "user", "uucp"], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, None, None, None, ["primary", "secondary", "tertiary"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "severity": MoPropertyMeta("severity", "severity", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["alerts", "critical", "debugging", "emergencies", "errors", "information", "notifications", "warnings"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "forwardingFacility": "forwarding_facility", 
        "hostname": "hostname", 
        "name": "name", 
        "rn": "rn", 
        "severity": "severity", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.forwarding_facility = None
        self.hostname = None
        self.severity = None
        self.status = None

        ManagedObject.__init__(self, "CommSyslogClient", parent_mo_or_dn, **kwargs)

