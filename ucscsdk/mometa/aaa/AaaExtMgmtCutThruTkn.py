"""This module contains the general information for AaaExtMgmtCutThruTkn ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AaaExtMgmtCutThruTknConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    REMOTE_FALSE = "false"
    REMOTE_NO = "no"
    REMOTE_TRUE = "true"
    REMOTE_YES = "yes"
    TYPE_KVM = "kvm"


class AaaExtMgmtCutThruTkn(ManagedObject):
    """This is AaaExtMgmtCutThruTkn class."""

    consts = AaaExtMgmtCutThruTknConsts()
    naming_props = set(['token'])

    mo_meta = MoMeta("AaaExtMgmtCutThruTkn", "aaaExtMgmtCutThruTkn", "cutthrutkn-[token]", VersionMeta.Version101a, "InputOutput", 0x7f, [], ["aaa", "admin"], ['aaaUserEp'], [], ["Get"])

    prop_meta = {
        "auth_user": MoPropertyMeta("auth_user", "authUser", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "locales": MoPropertyMeta("locales", "locales", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "priv": MoPropertyMeta("priv", "priv", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((ext-lan-policy|pn-maintenance|ls-security-policy|stats-management|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|kvm|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|tag|operations|ext-lan-config|pn-security|ls-network-policy|domain-group-management|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault),){0,41}(ext-lan-policy|pn-maintenance|ls-security-policy|stats-management|pod-security|pn-equipment|ls-config-policy|ls-compute|ext-san-policy|ls-security|aaa|power-mgmt|read-only|ext-lan-security|ls-config|ls-server-policy|kvm|pod-qos|pn-policy|ls-storage-policy|org-management|admin|ext-san-security|pod-config|ls-server|ext-lan-qos|ls-storage|ls-qos-policy|tag|operations|ext-lan-config|pn-security|ls-network-policy|domain-group-management|pod-policy|ext-san-qos|ls-qos|ls-server-oper|ext-san-config|ls-network|ls-ext-access|fault){0,1}""", [], []), 
        "remote": MoPropertyMeta("remote", "remote", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "token": MoPropertyMeta("token", "token", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x40, 1, 510, None, [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["kvm"], []), 
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "authUser": "auth_user", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "locales": "locales", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "priv": "priv", 
        "remote": "remote", 
        "rn": "rn", 
        "status": "status", 
        "token": "token", 
        "type": "type", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, token, **kwargs):
        self._dirty_mask = 0
        self.token = token
        self.auth_user = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.locales = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.priv = None
        self.remote = None
        self.status = None
        self.type = None
        self.user = None

        ManagedObject.__init__(self, "AaaExtMgmtCutThruTkn", parent_mo_or_dn, **kwargs)

