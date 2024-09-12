"""This module contains the general information for FirmwareComponentSpec ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareComponentSpecConsts():
    EXCLUDE_BY_DEFAULT_FALSE = "false"
    EXCLUDE_BY_DEFAULT_NO = "no"
    EXCLUDE_BY_DEFAULT_TRUE = "true"
    EXCLUDE_BY_DEFAULT_YES = "yes"
    TYPE_ADAPTOR = "adaptor"
    TYPE_BLADE_BIOS = "blade-bios"
    TYPE_BLADE_CONTROLLER = "blade-controller"
    TYPE_BOARD_CONTROLLER = "board-controller"
    TYPE_CPLD = "cpld"
    TYPE_FLEXFLASH_CONTROLLER = "flexflash-controller"
    TYPE_GRAPHICS_CARD = "graphics-card"
    TYPE_HOST_HBA = "host-hba"
    TYPE_HOST_HBA_OPTIONROM = "host-hba-optionrom"
    TYPE_HOST_NIC = "host-nic"
    TYPE_HOST_NIC_OPTIONROM = "host-nic-optionrom"
    TYPE_INTEL_AMC = "intel-amc"
    TYPE_LOCAL_DISK = "local-disk"
    TYPE_NVME_MSWITCH = "nvme-mswitch"
    TYPE_PERSISTENT_MEMORY_DIMM = "persistent-memory-dimm"
    TYPE_PLX_SWITCH = "plx-switch"
    TYPE_PSU = "psu"
    TYPE_RETIMER = "retimer"
    TYPE_SAS_EXP_REG_FW = "sas-exp-reg-fw"
    TYPE_SAS_EXPANDER = "sas-expander"
    TYPE_STORAGE_CONTROLLER = "storage-controller"
    TYPE_STORAGE_CONTROLLER_ONBOARD_DEVICE = "storage-controller-onboard-device"
    TYPE_STORAGE_CONTROLLER_ONBOARD_DEVICE_CPLD = "storage-controller-onboard-device-cpld"
    TYPE_STORAGE_CONTROLLER_ONBOARD_DEVICE_PSOC = "storage-controller-onboard-device-psoc"
    TYPE_STORAGE_DEV_BRIDGE = "storage-dev-bridge"
    TYPE_UBM = "ubm"
    TYPE_UNSPECIFIED = "unspecified"


class FirmwareComponentSpec(ManagedObject):
    """This is FirmwareComponentSpec class."""

    consts = FirmwareComponentSpecConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("FirmwareComponentSpec", "firmwareComponentSpec", "component-spec-[type]", VersionMeta.Version141a, "InputOutput", 0x1f, [], [""], ['firmwareBundleTypeCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "exclude_by_default": MoPropertyMeta("exclude_by_default", "excludeByDefault", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["adaptor", "blade-bios", "blade-controller", "board-controller", "cpld", "flexflash-controller", "graphics-card", "host-hba", "host-hba-optionrom", "host-nic", "host-nic-optionrom", "intel-amc", "local-disk", "nvme-mswitch", "persistent-memory-dimm", "plx-switch", "psu", "retimer", "sas-exp-reg-fw", "sas-expander", "storage-controller", "storage-controller-onboard-device", "storage-controller-onboard-device-cpld", "storage-controller-onboard-device-psoc", "storage-dev-bridge", "ubm", "unspecified"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "excludeByDefault": "exclude_by_default", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.exclude_by_default = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareComponentSpec", parent_mo_or_dn, **kwargs)

