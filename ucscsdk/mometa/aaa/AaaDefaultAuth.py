"""This module contains the general information for AaaDefaultAuth ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AaaDefaultAuthConsts():
    REALM_LDAP = "ldap"
    REALM_LOCAL = "local"
    REALM_NONE = "none"
    REALM_RADIUS = "radius"
    REALM_TACACS = "tacacs"


class AaaDefaultAuth(ManagedObject):
    """This is AaaDefaultAuth class."""

    consts = AaaDefaultAuthConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaDefaultAuth", "aaaDefaultAuth", "default-auth", VersionMeta.Version101a, "InputOutput", 0x3ff, [], ["aaa", "admin", "domain-group-management"], ['aaaAuthRealm'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "provider_group": MoPropertyMeta("provider_group", "providerGroup", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, 0, 127, None, [], []), 
        "realm": MoPropertyMeta("realm", "realm", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["ldap", "local", "none", "radius", "tacacs"], []), 
        "refresh_period": MoPropertyMeta("refresh_period", "refreshPeriod", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["60-172800"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "session_timeout": MoPropertyMeta("session_timeout", "sessionTimeout", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["60-172800"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "providerGroup": "provider_group", 
        "realm": "realm", 
        "refreshPeriod": "refresh_period", 
        "rn": "rn", 
        "sessionTimeout": "session_timeout", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.name = None
        self.provider_group = None
        self.realm = None
        self.refresh_period = None
        self.session_timeout = None
        self.status = None

        ManagedObject.__init__(self, "AaaDefaultAuth", parent_mo_or_dn, **kwargs)

