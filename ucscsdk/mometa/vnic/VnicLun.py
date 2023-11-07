"""This module contains the general information for VnicLun ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicLunConsts():
    BOOTABLE_FALSE = "false"
    BOOTABLE_NO = "no"
    BOOTABLE_TRUE = "true"
    BOOTABLE_YES = "yes"


class VnicLun(ManagedObject):
    """This is VnicLun class."""

    consts = VnicLunConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicLun", "vnicLun", "lun", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["admin", "ls-config", "ls-server", "ls-storage"], ['vnicIScsiStaticTargetIf'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "bootable": MoPropertyMeta("bootable", "bootable", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-65535"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "bootable": "bootable", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.bootable = None
        self.child_action = None
        self.id = None
        self.status = None

        ManagedObject.__init__(self, "VnicLun", parent_mo_or_dn, **kwargs)

