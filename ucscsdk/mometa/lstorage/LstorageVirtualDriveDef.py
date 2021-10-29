"""This module contains the general information for LstorageVirtualDriveDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LstorageVirtualDriveDefConsts():
    ACCESS_POLICY_BLOCKED = "blocked"
    ACCESS_POLICY_HIDDEN = "hidden"
    ACCESS_POLICY_PLATFORM_DEFAULT = "platform-default"
    ACCESS_POLICY_READ_ONLY = "read-only"
    ACCESS_POLICY_READ_WRITE = "read-write"
    ACCESS_POLICY_TRANSPORT_READY = "transport-ready"
    ACCESS_POLICY_UNKNOWN = "unknown"
    DRIVE_CACHE_DISABLE = "disable"
    DRIVE_CACHE_ENABLE = "enable"
    DRIVE_CACHE_NO_CHANGE = "no-change"
    DRIVE_CACHE_PLATFORM_DEFAULT = "platform-default"
    DRIVE_CACHE_UNKNOWN = "unknown"
    IO_POLICY_CACHED = "cached"
    IO_POLICY_DIRECT = "direct"
    IO_POLICY_PLATFORM_DEFAULT = "platform-default"
    IO_POLICY_UNKNOWN = "unknown"
    READ_POLICY_NORMAL = "normal"
    READ_POLICY_PLATFORM_DEFAULT = "platform-default"
    READ_POLICY_READ_AHEAD = "read-ahead"
    READ_POLICY_UNKNOWN = "unknown"
    SECURITY_FALSE = "false"
    SECURITY_NO = "no"
    SECURITY_TRUE = "true"
    SECURITY_YES = "yes"
    STRIP_SIZE_1024_KB = "1024KB"
    STRIP_SIZE_128_KB = "128KB"
    STRIP_SIZE_16_KB = "16KB"
    STRIP_SIZE_256_KB = "256KB"
    STRIP_SIZE_32_KB = "32KB"
    STRIP_SIZE_512_KB = "512KB"
    STRIP_SIZE_64_KB = "64KB"
    STRIP_SIZE_8_KB = "8KB"
    STRIP_SIZE_PLATFORM_DEFAULT = "platform-default"
    STRIP_SIZE_UNSPECIFIED = "unspecified"
    WRITE_CACHE_POLICY_ALWAYS_WRITE_BACK = "always-write-back"
    WRITE_CACHE_POLICY_PLATFORM_DEFAULT = "platform-default"
    WRITE_CACHE_POLICY_UNKNOWN = "unknown"
    WRITE_CACHE_POLICY_WRITE_BACK_GOOD_BBU = "write-back-good-bbu"
    WRITE_CACHE_POLICY_WRITE_THROUGH = "write-through"


class LstorageVirtualDriveDef(ManagedObject):
    """This is LstorageVirtualDriveDef class."""

    consts = LstorageVirtualDriveDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageVirtualDriveDef", "lstorageVirtualDriveDef", "virtual-drive-def", VersionMeta.Version131a, "InputOutput", 0x7ff, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], [u'lstorageDiskGroupConfigDef', u'lstorageDiskGroupConfigPolicy'], [], ["Get", "Set"])

    prop_meta = {
        "access_policy": MoPropertyMeta("access_policy", "accessPolicy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["blocked", "hidden", "platform-default", "read-only", "read-write", "transport-ready", "unknown"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "drive_cache": MoPropertyMeta("drive_cache", "driveCache", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["disable", "enable", "no-change", "platform-default", "unknown"], []), 
        "io_policy": MoPropertyMeta("io_policy", "ioPolicy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["cached", "direct", "platform-default", "unknown"], []), 
        "read_policy": MoPropertyMeta("read_policy", "readPolicy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["normal", "platform-default", "read-ahead", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "security": MoPropertyMeta("security", "security", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "no", "true", "yes"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "strip_size": MoPropertyMeta("strip_size", "stripSize", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["1024KB", "128KB", "16KB", "256KB", "32KB", "512KB", "64KB", "8KB", "platform-default", "unspecified"], []), 
        "write_cache_policy": MoPropertyMeta("write_cache_policy", "writeCachePolicy", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["always-write-back", "platform-default", "unknown", "write-back-good-bbu", "write-through"], []), 
    }

    prop_map = {
        "accessPolicy": "access_policy", 
        "childAction": "child_action", 
        "dn": "dn", 
        "driveCache": "drive_cache", 
        "ioPolicy": "io_policy", 
        "readPolicy": "read_policy", 
        "rn": "rn", 
        "security": "security", 
        "status": "status", 
        "stripSize": "strip_size", 
        "writeCachePolicy": "write_cache_policy", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.access_policy = None
        self.child_action = None
        self.drive_cache = None
        self.io_policy = None
        self.read_policy = None
        self.security = None
        self.status = None
        self.strip_size = None
        self.write_cache_policy = None

        ManagedObject.__init__(self, "LstorageVirtualDriveDef", parent_mo_or_dn, **kwargs)

