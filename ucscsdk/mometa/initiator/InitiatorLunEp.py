"""This module contains the general information for InitiatorLunEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class InitiatorLunEpConsts():
    BOOTABLE_FALSE = "false"
    BOOTABLE_NO = "no"
    BOOTABLE_TRUE = "true"
    BOOTABLE_YES = "yes"
    ID_UNSPECIFIED = "unspecified"


class InitiatorLunEp(ManagedObject):
    """This is InitiatorLunEp class."""

    consts = InitiatorLunEpConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("InitiatorLunEp", "initiatorLunEp", "lun-[id]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['storageIScsiTargetIf'], [], [None])

    prop_meta = {
        "bootable": MoPropertyMeta("bootable", "bootable", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "bootable": "bootable", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "id": "id", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.bootable = None
        self.child_action = None
        self.ep_dn = None
        self.status = None

        ManagedObject.__init__(self, "InitiatorLunEp", parent_mo_or_dn, **kwargs)

