"""This module contains the general information for FaultSummaryInst ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FaultSummaryInstConsts():
    SEVERITY_CLEARED = "cleared"
    SEVERITY_CONDITION = "condition"
    SEVERITY_CRITICAL = "critical"
    SEVERITY_INFO = "info"
    SEVERITY_MAJOR = "major"
    SEVERITY_MINOR = "minor"
    SEVERITY_WARNING = "warning"


class FaultSummaryInst(ManagedObject):
    """This is FaultSummaryInst class."""

    consts = FaultSummaryInstConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FaultSummaryInst", "faultSummaryInst", "fault-summary-[name]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["admin", "fault", "operations"], ['faultDomainEp', 'faultSummaryInst'], ['faultSummaryInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "context": MoPropertyMeta("context", "context", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_inst_ref": MoPropertyMeta("domain_inst_ref", "domainInstRef", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "fault_code": MoPropertyMeta("fault_code", "faultCode", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "severity": MoPropertyMeta("severity", "severity", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "context": "context", 
        "dn": "dn", 
        "domainInstRef": "domain_inst_ref", 
        "faultCode": "fault_code", 
        "id": "id", 
        "name": "name", 
        "rn": "rn", 
        "severity": "severity", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.context = None
        self.domain_inst_ref = None
        self.fault_code = None
        self.id = None
        self.severity = None
        self.status = None

        ManagedObject.__init__(self, "FaultSummaryInst", parent_mo_or_dn, **kwargs)

