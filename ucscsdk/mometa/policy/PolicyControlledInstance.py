"""This module contains the general information for PolicyControlledInstance ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyControlledInstanceConsts():
    RESOLVE_TYPE_NAME = "name"
    RESOLVE_TYPE_RN = "rn"


class PolicyControlledInstance(ManagedObject):
    """This is PolicyControlledInstance class."""

    consts = PolicyControlledInstanceConsts()
    naming_props = set(['type', 'name'])

    mo_meta = MoMeta("PolicyControlledInstance", "policyControlledInstance", "ctrlled-[type]-inst-[name]", VersionMeta.Version131a, "InputOutput", 0xff, [], ["admin"], ['policyCommunication', 'policyConfigBackup', 'policyDateTime', 'policyDiscovery', 'policyDns', 'policyEquipment', 'policyFault', 'policyInfraFirmware', 'policyMEp', 'policyModularChassisFan', 'policyMonitoring', 'policyPortConfig', 'policyPowerExtended', 'policyPowerMgmt', 'policyPowerSave', 'policyPsu', 'policySecurity', 'policyStorageAutoConfig'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_dn": MoPropertyMeta("def_dn", "defDn", "string", VersionMeta.Version131a, MoPropertyMeta.CREATE_ONLY, 0x2, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "external_resolve_name": MoPropertyMeta("external_resolve_name", "externalResolveName", "string", VersionMeta.Version131a, MoPropertyMeta.CREATE_ONLY, 0x8, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []), 
        "resolve_type": MoPropertyMeta("resolve_type", "resolveType", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["name", "rn"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "defDn": "def_dn", 
        "dn": "dn", 
        "externalResolveName": "external_resolve_name", 
        "name": "name", 
        "resolveType": "resolve_type", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, name, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.name = name
        self.child_action = None
        self.def_dn = None
        self.external_resolve_name = None
        self.resolve_type = None
        self.status = None

        ManagedObject.__init__(self, "PolicyControlledInstance", parent_mo_or_dn, **kwargs)

