"""This module contains the general information for IdentpoolDomainGroupQual ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IdentpoolDomainGroupQualConsts():
    ALLOW_DESCENDANTS_FALSE = "false"
    ALLOW_DESCENDANTS_NO = "no"
    ALLOW_DESCENDANTS_TRUE = "true"
    ALLOW_DESCENDANTS_YES = "yes"


class IdentpoolDomainGroupQual(ManagedObject):
    """This is IdentpoolDomainGroupQual class."""

    consts = IdentpoolDomainGroupQualConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("IdentpoolDomainGroupQual", "identpoolDomainGroupQual", "domaingroup-[name]", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["admin"], ['identpoolBlockQual'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "allow_descendants": MoPropertyMeta("allow_descendants", "allowDescendants", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "group_dn": MoPropertyMeta("group_dn", "groupDn", "string", VersionMeta.Version111a, MoPropertyMeta.CREATE_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "allowDescendants": "allow_descendants", 
        "childAction": "child_action", 
        "dn": "dn", 
        "groupDn": "group_dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.allow_descendants = None
        self.child_action = None
        self.group_dn = None
        self.status = None

        ManagedObject.__init__(self, "IdentpoolDomainGroupQual", parent_mo_or_dn, **kwargs)

