"""This module contains the general information for ComputeSession ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeSessionConsts():
    pass


class ComputeSession(ManagedObject):
    """This is ComputeSession class."""

    consts = ComputeSessionConsts()
    naming_props = set(['systemName'])

    mo_meta = MoMeta("ComputeSession", "computeSession", "session-[system_name]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["aaa", "admin"], ['computeUser'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cookie": MoPropertyMeta("cookie", "cookie", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "system_name": MoPropertyMeta("system_name", "systemName", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "cookie": "cookie", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "systemName": "system_name", 
    }

    def __init__(self, parent_mo_or_dn, system_name, **kwargs):
        self._dirty_mask = 0
        self.system_name = system_name
        self.child_action = None
        self.cookie = None
        self.status = None

        ManagedObject.__init__(self, "ComputeSession", parent_mo_or_dn, **kwargs)

