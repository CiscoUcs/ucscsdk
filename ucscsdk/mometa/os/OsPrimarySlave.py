"""This module contains the general information for OsPrimarySlave ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class OsPrimarySlaveConsts():
    RESELECT_POLICY_ALWAYS = "always"
    RESELECT_POLICY_BETTER = "better"
    RESELECT_POLICY_FAILURE = "failure"


class OsPrimarySlave(ManagedObject):
    """This is OsPrimarySlave class."""

    consts = OsPrimarySlaveConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("OsPrimarySlave", "osPrimarySlave", "slave-intf-[name]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "reselect_policy": MoPropertyMeta("reselect_policy", "reselectPolicy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["always", "better", "failure"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "reselectPolicy": "reselect_policy", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.reselect_policy = None
        self.status = None

        ManagedObject.__init__(self, "OsPrimarySlave", parent_mo_or_dn, **kwargs)

