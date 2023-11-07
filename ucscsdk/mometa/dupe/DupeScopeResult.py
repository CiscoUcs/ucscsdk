"""This module contains the general information for DupeScopeResult ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class DupeScopeResultConsts():
    SCOPE_STATUS_FAILURE = "failure"
    SCOPE_STATUS_SUCCESS = "success"


class DupeScopeResult(ManagedObject):
    """This is DupeScopeResult class."""

    consts = DupeScopeResultConsts()
    naming_props = set([])

    mo_meta = MoMeta("DupeScopeResult", "dupeScopeResult", "result", VersionMeta.Version131a, "InputOutput", 0xf, [], ["read-only"], ['dupeScope'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "message": MoPropertyMeta("message", "message", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "scope_status": MoPropertyMeta("scope_status", "scopeStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failure", "success"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "update_time": MoPropertyMeta("update_time", "updateTime", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "message": "message", 
        "rn": "rn", 
        "scopeStatus": "scope_status", 
        "status": "status", 
        "updateTime": "update_time", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.message = None
        self.scope_status = None
        self.status = None
        self.update_time = None

        ManagedObject.__init__(self, "DupeScopeResult", parent_mo_or_dn, **kwargs)

