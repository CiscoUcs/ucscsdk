"""This module contains the general information for IdentpoolConsumed ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IdentpoolConsumedConsts():
    CONS_TYPE_CHASSIS = "chassis"
    CONS_TYPE_SERVER = "server"
    CONS_TYPE_VHBA = "vhba"
    CONS_TYPE_VM = "vm"
    CONS_TYPE_VMNIC = "vmnic"
    CONS_TYPE_VNIC = "vnic"
    DEFINED_IN_IDM_NO = "no"
    DEFINED_IN_IDM_YES = "yes"
    OWNER_END_POINT = "end-point"
    OWNER_POOL = "pool"


class IdentpoolConsumed(ManagedObject):
    """This is IdentpoolConsumed class."""

    consts = IdentpoolConsumedConsts()
    naming_props = set(['sysId'])

    mo_meta = MoMeta("IdentpoolConsumed", "identpoolConsumed", "cons-[sys_id]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["read-only"], ['fcpoolAddr', 'ippoolAddr', 'ippoolIpV6Addr', 'iqnpoolAddr', 'macpoolAddr', 'uuidpoolAddr'], ['identpoolDomain'], [None])

    prop_meta = {
        "assigned_from_pool": MoPropertyMeta("assigned_from_pool", "assignedFromPool", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "assigned_on_behalf": MoPropertyMeta("assigned_on_behalf", "assignedOnBehalf", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cons_type": MoPropertyMeta("cons_type", "consType", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis", "server", "vhba", "vm", "vmnic", "vnic"], []), 
        "defined_in_idm": MoPropertyMeta("defined_in_idm", "definedInIdm", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_id": MoPropertyMeta("domain_id", "domainId", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["end-point", "pool"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sys_id": MoPropertyMeta("sys_id", "sysId", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
    }

    prop_map = {
        "assignedFromPool": "assigned_from_pool", 
        "assignedOnBehalf": "assigned_on_behalf", 
        "assignedToDn": "assigned_to_dn", 
        "childAction": "child_action", 
        "consType": "cons_type", 
        "definedInIdm": "defined_in_idm", 
        "dn": "dn", 
        "domainId": "domain_id", 
        "id": "id", 
        "owner": "owner", 
        "rn": "rn", 
        "status": "status", 
        "sysId": "sys_id", 
    }

    def __init__(self, parent_mo_or_dn, sys_id, **kwargs):
        self._dirty_mask = 0
        self.sys_id = sys_id
        self.assigned_from_pool = None
        self.assigned_on_behalf = None
        self.assigned_to_dn = None
        self.child_action = None
        self.cons_type = None
        self.defined_in_idm = None
        self.domain_id = None
        self.id = None
        self.owner = None
        self.status = None

        ManagedObject.__init__(self, "IdentpoolConsumed", parent_mo_or_dn, **kwargs)

