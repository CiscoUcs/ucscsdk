"""This module contains the general information for PowerGroupQual ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PowerGroupQualConsts():
    pass


class PowerGroupQual(ManagedObject):
    """This is PowerGroupQual class."""

    consts = PowerGroupQualConsts()
    naming_props = set(['groupName'])

    mo_meta = MoMeta("PowerGroupQual", "powerGroupQual", "power-group-[group_name]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['computeQual'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "group_name": MoPropertyMeta("group_name", "groupName", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "groupName": "group_name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, group_name, **kwargs):
        self._dirty_mask = 0
        self.group_name = group_name
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "PowerGroupQual", parent_mo_or_dn, **kwargs)

