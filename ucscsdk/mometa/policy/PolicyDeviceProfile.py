"""This module contains the general information for PolicyDeviceProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyDeviceProfileConsts():
    MIGRATE_ADMIN_SETTING_DISABLED = "disabled"
    MIGRATE_ADMIN_SETTING_ENABLED = "enabled"
    INT_ID_NONE = "none"


class PolicyDeviceProfile(ManagedObject):
    """This is PolicyDeviceProfile class."""

    consts = PolicyDeviceProfileConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("PolicyDeviceProfile", "policyDeviceProfile", "deviceprofile-[name]", VersionMeta.Version112a, "InputOutput", 0x7f, [], ["admin"], ['orgOrg'], ['aaaAuthRealm', 'aaaLdapEp', 'aaaLocale', 'aaaPwdProfile', 'aaaRadiusEp', 'aaaRole', 'aaaTacacsPlusEp', 'aaaUser', 'callhomeEp', 'commCoreFile', 'commDateTime', 'commDns', 'commHttp', 'commHttps', 'commShellSvcLimits', 'commSnmp', 'commSsh', 'commSyslog', 'commTelnet', 'commWebSvcLimits', 'extmgmtIfMonPolicy', 'faultPolicy', 'mgmtBackupPolicy', 'mgmtCfgExportPolicy', 'pkiEp', 'smartlicenseEp', 'sysdebugAutoCoreFileExportTarget'], ["Get", "Set"])

    prop_meta = {
        "migrate_admin_setting": MoPropertyMeta("migrate_admin_setting", "MigrateAdminSetting", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "MigrateAdminSetting": "migrate_admin_setting", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.migrate_admin_setting = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.status = None

        ManagedObject.__init__(self, "PolicyDeviceProfile", parent_mo_or_dn, **kwargs)

