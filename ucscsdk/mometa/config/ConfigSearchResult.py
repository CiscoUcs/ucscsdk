"""This module contains the general information for ConfigSearchResult ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigSearchResultConsts():
    IS_RENAMEABLE_FALSE = "false"
    IS_RENAMEABLE_NO = "no"
    IS_RENAMEABLE_TRUE = "true"
    IS_RENAMEABLE_YES = "yes"
    PARENT_ORG_TYPE_DOMAIN_ORG = "DomainOrg"
    PARENT_ORG_TYPE_ORG_ORG = "OrgOrg"
    PARENT_ORG_TYPE_UNSPECIFIED = "Unspecified"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class ConfigSearchResult(ManagedObject):
    """This is ConfigSearchResult class."""

    consts = ConfigSearchResultConsts()
    naming_props = set(['convertedDn', 'domainId'])

    mo_meta = MoMeta("ConfigSearchResult", "configSearchResult", "policy-[converted_dn]-domain-[domain_id]", VersionMeta.Version112a, "InputOutput", 0x3f, [], ["read-only"], [], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "converted_dn": MoPropertyMeta("converted_dn", "convertedDn", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x2, 1, 510, None, [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "domain_group": MoPropertyMeta("domain_group", "domainGroup", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "domain_id": MoPropertyMeta("domain_id", "domainId", "uint", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "is_renameable": MoPropertyMeta("is_renameable", "isRenameable", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "object_type": MoPropertyMeta("object_type", "objectType", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "parent_org_type": MoPropertyMeta("parent_org_type", "parentOrgType", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["DomainOrg", "OrgOrg", "Unspecified"], []), 
        "policy_dn": MoPropertyMeta("policy_dn", "policyDn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "convertedDn": "converted_dn", 
        "descr": "descr", 
        "dn": "dn", 
        "domainGroup": "domain_group", 
        "domainId": "domain_id", 
        "domainName": "domain_name", 
        "isRenameable": "is_renameable", 
        "name": "name", 
        "objectType": "object_type", 
        "parentOrgType": "parent_org_type", 
        "policyDn": "policy_dn", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, converted_dn, domain_id, **kwargs):
        self._dirty_mask = 0
        self.converted_dn = converted_dn
        self.domain_id = domain_id
        self.child_action = None
        self.descr = None
        self.domain_group = None
        self.domain_name = None
        self.is_renameable = None
        self.name = None
        self.object_type = None
        self.parent_org_type = None
        self.policy_dn = None
        self.policy_owner = None
        self.status = None

        ManagedObject.__init__(self, "ConfigSearchResult", parent_mo_or_dn, **kwargs)

