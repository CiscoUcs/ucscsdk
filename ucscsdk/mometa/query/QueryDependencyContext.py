"""This module contains the general information for QueryDependencyContext ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class QueryDependencyContextConsts():
    ADMIN_STATE_IDLE = "idle"
    ADMIN_STATE_RESTART = "restart"
    ORG_CATEGORY_DOMAIN_ORG = "DomainOrg"
    ORG_CATEGORY_ORG_ORG = "OrgOrg"
    ORG_CATEGORY_UNSPECIFIED = "Unspecified"
    QUERY_STATUS_FAILED = "failed"
    QUERY_STATUS_PENDING = "pending"
    QUERY_STATUS_SUCCESS = "success"
    QUERY_STATUS_TIMEOUT = "timeout"


class QueryDependencyContext(ManagedObject):
    """This is QueryDependencyContext class."""

    consts = QueryDependencyContextConsts()
    naming_props = set(['sessionId'])

    mo_meta = MoMeta("QueryDependencyContext", "queryDependencyContext", "dependency-[session_id]", VersionMeta.Version112a, "InputOutput", 0x1ff, [], ["admin"], ['queryEp'], ['faultInst', 'queryresultDomainGroupEp', 'queryresultOrgEp'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "numberof_policy": MoPropertyMeta("numberof_policy", "NumberofPolicy", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "numberof_pool": MoPropertyMeta("numberof_pool", "NumberofPool", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "numberof_vlan": MoPropertyMeta("numberof_vlan", "NumberofVlan", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "numberof_vsan": MoPropertyMeta("numberof_vsan", "NumberofVsan", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["idle", "restart"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "domain_id": MoPropertyMeta("domain_id", "domainId", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "number_of_dependency": MoPropertyMeta("number_of_dependency", "numberOfDependency", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "number_of_non_importable": MoPropertyMeta("number_of_non_importable", "numberOfNonImportable", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "org_category": MoPropertyMeta("org_category", "orgCategory", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["DomainOrg", "OrgOrg", "Unspecified"], []), 
        "query_status": MoPropertyMeta("query_status", "queryStatus", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "pending", "success", "timeout"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "session_id": MoPropertyMeta("session_id", "sessionId", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x40, 1, 510, None, [], []), 
        "start_time": MoPropertyMeta("start_time", "startTime", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "status_description": MoPropertyMeta("status_description", "statusDescription", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "target_dn": MoPropertyMeta("target_dn", "targetDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, None, [], []), 
    }

    prop_map = {
        "NumberofPolicy": "numberof_policy", 
        "NumberofPool": "numberof_pool", 
        "NumberofVlan": "numberof_vlan", 
        "NumberofVsan": "numberof_vsan", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "domainId": "domain_id", 
        "numberOfDependency": "number_of_dependency", 
        "numberOfNonImportable": "number_of_non_importable", 
        "orgCategory": "org_category", 
        "queryStatus": "query_status", 
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
        self.numberof_policy = None
        self.numberof_pool = None
        self.numberof_vlan = None
        self.numberof_vsan = None
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.domain_id = None
        self.number_of_dependency = None
        self.number_of_non_importable = None
        self.org_category = None
        self.query_status = None
        self.start_time = None
        self.status = None
        self.status_description = None
        self.target_dn = None

        ManagedObject.__init__(self, "QueryDependencyContext", parent_mo_or_dn, **kwargs)

