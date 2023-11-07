"""This module contains the general information for FabricEthMonSrcEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricEthMonSrcEpConsts():
    DIRECTION_BOTH = "both"
    DIRECTION_RX = "rx"
    DIRECTION_TX = "tx"


class FabricEthMonSrcEp(ManagedObject):
    """This is FabricEthMonSrcEp class."""

    consts = FabricEthMonSrcEpConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricEthMonSrcEp", "fabricEthMonSrcEp", "mon-src-[name]", VersionMeta.Version151a, "InputOutput", 0x7f, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['adaptorExtEthIf', 'fabricDceSwSrvEp', 'fabricEthEstcEp', 'fabricEthEstcPc', 'fabricEthLanEp', 'fabricEthLanPc', 'fabricFcoeEstcEp', 'fabricFcoeSanEp', 'fabricFcoeSanPc', 'fabricVlan', 'vmNic', 'vnicEther', 'vnicFc', 'vnicIScsi', 'vnicIScsiLCP', 'vnicIniGrpFc', 'vnicIniGrpFcB', 'vnicLstorageIScsi', 'vnicMgmt', 'vnicMonSesFc'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "direction": MoPropertyMeta("direction", "direction", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["both", "rx", "tx"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "session": MoPropertyMeta("session", "session", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-255"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "direction": "direction", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "session": "session", 
        "status": "status", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.direction = None
        self.session = None
        self.status = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricEthMonSrcEp", parent_mo_or_dn, **kwargs)

