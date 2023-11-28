"""This module contains the general information for FabricConsumer ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricConsumerConsts():
    pass


class FabricConsumer(ManagedObject):
    """This is FabricConsumer class."""

    consts = FabricConsumerConsts()
    naming_props = set(['clientId'])

    mo_meta = MoMeta("FabricConsumer", "fabricConsumer", "ucsm-[client_id]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['adaptorVlan', 'fabricVlan', 'fabricVlanEp', 'fabricVsan', 'fabricVsanEp'], [], ["Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "client_id": MoPropertyMeta("client_id", "clientId", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x2, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "clientId": "client_id", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, client_id, **kwargs):
        self._dirty_mask = 0
        self.client_id = client_id
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "FabricConsumer", parent_mo_or_dn, **kwargs)

