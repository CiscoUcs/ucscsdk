"""This module contains the general information for FcpoolInitiatorEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FcpoolInitiatorEpConsts():
    pass


class FcpoolInitiatorEp(ManagedObject):
    """This is FcpoolInitiatorEp class."""

    consts = FcpoolInitiatorEpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FcpoolInitiatorEp", "fcpoolInitiatorEp", "[id]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["read-only"], ['fcpoolInitiator'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
        "initiator_dn": MoPropertyMeta("initiator_dn", "initiatorDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "initiatorDn": "initiator_dn", 
        "purpose": "purpose", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.initiator_dn = None
        self.purpose = None
        self.status = None

        ManagedObject.__init__(self, "FcpoolInitiatorEp", parent_mo_or_dn, **kwargs)

