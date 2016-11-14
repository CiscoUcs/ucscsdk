"""This module contains the general information for ConfigPolicyUsageItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigPolicyUsageItemConsts():
    pass


class ConfigPolicyUsageItem(ManagedObject):
    """This is ConfigPolicyUsageItem class."""

    consts = ConfigPolicyUsageItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigPolicyUsageItem", "configPolicyUsageItem", "policy-usage-item", VersionMeta.Version151a, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "class_name": MoPropertyMeta("class_name", "className", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "consumer_dn": MoPropertyMeta("consumer_dn", "consumerDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "consumer_name": MoPropertyMeta("consumer_name", "consumerName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "className": "class_name", 
        "consumerDn": "consumer_dn", 
        "consumerName": "consumer_name", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.class_name = None
        self.consumer_dn = None
        self.consumer_name = None
        self.status = None

        ManagedObject.__init__(self, "ConfigPolicyUsageItem", parent_mo_or_dn, **kwargs)

