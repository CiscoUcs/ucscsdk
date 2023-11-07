"""This module contains the general information for ComputeSystemAddrQual ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeSystemAddrQualConsts():
    pass


class ComputeSystemAddrQual(ManagedObject):
    """This is ComputeSystemAddrQual class."""

    consts = ComputeSystemAddrQualConsts()
    naming_props = set(['minAddr', 'maxAddr'])

    mo_meta = MoMeta("ComputeSystemAddrQual", "computeSystemAddrQual", "ip-from-[min_addr]-to-[max_addr]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin", "pn-policy", "read-only"], ['computeDomainQual', 'computeSystemQual'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "max_addr": MoPropertyMeta("max_addr", "maxAddr", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "min_addr": MoPropertyMeta("min_addr", "minAddr", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maxAddr": "max_addr", 
        "minAddr": "min_addr", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, min_addr, max_addr, **kwargs):
        self._dirty_mask = 0
        self.min_addr = min_addr
        self.max_addr = max_addr
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "ComputeSystemAddrQual", parent_mo_or_dn, **kwargs)

