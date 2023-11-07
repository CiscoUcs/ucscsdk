"""This module contains the general information for FabricEtherRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricEtherRefConsts():
    LC_CTRL_STATE_ALLOCATED = "allocated"
    LC_CTRL_STATE_AVAILABLE = "available"
    LC_CTRL_STATE_DEALLOCATED = "deallocated"
    LC_CTRL_STATE_REPURPOSED = "repurposed"


class FabricEtherRef(ManagedObject):
    """This is FabricEtherRef class."""

    consts = FabricEtherRefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricEtherRef", "fabricEtherRef", "EtherRef-[name]", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["admin", "ext-lan-config", "ext-lan-policy", "ls-network"], ['adaptorVlan', 'fabricVlan', 'fabricVlanEp', 'fabricVsan', 'fabricVsanEp'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "client_id": MoPropertyMeta("client_id", "clientId", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "lc_ctrl_state": MoPropertyMeta("lc_ctrl_state", "lcCtrlState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, 1, 256, None, [], []), 
        "oper_eth_dn": MoPropertyMeta("oper_eth_dn", "operEthDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "clientId": "client_id", 
        "dn": "dn", 
        "lcCtrlState": "lc_ctrl_state", 
        "name": "name", 
        "operEthDn": "oper_eth_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.client_id = None
        self.lc_ctrl_state = None
        self.oper_eth_dn = None
        self.status = None

        ManagedObject.__init__(self, "FabricEtherRef", parent_mo_or_dn, **kwargs)

