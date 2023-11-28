"""This module contains the general information for ConfigInputConfigSet ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigInputConfigSetConsts():
    pass


class ConfigInputConfigSet(ManagedObject):
    """This is ConfigInputConfigSet class."""

    consts = ConfigInputConfigSetConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigInputConfigSet", "configInputConfigSet", "InputConfigSet", VersionMeta.Version111a, "InputOutput", 0xf, [], ["read-only"], ['configImpactAnalyzer'], ['configInputConfig'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "created": MoPropertyMeta("created", "created", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "deleted": MoPropertyMeta("deleted", "deleted", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "modified": MoPropertyMeta("modified", "modified", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "created": "created", 
        "deleted": "deleted", 
        "dn": "dn", 
        "modified": "modified", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.created = None
        self.deleted = None
        self.modified = None
        self.status = None

        ManagedObject.__init__(self, "ConfigInputConfigSet", parent_mo_or_dn, **kwargs)

