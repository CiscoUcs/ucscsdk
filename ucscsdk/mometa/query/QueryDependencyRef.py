"""This module contains the general information for QueryDependencyRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class QueryDependencyRefConsts():
    pass


class QueryDependencyRef(ManagedObject):
    """This is QueryDependencyRef class."""

    consts = QueryDependencyRefConsts()
    naming_props = set(['index'])

    mo_meta = MoMeta("QueryDependencyRef", "queryDependencyRef", "depref-[index]", VersionMeta.Version112a, "InputOutput", 0x3f, [], ["admin"], ['queryImportContext'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "dependency_dn": MoPropertyMeta("dependency_dn", "DependencyDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "DependencyDn": "dependency_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "index": "index", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, index, **kwargs):
        self._dirty_mask = 0
        self.index = index
        self.dependency_dn = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "QueryDependencyRef", parent_mo_or_dn, **kwargs)

