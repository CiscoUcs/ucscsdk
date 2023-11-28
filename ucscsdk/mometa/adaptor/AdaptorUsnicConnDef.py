"""This module contains the general information for AdaptorUsnicConnDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorUsnicConnDefConsts():
    pass


class AdaptorUsnicConnDef(ManagedObject):
    """This is AdaptorUsnicConnDef class."""

    consts = AdaptorUsnicConnDefConsts()
    naming_props = set(['conPolicyName'])

    mo_meta = MoMeta("AdaptorUsnicConnDef", "adaptorUsnicConnDef", "usnic-conn-def-[con_policy_name]", VersionMeta.Version112a, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-server", "read-only"], ['adaptorHostEthIf'], ['adaptorEthCompQueueProfile', 'adaptorEthFailoverProfile', 'adaptorEthInterruptProfile', 'adaptorEthInterruptScalingProfile', 'adaptorEthOffloadProfile', 'adaptorEthRecvQueueProfile', 'adaptorEthWorkQueueProfile', 'adaptorExtIpV6RssHashProfile', 'adaptorIpV4RssHashProfile', 'adaptorIpV6RssHashProfile', 'adaptorRssProfile'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "con_policy_name": MoPropertyMeta("con_policy_name", "conPolicyName", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "usnic_count": MoPropertyMeta("usnic_count", "usnicCount", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "conPolicyName": "con_policy_name", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "usnicCount": "usnic_count", 
    }

    def __init__(self, parent_mo_or_dn, con_policy_name, **kwargs):
        self._dirty_mask = 0
        self.con_policy_name = con_policy_name
        self.child_action = None
        self.status = None
        self.usnic_count = None

        ManagedObject.__init__(self, "AdaptorUsnicConnDef", parent_mo_or_dn, **kwargs)

