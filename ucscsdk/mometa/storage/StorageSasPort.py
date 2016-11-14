"""This module contains the general information for StorageSasPort ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageSasPortConsts():
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    LINK_SPEED_1_5_GBPS = "1-5-gbps"
    LINK_SPEED_12_GBPS = "12-gbps"
    LINK_SPEED_3_GBPS = "3-gbps"
    LINK_SPEED_6_GBPS = "6-gbps"
    LINK_SPEED_DISABLED = "disabled"
    LINK_SPEED_DOWN = "down"
    LINK_SPEED_HOST_POWER_OFF = "host-power-off"
    LINK_SPEED_UNKNOWN = "unknown"
    LINK_SPEED_UNSUPPORTED_DEVICE = "unsupported-device"


class StorageSasPort(ManagedObject):
    """This is StorageSasPort class."""

    consts = StorageSasPortConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("StorageSasPort", "storageSasPort", "sas-port-[id]", VersionMeta.Version151a, "InputOutput", 0x1f, [], ["read-only"], [u'storageEnclosureLocalDiskConfig', u'storageLocalDisk'], [], ["Get"])

    prop_meta = {
        "address": MoPropertyMeta("address", "address", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "endpoint": MoPropertyMeta("endpoint", "endpoint", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "link_descr": MoPropertyMeta("link_descr", "linkDescr", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "link_speed": MoPropertyMeta("link_speed", "linkSpeed", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1-5-gbps", "12-gbps", "3-gbps", "6-gbps", "disabled", "down", "host-power-off", "unknown", "unsupported-device"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "address": "address", 
        "childAction": "child_action", 
        "dn": "dn", 
        "endpoint": "endpoint", 
        "id": "id", 
        "lc": "lc", 
        "linkDescr": "link_descr", 
        "linkSpeed": "link_speed", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.address = None
        self.child_action = None
        self.endpoint = None
        self.lc = None
        self.link_descr = None
        self.link_speed = None
        self.status = None

        ManagedObject.__init__(self, "StorageSasPort", parent_mo_or_dn, **kwargs)

