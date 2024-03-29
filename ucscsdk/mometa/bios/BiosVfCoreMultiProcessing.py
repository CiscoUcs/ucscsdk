"""This module contains the general information for BiosVfCoreMultiProcessing ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfCoreMultiProcessingConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_CORE_MULTI_PROCESSING_1 = "1"
    VP_CORE_MULTI_PROCESSING_10 = "10"
    VP_CORE_MULTI_PROCESSING_11 = "11"
    VP_CORE_MULTI_PROCESSING_12 = "12"
    VP_CORE_MULTI_PROCESSING_13 = "13"
    VP_CORE_MULTI_PROCESSING_14 = "14"
    VP_CORE_MULTI_PROCESSING_15 = "15"
    VP_CORE_MULTI_PROCESSING_16 = "16"
    VP_CORE_MULTI_PROCESSING_17 = "17"
    VP_CORE_MULTI_PROCESSING_18 = "18"
    VP_CORE_MULTI_PROCESSING_19 = "19"
    VP_CORE_MULTI_PROCESSING_2 = "2"
    VP_CORE_MULTI_PROCESSING_20 = "20"
    VP_CORE_MULTI_PROCESSING_21 = "21"
    VP_CORE_MULTI_PROCESSING_22 = "22"
    VP_CORE_MULTI_PROCESSING_23 = "23"
    VP_CORE_MULTI_PROCESSING_24 = "24"
    VP_CORE_MULTI_PROCESSING_3 = "3"
    VP_CORE_MULTI_PROCESSING_4 = "4"
    VP_CORE_MULTI_PROCESSING_5 = "5"
    VP_CORE_MULTI_PROCESSING_6 = "6"
    VP_CORE_MULTI_PROCESSING_7 = "7"
    VP_CORE_MULTI_PROCESSING_8 = "8"
    VP_CORE_MULTI_PROCESSING_9 = "9"
    VP_CORE_MULTI_PROCESSING_ALL = "all"
    VP_CORE_MULTI_PROCESSING_PLATFORM_DEFAULT = "platform-default"
    VP_CORE_MULTI_PROCESSING_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfCoreMultiProcessing(ManagedObject):
    """This is BiosVfCoreMultiProcessing class."""

    consts = BiosVfCoreMultiProcessingConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfCoreMultiProcessing", "biosVfCoreMultiProcessing", "Core-MultiProcessing", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_core_multi_processing": MoPropertyMeta("vp_core_multi_processing", "vpCoreMultiProcessing", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "2", "20", "21", "22", "23", "24", "3", "4", "5", "6", "7", "8", "9", "all", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpCoreMultiProcessing": "vp_core_multi_processing", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_core_multi_processing = None

        ManagedObject.__init__(self, "BiosVfCoreMultiProcessing", parent_mo_or_dn, **kwargs)

