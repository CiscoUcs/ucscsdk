"""This module contains the general information for ComputeResourceSetMember ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeResourceSetMemberConsts():
    OPER_STATE_INITIALIZING = "initializing"
    OPER_STATE_READY = "ready"
    OPER_STATE_TIMEDOUT = "timedout"


class ComputeResourceSetMember(ManagedObject):
    """This is ComputeResourceSetMember class."""

    consts = ComputeResourceSetMemberConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputeResourceSetMember", "computeResourceSetMember", "rsrc-set-member-[id]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin"], ['computeResourceSet'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["initializing", "ready", "timedout"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "operState": "oper_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.oper_state = None
        self.status = None

        ManagedObject.__init__(self, "ComputeResourceSetMember", parent_mo_or_dn, **kwargs)

