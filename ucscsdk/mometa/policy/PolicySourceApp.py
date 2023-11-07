"""This module contains the general information for PolicySourceApp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicySourceAppConsts():
    pass


class PolicySourceApp(ManagedObject):
    """This is PolicySourceApp class."""

    consts = PolicySourceAppConsts()
    naming_props = set(['sourceDme'])

    mo_meta = MoMeta("PolicySourceApp", "policySourceApp", "source-[source_dme]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["read-only"], ['policyControlEp'], ['policyContext'], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "source_dme": MoPropertyMeta("source_dme", "sourceDme", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sourceDme": "source_dme", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, source_dme, **kwargs):
        self._dirty_mask = 0
        self.source_dme = source_dme
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "PolicySourceApp", parent_mo_or_dn, **kwargs)

