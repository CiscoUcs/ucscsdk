"""This module contains the general information for FirmwareRunning ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareRunningConsts():
    DEPLOYMENT_BACKUP = "backup"
    DEPLOYMENT_BOOT_LOADER = "boot-loader"
    DEPLOYMENT_KERNEL = "kernel"
    DEPLOYMENT_PROVIDER = "provider"
    DEPLOYMENT_SERVICE_PACK = "service-pack"
    DEPLOYMENT_SYSTEM = "system"
    DEPLOYMENT_UNSPECIFIED = "unspecified"
    TYPE_ADAPTOR = "adaptor"
    TYPE_BLADE_BIOS = "blade-bios"
    TYPE_BLADE_CONTROLLER = "blade-controller"
    TYPE_BOARD_CONTROLLER = "board-controller"
    TYPE_CATALOG = "catalog"
    TYPE_CHASSIS_BOARD_CONTROLLER = "chassis-board-controller"
    TYPE_CMC = "cmc"
    TYPE_CORE = "core"
    TYPE_CPLD = "cpld"
    TYPE_DEBUG_PLUG_IN = "debug-plug-in"
    TYPE_DIAG = "diag"
    TYPE_FEX = "fex"
    TYPE_FI_SERVICE_PACK = "fi-service-pack"
    TYPE_FLEXFLASH_CONTROLLER = "flexflash-controller"
    TYPE_GRAPHICS_CARD = "graphics-card"
    TYPE_HOST_HBA = "host-hba"
    TYPE_HOST_HBA_OPTIONROM = "host-hba-optionrom"
    TYPE_HOST_NIC = "host-nic"
    TYPE_HOST_NIC_OPTIONROM = "host-nic-optionrom"
    TYPE_IDENTIFIER_MGR = "identifier-mgr"
    TYPE_INTEL_AMC = "intel-amc"
    TYPE_IOCARD = "iocard"
    TYPE_LOCAL_DISK = "local-disk"
    TYPE_MGMT_EXT = "mgmt-ext"
    TYPE_MGMT_SERVICE_PACK = "mgmt-service-pack"
    TYPE_NVME_MSWITCH = "nvme-mswitch"
    TYPE_OPERATION_MGR = "operation-mgr"
    TYPE_PERSISTENT_MEMORY_DIMM = "persistent-memory-dimm"
    TYPE_PLX_SWITCH = "plx-switch"
    TYPE_POLICY_MGR = "policy-mgr"
    TYPE_PROVIDER = "provider"
    TYPE_PSU = "psu"
    TYPE_RESOURCE_AGGR = "resource-aggr"
    TYPE_RETIMER = "retimer"
    TYPE_SAS_EXP_REG_FW = "sas-exp-reg-fw"
    TYPE_SAS_EXPANDER = "sas-expander"
    TYPE_SERVICE_REG = "service-reg"
    TYPE_STATS_MGR = "stats-mgr"
    TYPE_STORAGE_BROKER = "storage-broker"
    TYPE_STORAGE_CONTROLLER = "storage-controller"
    TYPE_STORAGE_CONTROLLER_ONBOARD_DEVICE = "storage-controller-onboard-device"
    TYPE_STORAGE_CONTROLLER_ONBOARD_DEVICE_CPLD = "storage-controller-onboard-device-cpld"
    TYPE_STORAGE_CONTROLLER_ONBOARD_DEVICE_PSOC = "storage-controller-onboard-device-psoc"
    TYPE_STORAGE_DEV_BRIDGE = "storage-dev-bridge"
    TYPE_SWITCH = "switch"
    TYPE_SWITCH_KERNEL = "switch-kernel"
    TYPE_SWITCH_SOFTWARE = "switch-software"
    TYPE_SYSTEM = "system"
    TYPE_UBM = "ubm"
    TYPE_UNSPECIFIED = "unspecified"


class FirmwareRunning(ManagedObject):
    """This is FirmwareRunning class."""

    consts = FirmwareRunningConsts()
    naming_props = set(['deployment'])

    mo_meta = MoMeta("FirmwareRunning", "firmwareRunning", "fw-[deployment]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["read-only"], ['biosUnit', 'equipmentPsu', 'graphicsCard', 'mgmtController', 'osController', 'storageController', 'storageFlexFlashController', 'storageLocalDisk', 'storageOnboardDevice', 'storageSasExpander'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "deployment": MoPropertyMeta("deployment", "deployment", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x2, None, None, None, ["backup", "boot-loader", "kernel", "provider", "service-pack", "system", "unspecified"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "package_version": MoPropertyMeta("package_version", "packageVersion", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "blade-bios", "blade-controller", "board-controller", "catalog", "chassis-board-controller", "cmc", "core", "cpld", "debug-plug-in", "diag", "fex", "fi-service-pack", "flexflash-controller", "graphics-card", "host-hba", "host-hba-optionrom", "host-nic", "host-nic-optionrom", "identifier-mgr", "intel-amc", "iocard", "local-disk", "mgmt-ext", "mgmt-service-pack", "nvme-mswitch", "operation-mgr", "persistent-memory-dimm", "plx-switch", "policy-mgr", "provider", "psu", "resource-aggr", "retimer", "sas-exp-reg-fw", "sas-expander", "service-reg", "stats-mgr", "storage-broker", "storage-controller", "storage-controller-onboard-device", "storage-controller-onboard-device-cpld", "storage-controller-onboard-device-psoc", "storage-dev-bridge", "switch", "switch-kernel", "switch-software", "system", "ubm", "unspecified"], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "deployment": "deployment", 
        "dn": "dn", 
        "packageVersion": "package_version", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, deployment, **kwargs):
        self._dirty_mask = 0
        self.deployment = deployment
        self.child_action = None
        self.package_version = None
        self.status = None
        self.type = None
        self.version = None

        ManagedObject.__init__(self, "FirmwareRunning", parent_mo_or_dn, **kwargs)

