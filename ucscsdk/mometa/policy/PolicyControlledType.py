"""This module contains the general information for PolicyControlledType ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyControlledTypeConsts():
    pass


class PolicyControlledType(ManagedObject):
    """This is PolicyControlledType class."""

    consts = PolicyControlledTypeConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("PolicyControlledType", "policyControlledType", "ctrlled-type-[type]", VersionMeta.Version131a, "InputOutput", 0x3f, [], ["admin"], ['policyCommunication', 'policyConfigBackup', 'policyDateTime', 'policyDiscovery', 'policyDns', 'policyEquipment', 'policyFault', 'policyInfraFirmware', 'policyMEp', 'policyModularChassisFan', 'policyMonitoring', 'policyPortConfig', 'policyPowerExtended', 'policyPowerMgmt', 'policyPowerSave', 'policyPsu', 'policySecurity', 'policyStorageAutoConfig'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "parent_context": MoPropertyMeta("parent_context", "parentContext", "string", VersionMeta.Version131a, MoPropertyMeta.CREATE_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "parentContext": "parent_context", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.parent_context = None
        self.status = None

        ManagedObject.__init__(self, "PolicyControlledType", parent_mo_or_dn, **kwargs)

