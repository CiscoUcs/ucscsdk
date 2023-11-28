"""This module contains the general information for FaultHolder ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FaultHolderConsts():
    IS_PINNING_CLEARED_FALSE = "false"
    IS_PINNING_CLEARED_NO = "no"
    IS_PINNING_CLEARED_TRUE = "true"
    IS_PINNING_CLEARED_YES = "yes"


class FaultHolder(ManagedObject):
    """This is FaultHolder class."""

    consts = FaultHolderConsts()
    naming_props = set([])

    mo_meta = MoMeta("FaultHolder", "faultHolder", "fault", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin", "fault"], ['topRoot'], ['faultTypedHolder'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "is_pinning_cleared": MoPropertyMeta("is_pinning_cleared", "isPinningCleared", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "last_pin_time": MoPropertyMeta("last_pin_time", "lastPinTime", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "total_faults": MoPropertyMeta("total_faults", "totalFaults", "ulong", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isPinningCleared": "is_pinning_cleared", 
        "lastPinTime": "last_pin_time", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "totalFaults": "total_faults", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.is_pinning_cleared = None
        self.last_pin_time = None
        self.name = None
        self.status = None
        self.total_faults = None

        ManagedObject.__init__(self, "FaultHolder", **kwargs)

