"""This module contains the general information for SesDiskSlotEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SesDiskSlotEpConsts():
    DISK_PRESENT_FALSE = "false"
    DISK_PRESENT_NO = "no"
    DISK_PRESENT_TRUE = "true"
    DISK_PRESENT_YES = "yes"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    SCSI_DISK_STATE_BAD = "bad"
    SCSI_DISK_STATE_GOOD = "good"
    SCSI_DISK_STATE_UNKNOWN = "unknown"


class SesDiskSlotEp(ManagedObject):
    """This is SesDiskSlotEp class."""

    consts = SesDiskSlotEpConsts()
    naming_props = set(['encId', 'id'])

    mo_meta = MoMeta("SesDiskSlotEp", "sesDiskSlotEp", "disk-slot-ep-[enc_id]-id-[id]", VersionMeta.Version151a, "InputOutput", 0x3f, [], ["read-only"], ['sesEnclosure'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "disk_dn": MoPropertyMeta("disk_dn", "diskDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "disk_present": MoPropertyMeta("disk_present", "diskPresent", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "enc_id": MoPropertyMeta("enc_id", "encId", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "scsi_disk_state": MoPropertyMeta("scsi_disk_state", "scsiDiskState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bad", "good", "unknown"], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "slot_dn": MoPropertyMeta("slot_dn", "slotDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "diskDn": "disk_dn", 
        "diskPresent": "disk_present", 
        "dn": "dn", 
        "encId": "enc_id", 
        "id": "id", 
        "lc": "lc", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "scsiDiskState": "scsi_disk_state", 
        "serial": "serial", 
        "slotDn": "slot_dn", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, enc_id, id, **kwargs):
        self._dirty_mask = 0
        self.enc_id = enc_id
        self.id = id
        self.child_action = None
        self.disk_dn = None
        self.disk_present = None
        self.lc = None
        self.model = None
        self.revision = None
        self.scsi_disk_state = None
        self.serial = None
        self.slot_dn = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "SesDiskSlotEp", parent_mo_or_dn, **kwargs)

