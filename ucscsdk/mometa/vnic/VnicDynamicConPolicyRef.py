"""This module contains the general information for VnicDynamicConPolicyRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicDynamicConPolicyRefConsts():
    pass


class VnicDynamicConPolicyRef(ManagedObject):
    """This is VnicDynamicConPolicyRef class."""

    consts = VnicDynamicConPolicyRefConsts()
    naming_props = set(['conPolicyName'])

    mo_meta = MoMeta("VnicDynamicConPolicyRef", "vnicDynamicConPolicyRef", "con-ref-[con_policy_name]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin", "ls-config", "ls-network", "ls-network-policy", "ls-server"], ['vnicEther', 'vnicLanConnTempl'], ['faultInst'], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "con_policy_name": MoPropertyMeta("con_policy_name", "conPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "oper_con_policy_name": MoPropertyMeta("oper_con_policy_name", "operConPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "conPolicyName": "con_policy_name", 
        "dn": "dn", 
        "operConPolicyName": "oper_con_policy_name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, con_policy_name, **kwargs):
        self._dirty_mask = 0
        self.con_policy_name = con_policy_name
        self.child_action = None
        self.oper_con_policy_name = None
        self.status = None

        ManagedObject.__init__(self, "VnicDynamicConPolicyRef", parent_mo_or_dn, **kwargs)

