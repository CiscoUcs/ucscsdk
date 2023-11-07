"""This module contains the general information for BiosVfPackageCStateLimit ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfPackageCStateLimitConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_PACKAGE_CSTATE_LIMIT_AUTO = "auto"
    VP_PACKAGE_CSTATE_LIMIT_C0 = "c0"
    VP_PACKAGE_CSTATE_LIMIT_C1 = "c1"
    VP_PACKAGE_CSTATE_LIMIT_C2 = "c2"
    VP_PACKAGE_CSTATE_LIMIT_C3 = "c3"
    VP_PACKAGE_CSTATE_LIMIT_C6 = "c6"
    VP_PACKAGE_CSTATE_LIMIT_C7 = "c7"
    VP_PACKAGE_CSTATE_LIMIT_C7S = "c7s"
    VP_PACKAGE_CSTATE_LIMIT_NO_LIMIT = "no-limit"
    VP_PACKAGE_CSTATE_LIMIT_PLATFORM_DEFAULT = "platform-default"
    VP_PACKAGE_CSTATE_LIMIT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfPackageCStateLimit(ManagedObject):
    """This is BiosVfPackageCStateLimit class."""

    consts = BiosVfPackageCStateLimitConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfPackageCStateLimit", "biosVfPackageCStateLimit", "Package-C-State-Limit", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_package_c_state_limit": MoPropertyMeta("vp_package_c_state_limit", "vpPackageCStateLimit", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "c0", "c1", "c2", "c3", "c6", "c7", "c7s", "no-limit", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpPackageCStateLimit": "vp_package_c_state_limit", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_package_c_state_limit = None

        ManagedObject.__init__(self, "BiosVfPackageCStateLimit", parent_mo_or_dn, **kwargs)

