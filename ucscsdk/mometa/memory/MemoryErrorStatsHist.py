"""This module contains the general information for MemoryErrorStatsHist ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MemoryErrorStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class MemoryErrorStatsHist(ManagedObject):
    """This is MemoryErrorStatsHist class."""

    consts = MemoryErrorStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("MemoryErrorStatsHist", "memoryErrorStatsHist", "[id]", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["read-only"], ['memoryErrorStats'], [], [None])

    prop_meta = {
        "address_parity_errors": MoPropertyMeta("address_parity_errors", "addressParityErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "address_parity_errors_avg": MoPropertyMeta("address_parity_errors_avg", "addressParityErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "address_parity_errors_max": MoPropertyMeta("address_parity_errors_max", "addressParityErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "address_parity_errors_min": MoPropertyMeta("address_parity_errors_min", "addressParityErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "address_parity_errors_running": MoPropertyMeta("address_parity_errors_running", "addressParityErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ecc_multibit_errors": MoPropertyMeta("ecc_multibit_errors", "eccMultibitErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ecc_multibit_errors_avg": MoPropertyMeta("ecc_multibit_errors_avg", "eccMultibitErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ecc_multibit_errors_max": MoPropertyMeta("ecc_multibit_errors_max", "eccMultibitErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ecc_multibit_errors_min": MoPropertyMeta("ecc_multibit_errors_min", "eccMultibitErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ecc_multibit_errors_running": MoPropertyMeta("ecc_multibit_errors_running", "eccMultibitErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ecc_singlebit_errors": MoPropertyMeta("ecc_singlebit_errors", "eccSinglebitErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ecc_singlebit_errors_avg": MoPropertyMeta("ecc_singlebit_errors_avg", "eccSinglebitErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ecc_singlebit_errors_max": MoPropertyMeta("ecc_singlebit_errors_max", "eccSinglebitErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ecc_singlebit_errors_min": MoPropertyMeta("ecc_singlebit_errors_min", "eccSinglebitErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ecc_singlebit_errors_running": MoPropertyMeta("ecc_singlebit_errors_running", "eccSinglebitErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111a, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "mismatch_errors": MoPropertyMeta("mismatch_errors", "mismatchErrors", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mismatch_errors_avg": MoPropertyMeta("mismatch_errors_avg", "mismatchErrorsAvg", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mismatch_errors_max": MoPropertyMeta("mismatch_errors_max", "mismatchErrorsMax", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mismatch_errors_min": MoPropertyMeta("mismatch_errors_min", "mismatchErrorsMin", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mismatch_errors_running": MoPropertyMeta("mismatch_errors_running", "mismatchErrorsRunning", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "addressParityErrors": "address_parity_errors", 
        "addressParityErrorsAvg": "address_parity_errors_avg", 
        "addressParityErrorsMax": "address_parity_errors_max", 
        "addressParityErrorsMin": "address_parity_errors_min", 
        "addressParityErrorsRunning": "address_parity_errors_running", 
        "childAction": "child_action", 
        "dn": "dn", 
        "eccMultibitErrors": "ecc_multibit_errors", 
        "eccMultibitErrorsAvg": "ecc_multibit_errors_avg", 
        "eccMultibitErrorsMax": "ecc_multibit_errors_max", 
        "eccMultibitErrorsMin": "ecc_multibit_errors_min", 
        "eccMultibitErrorsRunning": "ecc_multibit_errors_running", 
        "eccSinglebitErrors": "ecc_singlebit_errors", 
        "eccSinglebitErrorsAvg": "ecc_singlebit_errors_avg", 
        "eccSinglebitErrorsMax": "ecc_singlebit_errors_max", 
        "eccSinglebitErrorsMin": "ecc_singlebit_errors_min", 
        "eccSinglebitErrorsRunning": "ecc_singlebit_errors_running", 
        "id": "id", 
        "mismatchErrors": "mismatch_errors", 
        "mismatchErrorsAvg": "mismatch_errors_avg", 
        "mismatchErrorsMax": "mismatch_errors_max", 
        "mismatchErrorsMin": "mismatch_errors_min", 
        "mismatchErrorsRunning": "mismatch_errors_running", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.address_parity_errors = None
        self.address_parity_errors_avg = None
        self.address_parity_errors_max = None
        self.address_parity_errors_min = None
        self.address_parity_errors_running = None
        self.child_action = None
        self.ecc_multibit_errors = None
        self.ecc_multibit_errors_avg = None
        self.ecc_multibit_errors_max = None
        self.ecc_multibit_errors_min = None
        self.ecc_multibit_errors_running = None
        self.ecc_singlebit_errors = None
        self.ecc_singlebit_errors_avg = None
        self.ecc_singlebit_errors_max = None
        self.ecc_singlebit_errors_min = None
        self.ecc_singlebit_errors_running = None
        self.mismatch_errors = None
        self.mismatch_errors_avg = None
        self.mismatch_errors_max = None
        self.mismatch_errors_min = None
        self.mismatch_errors_running = None
        self.most_recent = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "MemoryErrorStatsHist", parent_mo_or_dn, **kwargs)

