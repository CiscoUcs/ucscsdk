"""This module contains the general information for DiagLogEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class DiagLogEpConsts():
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"


class DiagLogEp(ManagedObject):
    """This is DiagLogEp class."""

    consts = DiagLogEpConsts()
    naming_props = set(['switchId'])

    mo_meta = MoMeta("DiagLogEp", "diagLogEp", "logep-[switch_id]", VersionMeta.Version201b, "InputOutput", 0x1f, [], [""], ['diagRslt'], [], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "log_dn": MoPropertyMeta("log_dn", "logDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x10, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "logDn": "log_dn", 
        "rn": "rn", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, switch_id, **kwargs):
        self._dirty_mask = 0
        self.switch_id = switch_id
        self.child_action = None
        self.log_dn = None
        self.status = None

        ManagedObject.__init__(self, "DiagLogEp", parent_mo_or_dn, **kwargs)

