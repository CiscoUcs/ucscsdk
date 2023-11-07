"""This module contains the general information for ComputeResourceAggrEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeResourceAggrEpConsts():
    POLLING_INTERVAL_10_MIN = "10 min"
    POLLING_INTERVAL_15_MIN = "15 min"
    POLLING_INTERVAL_20_MIN = "20 min"
    POLLING_INTERVAL_30_MIN = "30 min"
    POLLING_INTERVAL_45_MIN = "45 min"
    POLLING_INTERVAL_5_MIN = "5 min"
    POLLING_INTERVAL_60_MIN = "60 min"


class ComputeResourceAggrEp(ManagedObject):
    """This is ComputeResourceAggrEp class."""

    consts = ComputeResourceAggrEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeResourceAggrEp", "computeResourceAggrEp", "compute", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin"], ['topRoot'], ['computeFaultUpgradeFlag', 'computeGroupMembership', 'computeProfile', 'computeResourceSetManager', 'computeSystem', 'faultGlobalSeverityHolder', 'faultGlobalTypedHolder'], ["Get", "Set"])

    prop_meta = {
        "available_physical_cnt": MoPropertyMeta("available_physical_cnt", "availablePhysicalCnt", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "polling_interval": MoPropertyMeta("polling_interval", "pollingInterval", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["10 min", "15 min", "20 min", "30 min", "45 min", "5 min", "60 min"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "total_physical_cnt": MoPropertyMeta("total_physical_cnt", "totalPhysicalCnt", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "availablePhysicalCnt": "available_physical_cnt", 
        "childAction": "child_action", 
        "dn": "dn", 
        "pollingInterval": "polling_interval", 
        "rn": "rn", 
        "status": "status", 
        "totalPhysicalCnt": "total_physical_cnt", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.available_physical_cnt = None
        self.child_action = None
        self.polling_interval = None
        self.status = None
        self.total_physical_cnt = None

        ManagedObject.__init__(self, "ComputeResourceAggrEp", **kwargs)

