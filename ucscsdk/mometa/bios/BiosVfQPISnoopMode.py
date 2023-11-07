"""This module contains the general information for BiosVfQPISnoopMode ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfQPISnoopModeConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_QPISNOOP_MODE_AUTO = "auto"
    VP_QPISNOOP_MODE_CLUSTER_ON_DIE = "cluster-on-die"
    VP_QPISNOOP_MODE_EARLY_SNOOP = "early-snoop"
    VP_QPISNOOP_MODE_HOME_DIRECTORY_SNOOP_WITH_OSB = "home-directory-snoop-with-osb"
    VP_QPISNOOP_MODE_HOME_SNOOP = "home-snoop"
    VP_QPISNOOP_MODE_PLATFORM_DEFAULT = "platform-default"
    VP_QPISNOOP_MODE_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfQPISnoopMode(ManagedObject):
    """This is BiosVfQPISnoopMode class."""

    consts = BiosVfQPISnoopModeConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfQPISnoopMode", "biosVfQPISnoopMode", "QPI-Snoop-Mode", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_qpi_snoop_mode": MoPropertyMeta("vp_qpi_snoop_mode", "vpQPISnoopMode", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "cluster-on-die", "early-snoop", "home-directory-snoop-with-osb", "home-snoop", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpQPISnoopMode": "vp_qpi_snoop_mode", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_qpi_snoop_mode = None

        ManagedObject.__init__(self, "BiosVfQPISnoopMode", parent_mo_or_dn, **kwargs)

