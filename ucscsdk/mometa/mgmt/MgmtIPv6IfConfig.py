"""This module contains the general information for MgmtIPv6IfConfig ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtIPv6IfConfigConsts():
    LINK_LOCAL_DISABLE = "disable"
    LINK_LOCAL_ENABLE = "enable"


class MgmtIPv6IfConfig(ManagedObject):
    """This is MgmtIPv6IfConfig class."""

    consts = MgmtIPv6IfConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtIPv6IfConfig", "mgmtIPv6IfConfig", "ifConfig-ipv6", VersionMeta.Version112a, "InputOutput", 0x1f, [], ["admin", "ext-lan-config"], [u'mgmtIf', u'networkElement'], [u'mgmtIPv6IfAddr'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "link_local": MoPropertyMeta("link_local", "linkLocal", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["disable", "enable"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "linkLocal": "link_local", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.link_local = None
        self.status = None

        ManagedObject.__init__(self, "MgmtIPv6IfConfig", parent_mo_or_dn, **kwargs)

