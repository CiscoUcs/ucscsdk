"""This module contains the general information for DupeIntRequestor ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class DupeIntRequestorConsts():
    pass


class DupeIntRequestor(ManagedObject):
    """This is DupeIntRequestor class."""

    consts = DupeIntRequestorConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("DupeIntRequestor", "dupeIntRequestor", "int-requestor-[name]", VersionMeta.Version131a, "InputOutput", 0x3f, [], ["read-only"], ['dupeScope'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "on_behalf_of_ident": MoPropertyMeta("on_behalf_of_ident", "onBehalfOfIdent", "string", VersionMeta.Version131a, MoPropertyMeta.CREATE_ONLY, 0x8, 0, 510, None, [], []), 
        "on_behalf_of_type": MoPropertyMeta("on_behalf_of_type", "onBehalfOfType", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "onBehalfOfIdent": "on_behalf_of_ident", 
        "onBehalfOfType": "on_behalf_of_type", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.on_behalf_of_ident = None
        self.on_behalf_of_type = None
        self.status = None

        ManagedObject.__init__(self, "DupeIntRequestor", parent_mo_or_dn, **kwargs)

