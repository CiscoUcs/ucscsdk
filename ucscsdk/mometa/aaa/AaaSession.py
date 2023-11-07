"""This module contains the general information for AaaSession ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AaaSessionConsts():
    INT_DEL_FALSE = "false"
    INT_DEL_NO = "no"
    INT_DEL_TRUE = "true"
    INT_DEL_YES = "yes"
    UI_EP = "ep"
    UI_NONE = "none"
    UI_SHELL = "shell"
    UI_WEB = "web"


class AaaSession(ManagedObject):
    """This is AaaSession class."""

    consts = AaaSessionConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("AaaSession", "aaaSession", "term-[id]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["aaa", "admin", "domain-group-management"], ['aaaRemoteUser', 'aaaUser'], [], ["Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "host": MoPropertyMeta("host", "host", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, 1, 32, None, [], []), 
        "int_del": MoPropertyMeta("int_del", "intDel", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "login_time": MoPropertyMeta("login_time", "loginTime", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "pid": MoPropertyMeta("pid", "pid", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "term": MoPropertyMeta("term", "term", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 16, None, [], []), 
        "ui": MoPropertyMeta("ui", "ui", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ep", "none", "shell", "web"], []), 
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "host": "host", 
        "id": "id", 
        "intDel": "int_del", 
        "loginTime": "login_time", 
        "pid": "pid", 
        "rn": "rn", 
        "status": "status", 
        "term": "term", 
        "ui": "ui", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.host = None
        self.int_del = None
        self.login_time = None
        self.pid = None
        self.status = None
        self.term = None
        self.ui = None
        self.user = None

        ManagedObject.__init__(self, "AaaSession", parent_mo_or_dn, **kwargs)

