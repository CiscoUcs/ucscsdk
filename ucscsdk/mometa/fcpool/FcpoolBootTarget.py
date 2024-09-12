"""This module contains the general information for FcpoolBootTarget ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FcpoolBootTargetConsts():
    LUN_UNSPECIFIED = "unspecified"


class FcpoolBootTarget(ManagedObject):
    """This is FcpoolBootTarget class."""

    consts = FcpoolBootTargetConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("FcpoolBootTarget", "fcpoolBootTarget", "target-[type]", VersionMeta.Version101a, "InputOutput", 0x7f, [], ["admin", "ls-storage-policy"], ['fcpoolBlock', 'fcpoolInitiator'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "lun": MoPropertyMeta("lun", "lun", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
        "wwn": MoPropertyMeta("wwn", "wwn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lun": "lun", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "wwn": "wwn", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.lun = None
        self.status = None
        self.wwn = None

        ManagedObject.__init__(self, "FcpoolBootTarget", parent_mo_or_dn, **kwargs)

