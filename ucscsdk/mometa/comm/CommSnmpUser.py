"""This module contains the general information for CommSnmpUser ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class CommSnmpUserConsts():
    AUTH_MD5 = "md5"
    AUTH_SHA = "sha"
    ENC_ALGORITHM_AES = "AES"
    ENC_ALGORITHM_NONE = "None"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PRIV_PWD_SET_FALSE = "false"
    PRIV_PWD_SET_NO = "no"
    PRIV_PWD_SET_TRUE = "true"
    PRIV_PWD_SET_YES = "yes"
    PWD_SET_FALSE = "false"
    PWD_SET_NO = "no"
    PWD_SET_TRUE = "true"
    PWD_SET_YES = "yes"
    USE_AES_FALSE = "false"
    USE_AES_NO = "no"
    USE_AES_TRUE = "true"
    USE_AES_YES = "yes"


class CommSnmpUser(ManagedObject):
    """This is CommSnmpUser class."""

    consts = CommSnmpUserConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("CommSnmpUser", "commSnmpUser", "snmpv3-user-[name]", VersionMeta.Version101a, "InputOutput", 0xfff, [], ["aaa", "admin"], ['commSnmp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "auth": MoPropertyMeta("auth", "auth", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["md5", "sha"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "enc_algorithm": MoPropertyMeta("enc_algorithm", "encAlgorithm", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["AES", "None"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, None, None, r"""[a-zA-Z][a-zA-Z0-9_.@-]{0,31}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "priv_pwd_set": MoPropertyMeta("priv_pwd_set", "privPwdSet", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "privpwd": MoPropertyMeta("privpwd", "privpwd", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,128}""", [], []), 
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,128}""", [], []), 
        "pwd_set": MoPropertyMeta("pwd_set", "pwdSet", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "role": MoPropertyMeta("role", "role", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, 1, 32, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "use_aes": MoPropertyMeta("use_aes", "useAes", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "auth": "auth", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "encAlgorithm": "enc_algorithm", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "privPwdSet": "priv_pwd_set", 
        "privpwd": "privpwd", 
        "pwd": "pwd", 
        "pwdSet": "pwd_set", 
        "rn": "rn", 
        "role": "role", 
        "status": "status", 
        "useAes": "use_aes", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.auth = None
        self.child_action = None
        self.descr = None
        self.enc_algorithm = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.priv_pwd_set = None
        self.privpwd = None
        self.pwd = None
        self.pwd_set = None
        self.role = None
        self.status = None
        self.use_aes = None

        ManagedObject.__init__(self, "CommSnmpUser", parent_mo_or_dn, **kwargs)

