"""This module contains the general information for ProcTxCounts ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ProcTxCountsConsts():
    pass


class ProcTxCounts(ManagedObject):
    """This is ProcTxCounts class."""

    consts = ProcTxCountsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ProcTxCounts", "procTxCounts", "tx", VersionMeta.Version101a, "InputOutput", 0xf, [], ["read-only"], ['procManager', 'procSvc'], [], ["Get"])

    prop_meta = {
        "bulked": MoPropertyMeta("bulked", "bulked", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "failed": MoPropertyMeta("failed", "failed", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "retried": MoPropertyMeta("retried", "retried", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "singleton": MoPropertyMeta("singleton", "singleton", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "successfull": MoPropertyMeta("successfull", "successfull", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "total": MoPropertyMeta("total", "total", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "bulked": "bulked", 
        "childAction": "child_action", 
        "dn": "dn", 
        "failed": "failed", 
        "retried": "retried", 
        "rn": "rn", 
        "singleton": "singleton", 
        "status": "status", 
        "successfull": "successfull", 
        "total": "total", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.bulked = None
        self.child_action = None
        self.failed = None
        self.retried = None
        self.singleton = None
        self.status = None
        self.successfull = None
        self.total = None

        ManagedObject.__init__(self, "ProcTxCounts", parent_mo_or_dn, **kwargs)

