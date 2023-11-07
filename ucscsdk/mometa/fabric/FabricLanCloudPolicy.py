"""This module contains the general information for FabricLanCloudPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricLanCloudPolicyConsts():
    INT_ID_NONE = "none"
    MAC_AGING_MODE_DEFAULT = "mode-default"
    MAC_AGING_NEVER = "never"
    MODE_END_HOST = "end-host"
    MODE_SWITCH = "switch"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    VLAN_COMPRESSION_DISABLED = "disabled"
    VLAN_COMPRESSION_ENABLED = "enabled"


class FabricLanCloudPolicy(ManagedObject):
    """This is FabricLanCloudPolicy class."""

    consts = FabricLanCloudPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricLanCloudPolicy", "fabricLanCloudPolicy", "lan-policy", VersionMeta.Version141a, "InputOutput", 0x1ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['orgDomainGroup', 'orgOrg'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mac_aging": MoPropertyMeta("mac_aging", "macAging", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["mode-default", "never"], ["0-1000001"]), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["end-host", "switch"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vlan_compression": MoPropertyMeta("vlan_compression", "vlanCompression", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["disabled", "enabled"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "macAging": "mac_aging", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
        "vlanCompression": "vlan_compression", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.mac_aging = None
        self.mode = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None
        self.vlan_compression = None

        ManagedObject.__init__(self, "FabricLanCloudPolicy", parent_mo_or_dn, **kwargs)

