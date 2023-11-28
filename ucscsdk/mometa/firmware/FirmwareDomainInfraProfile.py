"""This module contains the general information for FirmwareDomainInfraProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareDomainInfraProfileConsts():
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGER_IMMEDIATE = "trigger-immediate"
    ADMIN_STATE_TRIGGERED = "triggered"
    ADMIN_STATE_UNTRIGGERED = "untriggered"
    ADMIN_STATE_USER_ACK = "user-ack"
    INFRA_PROFILE_STATUS_FAILED_TO_TRIGGER = "failed-to-trigger"
    INFRA_PROFILE_STATUS_PENDING = "pending"
    INFRA_PROFILE_STATUS_TRIGGERED = "triggered"
    INFRA_PROFILE_STATUS_TRIGGERED_ACTIVE = "triggered-active"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class FirmwareDomainInfraProfile(ManagedObject):
    """This is FirmwareDomainInfraProfile class."""

    consts = FirmwareDomainInfraProfileConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FirmwareDomainInfraProfile", "firmwareDomainInfraProfile", "domain-infra-profile-[name]", VersionMeta.Version151a, "InputOutput", 0x7f, [], ["admin", "operations"], ['orgOrg'], ['firmwareCatalogPack', 'firmwareCatalogPackConfig', 'firmwareDomainInfo', 'firmwareProductFamily', 'trigMeta', 'trigSched'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["trigger", "trigger-immediate", "triggered", "untriggered", "user-ack"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "infra_profile_status": MoPropertyMeta("infra_profile_status", "infraProfileStatus", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed-to-trigger", "pending", "triggered", "triggered-active"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sched_date": MoPropertyMeta("sched_date", "schedDate", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tag_name": MoPropertyMeta("tag_name", "tagName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, 0, 64, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?]+""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "infraProfileStatus": "infra_profile_status", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "schedDate": "sched_date", 
        "status": "status", 
        "tagName": "tag_name", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.infra_profile_status = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.sched_date = None
        self.status = None
        self.tag_name = None

        ManagedObject.__init__(self, "FirmwareDomainInfraProfile", parent_mo_or_dn, **kwargs)

