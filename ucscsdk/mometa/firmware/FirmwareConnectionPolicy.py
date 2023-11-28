"""This module contains the general information for FirmwareConnectionPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareConnectionPolicyConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PROXY_PWD_SET_FALSE = "false"
    PROXY_PWD_SET_NO = "no"
    PROXY_PWD_SET_TRUE = "true"
    PROXY_PWD_SET_YES = "yes"
    PWD_SET_FALSE = "false"
    PWD_SET_NO = "no"
    PWD_SET_TRUE = "true"
    PWD_SET_YES = "yes"
    TYPE_CISCO = "Cisco"
    TYPE_LOCAL = "local"
    USE_FOR_FW_DLD_FALSE = "false"
    USE_FOR_FW_DLD_NO = "no"
    USE_FOR_FW_DLD_TRUE = "true"
    USE_FOR_FW_DLD_YES = "yes"
    USE_FOR_HCL_DLD_FALSE = "false"
    USE_FOR_HCL_DLD_NO = "no"
    USE_FOR_HCL_DLD_TRUE = "true"
    USE_FOR_HCL_DLD_YES = "yes"


class FirmwareConnectionPolicy(ManagedObject):
    """This is FirmwareConnectionPolicy class."""

    consts = FirmwareConnectionPolicyConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("FirmwareConnectionPolicy", "firmwareConnectionPolicy", "conn-policy-[type]", VersionMeta.Version151a, "InputOutput", 0xffff, [], ["admin"], ['orgDomainGroup'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "enc_password": MoPropertyMeta("enc_password", "encPassword", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "enc_proxy_pwd": MoPropertyMeta("enc_proxy_pwd", "encProxyPwd", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "http_proxy": MoPropertyMeta("http_proxy", "httpProxy", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""^([a-zA-Z0-9][a-zA-Z0-9_.@-]{0,63}(:[0-9]|:[1-9][0-9]|:[1-9][0-9][0-9]|:[1-9][0-9][0-9][0-9]|:[1-5][0-9][0-9][0-9][0-9]|:6[0-4][0-9][0-9][0-9]|:65[0-4][0-9][0-9]|:655[0-2][0-9]|:6553[0-5])?)?$""", [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, 0, 64, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "proxy_pwd": MoPropertyMeta("proxy_pwd", "proxyPwd", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x100, 0, 64, None, [], []), 
        "proxy_pwd_set": MoPropertyMeta("proxy_pwd_set", "proxyPwdSet", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "proxy_user": MoPropertyMeta("proxy_user", "proxyUser", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""^([a-zA-Z0-9_.@-]{0,64})?$""", [], []), 
        "pwd_set": MoPropertyMeta("pwd_set", "pwdSet", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x400, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x1000, None, None, None, ["Cisco", "local"], []), 
        "use_for_fw_dld": MoPropertyMeta("use_for_fw_dld", "useForFwDld", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["false", "no", "true", "yes"], []), 
        "use_for_hcl_dld": MoPropertyMeta("use_for_hcl_dld", "useForHclDld", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["false", "no", "true", "yes"], []), 
        "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, r"""^([a-zA-Z0-9_.@-]{0,64})?$""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "encPassword": "enc_password", 
        "encProxyPwd": "enc_proxy_pwd", 
        "httpProxy": "http_proxy", 
        "intId": "int_id", 
        "name": "name", 
        "password": "password", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "proxyPwd": "proxy_pwd", 
        "proxyPwdSet": "proxy_pwd_set", 
        "proxyUser": "proxy_user", 
        "pwdSet": "pwd_set", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "useForFwDld": "use_for_fw_dld", 
        "useForHclDld": "use_for_hcl_dld", 
        "username": "username", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.descr = None
        self.enc_password = None
        self.enc_proxy_pwd = None
        self.http_proxy = None
        self.int_id = None
        self.name = None
        self.password = None
        self.policy_level = None
        self.policy_owner = None
        self.proxy_pwd = None
        self.proxy_pwd_set = None
        self.proxy_user = None
        self.pwd_set = None
        self.status = None
        self.use_for_fw_dld = None
        self.use_for_hcl_dld = None
        self.username = None

        ManagedObject.__init__(self, "FirmwareConnectionPolicy", parent_mo_or_dn, **kwargs)

