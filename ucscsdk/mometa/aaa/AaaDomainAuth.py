"""This module contains the general information for AaaDomainAuth ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AaaDomainAuthConsts():
    REALM_LDAP = "ldap"
    REALM_LOCAL = "local"
    REALM_NONE = "none"
    REALM_RADIUS = "radius"
    REALM_TACACS = "tacacs"


class AaaDomainAuth(ManagedObject):
    """This is AaaDomainAuth class."""

    consts = AaaDomainAuthConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaDomainAuth", "aaaDomainAuth", "domain-auth", VersionMeta.Version101a, "InputOutput", 0xff, [], ["aaa", "admin", "domain-group-management"], ['aaaDomain'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "provider_group": MoPropertyMeta("provider_group", "providerGroup", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, 0, 127, None, [], []), 
        "realm": MoPropertyMeta("realm", "realm", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["ldap", "local", "none", "radius", "tacacs"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "providerGroup": "provider_group", 
        "realm": "realm", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.name = None
        self.provider_group = None
        self.realm = None
        self.status = None

        ManagedObject.__init__(self, "AaaDomainAuth", parent_mo_or_dn, **kwargs)

