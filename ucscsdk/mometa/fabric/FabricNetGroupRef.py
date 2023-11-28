"""This module contains the general information for FabricNetGroupRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricNetGroupRefConsts():
    OWNER_POLICY_EXTERNAL = "policy-external"
    OWNER_POLICY_GLOBAL = "policy-global"
    OWNER_POLICY_LOCAL = "policy-local"


class FabricNetGroupRef(ManagedObject):
    """This is FabricNetGroupRef class."""

    consts = FabricNetGroupRefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricNetGroupRef", "fabricNetGroupRef", "net-group-ref-[name]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["admin", "ext-lan-config", "ext-lan-policy", "ls-config", "ls-network", "ls-server"], ['dcxVc', 'vnicEther', 'vnicLanConnTempl', 'vnicSanConnTempl'], ['faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_name": MoPropertyMeta("oper_name", "operName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_net_group_name": MoPropertyMeta("oper_net_group_name", "operNetGroupName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["policy-external", "policy-global", "policy-local"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "operName": "oper_name", 
        "operNetGroupName": "oper_net_group_name", 
        "owner": "owner", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.oper_name = None
        self.oper_net_group_name = None
        self.owner = None
        self.status = None

        ManagedObject.__init__(self, "FabricNetGroupRef", parent_mo_or_dn, **kwargs)

