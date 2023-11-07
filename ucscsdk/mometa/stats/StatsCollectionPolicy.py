"""This module contains the general information for StatsCollectionPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StatsCollectionPolicyConsts():
    COLLECTION_INTERVAL_1MINUTE = "1minute"
    COLLECTION_INTERVAL_2MINUTES = "2minutes"
    COLLECTION_INTERVAL_30SECONDS = "30seconds"
    COLLECTION_INTERVAL_5MINUTES = "5minutes"
    NAME_ADAPTER = "adapter"
    NAME_CHASSIS = "chassis"
    NAME_FEX = "fex"
    NAME_HOST = "host"
    NAME_PORT = "port"
    NAME_SERVER = "server"
    NAME_UNKNOWN = "unknown"
    REPORTING_INTERVAL_15MINUTES = "15minutes"
    REPORTING_INTERVAL_2HOURS = "2hours"
    REPORTING_INTERVAL_2MINUTES = "2minutes"
    REPORTING_INTERVAL_30MINUTES = "30minutes"
    REPORTING_INTERVAL_4HOURS = "4hours"
    REPORTING_INTERVAL_60MINUTES = "60minutes"
    REPORTING_INTERVAL_8HOURS = "8hours"


class StatsCollectionPolicy(ManagedObject):
    """This is StatsCollectionPolicy class."""

    consts = StatsCollectionPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("StatsCollectionPolicy", "statsCollectionPolicy", "coll-policy-[name]", VersionMeta.Version101a, "InputOutput", 0xff, [], ["admin", "operations"], ['statsHolder'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "collection_interval": MoPropertyMeta("collection_interval", "collectionInterval", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["1minute", "2minutes", "30seconds", "5minutes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ushort", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x8, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["adapter", "chassis", "fex", "host", "port", "server", "unknown"], []), 
        "reporting_interval": MoPropertyMeta("reporting_interval", "reportingInterval", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["15minutes", "2hours", "2minutes", "30minutes", "4hours", "60minutes", "8hours"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "collectionInterval": "collection_interval", 
        "dn": "dn", 
        "id": "id", 
        "name": "name", 
        "reportingInterval": "reporting_interval", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.collection_interval = None
        self.id = None
        self.reporting_interval = None
        self.status = None

        ManagedObject.__init__(self, "StatsCollectionPolicy", parent_mo_or_dn, **kwargs)

