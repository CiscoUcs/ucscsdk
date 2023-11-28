"""This module contains the general information for AaaEpLogin ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AaaEpLoginConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    SESSION_LOCAL = "local"
    SESSION_REMOTE = "remote"


class AaaEpLogin(ManagedObject):
    """This is AaaEpLogin class."""

    consts = AaaEpLoginConsts()
    naming_props = set(['name', 'id'])

    mo_meta = MoMeta("AaaEpLogin", "aaaEpLogin", "ep-login-[name]-[id]", VersionMeta.Version101a, "InputOutput", 0x7f, [], ["read-only"], ['aaaUserEp'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, 1, 32, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "local_host": MoPropertyMeta("local_host", "localHost", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[a-zA-Z][a-zA-Z0-9_.@-]{0,31}[\\]{0,1}[a-zA-Z][a-zA-Z0-9_.@-]{0,31}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "remote_host": MoPropertyMeta("remote_host", "remoteHost", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "session": MoPropertyMeta("session", "session", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "remote"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "id": "id", 
        "intId": "int_id", 
        "localHost": "local_host", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "remoteHost": "remote_host", 
        "rn": "rn", 
        "session": "session", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, id, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.id = id
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.local_host = None
        self.policy_level = None
        self.policy_owner = None
        self.remote_host = None
        self.session = None
        self.status = None

        ManagedObject.__init__(self, "AaaEpLogin", parent_mo_or_dn, **kwargs)

