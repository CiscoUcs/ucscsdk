"""This module contains the general information for VersionFilter ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VersionFilterConsts():
    pass


class VersionFilter(ManagedObject):
    """This is VersionFilter class."""

    consts = VersionFilterConsts()
    naming_props = set(['capability'])

    mo_meta = MoMeta("VersionFilter", "versionFilter", "filter-[capability]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["read-only"], ['versionMatrix'], [], [None])

    prop_meta = {
        "capability": MoPropertyMeta("capability", "capability", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x2, None, None, None, [], ["0-4294967295"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "compatible_version": MoPropertyMeta("compatible_version", "compatibleVersion", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "capability": "capability", 
        "childAction": "child_action", 
        "compatibleVersion": "compatible_version", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, capability, **kwargs):
        self._dirty_mask = 0
        self.capability = capability
        self.child_action = None
        self.compatible_version = None
        self.status = None

        ManagedObject.__init__(self, "VersionFilter", parent_mo_or_dn, **kwargs)

