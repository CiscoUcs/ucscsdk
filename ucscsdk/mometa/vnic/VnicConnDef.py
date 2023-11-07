"""This module contains the general information for VnicConnDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicConnDefConsts():
    pass


class VnicConnDef(ManagedObject):
    """This is VnicConnDef class."""

    consts = VnicConnDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicConnDef", "vnicConnDef", "conn-def", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-server"], ['lsServer'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "lan_conn_policy_name": MoPropertyMeta("lan_conn_policy_name", "lanConnPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_lan_conn_policy_name": MoPropertyMeta("oper_lan_conn_policy_name", "operLanConnPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_san_conn_policy_name": MoPropertyMeta("oper_san_conn_policy_name", "operSanConnPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "san_conn_policy_name": MoPropertyMeta("san_conn_policy_name", "sanConnPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "lanConnPolicyName": "lan_conn_policy_name", 
        "operLanConnPolicyName": "oper_lan_conn_policy_name", 
        "operSanConnPolicyName": "oper_san_conn_policy_name", 
        "rn": "rn", 
        "sanConnPolicyName": "san_conn_policy_name", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.flt_aggr = None
        self.lan_conn_policy_name = None
        self.oper_lan_conn_policy_name = None
        self.oper_san_conn_policy_name = None
        self.san_conn_policy_name = None
        self.status = None

        ManagedObject.__init__(self, "VnicConnDef", parent_mo_or_dn, **kwargs)

