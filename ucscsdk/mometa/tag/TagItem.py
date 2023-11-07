"""This module contains the general information for TagItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class TagItemConsts():
    pass


class TagItem(ManagedObject):
    """This is TagItem class."""

    consts = TagItemConsts()
    naming_props = set(['value'])

    mo_meta = MoMeta("TagItem", "tagItem", "tag-[value]", VersionMeta.Version151a, "InputOutput", 0x1f, [], ["admin", "tag"], ['tagDef'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x10, 1, 64, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "value": "value", 
    }

    def __init__(self, parent_mo_or_dn, value, **kwargs):
        self._dirty_mask = 0
        self.value = value
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "TagItem", parent_mo_or_dn, **kwargs)

