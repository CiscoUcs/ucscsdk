"""This module contains the general information for AaaUserData ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AaaUserDataConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class AaaUserData(ManagedObject):
    """This is AaaUserData class."""

    consts = AaaUserDataConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaUserData", "aaaUserData", "user-data", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["aaa", "admin"], ['aaaUser'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "pwd_change_count": MoPropertyMeta("pwd_change_count", "pwdChangeCount", "byte", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-10"]), 
        "pwd_change_interval_begin": MoPropertyMeta("pwd_change_interval_begin", "pwdChangeIntervalBegin", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "pwd_changed_date": MoPropertyMeta("pwd_changed_date", "pwdChangedDate", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "pwd_history": MoPropertyMeta("pwd_history", "pwdHistory", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 1024, None, [], []), 
        "pwd_history2": MoPropertyMeta("pwd_history2", "pwdHistory2", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 1024, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "pwdChangeCount": "pwd_change_count", 
        "pwdChangeIntervalBegin": "pwd_change_interval_begin", 
        "pwdChangedDate": "pwd_changed_date", 
        "pwdHistory": "pwd_history", 
        "pwdHistory2": "pwd_history2", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.pwd_change_count = None
        self.pwd_change_interval_begin = None
        self.pwd_changed_date = None
        self.pwd_history = None
        self.pwd_history2 = None
        self.status = None

        ManagedObject.__init__(self, "AaaUserData", parent_mo_or_dn, **kwargs)

