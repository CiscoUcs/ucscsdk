"""This module contains the general information for AaaLdapGroupRule ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AaaLdapGroupRuleConsts():
    AUTHORIZATION_DISABLE = "disable"
    AUTHORIZATION_ENABLE = "enable"
    TRAVERSAL_NON_RECURSIVE = "non-recursive"
    TRAVERSAL_RECURSIVE = "recursive"


class AaaLdapGroupRule(ManagedObject):
    """This is AaaLdapGroupRule class."""

    consts = AaaLdapGroupRuleConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaLdapGroupRule", "aaaLdapGroupRule", "ldapgroup-rule", VersionMeta.Version101a, "InputOutput", 0x1ff, [], ["aaa", "admin", "domain-group-management"], ['aaaLdapEp', 'aaaLdapProvider'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "authorization": MoPropertyMeta("authorization", "authorization", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disable", "enable"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "target_attr": MoPropertyMeta("target_attr", "targetAttr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, 0, 63, None, [], []), 
        "traversal": MoPropertyMeta("traversal", "traversal", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["non-recursive", "recursive"], []), 
    }

    prop_map = {
        "authorization": "authorization", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "targetAttr": "target_attr", 
        "traversal": "traversal", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.authorization = None
        self.child_action = None
        self.descr = None
        self.name = None
        self.status = None
        self.target_attr = None
        self.traversal = None

        ManagedObject.__init__(self, "AaaLdapGroupRule", parent_mo_or_dn, **kwargs)

