"""This module contains the general information for ComputeDomainGroupQual ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeDomainGroupQualConsts():
    HIERARCHICAL_FALSE = "false"
    HIERARCHICAL_NO = "no"
    HIERARCHICAL_TRUE = "true"
    HIERARCHICAL_YES = "yes"


class ComputeDomainGroupQual(ManagedObject):
    """This is ComputeDomainGroupQual class."""

    consts = ComputeDomainGroupQualConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ComputeDomainGroupQual", "computeDomainGroupQual", "domaingroup-qualifier-[name]", VersionMeta.Version141a, "InputOutput", 0x7f, [], ["admin", "pn-policy", "read-only"], ['computeDomainQual'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, None, [], []), 
        "hierarchical": MoPropertyMeta("hierarchical", "hierarchical", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "domainGroupDn": "domain_group_dn", 
        "hierarchical": "hierarchical", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.domain_group_dn = None
        self.hierarchical = None
        self.status = None

        ManagedObject.__init__(self, "ComputeDomainGroupQual", parent_mo_or_dn, **kwargs)

