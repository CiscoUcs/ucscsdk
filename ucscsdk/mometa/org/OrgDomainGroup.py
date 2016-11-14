"""This module contains the general information for OrgDomainGroup ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class OrgDomainGroupConsts():
    LEVEL_1 = "1"
    LEVEL_2 = "2"
    LEVEL_3 = "3"
    LEVEL_4 = "4"
    LEVEL_5 = "5"
    LEVEL_ROOT = "root"


class OrgDomainGroup(ManagedObject):
    """This is OrgDomainGroup class."""

    consts = OrgDomainGroupConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("OrgDomainGroup", "orgDomainGroup", "domaingroup-[name]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin", "read-only"], [u'orgDomainGroup'], [u'aaaAuthRealm', u'aaaEpAuthProfile', u'aaaLdapEp', u'aaaLocale', u'aaaPwdProfile', u'aaaRadiusEp', u'aaaRole', u'aaaTacacsPlusEp', u'aaaUser', u'callhomeEp', u'commCimxml', u'commCoreFile', u'commDateTime', u'commDns', u'commEvtChannel', u'commHttp', u'commHttps', u'commShellSvcLimits', u'commSmashCLP', u'commSnmp', u'commSsh', u'commSyslog', u'commTelnet', u'commWebChannel', u'commWebSvcLimits', u'commWsman', u'commXmlClConnPolicy', u'computeAutoconfigPolicy', u'computeBladeDiscPolicy', u'computeBladeInheritPolicy', u'computeChassisConnPolicy', u'computeChassisDiscPolicy', u'computePsuPolicy', u'computeServerDiscPolicy', u'computeServerMgmtPolicy', u'extmgmtIfMonPolicy', u'fabricEp', u'fabricEthLinkProfile', u'fabricLacpPolicy', u'fabricLanCloudPolicy', u'fabricUdldLinkPolicy', u'faultPolicy', u'firmwareAutoSyncPolicy', u'firmwareCatalogPack', u'firmwareCatalogPackConfig', u'firmwareChassisPack', u'firmwareComputeHostPack', u'firmwareComputeMgmtPack', u'firmwareComputeStoragePack', u'firmwareConnectionPolicy', u'firmwareDownloadPolicy', u'firmwareInfraPack', u'firmwareInfraPackConfig', u'firmwareInfraPolicy', u'firmwarePolicy', u'flowctrlDefinition', u'hcDownloadPolicy', u'lsmaintMaintPolicy', u'mgmtBackupPolicy', u'mgmtCfgExportPolicy', u'nfsRepositorySpecPolicy', u'nwctrlDefinition', u'orgDomainGroup', u'pkiTP', u'policyIdentifierPolicy', u'policyLogProfile', u'powerEp', u'powerMgmtPolicy', u'sysdebugAutoCoreFileExportTarget', u'sysdebugMEpLogPolicy', u'topInfoSyncPolicy', u'trigMeta', u'trigPendingAckCount', u'trigSched', u'trigTest'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "level": MoPropertyMeta("level", "level", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4", "5", "root"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "level": "level", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.flt_aggr = None
        self.level = None
        self.status = None

        ManagedObject.__init__(self, "OrgDomainGroup", parent_mo_or_dn, **kwargs)

