"""This module contains the general information for BiosVProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVProfileConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    REBOOT_ON_UPDATE_FALSE = "false"
    REBOOT_ON_UPDATE_NO = "no"
    REBOOT_ON_UPDATE_TRUE = "true"
    REBOOT_ON_UPDATE_YES = "yes"


class BiosVProfile(ManagedObject):
    """This is BiosVProfile class."""

    consts = BiosVProfileConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("BiosVProfile", "biosVProfile", "bios-prof-[name]", VersionMeta.Version111a, "InputOutput", 0x7f, [], ["read-only"], ['orgOrg'], ['biosTokenFeatureGroup', 'biosVfACPI10Support', 'biosVfASPMSupport', 'biosVfAllUSBDevices', 'biosVfAltitude', 'biosVfAssertNMIOnPERR', 'biosVfAssertNMIOnSERR', 'biosVfBootOptionRetry', 'biosVfCPUHardwarePowerManagement', 'biosVfCPUPerformance', 'biosVfCPUPowerManagement', 'biosVfConsistentDeviceNameControl', 'biosVfConsoleRedirection', 'biosVfCoreMultiProcessing', 'biosVfDDR3VoltageSelection', 'biosVfDRAMClockThrottling', 'biosVfDirectCacheAccess', 'biosVfDramRefreshRate', 'biosVfEnergyPerformanceTuning', 'biosVfEnhancedIntelSpeedStepTech', 'biosVfEnhancedPowerCappingSupport', 'biosVfExecuteDisableBit', 'biosVfFRB2Timer', 'biosVfFrequencyFloorOverride', 'biosVfFrontPanelLockout', 'biosVfIOEMezz1OptionROM', 'biosVfIOENVMe1OptionROM', 'biosVfIOENVMe2OptionROM', 'biosVfIOESlot1OptionROM', 'biosVfIOESlot2OptionROM', 'biosVfIntegratedGraphics', 'biosVfIntegratedGraphicsApertureSize', 'biosVfIntelEntrySASRAIDModule', 'biosVfIntelHyperThreadingTech', 'biosVfIntelTrustedExecutionTechnology', 'biosVfIntelTurboBoostTech', 'biosVfIntelVTForDirectedIO', 'biosVfIntelVirtualizationTechnology', 'biosVfInterleaveConfiguration', 'biosVfLocalX2Apic', 'biosVfLvDIMMSupport', 'biosVfMaxVariableMTRRSetting', 'biosVfMaximumMemoryBelow4GB', 'biosVfMemoryMappedIOAbove4GB', 'biosVfMirroringMode', 'biosVfNUMAOptimized', 'biosVfOSBootWatchdogTimer', 'biosVfOSBootWatchdogTimerPolicy', 'biosVfOSBootWatchdogTimerTimeout', 'biosVfOnboardGraphics', 'biosVfOnboardSATAController', 'biosVfOnboardStorage', 'biosVfOptionROMEnable', 'biosVfOptionROMLoad', 'biosVfOutOfBandManagement', 'biosVfPCHSATAMode', 'biosVfPCILOMPortsConfiguration', 'biosVfPCIROMCLP', 'biosVfPCISlotLinkSpeed', 'biosVfPCISlotOptionROMEnable', 'biosVfPOSTErrorPause', 'biosVfPSTATECoordination', 'biosVfPackageCStateLimit', 'biosVfProcessorC1E', 'biosVfProcessorC3Report', 'biosVfProcessorC6Report', 'biosVfProcessorC7Report', 'biosVfProcessorCMCI', 'biosVfProcessorCState', 'biosVfProcessorEnergyConfiguration', 'biosVfProcessorPrefetchConfig', 'biosVfQPILinkFrequencySelect', 'biosVfQPISnoopMode', 'biosVfQuietBoot', 'biosVfRedirectionAfterBIOSPOST', 'biosVfResumeOnACPowerLoss', 'biosVfSBMezz1OptionROM', 'biosVfSBNVMe1OptionROM', 'biosVfSIOC1OptionROM', 'biosVfSIOC2OptionROM', 'biosVfScrubPolicies', 'biosVfSelectMemoryRASConfiguration', 'biosVfSerialPortAEnable', 'biosVfSparingMode', 'biosVfSriovConfig', 'biosVfTPMPendingOperation', 'biosVfTPMSupport', 'biosVfTrustedPlatformModule', 'biosVfUCSMBootModeControl', 'biosVfUCSMBootOrderRuleControl', 'biosVfUEFIOSUseLegacyVideo', 'biosVfUSBBootConfig', 'biosVfUSBConfiguration', 'biosVfUSBFrontPanelAccessLock', 'biosVfUSBPortConfiguration', 'biosVfUSBSystemIdlePowerOptimizingSetting', 'biosVfVGAPriority', 'biosVfWorkloadConfiguration'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rebootOnUpdate": "reboot_on_update", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.reboot_on_update = None
        self.status = None

        ManagedObject.__init__(self, "BiosVProfile", parent_mo_or_dn, **kwargs)

