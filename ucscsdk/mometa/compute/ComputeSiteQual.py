"""This module contains the general information for ComputeSiteQual ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeSiteQualConsts():
    pass


class ComputeSiteQual(ManagedObject):
    """This is ComputeSiteQual class."""

    consts = ComputeSiteQualConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ComputeSiteQual", "computeSiteQual", "site-[name]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin", "pn-policy", "read-only"], ['computeDomainQual', 'computeSystemQual'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "regex": MoPropertyMeta("regex", "regex", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r""".+""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "regex": "regex", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.regex = None
        self.status = None

        ManagedObject.__init__(self, "ComputeSiteQual", parent_mo_or_dn, **kwargs)

