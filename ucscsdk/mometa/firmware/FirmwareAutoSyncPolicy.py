"""This module contains the general information for FirmwareAutoSyncPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareAutoSyncPolicyConsts():
    CONFIG_ISSUE_DEFAULT_PACKAGE_MISSING = "Default Package Missing"
    CONFIG_ISSUE_NO_ISSUES = "No Issues"
    CONFIG_ISSUE_VERSIONS_EMPTY_IN_DEFAULT_PACKAGE = "Versions Empty in Default Package"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    SYNC_STATE_NO_ACTIONS = "No Actions"
    SYNC_STATE_USER_ACKNOWLEDGE = "User Acknowledge"


class FirmwareAutoSyncPolicy(ManagedObject):
    """This is FirmwareAutoSyncPolicy class."""

    consts = FirmwareAutoSyncPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareAutoSyncPolicy", "firmwareAutoSyncPolicy", "fw-auto-sync", VersionMeta.Version141a, "InputOutput", 0xff, [], ["admin"], ['orgDomainGroup'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_issue": MoPropertyMeta("config_issue", "configIssue", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Default Package Missing", "No Issues", "Versions Empty in Default Package"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sync_state": MoPropertyMeta("sync_state", "syncState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["No Actions", "User Acknowledge"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configIssue": "config_issue", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
        "syncState": "sync_state", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_issue = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None
        self.sync_state = None

        ManagedObject.__init__(self, "FirmwareAutoSyncPolicy", parent_mo_or_dn, **kwargs)

