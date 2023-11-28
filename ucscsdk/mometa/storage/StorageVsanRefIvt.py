"""This module contains the general information for StorageVsanRefIvt ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageVsanRefIvtConsts():
    ZONING_STATE_DISABLED = "disabled"
    ZONING_STATE_ENABLED = "enabled"


class StorageVsanRefIvt(ManagedObject):
    """This is StorageVsanRefIvt class."""

    consts = StorageVsanRefIvtConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageVsanRefIvt", "storageVsanRefIvt", "vsan-ref-ivt", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["admin", "ext-san-config", "ext-san-policy", "ls-storage", "ls-storage-policy"], ['fabricFcUserZoneIvt'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "zoning_state": MoPropertyMeta("zoning_state", "zoningState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "zoningState": "zoning_state", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.name = None
        self.status = None
        self.zoning_state = None

        ManagedObject.__init__(self, "StorageVsanRefIvt", parent_mo_or_dn, **kwargs)

