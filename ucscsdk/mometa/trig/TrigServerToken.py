"""This module contains the general information for TrigServerToken ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class TrigServerTokenConsts():
    OPER_STATE_EXPIRED = "expired"
    OPER_STATE_VALID = "valid"


class TrigServerToken(ManagedObject):
    """This is TrigServerToken class."""

    consts = TrigServerTokenConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("TrigServerToken", "trigServerToken", "servertoken-[id]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["read-only"], ['trigMeta'], [], ["Get"])

    prop_meta = {
        "activity_ts": MoPropertyMeta("activity_ts", "activityTs", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["expired", "valid"], []), 
        "owner_dn": MoPropertyMeta("owner_dn", "ownerDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "token_requestor_dn": MoPropertyMeta("token_requestor_dn", "tokenRequestorDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "triggerable_dn": MoPropertyMeta("triggerable_dn", "triggerableDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
    }

    prop_map = {
        "activityTs": "activity_ts", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "operState": "oper_state", 
        "ownerDn": "owner_dn", 
        "rn": "rn", 
        "status": "status", 
        "tokenRequestorDn": "token_requestor_dn", 
        "triggerableDn": "triggerable_dn", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.activity_ts = None
        self.child_action = None
        self.oper_state = None
        self.owner_dn = None
        self.status = None
        self.token_requestor_dn = None
        self.triggerable_dn = None

        ManagedObject.__init__(self, "TrigServerToken", parent_mo_or_dn, **kwargs)

