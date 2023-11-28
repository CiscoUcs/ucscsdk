"""This module contains the general information for FabricLacpPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricLacpPolicyConsts():
    FAST_TIMER_FAST = "fast"
    FAST_TIMER_NORMAL = "normal"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    SUSPEND_INDIVIDUAL_FALSE = "false"
    SUSPEND_INDIVIDUAL_TRUE = "true"


class FabricLacpPolicy(ManagedObject):
    """This is FabricLacpPolicy class."""

    consts = FabricLacpPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricLacpPolicy", "fabricLacpPolicy", "lacp-[name]", VersionMeta.Version121a, "InputOutput", 0xff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['orgDomainGroup', 'orgOrg'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "fast_timer": MoPropertyMeta("fast_timer", "fastTimer", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["fast", "normal"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version121a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspend_individual": MoPropertyMeta("suspend_individual", "suspendIndividual", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "true"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fastTimer": "fast_timer", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
        "suspendIndividual": "suspend_individual", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.fast_timer = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None
        self.suspend_individual = None

        ManagedObject.__init__(self, "FabricLacpPolicy", parent_mo_or_dn, **kwargs)

