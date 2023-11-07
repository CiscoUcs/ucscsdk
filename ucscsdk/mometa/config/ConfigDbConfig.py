"""This module contains the general information for ConfigDbConfig ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigDbConfigConsts():
    DB_ERROR_FALSE = "false"
    DB_ERROR_NO = "no"
    DB_ERROR_TRUE = "true"
    DB_ERROR_YES = "yes"
    TYPE_MSSQL = "mssql"
    TYPE_ORACLE = "oracle"
    TYPE_POSTGRES = "postgres"
    TYPE_UNKNOWN = "unknown"


class ConfigDbConfig(ManagedObject):
    """This is ConfigDbConfig class."""

    consts = ConfigDbConfigConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigDbConfig", "configDbConfig", "dbconfig", VersionMeta.Version111b, "InputOutput", 0x7ff, [], ["admin"], ['topSystem'], ['faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "database": MoPropertyMeta("database", "database", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "db_error": MoPropertyMeta("db_error", "dbError", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x8, 1, 255, None, [], []), 
        "instance": MoPropertyMeta("instance", "instance", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, 0, 32, None, [], []), 
        "last_db_status": MoPropertyMeta("last_db_status", "lastDbStatus", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, None, 0, 999, None, [], []), 
        "port": MoPropertyMeta("port", "port", "ushort", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x40, 0, 64, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["mssql", "oracle", "postgres", "unknown"], []), 
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "database": "database", 
        "dbError": "db_error", 
        "dn": "dn", 
        "hostname": "hostname", 
        "instance": "instance", 
        "lastDbStatus": "last_db_status", 
        "port": "port", 
        "pwd": "pwd", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.database = None
        self.db_error = None
        self.hostname = None
        self.instance = None
        self.last_db_status = None
        self.port = None
        self.pwd = None
        self.status = None
        self.type = None
        self.user = None

        ManagedObject.__init__(self, "ConfigDbConfig", parent_mo_or_dn, **kwargs)

