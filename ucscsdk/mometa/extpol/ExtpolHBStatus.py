"""This module contains the general information for ExtpolHBStatus ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ExtpolHBStatusConsts():
    SCAN_COMPLETED_COMPLETED = "completed"
    SCAN_COMPLETED_IN_PROGRESS = "in-progress"
    SCAN_ENABLED_DISABLED = "disabled"
    SCAN_ENABLED_ENABLED = "enabled"


class ExtpolHBStatus(ManagedObject):
    """This is ExtpolHBStatus class."""

    consts = ExtpolHBStatusConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtpolHBStatus", "extpolHBStatus", "hb-status", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["admin"], ['extpolClientCont'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "scan_completed": MoPropertyMeta("scan_completed", "scanCompleted", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["completed", "in-progress"], []), 
        "scan_enabled": MoPropertyMeta("scan_enabled", "scanEnabled", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["disabled", "enabled"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "scanCompleted": "scan_completed", 
        "scanEnabled": "scan_enabled", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.scan_completed = None
        self.scan_enabled = None
        self.status = None

        ManagedObject.__init__(self, "ExtpolHBStatus", parent_mo_or_dn, **kwargs)

