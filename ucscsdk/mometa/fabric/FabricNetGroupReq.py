"""This module contains the general information for FabricNetGroupReq ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricNetGroupReqConsts():
    pass


class FabricNetGroupReq(ManagedObject):
    """This is FabricNetGroupReq class."""

    consts = FabricNetGroupReqConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricNetGroupReq", "fabricNetGroupReq", "ngreq-[name]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["admin", "ext-lan-config", "ext-lan-policy", "ls-network"], ['orgOrg'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_issues": MoPropertyMeta("config_issues", "configIssues", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|permit-unresolved),){0,2}(defaultValue|not-applicable|permit-unresolved){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configIssues": "config_issues", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config_issues = None
        self.status = None

        ManagedObject.__init__(self, "FabricNetGroupReq", parent_mo_or_dn, **kwargs)

