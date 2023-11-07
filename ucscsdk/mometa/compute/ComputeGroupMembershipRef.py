"""This module contains the general information for ComputeGroupMembershipRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeGroupMembershipRefConsts():
    pass


class ComputeGroupMembershipRef(ManagedObject):
    """This is ComputeGroupMembershipRef class."""

    consts = ComputeGroupMembershipRefConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ComputeGroupMembershipRef", "computeGroupMembershipRef", "membershipref-[id]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["read-only"], ['orgDomainGroup'], [], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "oper_sys_dn": MoPropertyMeta("oper_sys_dn", "operSysDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "operSysDn": "oper_sys_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.oper_sys_dn = None
        self.status = None

        ManagedObject.__init__(self, "ComputeGroupMembershipRef", parent_mo_or_dn, **kwargs)

