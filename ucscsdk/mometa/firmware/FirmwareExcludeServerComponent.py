"""This module contains the general information for FirmwareExcludeServerComponent ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareExcludeServerComponentConsts():
    SERVER_COMPONENT_ADAPTOR = "adaptor"
    SERVER_COMPONENT_BLADE_BIOS = "blade-bios"
    SERVER_COMPONENT_BLADE_CONTROLLER = "blade-controller"
    SERVER_COMPONENT_BOARD_CONTROLLER = "board-controller"
    SERVER_COMPONENT_FLEXFLASH_CONTROLLER = "flexflash-controller"
    SERVER_COMPONENT_GRAPHICS_CARD = "graphics-card"
    SERVER_COMPONENT_HOST_HBA = "host-hba"
    SERVER_COMPONENT_HOST_HBA_OPTIONROM = "host-hba-optionrom"
    SERVER_COMPONENT_HOST_NIC = "host-nic"
    SERVER_COMPONENT_HOST_NIC_OPTIONROM = "host-nic-optionrom"
    SERVER_COMPONENT_LOCAL_DISK = "local-disk"
    SERVER_COMPONENT_PSU = "psu"
    SERVER_COMPONENT_SAS_EXP_REG_FW = "sas-exp-reg-fw"
    SERVER_COMPONENT_SAS_EXPANDER = "sas-expander"
    SERVER_COMPONENT_STORAGE_CONTROLLER = "storage-controller"
    SERVER_COMPONENT_STORAGE_CONTROLLER_ONBOARD_DEVICE = "storage-controller-onboard-device"
    SERVER_COMPONENT_STORAGE_CONTROLLER_ONBOARD_DEVICE_CPLD = "storage-controller-onboard-device-cpld"
    SERVER_COMPONENT_STORAGE_DEV_BRIDGE = "storage-dev-bridge"
    SERVER_COMPONENT_UNSPECIFIED = "unspecified"


class FirmwareExcludeServerComponent(ManagedObject):
    """This is FirmwareExcludeServerComponent class."""

    consts = FirmwareExcludeServerComponentConsts()
    naming_props = set(['serverComponent'])

    mo_meta = MoMeta("FirmwareExcludeServerComponent", "firmwareExcludeServerComponent", "exclude-server-component-[server_component]", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config-policy", "ls-server-policy"], ['firmwareComputeHostPack'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "server_component": MoPropertyMeta("server_component", "serverComponent", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x8, None, None, None, ["adaptor", "blade-bios", "blade-controller", "board-controller", "flexflash-controller", "graphics-card", "host-hba", "host-hba-optionrom", "host-nic", "host-nic-optionrom", "local-disk", "psu", "sas-exp-reg-fw", "sas-expander", "storage-controller", "storage-controller-onboard-device", "storage-controller-onboard-device-cpld", "storage-dev-bridge", "unspecified"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "serverComponent": "server_component", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, server_component, **kwargs):
        self._dirty_mask = 0
        self.server_component = server_component
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareExcludeServerComponent", parent_mo_or_dn, **kwargs)

