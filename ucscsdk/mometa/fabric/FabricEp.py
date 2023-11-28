"""This module contains the general information for FabricEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricEpConsts():
    pass


class FabricEp(ManagedObject):
    """This is FabricEp class."""

    consts = FabricEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricEp", "fabricEp", "fabric", VersionMeta.Version111a, "InputOutput", 0xf, [], ["admin"], ['computeSystem', 'fabricSystem', 'orgDomainGroup'], ['fabricCabling', 'fabricDceSrv', 'fabricEthEstcCloud', 'fabricFcEstcCloud', 'fabricLanAccessMgr', 'fabricLanCloud', 'fabricLanMonCloud', 'fabricSanCloud', 'fabricSanMonCloud'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "FabricEp", parent_mo_or_dn, **kwargs)

