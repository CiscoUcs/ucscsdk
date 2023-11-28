"""This module contains the general information for AdaptorVmmqConnDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorVmmqConnDefConsts():
    pass


class AdaptorVmmqConnDef(ManagedObject):
    """This is AdaptorVmmqConnDef class."""

    consts = AdaptorVmmqConnDefConsts()
    naming_props = set(['conPolicyName'])

    mo_meta = MoMeta("AdaptorVmmqConnDef", "adaptorVmmqConnDef", "vmmq-conn-def-[con_policy_name]", VersionMeta.Version201f, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-server", "read-only"], ['adaptorHostEthIf'], ['adaptorEthCompQueueProfile', 'adaptorEthInterruptProfile', 'adaptorEthRecvQueueProfile', 'adaptorEthRoCEProfile', 'adaptorEthWorkQueueProfile', 'adaptorRssProfile'], [None])

    prop_meta = {
        "vmmq_sub_vnic_count": MoPropertyMeta("vmmq_sub_vnic_count", "VmmqSubVnicCount", "uint", VersionMeta.Version201f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201f, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "con_policy_name": MoPropertyMeta("con_policy_name", "conPolicyName", "string", VersionMeta.Version201f, MoPropertyMeta.NAMING, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201f, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201f, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201f, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "VmmqSubVnicCount": "vmmq_sub_vnic_count", 
        "childAction": "child_action", 
        "conPolicyName": "con_policy_name", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, con_policy_name, **kwargs):
        self._dirty_mask = 0
        self.con_policy_name = con_policy_name
        self.vmmq_sub_vnic_count = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorVmmqConnDef", parent_mo_or_dn, **kwargs)

