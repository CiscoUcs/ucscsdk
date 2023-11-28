"""This module contains the general information for FabricSanCloud ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricSanCloudConsts():
    MODE_END_HOST = "end-host"
    MODE_SWITCH = "switch"


class FabricSanCloud(ManagedObject):
    """This is FabricSanCloud class."""

    consts = FabricSanCloudConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricSanCloud", "fabricSanCloud", "san", VersionMeta.Version111a, "InputOutput", 0x1f, [], [""], ['fabricEp'], ['fabricFcSan', 'fabricFcUplinkOperation', 'fabricSanPinGroup', 'fabricSanPinGroupOperation', 'firmwareAck', 'statsThresholdPolicy'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["end-host", "switch"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "mode": "mode", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.mode = None
        self.status = None

        ManagedObject.__init__(self, "FabricSanCloud", parent_mo_or_dn, **kwargs)

