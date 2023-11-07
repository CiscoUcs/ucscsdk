"""This module contains the general information for QueryImportContext ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class QueryImportContextConsts():
    ADMIN_STATE_IDLE = "idle"
    ADMIN_STATE_RESTART = "restart"
    IMPORT_ALL_FALSE = "false"
    IMPORT_ALL_NO = "no"
    IMPORT_ALL_TRUE = "true"
    IMPORT_ALL_YES = "yes"
    IS_RESOURCE_IMPORTED_FALSE = "false"
    IS_RESOURCE_IMPORTED_NO = "no"
    IS_RESOURCE_IMPORTED_TRUE = "true"
    IS_RESOURCE_IMPORTED_YES = "yes"
    OPERATION_ESTIMATE = "Estimate"
    OPERATION_IMPORT = "Import"
    QUERY_STATUS_FAILED = "failed"
    QUERY_STATUS_PENDING = "pending"
    QUERY_STATUS_SUCCESS = "success"
    QUERY_STATUS_TIMEOUT = "timeout"


class QueryImportContext(ManagedObject):
    """This is QueryImportContext class."""

    consts = QueryImportContextConsts()
    naming_props = set(['sessionId'])

    mo_meta = MoMeta("QueryImportContext", "queryImportContext", "import-[session_id]", VersionMeta.Version112a, "InputOutput", 0x3fff, [], ["admin"], ['queryEp'], ['faultInst', 'queryDependencyRef'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["idle", "restart"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "domain_id": MoPropertyMeta("domain_id", "domainId", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "impact_analyzer_dn": MoPropertyMeta("impact_analyzer_dn", "impactAnalyzerDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "import_all": MoPropertyMeta("import_all", "importAll", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []), 
        "imported_name": MoPropertyMeta("imported_name", "importedName", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []), 
        "is_resource_imported": MoPropertyMeta("is_resource_imported", "isResourceImported", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "operation": MoPropertyMeta("operation", "operation", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Estimate", "Import"], []), 
        "policy_dest_dn": MoPropertyMeta("policy_dest_dn", "policyDestDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, None, [], []), 
        "query_status": MoPropertyMeta("query_status", "queryStatus", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "pending", "success", "timeout"], []), 
        "resource_dest_dn": MoPropertyMeta("resource_dest_dn", "resourceDestDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x200, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []), 
        "session_id": MoPropertyMeta("session_id", "sessionId", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x800, 1, 510, None, [], []), 
        "start_time": MoPropertyMeta("start_time", "startTime", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "status_description": MoPropertyMeta("status_description", "statusDescription", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "target_dn": MoPropertyMeta("target_dn", "targetDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2000, 0, 256, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "domainId": "domain_id", 
        "impactAnalyzerDn": "impact_analyzer_dn", 
        "importAll": "import_all", 
        "importedName": "imported_name", 
        "isResourceImported": "is_resource_imported", 
        "operation": "operation", 
        "policyDestDn": "policy_dest_dn", 
        "queryStatus": "query_status", 
        "resourceDestDn": "resource_dest_dn", 
        "rn": "rn", 
        "sessionId": "session_id", 
        "startTime": "start_time", 
        "status": "status", 
        "statusDescription": "status_description", 
        "targetDn": "target_dn", 
    }

    def __init__(self, parent_mo_or_dn, session_id, **kwargs):
        self._dirty_mask = 0
        self.session_id = session_id
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.domain_id = None
        self.impact_analyzer_dn = None
        self.import_all = None
        self.imported_name = None
        self.is_resource_imported = None
        self.operation = None
        self.policy_dest_dn = None
        self.query_status = None
        self.resource_dest_dn = None
        self.start_time = None
        self.status = None
        self.status_description = None
        self.target_dn = None

        ManagedObject.__init__(self, "QueryImportContext", parent_mo_or_dn, **kwargs)

