"""This module contains the general information for FaultGlobalTypedHolder ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FaultGlobalTypedHolderConsts():
    pass


class FaultGlobalTypedHolder(ManagedObject):
    """This is FaultGlobalTypedHolder class."""

    consts = FaultGlobalTypedHolderConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("FaultGlobalTypedHolder", "faultGlobalTypedHolder", "type-[type]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin"], ['computeResourceAggrEp'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "critical_cnt": MoPropertyMeta("critical_cnt", "criticalCnt", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "major_cnt": MoPropertyMeta("major_cnt", "majorCnt", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "minor_cnt": MoPropertyMeta("minor_cnt", "minorCnt", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []), 
        "warning_cnt": MoPropertyMeta("warning_cnt", "warningCnt", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "criticalCnt": "critical_cnt", 
        "dn": "dn", 
        "majorCnt": "major_cnt", 
        "minorCnt": "minor_cnt", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "warningCnt": "warning_cnt", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.critical_cnt = None
        self.major_cnt = None
        self.minor_cnt = None
        self.name = None
        self.status = None
        self.warning_cnt = None

        ManagedObject.__init__(self, "FaultGlobalTypedHolder", parent_mo_or_dn, **kwargs)

