"""This module contains the general information for MgmtNamedKmipCertPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtNamedKmipCertPolicyConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class MgmtNamedKmipCertPolicy(ManagedObject):
    """This is MgmtNamedKmipCertPolicy class."""

    consts = MgmtNamedKmipCertPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("MgmtNamedKmipCertPolicy", "mgmtNamedKmipCertPolicy", "kmip-cert-[name]", VersionMeta.Version201b, "InputOutput", 0x1fff, [], ["aaa", "admin", "domain-group-management", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-oper", "ls-server-policy", "read-only"], ['orgDomainGroup'], [], ["add", "get", "remove", "set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "country_code": MoPropertyMeta("country_code", "countryCode", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""^([A-Z]{2})?$""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "email_addr": MoPropertyMeta("email_addr", "emailAddr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "locality": MoPropertyMeta("locality", "locality", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "org_name": MoPropertyMeta("org_name", "orgName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], []), 
        "org_unit_name": MoPropertyMeta("org_unit_name", "orgUnitName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[\t\n\x0b\x0c\r \(\)\+,\-\./:@\^_a-zA-Z0-9]{0,64}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "validity": MoPropertyMeta("validity", "validity", "ushort", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], ["365-3650"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "countryCode": "country_code", 
        "descr": "descr", 
        "dn": "dn", 
        "emailAddr": "email_addr", 
        "intId": "int_id", 
        "locality": "locality", 
        "name": "name", 
        "orgName": "org_name", 
        "orgUnitName": "org_unit_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "state": "state", 
        "status": "status", 
        "validity": "validity", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.country_code = None
        self.descr = None
        self.email_addr = None
        self.int_id = None
        self.locality = None
        self.org_name = None
        self.org_unit_name = None
        self.policy_level = None
        self.policy_owner = None
        self.state = None
        self.status = None
        self.validity = None

        ManagedObject.__init__(self, "MgmtNamedKmipCertPolicy", parent_mo_or_dn, **kwargs)

