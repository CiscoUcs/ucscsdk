"""This module contains the general information for BiosVfResumeOnACPowerLoss ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfResumeOnACPowerLossConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_RESUME_ON_ACPOWER_LOSS_LAST_STATE = "last-state"
    VP_RESUME_ON_ACPOWER_LOSS_PLATFORM_DEFAULT = "platform-default"
    VP_RESUME_ON_ACPOWER_LOSS_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_RESUME_ON_ACPOWER_LOSS_RESET = "reset"
    VP_RESUME_ON_ACPOWER_LOSS_STAY_OFF = "stay-off"


class BiosVfResumeOnACPowerLoss(ManagedObject):
    """This is BiosVfResumeOnACPowerLoss class."""

    consts = BiosVfResumeOnACPowerLossConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfResumeOnACPowerLoss", "biosVfResumeOnACPowerLoss", "Resume-on-AC-power-loss", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_resume_on_ac_power_loss": MoPropertyMeta("vp_resume_on_ac_power_loss", "vpResumeOnACPowerLoss", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["last-state", "platform-default", "platform-recommended", "reset", "stay-off"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpResumeOnACPowerLoss": "vp_resume_on_ac_power_loss", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_resume_on_ac_power_loss = None

        ManagedObject.__init__(self, "BiosVfResumeOnACPowerLoss", parent_mo_or_dn, **kwargs)

