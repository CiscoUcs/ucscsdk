"""This module contains the general information for PowerPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PowerPolicyConsts():
    FAN_SPEED_ANY = "any"
    FAN_SPEED_BALANCED = "balanced"
    FAN_SPEED_ERR = "err"
    FAN_SPEED_HIGH_POWER = "high-power"
    FAN_SPEED_LOW_POWER = "low-power"
    FAN_SPEED_MAX_POWER = "max-power"
    FAN_SPEED_NA = "na"
    FAN_SPEED_NO_UPDATE = "no-update"
    FAN_SPEED_NOT_SUPPORTED = "not-supported"
    FAN_SPEED_PERFORMANCE = "performance"
    INT_ID_NONE = "none"
    OPER_PRIO_NO_CAP = "no-cap"
    OPER_PRIO_UTILITY = "utility"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PRIO_NO_CAP = "no-cap"
    PRIO_UTILITY = "utility"


class PowerPolicy(ManagedObject):
    """This is PowerPolicy class."""

    consts = PowerPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PowerPolicy", "powerPolicy", "power-policy-[name]", VersionMeta.Version111a, "InputOutput", 0xff, [], ["read-only"], ['orgOrg', 'policySystemEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "fan_speed": MoPropertyMeta("fan_speed", "fanSpeed", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["any", "balanced", "err", "high-power", "low-power", "max-power", "na", "no-update", "not-supported", "performance"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_prio": MoPropertyMeta("oper_prio", "operPrio", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no-cap", "utility"], ["1-10"]), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "prio": MoPropertyMeta("prio", "prio", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["no-cap", "utility"], ["1-10"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fanSpeed": "fan_speed", 
        "intId": "int_id", 
        "name": "name", 
        "operPrio": "oper_prio", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "prio": "prio", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.fan_speed = None
        self.int_id = None
        self.oper_prio = None
        self.policy_level = None
        self.policy_owner = None
        self.prio = None
        self.status = None

        ManagedObject.__init__(self, "PowerPolicy", parent_mo_or_dn, **kwargs)

