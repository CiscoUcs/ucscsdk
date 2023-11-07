"""This module contains the general information for ObserveObservedCont ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ObserveObservedContConsts():
    pass


class ObserveObservedCont(ManagedObject):
    """This is ObserveObservedCont class."""

    consts = ObserveObservedContConsts()
    naming_props = set([])

    mo_meta = MoMeta("ObserveObservedCont", "observeObservedCont", "observe", VersionMeta.Version101a, "InputOutput", 0xf, [], ["admin"], ['topRoot'], ['observeObserved'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id_count": MoPropertyMeta("id_count", "idCount", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tx_id": MoPropertyMeta("tx_id", "txId", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "idCount": "id_count", 
        "rn": "rn", 
        "status": "status", 
        "txId": "tx_id", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.id_count = None
        self.status = None
        self.tx_id = None

        ManagedObject.__init__(self, "ObserveObservedCont", **kwargs)

