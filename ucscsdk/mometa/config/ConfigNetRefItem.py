"""This module contains the general information for ConfigNetRefItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigNetRefItemConsts():
    TYPE_ACI = "aci"
    TYPE_ALL = "all"
    TYPE_CLASSIC = "classic"


class ConfigNetRefItem(ManagedObject):
    """This is ConfigNetRefItem class."""

    consts = ConfigNetRefItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigNetRefItem", "configNetRefItem", "", VersionMeta.Version201b, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "inband_policy_dn": MoPropertyMeta("inband_policy_dn", "inbandPolicyDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "net_group_dn": MoPropertyMeta("net_group_dn", "netGroupDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aci", "all", "classic"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "inbandPolicyDn": "inband_policy_dn", 
        "name": "name", 
        "netGroupDn": "net_group_dn", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.inband_policy_dn = None
        self.name = None
        self.net_group_dn = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "ConfigNetRefItem", parent_mo_or_dn, **kwargs)

