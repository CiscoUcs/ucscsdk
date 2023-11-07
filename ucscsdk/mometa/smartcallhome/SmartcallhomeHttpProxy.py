"""This module contains the general information for SmartcallhomeHttpProxy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SmartcallhomeHttpProxyConsts():
    pass


class SmartcallhomeHttpProxy(ManagedObject):
    """This is SmartcallhomeHttpProxy class."""

    consts = SmartcallhomeHttpProxyConsts()
    naming_props = set([])

    mo_meta = MoMeta("SmartcallhomeHttpProxy", "smartcallhomeHttpProxy", "proxy", VersionMeta.Version141a, "InputOutput", 0x3f, [], ["admin", "operations"], ['callhomeEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-65535"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "url": MoPropertyMeta("url", "url", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "port": "port", 
        "rn": "rn", 
        "status": "status", 
        "url": "url", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.port = None
        self.status = None
        self.url = None

        ManagedObject.__init__(self, "SmartcallhomeHttpProxy", parent_mo_or_dn, **kwargs)

