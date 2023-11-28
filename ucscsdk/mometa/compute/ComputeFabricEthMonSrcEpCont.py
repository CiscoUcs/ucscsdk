"""This module contains the general information for ComputeFabricEthMonSrcEpCont ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeFabricEthMonSrcEpContConsts():
    pass


class ComputeFabricEthMonSrcEpCont(ManagedObject):
    """This is ComputeFabricEthMonSrcEpCont class."""

    consts = ComputeFabricEthMonSrcEpContConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeFabricEthMonSrcEpCont", "computeFabricEthMonSrcEpCont", "eth-mon", VersionMeta.Version201b, "InputOutput", 0xf, [], ["admin", "operations"], ['computeSystem'], ['computeFabricEthMonSrcEp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.id = None
        self.status = None

        ManagedObject.__init__(self, "ComputeFabricEthMonSrcEpCont", parent_mo_or_dn, **kwargs)

