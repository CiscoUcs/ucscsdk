"""This module contains the general information for AaaDomain ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AaaDomainConsts():
    pass


class AaaDomain(ManagedObject):
    """This is AaaDomain class."""

    consts = AaaDomainConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("AaaDomain", "aaaDomain", "domain-[name]", VersionMeta.Version101a, "InputOutput", 0xff, [], ["aaa", "admin", "domain-group-management"], ['aaaAuthRealm'], ['aaaDomainAuth'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[a-zA-Z0-9_.-]{1,16}""", [], []), 
        "refresh_period": MoPropertyMeta("refresh_period", "refreshPeriod", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["60-172800"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "session_timeout": MoPropertyMeta("session_timeout", "sessionTimeout", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["60-172800"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "refreshPeriod": "refresh_period", 
        "rn": "rn", 
        "sessionTimeout": "session_timeout", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.refresh_period = None
        self.session_timeout = None
        self.status = None

        ManagedObject.__init__(self, "AaaDomain", parent_mo_or_dn, **kwargs)

