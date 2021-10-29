"""This module contains the general information for BiosVfTPMSupport ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfTPMSupportConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_TPMSUPPORT_DISABLED = "disabled"
    VP_TPMSUPPORT_ENABLED = "enabled"
    VP_TPMSUPPORT_PLATFORM_DEFAULT = "platform-default"
    VP_TPMSUPPORT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfTPMSupport(ManagedObject):
    """This is BiosVfTPMSupport class."""

    consts = BiosVfTPMSupportConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfTPMSupport", "biosVfTPMSupport", "TPM-Support", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["read-only"], [u'biosVProfile'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_tpm_support": MoPropertyMeta("vp_tpm_support", "vpTPMSupport", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpTPMSupport": "vp_tpm_support", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_tpm_support = None

        ManagedObject.__init__(self, "BiosVfTPMSupport", parent_mo_or_dn, **kwargs)

