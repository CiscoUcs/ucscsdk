"""This module contains the general information for EquipmentPciDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentPciDefConsts():
    DEVICE_TYPE_BROADCOM57712_NIC = "Broadcom57712Nic"
    DEVICE_TYPE_BROADCOM_NIC = "BroadcomNic"
    DEVICE_TYPE_EMULEX_NIC = "EmulexNic"
    DEVICE_TYPE_FUSION_HBA = "FusionHba"
    DEVICE_TYPE_INTEL_ICH10_RHBA = "IntelICH10RHba"
    DEVICE_TYPE_INTEL_NIC = "IntelNic"
    DEVICE_TYPE_LSIMEGA_RAID3008 = "LSIMegaRaid3008"
    DEVICE_TYPE_LODI_HBA = "LodiHba"
    DEVICE_TYPE_LSI1064_EHBA = "Lsi1064EHba"
    DEVICE_TYPE_LSI1068_EHBA = "Lsi1068EHba"
    DEVICE_TYPE_LSI_EXTERNAL_MEGA_RAID_HBA = "LsiExternalMegaRaidHba"
    DEVICE_TYPE_LSI_MEGA_RAID_HBA = "LsiMegaRaidHba"
    DEVICE_TYPE_LSI_WALNUT_CREEK_HBA = "LsiWalnutCreekHba"
    DEVICE_TYPE_MAX_COUNT = "MaxCount"
    DEVICE_TYPE_MENLO_EMULEX_HBA = "MenloEmulexHba"
    DEVICE_TYPE_MENLO_QLOGIC_FC_HBA = "MenloQlogicFcHba"
    DEVICE_TYPE_MEZZ_DUBLIN_QLOGIC_FC_HBA = "MezzDublinQlogicFcHba"
    DEVICE_TYPE_MEZZ_SCHULZ_QLOGIC_FC_HBA = "MezzSchulzQlogicFcHba"
    DEVICE_TYPE_MEZZ_TIGER_SHARK_HBA = "MezzTigerSharkHba"
    DEVICE_TYPE_NVME_HBA = "NvmeHba"
    DEVICE_TYPE_PCI_DUBLIN_QLOGIC_FC_HBA = "PciDublinQlogicFcHba"
    DEVICE_TYPE_PCI_EVEREST_NIC = "PciEverestNic"
    DEVICE_TYPE_PCI_INTEL_X520_NIC = "PciIntelX520Nic"
    DEVICE_TYPE_PCI_MPCISCO_NIC = "PciMPCiscoNic"
    DEVICE_TYPE_PCI_NIANTIC_NIC = "PciNianticNic"
    DEVICE_TYPE_PCI_QLOGIC8362_FC_HBA = "PciQlogic8362FcHba"
    DEVICE_TYPE_PCI_SCHULZ_QLOGIC_FC_HBA = "PciSchulzQlogicFcHba"
    DEVICE_TYPE_PCI_TIGER_SHARK_HBA = "PciTigerSharkHba"
    DEVICE_TYPE_QLOGIC_NIC = "QlogicNic"
    DEVICE_TYPE_SATA_HBA = "SataHba"
    DEVICE_TYPE_UNKNOWN = "Unknown"
    DEVICE_TYPE_WELLSBURG_HBA = "WellsburgHba"


class EquipmentPciDef(ManagedObject):
    """This is EquipmentPciDef class."""

    consts = EquipmentPciDefConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("EquipmentPciDef", "equipmentPciDef", "pci-[name]", VersionMeta.Version151a, "InputOutput", 0x1f, [], [""], ['equipmentLocalDiskControllerCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "device": MoPropertyMeta("device", "device", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "device_type": MoPropertyMeta("device_type", "deviceType", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Broadcom57712Nic", "BroadcomNic", "EmulexNic", "FusionHba", "IntelICH10RHba", "IntelNic", "LSIMegaRaid3008", "LodiHba", "Lsi1064EHba", "Lsi1068EHba", "LsiExternalMegaRaidHba", "LsiMegaRaidHba", "LsiWalnutCreekHba", "MaxCount", "MenloEmulexHba", "MenloQlogicFcHba", "MezzDublinQlogicFcHba", "MezzSchulzQlogicFcHba", "MezzTigerSharkHba", "NvmeHba", "PciDublinQlogicFcHba", "PciEverestNic", "PciIntelX520Nic", "PciMPCiscoNic", "PciNianticNic", "PciQlogic8362FcHba", "PciSchulzQlogicFcHba", "PciTigerSharkHba", "QlogicNic", "SataHba", "Unknown", "WellsburgHba"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, 1, 512, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subdevice": MoPropertyMeta("subdevice", "subdevice", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "subvendor": MoPropertyMeta("subvendor", "subvendor", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "device": "device", 
        "deviceType": "device_type", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "subdevice": "subdevice", 
        "subvendor": "subvendor", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.device = None
        self.device_type = None
        self.status = None
        self.subdevice = None
        self.subvendor = None
        self.vendor = None

        ManagedObject.__init__(self, "EquipmentPciDef", parent_mo_or_dn, **kwargs)

