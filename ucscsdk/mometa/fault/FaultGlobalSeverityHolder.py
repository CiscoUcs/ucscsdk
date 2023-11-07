"""This module contains the general information for FaultGlobalSeverityHolder ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FaultGlobalSeverityHolderConsts():
    pass


class FaultGlobalSeverityHolder(ManagedObject):
    """This is FaultGlobalSeverityHolder class."""

    consts = FaultGlobalSeverityHolderConsts()
    naming_props = set([])

    mo_meta = MoMeta("FaultGlobalSeverityHolder", "faultGlobalSeverityHolder", "faultholder", VersionMeta.Version101a, "InputOutput", 0xf, [], ["admin"], ['computeResourceAggrEp'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "critical_cnt": MoPropertyMeta("critical_cnt", "criticalCnt", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "major_cnt": MoPropertyMeta("major_cnt", "majorCnt", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "minor_cnt": MoPropertyMeta("minor_cnt", "minorCnt", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "warning_cnt": MoPropertyMeta("warning_cnt", "warningCnt", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "criticalCnt": "critical_cnt", 
        "dn": "dn", 
        "majorCnt": "major_cnt", 
        "minorCnt": "minor_cnt", 
        "rn": "rn", 
        "status": "status", 
        "warningCnt": "warning_cnt", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.critical_cnt = None
        self.major_cnt = None
        self.minor_cnt = None
        self.status = None
        self.warning_cnt = None

        ManagedObject.__init__(self, "FaultGlobalSeverityHolder", parent_mo_or_dn, **kwargs)

