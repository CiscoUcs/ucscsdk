"""This module contains the general information for TagInstanceItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class TagInstanceItemConsts():
    SRC_DME_CENTRAL_MGR = "central-mgr"
    SRC_DME_IDENTIFIER_MGR = "identifier-mgr"
    SRC_DME_MGMT_CONTROLLER = "mgmt-controller"
    SRC_DME_OPERATION_MGR = "operation-mgr"
    SRC_DME_POLICY_MGR = "policy-mgr"
    SRC_DME_RESOURCE_MGR = "resource-mgr"
    SRC_DME_SERVER_MGR = "server-mgr"
    SRC_DME_SERVICE_REG = "service-reg"
    SRC_DME_STATS_MGR = "stats-mgr"
    SRC_DME_UNKNOWN = "unknown"


class TagInstanceItem(ManagedObject):
    """This is TagInstanceItem class."""

    consts = TagInstanceItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("TagInstanceItem", "tagInstanceItem", "tag-instance-item", VersionMeta.Version151a, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_dn": MoPropertyMeta("def_dn", "defDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "def_name": MoPropertyMeta("def_name", "defName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\.:;=\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "object_name": MoPropertyMeta("object_name", "objectName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\.:;=\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "object_type": MoPropertyMeta("object_type", "objectType", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "org_dn": MoPropertyMeta("org_dn", "orgDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "src_dme": MoPropertyMeta("src_dme", "srcDme", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["central-mgr", "identifier-mgr", "mgmt-controller", "operation-mgr", "policy-mgr", "resource-mgr", "server-mgr", "service-reg", "stats-mgr", "unknown"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tagged_object_dn": MoPropertyMeta("tagged_object_dn", "taggedObjectDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 64, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?]+""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "defDn": "def_dn", 
        "defName": "def_name", 
        "dn": "dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainName": "domain_name", 
        "objectName": "object_name", 
        "objectType": "object_type", 
        "orgDn": "org_dn", 
        "rn": "rn", 
        "srcDme": "src_dme", 
        "status": "status", 
        "taggedObjectDn": "tagged_object_dn", 
        "value": "value", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.def_dn = None
        self.def_name = None
        self.domain_group_dn = None
        self.domain_name = None
        self.object_name = None
        self.object_type = None
        self.org_dn = None
        self.src_dme = None
        self.status = None
        self.tagged_object_dn = None
        self.value = None
        self.vendor = None

        ManagedObject.__init__(self, "TagInstanceItem", parent_mo_or_dn, **kwargs)

