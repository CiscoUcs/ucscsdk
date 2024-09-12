"""This module contains the general information for VnicBootTarget ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicBootTargetConsts():
    LUN_UNSPECIFIED = "unspecified"


class VnicBootTarget(ManagedObject):
    """This is VnicBootTarget class."""

    consts = VnicBootTargetConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicBootTarget", "vnicBootTarget", "boot-target", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["admin", "ls-config", "ls-server", "ls-storage"], ['vnicFc'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "lun": MoPropertyMeta("lun", "lun", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "wwn": MoPropertyMeta("wwn", "wwn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lun": "lun", 
        "rn": "rn", 
        "status": "status", 
        "wwn": "wwn", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.lun = None
        self.status = None
        self.wwn = None

        ManagedObject.__init__(self, "VnicBootTarget", parent_mo_or_dn, **kwargs)

