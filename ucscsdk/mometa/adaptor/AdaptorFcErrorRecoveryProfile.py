"""This module contains the general information for AdaptorFcErrorRecoveryProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorFcErrorRecoveryProfileConsts():
    pass


class AdaptorFcErrorRecoveryProfile(ManagedObject):
    """This is AdaptorFcErrorRecoveryProfile class."""

    consts = AdaptorFcErrorRecoveryProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcErrorRecoveryProfile", "adaptorFcErrorRecoveryProfile", "fc-err-rec", VersionMeta.Version111a, "InputOutput", 0xff, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage"], ['adaptorHostFcIfProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "error_detect_timeout": MoPropertyMeta("error_detect_timeout", "errorDetectTimeout", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "fcp_error_recovery": MoPropertyMeta("fcp_error_recovery", "fcpErrorRecovery", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "link_down_timeout": MoPropertyMeta("link_down_timeout", "linkDownTimeout", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-240000"]), 
        "port_down_io_retry_count": MoPropertyMeta("port_down_io_retry_count", "portDownIoRetryCount", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-255"]), 
        "port_down_timeout": MoPropertyMeta("port_down_timeout", "portDownTimeout", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-240000"]), 
        "resource_allocation_timeout": MoPropertyMeta("resource_allocation_timeout", "resourceAllocationTimeout", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "errorDetectTimeout": "error_detect_timeout", 
        "fcpErrorRecovery": "fcp_error_recovery", 
        "linkDownTimeout": "link_down_timeout", 
        "portDownIoRetryCount": "port_down_io_retry_count", 
        "portDownTimeout": "port_down_timeout", 
        "resourceAllocationTimeout": "resource_allocation_timeout", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.error_detect_timeout = None
        self.fcp_error_recovery = None
        self.link_down_timeout = None
        self.port_down_io_retry_count = None
        self.port_down_timeout = None
        self.resource_allocation_timeout = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorFcErrorRecoveryProfile", parent_mo_or_dn, **kwargs)

