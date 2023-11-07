"""This module contains the general information for AaaRadiusProvider ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AaaRadiusProviderConsts():
    KEY_SET_FALSE = "false"
    KEY_SET_NO = "no"
    KEY_SET_TRUE = "true"
    KEY_SET_YES = "yes"
    ORDER_LOWEST_AVAILABLE = "lowest-available"
    SERVICE_ACCOUNTING = "accounting"
    SERVICE_ALL = "all"
    SERVICE_AUTHORIZATION = "authorization"


class AaaRadiusProvider(ManagedObject):
    """This is AaaRadiusProvider class."""

    consts = AaaRadiusProviderConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("AaaRadiusProvider", "aaaRadiusProvider", "provider-[name]", VersionMeta.Version101a, "InputOutput", 0xfff, [], ["aaa", "admin"], ['aaaRadiusEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "auth_port": MoPropertyMeta("auth_port", "authPort", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-65535"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "enc_key": MoPropertyMeta("enc_key", "encKey", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, 0, 63, None, [], []), 
        "key": MoPropertyMeta("key", "key", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[!""#$%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,63}""", [], []), 
        "key_set": MoPropertyMeta("key_set", "keySet", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x40, None, None, r"""^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []), 
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["lowest-available"], ["0-16"]), 
        "retries": MoPropertyMeta("retries", "retries", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["0-5"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []), 
        "service": MoPropertyMeta("service", "service", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accounting", "all", "authorization"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], ["0-60"]), 
    }

    prop_map = {
        "authPort": "auth_port", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "encKey": "enc_key", 
        "key": "key", 
        "keySet": "key_set", 
        "name": "name", 
        "order": "order", 
        "retries": "retries", 
        "rn": "rn", 
        "service": "service", 
        "status": "status", 
        "timeout": "timeout", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.auth_port = None
        self.child_action = None
        self.descr = None
        self.enc_key = None
        self.key = None
        self.key_set = None
        self.order = None
        self.retries = None
        self.service = None
        self.status = None
        self.timeout = None

        ManagedObject.__init__(self, "AaaRadiusProvider", parent_mo_or_dn, **kwargs)

