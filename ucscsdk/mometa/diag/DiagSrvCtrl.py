"""This module contains the general information for DiagSrvCtrl ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class DiagSrvCtrlConsts():
    ADMIN_STATE_CANCEL = "cancel"
    ADMIN_STATE_READY = "ready"
    ADMIN_STATE_TRIGGER = "trigger"
    END_TS_NEVER = "never"
    END_TS_M_NEVER = "never"
    OPER_STATE_CANCELLED = "cancelled"
    OPER_STATE_COMPLETED = "completed"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_IDLE = "idle"
    OPER_STATE_IN_PROGRESS = "in-progress"
    OPER_STATE_UNKNOWN = "unknown"
    START_TS_NEVER = "never"
    START_TS_M_NEVER = "never"


class DiagSrvCtrl(ManagedObject):
    """This is DiagSrvCtrl class."""

    consts = DiagSrvCtrlConsts()
    naming_props = set([])

    mo_meta = MoMeta("DiagSrvCtrl", "diagSrvCtrl", "diag", VersionMeta.Version201b, "InputOutput", 0x3f, [], ["admin", "pn-equipment", "pn-maintenance"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], ['diagRslt', 'diagRunPolicy', 'diagSrvCtrlOperation', 'etherServerIntFIo'], ["get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["cancel", "ready", "trigger"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "end_ts": MoPropertyMeta("end_ts", "endTs", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "end_ts_m": MoPropertyMeta("end_ts_m", "endTsM", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["never"], ["0-4294967295"]), 
        "error_descr": MoPropertyMeta("error_descr", "errorDescr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_qualifier": MoPropertyMeta("oper_qualifier", "operQualifier", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|stage-failed|test-failure|run-cancelled|component-error|stages-completed),){0,6}(defaultValue|not-applicable|stage-failed|test-failure|run-cancelled|component-error|stages-completed){0,1}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cancelled", "completed", "failed", "idle", "in-progress", "unknown"], []), 
        "overall_progress": MoPropertyMeta("overall_progress", "overallProgress", "byte", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-100"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "run_policy_name": MoPropertyMeta("run_policy_name", "runPolicyName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "start_ts": MoPropertyMeta("start_ts", "startTs", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "start_ts_m": MoPropertyMeta("start_ts_m", "startTsM", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["never"], ["0-4294967295"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "endTs": "end_ts", 
        "endTsM": "end_ts_m", 
        "errorDescr": "error_descr", 
        "operQualifier": "oper_qualifier", 
        "operState": "oper_state", 
        "overallProgress": "overall_progress", 
        "rn": "rn", 
        "runPolicyName": "run_policy_name", 
        "startTs": "start_ts", 
        "startTsM": "start_ts_m", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.end_ts = None
        self.end_ts_m = None
        self.error_descr = None
        self.oper_qualifier = None
        self.oper_state = None
        self.overall_progress = None
        self.run_policy_name = None
        self.start_ts = None
        self.start_ts_m = None
        self.status = None

        ManagedObject.__init__(self, "DiagSrvCtrl", parent_mo_or_dn, **kwargs)

