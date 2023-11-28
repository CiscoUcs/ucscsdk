"""This module contains the general information for ComputeChassisConnPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeChassisConnPolicyConsts():
    ADMIN_STATE_GLOBAL = "global"
    ADMIN_STATE_NONE = "none"
    ADMIN_STATE_PORT_CHANNEL = "port-channel"
    BACKPLANE_SPEED_PREF_40_G = "40G"
    BACKPLANE_SPEED_PREF_4X10_G = "4x10G"
    BACKPLANE_SPEED_PREF_GLOBAL = "global"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"


class ComputeChassisConnPolicy(ManagedObject):
    """This is ComputeChassisConnPolicy class."""

    consts = ComputeChassisConnPolicyConsts()
    naming_props = set(['chassisId', 'switchId'])

    mo_meta = MoMeta("ComputeChassisConnPolicy", "computeChassisConnPolicy", "chassis-conn-policy-chassis-[chassis_id]-fabric-[switch_id]", VersionMeta.Version151a, "InputOutput", 0x3ff, [], ["admin", "domain-group-management", "pn-policy"], ['computeSystem', 'orgDomainGroup', 'orgOrg'], ['computeChassisConnPolicyOperation'], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["global", "none", "port-channel"], []), 
        "backplane_speed_pref": MoPropertyMeta("backplane_speed_pref", "backplaneSpeedPref", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["40G", "4x10G", "global"], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x200, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "backplaneSpeedPref": "backplane_speed_pref", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "qualifier": "qualifier", 
        "rn": "rn", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, chassis_id, switch_id, **kwargs):
        self._dirty_mask = 0
        self.chassis_id = chassis_id
        self.switch_id = switch_id
        self.admin_state = None
        self.backplane_speed_pref = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.qualifier = None
        self.status = None

        ManagedObject.__init__(self, "ComputeChassisConnPolicy", parent_mo_or_dn, **kwargs)

