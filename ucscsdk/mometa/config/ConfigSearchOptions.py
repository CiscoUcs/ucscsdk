"""This module contains the general information for ConfigSearchOptions ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigSearchOptionsConsts():
    OBJECT_TYPE_AAA_EP_AUTH_PROFILE = "aaaEpAuthProfile"
    OBJECT_TYPE_ADAPTOR_HOST_ETH_IF_PROFILE = "adaptorHostEthIfProfile"
    OBJECT_TYPE_ADAPTOR_HOST_FC_IF_PROFILE = "adaptorHostFcIfProfile"
    OBJECT_TYPE_ADAPTOR_HOST_ISCSI_IF_PROFILE = "adaptorHostIscsiIfProfile"
    OBJECT_TYPE_BIOS_VPROFILE = "biosVProfile"
    OBJECT_TYPE_CALLHOME_EP = "callhomeEp"
    OBJECT_TYPE_COMM_CIMXML = "commCimxml"
    OBJECT_TYPE_COMM_DATE_TIME = "commDateTime"
    OBJECT_TYPE_COMM_DNS = "commDns"
    OBJECT_TYPE_COMM_HTTP = "commHttp"
    OBJECT_TYPE_COMM_SHELL_SVC_LIMITS = "commShellSvcLimits"
    OBJECT_TYPE_COMM_SNMP = "commSnmp"
    OBJECT_TYPE_COMM_SYSLOG = "commSyslog"
    OBJECT_TYPE_COMM_TELNET = "commTelnet"
    OBJECT_TYPE_COMM_WEB_SVC_LIMITS = "commWebSvcLimits"
    OBJECT_TYPE_COMPUTE_GRAPHICS_CARD_POLICY = "computeGraphicsCardPolicy"
    OBJECT_TYPE_COMPUTE_MODULAR_CHASSIS_FAN_POLICY = "computeModularChassisFanPolicy"
    OBJECT_TYPE_COMPUTE_POOLING_POLICY = "computePoolingPolicy"
    OBJECT_TYPE_COMPUTE_POWER_EXTENDED_POLICY = "computePowerExtendedPolicy"
    OBJECT_TYPE_COMPUTE_POWER_SAVE_POLICY = "computePowerSavePolicy"
    OBJECT_TYPE_COMPUTE_POWER_SYNC_POLICY = "computePowerSyncPolicy"
    OBJECT_TYPE_COMPUTE_PSU_POLICY = "computePsuPolicy"
    OBJECT_TYPE_COMPUTE_QUAL = "computeQual"
    OBJECT_TYPE_COMPUTE_SCRUB_POLICY = "computeScrubPolicy"
    OBJECT_TYPE_CPMAINT_MAINT_POLICY = "cpmaintMaintPolicy"
    OBJECT_TYPE_DIAG_RUN_POLICY = "diagRunPolicy"
    OBJECT_TYPE_EPQOS_DEFINITION = "epqosDefinition"
    OBJECT_TYPE_EQUIPMENT_COMPUTE_CONN_POLICY_NAME = "equipmentComputeConnPolicyName"
    OBJECT_TYPE_EXTMGMT_IF_MON_POLICY = "extmgmtIfMonPolicy"
    OBJECT_TYPE_FABRIC_MULTICAST_POLICY = "fabricMulticastPolicy"
    OBJECT_TYPE_FABRIC_VCON_PROFILE = "fabricVConProfile"
    OBJECT_TYPE_FABRIC_VLAN = "fabricVlan"
    OBJECT_TYPE_FABRIC_VSAN = "fabricVsan"
    OBJECT_TYPE_FAULT_POLICY = "faultPolicy"
    OBJECT_TYPE_FCPOOL_INITIATORS = "fcpoolInitiators"
    OBJECT_TYPE_FIRMWARE_CHASSIS_PACK = "firmwareChassisPack"
    OBJECT_TYPE_FIRMWARE_COMPUTE_HOST_PACK = "firmwareComputeHostPack"
    OBJECT_TYPE_IPPOOL_POOL = "ippoolPool"
    OBJECT_TYPE_IQNPOOL_POOL = "iqnpoolPool"
    OBJECT_TYPE_ISCSI_AUTH_PROFILE = "iscsiAuthProfile"
    OBJECT_TYPE_LS_SERVER = "lsServer"
    OBJECT_TYPE_LSBOOT_POLICY = "lsbootPolicy"
    OBJECT_TYPE_LSMAINT_MAINT_POLICY = "lsmaintMaintPolicy"
    OBJECT_TYPE_LSTORAGE_DISK_GROUP_CONFIG_POLICY = "lstorageDiskGroupConfigPolicy"
    OBJECT_TYPE_LSTORAGE_DISK_ZONING_POLICY = "lstorageDiskZoningPolicy"
    OBJECT_TYPE_LSTORAGE_PROFILE = "lstorageProfile"
    OBJECT_TYPE_MACPOOL_POOL = "macpoolPool"
    OBJECT_TYPE_NWCTRL_DEFINITION = "nwctrlDefinition"
    OBJECT_TYPE_POWER_MGMT_POLICY = "powerMgmtPolicy"
    OBJECT_TYPE_POWER_POLICY = "powerPolicy"
    OBJECT_TYPE_SOL_POLICY = "solPolicy"
    OBJECT_TYPE_STATS_THRESHOLD_POLICY = "statsThresholdPolicy"
    OBJECT_TYPE_STORAGE_CONNECTION_POLICY = "storageConnectionPolicy"
    OBJECT_TYPE_STORAGE_LOCAL_DISK_CONFIG_POLICY = "storageLocalDiskConfigPolicy"
    OBJECT_TYPE_SYSDEBUG_AUTO_CORE_FILE_EXPORT_TARGET = "sysdebugAutoCoreFileExportTarget"
    OBJECT_TYPE_SYSDEBUG_MEP_LOG_POLICY = "sysdebugMEpLogPolicy"
    OBJECT_TYPE_TRIG_SCHED = "trigSched"
    OBJECT_TYPE_UNSPECIFIED = "unspecified"
    OBJECT_TYPE_UUIDPOOL_POOL = "uuidpoolPool"
    OBJECT_TYPE_VNIC_DYNAMIC_CON_POLICY = "vnicDynamicConPolicy"
    OBJECT_TYPE_VNIC_LAN_CONN_POLICY = "vnicLanConnPolicy"
    OBJECT_TYPE_VNIC_LAN_CONN_TEMPL = "vnicLanConnTempl"
    OBJECT_TYPE_VNIC_SAN_CONN_POLICY = "vnicSanConnPolicy"
    OBJECT_TYPE_VNIC_SAN_CONN_TEMPL = "vnicSanConnTempl"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    SEARCH_TYPE_CONTAINS = "contains"
    SEARCH_TYPE_EXACT_MATCH = "exactMatch"
    SEARCH_TYPE_STARTS_WITH = "startsWith"


class ConfigSearchOptions(ManagedObject):
    """This is ConfigSearchOptions class."""

    consts = ConfigSearchOptionsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigSearchOptions", "configSearchOptions", "", VersionMeta.Version112a, "InputOutput", 0xf, [], ["read-only"], [], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "object_type": MoPropertyMeta("object_type", "objectType", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aaaEpAuthProfile", "adaptorHostEthIfProfile", "adaptorHostFcIfProfile", "adaptorHostIscsiIfProfile", "biosVProfile", "callhomeEp", "commCimxml", "commDateTime", "commDns", "commHttp", "commShellSvcLimits", "commSnmp", "commSyslog", "commTelnet", "commWebSvcLimits", "computeGraphicsCardPolicy", "computeModularChassisFanPolicy", "computePoolingPolicy", "computePowerExtendedPolicy", "computePowerSavePolicy", "computePowerSyncPolicy", "computePsuPolicy", "computeQual", "computeScrubPolicy", "cpmaintMaintPolicy", "diagRunPolicy", "epqosDefinition", "equipmentComputeConnPolicyName", "extmgmtIfMonPolicy", "fabricMulticastPolicy", "fabricVConProfile", "fabricVlan", "fabricVsan", "faultPolicy", "fcpoolInitiators", "firmwareChassisPack", "firmwareComputeHostPack", "ippoolPool", "iqnpoolPool", "iscsiAuthProfile", "lsServer", "lsbootPolicy", "lsmaintMaintPolicy", "lstorageDiskGroupConfigPolicy", "lstorageDiskZoningPolicy", "lstorageProfile", "macpoolPool", "nwctrlDefinition", "powerMgmtPolicy", "powerPolicy", "solPolicy", "statsThresholdPolicy", "storageConnectionPolicy", "storageLocalDiskConfigPolicy", "sysdebugAutoCoreFileExportTarget", "sysdebugMEpLogPolicy", "trigSched", "unspecified", "uuidpoolPool", "vnicDynamicConPolicy", "vnicLanConnPolicy", "vnicLanConnTempl", "vnicSanConnPolicy", "vnicSanConnTempl"], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "search_type": MoPropertyMeta("search_type", "searchType", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["contains", "exactMatch", "startsWith"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "objectType": "object_type", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "searchType": "search_type", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.object_type = None
        self.policy_owner = None
        self.search_type = None
        self.status = None

        ManagedObject.__init__(self, "ConfigSearchOptions", parent_mo_or_dn, **kwargs)

