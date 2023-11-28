"""This module contains the general information for AaaPwdProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AaaPwdProfileConsts():
    CHANGE_DURING_INTERVAL_DISABLE = "disable"
    CHANGE_DURING_INTERVAL_ENABLE = "enable"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PWD_STRENGTH_CHECK_FALSE = "false"
    PWD_STRENGTH_CHECK_NO = "no"
    PWD_STRENGTH_CHECK_TRUE = "true"
    PWD_STRENGTH_CHECK_YES = "yes"


class AaaPwdProfile(ManagedObject):
    """This is AaaPwdProfile class."""

    consts = AaaPwdProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AaaPwdProfile", "aaaPwdProfile", "pwd-profile", VersionMeta.Version101a, "InputOutput", 0x1fff, [], ["aaa", "admin"], ['aaaUserEp', 'orgDomainGroup', 'policyDeviceProfile'], [], ["Get", "Set"])

    prop_meta = {
        "change_count": MoPropertyMeta("change_count", "changeCount", "byte", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-10"]), 
        "change_during_interval": MoPropertyMeta("change_during_interval", "changeDuringInterval", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["disable", "enable"], []), 
        "change_interval": MoPropertyMeta("change_interval", "changeInterval", "ushort", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-745"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "expiration_warn_time": MoPropertyMeta("expiration_warn_time", "expirationWarnTime", "byte", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-30"]), 
        "history_count": MoPropertyMeta("history_count", "historyCount", "byte", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["0-15"]), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x100, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "no_change_interval": MoPropertyMeta("no_change_interval", "noChangeInterval", "ushort", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["1-745"]), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "pwd_strength_check": MoPropertyMeta("pwd_strength_check", "pwdStrengthCheck", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "changeCount": "change_count", 
        "changeDuringInterval": "change_during_interval", 
        "changeInterval": "change_interval", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "expirationWarnTime": "expiration_warn_time", 
        "historyCount": "history_count", 
        "intId": "int_id", 
        "name": "name", 
        "noChangeInterval": "no_change_interval", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "pwdStrengthCheck": "pwd_strength_check", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.change_count = None
        self.change_during_interval = None
        self.change_interval = None
        self.child_action = None
        self.descr = None
        self.expiration_warn_time = None
        self.history_count = None
        self.int_id = None
        self.name = None
        self.no_change_interval = None
        self.policy_level = None
        self.policy_owner = None
        self.pwd_strength_check = None
        self.status = None

        ManagedObject.__init__(self, "AaaPwdProfile", parent_mo_or_dn, **kwargs)

