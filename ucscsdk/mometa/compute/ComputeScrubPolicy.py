"""This module contains the general information for ComputeScrubPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeScrubPolicyConsts():
    BIOS_SETTINGS_SCRUB_NO = "no"
    BIOS_SETTINGS_SCRUB_YES = "yes"
    DISK_SCRUB_NO = "no"
    DISK_SCRUB_YES = "yes"
    FLEX_FLASH_SCRUB_NO = "no"
    FLEX_FLASH_SCRUB_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class ComputeScrubPolicy(ManagedObject):
    """This is ComputeScrubPolicy class."""

    consts = ComputeScrubPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("ComputeScrubPolicy", "computeScrubPolicy", "scrub-[name]", VersionMeta.Version101a, "InputOutput", 0x1ff, [], ["read-only"], ['orgOrg'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "bios_settings_scrub": MoPropertyMeta("bios_settings_scrub", "biosSettingsScrub", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["no", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "disk_scrub": MoPropertyMeta("disk_scrub", "diskScrub", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["no", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "flex_flash_scrub": MoPropertyMeta("flex_flash_scrub", "flexFlashScrub", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["no", "yes"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "biosSettingsScrub": "bios_settings_scrub", 
        "childAction": "child_action", 
        "descr": "descr", 
        "diskScrub": "disk_scrub", 
        "dn": "dn", 
        "flexFlashScrub": "flex_flash_scrub", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.bios_settings_scrub = None
        self.child_action = None
        self.descr = None
        self.disk_scrub = None
        self.flex_flash_scrub = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None

        ManagedObject.__init__(self, "ComputeScrubPolicy", parent_mo_or_dn, **kwargs)

