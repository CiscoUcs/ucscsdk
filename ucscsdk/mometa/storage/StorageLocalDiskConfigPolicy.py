"""This module contains the general information for StorageLocalDiskConfigPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageLocalDiskConfigPolicyConsts():
    INT_ID_NONE = "none"
    MODE_ANY_CONFIGURATION = "any-configuration"
    MODE_BEST_EFFORT_MIRRORED = "best-effort-mirrored"
    MODE_BEST_EFFORT_MIRRORED_STRIPED = "best-effort-mirrored-striped"
    MODE_BEST_EFFORT_STRIPED = "best-effort-striped"
    MODE_BEST_EFFORT_STRIPED_DUAL_PARITY = "best-effort-striped-dual-parity"
    MODE_BEST_EFFORT_STRIPED_PARITY = "best-effort-striped-parity"
    MODE_DUAL_DISK = "dual-disk"
    MODE_NO_LOCAL_STORAGE = "no-local-storage"
    MODE_NO_RAID = "no-raid"
    MODE_RAID_MIRRORED = "raid-mirrored"
    MODE_RAID_MIRRORED_STRIPED = "raid-mirrored-striped"
    MODE_RAID_STRIPED = "raid-striped"
    MODE_RAID_STRIPED_DUAL_PARITY = "raid-striped-dual-parity"
    MODE_RAID_STRIPED_DUAL_PARITY_STRIPED = "raid-striped-dual-parity-striped"
    MODE_RAID_STRIPED_PARITY = "raid-striped-parity"
    MODE_RAID_STRIPED_PARITY_STRIPED = "raid-striped-parity-striped"
    MODE_SINGLE_DISK = "single-disk"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PROTECT_CONFIG_FALSE = "false"
    PROTECT_CONFIG_NO = "no"
    PROTECT_CONFIG_TRUE = "true"
    PROTECT_CONFIG_YES = "yes"


class StorageLocalDiskConfigPolicy(ManagedObject):
    """This is StorageLocalDiskConfigPolicy class."""

    consts = StorageLocalDiskConfigPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("StorageLocalDiskConfigPolicy", "storageLocalDiskConfigPolicy", "local-disk-config-[name]", VersionMeta.Version111a, "InputOutput", 0x3ff, [], ["read-only"], ['orgOrg'], ['lstorageSecurity', 'storageLocalDiskPartition'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flex_flash_raid_reporting_state": MoPropertyMeta("flex_flash_raid_reporting_state", "flexFlashRAIDReportingState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "flex_flash_state": MoPropertyMeta("flex_flash_state", "flexFlashState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["any-configuration", "best-effort-mirrored", "best-effort-mirrored-striped", "best-effort-striped", "best-effort-striped-dual-parity", "best-effort-striped-parity", "dual-disk", "no-local-storage", "no-raid", "raid-mirrored", "raid-mirrored-striped", "raid-striped", "raid-striped-dual-parity", "raid-striped-dual-parity-striped", "raid-striped-parity", "raid-striped-parity-striped", "single-disk"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "protect_config": MoPropertyMeta("protect_config", "protectConfig", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "flexFlashRAIDReportingState": "flex_flash_raid_reporting_state", 
        "flexFlashState": "flex_flash_state", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "protectConfig": "protect_config", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.flex_flash_raid_reporting_state = None
        self.flex_flash_state = None
        self.int_id = None
        self.mode = None
        self.policy_level = None
        self.policy_owner = None
        self.protect_config = None
        self.status = None

        ManagedObject.__init__(self, "StorageLocalDiskConfigPolicy", parent_mo_or_dn, **kwargs)

