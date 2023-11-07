"""This module contains the general information for EquipmentLocalDiskDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentLocalDiskDefConsts():
    FORCE_UPDATE_VERSION_FALSE = "false"
    FORCE_UPDATE_VERSION_NO = "no"
    FORCE_UPDATE_VERSION_TRUE = "true"
    FORCE_UPDATE_VERSION_YES = "yes"
    ME4308_SUPPORTED_FALSE = "false"
    ME4308_SUPPORTED_NO = "no"
    ME4308_SUPPORTED_TRUE = "true"
    ME4308_SUPPORTED_YES = "yes"
    SELF_ENCRYPTING_DRIVE_FALSE = "false"
    SELF_ENCRYPTING_DRIVE_NO = "no"
    SELF_ENCRYPTING_DRIVE_TRUE = "true"
    SELF_ENCRYPTING_DRIVE_YES = "yes"
    TECHNOLOGY_HDD = "HDD"
    TECHNOLOGY_NVME = "NVME"
    TECHNOLOGY_SSD = "SSD"
    TECHNOLOGY_UNSPECIFIED = "unspecified"


class EquipmentLocalDiskDef(ManagedObject):
    """This is EquipmentLocalDiskDef class."""

    consts = EquipmentLocalDiskDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentLocalDiskDef", "equipmentLocalDiskDef", "disk", VersionMeta.Version111a, "InputOutput", 0x1f, [], [""], ['equipmentLocalDiskCapProvider'], [], ["Get"])

    prop_meta = {
        "block_size": MoPropertyMeta("block_size", "blockSize", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "cache_size": MoPropertyMeta("cache_size", "cacheSize", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "capacity": MoPropertyMeta("capacity", "capacity", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "force_update_version": MoPropertyMeta("force_update_version", "forceUpdateVersion", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "link_speed": MoPropertyMeta("link_speed", "linkSpeed", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "me4308_supported": MoPropertyMeta("me4308_supported", "me4308Supported", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "number_of_blocks": MoPropertyMeta("number_of_blocks", "numberOfBlocks", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "rotational_speed": MoPropertyMeta("rotational_speed", "rotationalSpeed", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "seek_average_read_write": MoPropertyMeta("seek_average_read_write", "seekAverageReadWrite", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "seek_track_to_track_read_write": MoPropertyMeta("seek_track_to_track_read_write", "seekTrackToTrackReadWrite", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "self_encrypting_drive": MoPropertyMeta("self_encrypting_drive", "selfEncryptingDrive", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "technology": MoPropertyMeta("technology", "technology", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["HDD", "NVME", "SSD", "unspecified"], []), 
    }

    prop_map = {
        "blockSize": "block_size", 
        "cacheSize": "cache_size", 
        "capacity": "capacity", 
        "childAction": "child_action", 
        "dn": "dn", 
        "forceUpdateVersion": "force_update_version", 
        "linkSpeed": "link_speed", 
        "me4308Supported": "me4308_supported", 
        "name": "name", 
        "numberOfBlocks": "number_of_blocks", 
        "rn": "rn", 
        "rotationalSpeed": "rotational_speed", 
        "seekAverageReadWrite": "seek_average_read_write", 
        "seekTrackToTrackReadWrite": "seek_track_to_track_read_write", 
        "selfEncryptingDrive": "self_encrypting_drive", 
        "status": "status", 
        "technology": "technology", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.block_size = None
        self.cache_size = None
        self.capacity = None
        self.child_action = None
        self.force_update_version = None
        self.link_speed = None
        self.me4308_supported = None
        self.name = None
        self.number_of_blocks = None
        self.rotational_speed = None
        self.seek_average_read_write = None
        self.seek_track_to_track_read_write = None
        self.self_encrypting_drive = None
        self.status = None
        self.technology = None

        ManagedObject.__init__(self, "EquipmentLocalDiskDef", parent_mo_or_dn, **kwargs)

