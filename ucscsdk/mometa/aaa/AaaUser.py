"""This module contains the general information for AaaUser ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AaaUserConsts():
    ACCOUNT_STATUS_ACTIVE = "active"
    ACCOUNT_STATUS_INACTIVE = "inactive"
    CLEAR_PWD_HISTORY_NO = "no"
    CLEAR_PWD_HISTORY_YES = "yes"
    EXPIRATION_NEVER = "never"
    EXPIRES_FALSE = "false"
    EXPIRES_NO = "no"
    EXPIRES_TRUE = "true"
    EXPIRES_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PWD_LIFE_TIME_NO_PASSWORD_EXPIRE = "no-password-expire"
    PWD_SET_FALSE = "false"
    PWD_SET_NO = "no"
    PWD_SET_TRUE = "true"
    PWD_SET_YES = "yes"


class AaaUser(ManagedObject):
    """This is AaaUser class."""

    consts = AaaUserConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("AaaUser", "aaaUser", "user-[name]", VersionMeta.Version101a, "InputOutput", 0x1ffff, [], ["aaa", "admin"], ['orgDomainGroup', 'policyDeviceProfile'], ['aaaSession', 'aaaSshAuth', 'aaaUserData', 'aaaUserLocale', 'aaaUserRole'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "account_status": MoPropertyMeta("account_status", "accountStatus", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["active", "inactive"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "clear_pwd_history": MoPropertyMeta("clear_pwd_history", "clearPwdHistory", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["no", "yes"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []), 
        "enc_pwd": MoPropertyMeta("enc_pwd", "encPwd", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, None, [], []), 
        "expiration": MoPropertyMeta("expiration", "expiration", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "expires": MoPropertyMeta("expires", "expires", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["false", "no", "true", "yes"], []), 
        "first_name": MoPropertyMeta("first_name", "firstName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, 0, 32, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "last_name": MoPropertyMeta("last_name", "lastName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x400, 0, 32, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x800, None, None, r"""[a-zA-Z][a-zA-Z0-9_.-]{0,31}""", [], []), 
        "phone": MoPropertyMeta("phone", "phone", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((ext-lan-policy|pn-maintenance|ls-security-policy|stats-management|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|kvm|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|tag|operations|ext-lan-config|pn-security|ls-network-policy|domain-group-management|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault),){0,41}(ext-lan-policy|pn-maintenance|ls-security-policy|stats-management|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|kvm|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|tag|operations|ext-lan-config|pn-security|ls-network-policy|domain-group-management|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault){0,1}""", [], []), 
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,128}""", [], []), 
        "pwd_life_time": MoPropertyMeta("pwd_life_time", "pwdLifeTime", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["no-password-expire"], ["0-3650"]), 
        "pwd_set": MoPropertyMeta("pwd_set", "pwdSet", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8000, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "accountStatus": "account_status", 
        "childAction": "child_action", 
        "clearPwdHistory": "clear_pwd_history", 
        "descr": "descr", 
        "dn": "dn", 
        "email": "email", 
        "encPwd": "enc_pwd", 
        "expiration": "expiration", 
        "expires": "expires", 
        "firstName": "first_name", 
        "intId": "int_id", 
        "lastName": "last_name", 
        "name": "name", 
        "phone": "phone", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "priv": "priv", 
        "pwd": "pwd", 
        "pwdLifeTime": "pwd_life_time", 
        "pwdSet": "pwd_set", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.account_status = None
        self.child_action = None
        self.clear_pwd_history = None
        self.descr = None
        self.email = None
        self.enc_pwd = None
        self.expiration = None
        self.expires = None
        self.first_name = None
        self.int_id = None
        self.last_name = None
        self.phone = None
        self.policy_level = None
        self.policy_owner = None
        self.priv = None
        self.pwd = None
        self.pwd_life_time = None
        self.pwd_set = None
        self.status = None

        ManagedObject.__init__(self, "AaaUser", parent_mo_or_dn, **kwargs)

