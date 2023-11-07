"""This module contains the general information for LsbootNvmePciSsd ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsbootNvmePciSsdConsts():
    TYPE_DISK_SSD = "disk-ssd"
    TYPE_PCI_SSD = "pci-ssd"


class LsbootNvmePciSsd(ManagedObject):
    """This is LsbootNvmePciSsd class."""

    consts = LsbootNvmePciSsdConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootNvmePciSsd", "lsbootNvmePciSsd", "nvme-pci-ssd", VersionMeta.Version201f, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['lsbootNvme'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201f, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201f, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version201f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-16"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201f, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "ushort", VersionMeta.Version201f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201f, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disk-ssd", "pci-ssd"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "order": "order", 
        "rn": "rn", 
        "slotId": "slot_id", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.order = None
        self.slot_id = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LsbootNvmePciSsd", parent_mo_or_dn, **kwargs)

