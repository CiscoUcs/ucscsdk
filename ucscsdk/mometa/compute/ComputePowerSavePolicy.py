"""This module contains the general information for ComputePowerSavePolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputePowerSavePolicyConsts():
    EXTENDED_MODE_DISABLE = "Disable"
    EXTENDED_MODE_ENABLE = "Enable"
    INT_ID_NONE = "none"
    MODE_DISABLE = "Disable"
    MODE_ENABLE = "Enable"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    REDUNDANCY_GRID = "grid"
    REDUNDANCY_N_1 = "n+1"
    REDUNDANCY_N_2 = "n+2"
    REDUNDANCY_NON_REDUNDANT = "non-redundant"


class ComputePowerSavePolicy(ManagedObject):
    """This is ComputePowerSavePolicy class."""

    consts = ComputePowerSavePolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputePowerSavePolicy", "computePowerSavePolicy", "power-save-policy", VersionMeta.Version201u, "InputOutput", 0xff, [], ["admin", "domain-group-management", "pn-equipment", "pn-policy"], ['orgDomainGroup'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201u, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201u, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201u, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "extended_mode": MoPropertyMeta("extended_mode", "extendedMode", "string", VersionMeta.Version201u, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disable", "Enable"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version201u, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version201u, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disable", "Enable"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201u, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version201u, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version201u, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "redundancy": MoPropertyMeta("redundancy", "redundancy", "string", VersionMeta.Version201u, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["grid", "n+1", "n+2", "non-redundant"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201u, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201u, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "extendedMode": "extended_mode", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "redundancy": "redundancy", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.extended_mode = None
        self.int_id = None
        self.mode = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.redundancy = None
        self.status = None

        ManagedObject.__init__(self, "ComputePowerSavePolicy", parent_mo_or_dn, **kwargs)

