"""This module contains the general information for BiosVfPSTATECoordination ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfPSTATECoordinationConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_PSTATECOORDINATION_HW_ALL = "hw-all"
    VP_PSTATECOORDINATION_PLATFORM_DEFAULT = "platform-default"
    VP_PSTATECOORDINATION_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_PSTATECOORDINATION_SW_ALL = "sw-all"
    VP_PSTATECOORDINATION_SW_ANY = "sw-any"


class BiosVfPSTATECoordination(ManagedObject):
    """This is BiosVfPSTATECoordination class."""

    consts = BiosVfPSTATECoordinationConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfPSTATECoordination", "biosVfPSTATECoordination", "P-STATE-Coordination", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_pstate_coordination": MoPropertyMeta("vp_pstate_coordination", "vpPSTATECoordination", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["hw-all", "platform-default", "platform-recommended", "sw-all", "sw-any"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpPSTATECoordination": "vp_pstate_coordination", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_pstate_coordination = None

        ManagedObject.__init__(self, "BiosVfPSTATECoordination", parent_mo_or_dn, **kwargs)

