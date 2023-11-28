"""This module contains the general information for FabricLanCloud ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricLanCloudConsts():
    MAC_AGING_MODE_DEFAULT = "mode-default"
    MAC_AGING_NEVER = "never"
    MODE_END_HOST = "end-host"
    MODE_SWITCH = "switch"
    VLAN_COMPRESSION_DISABLED = "disabled"
    VLAN_COMPRESSION_ENABLED = "enabled"


class FabricLanCloud(ManagedObject):
    """This is FabricLanCloud class."""

    consts = FabricLanCloudConsts()
    naming_props = set([])

    mo_meta = MoMeta("FabricLanCloud", "fabricLanCloud", "lan", VersionMeta.Version111a, "InputOutput", 0x7f, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEp'], ['extvmmNetworkSets', 'extvmmVMNetworkSets', 'fabricEthLan', 'fabricEthLinkProfile', 'fabricLanPinGroup', 'fabricLanPinGroupOperation', 'fabricNetGroup', 'fabricUdldLinkPolicy', 'fabricVlan', 'firmwareAck', 'flowctrlDefinition', 'mgmtInbandProfile', 'qosclassDefinition', 'statsThresholdPolicy', 'vnicNetGroup', 'vnicProfileSet'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "mac_aging": MoPropertyMeta("mac_aging", "macAging", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["mode-default", "never"], ["0-1000001"]), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["end-host", "switch"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vlan_compression": MoPropertyMeta("vlan_compression", "vlanCompression", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["disabled", "enabled"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "macAging": "mac_aging", 
        "mode": "mode", 
        "rn": "rn", 
        "status": "status", 
        "vlanCompression": "vlan_compression", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.mac_aging = None
        self.mode = None
        self.status = None
        self.vlan_compression = None

        ManagedObject.__init__(self, "FabricLanCloud", parent_mo_or_dn, **kwargs)

