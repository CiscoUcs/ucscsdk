"""This module contains the general information for FirmwareCatalogPackConfig ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareCatalogPackConfigConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    UPDATE_TRIGGER_IMMEDIATE = "immediate"


class FirmwareCatalogPackConfig(ManagedObject):
    """This is FirmwareCatalogPackConfig class."""

    consts = FirmwareCatalogPackConfigConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FirmwareCatalogPackConfig", "firmwareCatalogPackConfig", "fw-catalog-pack-config[name]", VersionMeta.Version151a, "InputOutput", 0x3ff, [], ["admin", "operations"], ['firmwareDomainInfraProfile', 'orgDomainGroup', 'orgOrg'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "catalog_name": MoPropertyMeta("catalog_name", "catalogName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "catalog_version": MoPropertyMeta("catalog_version", "catalogVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "stage_size": MoPropertyMeta("stage_size", "stageSize", "ushort", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "update_trigger": MoPropertyMeta("update_trigger", "updateTrigger", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], []), 
    }

    prop_map = {
        "catalogName": "catalog_name", 
        "catalogVersion": "catalog_version", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "stageSize": "stage_size", 
        "status": "status", 
        "updateTrigger": "update_trigger", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.catalog_name = None
        self.catalog_version = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.mode = None
        self.policy_level = None
        self.policy_owner = None
        self.stage_size = None
        self.status = None
        self.update_trigger = None

        ManagedObject.__init__(self, "FirmwareCatalogPackConfig", parent_mo_or_dn, **kwargs)

