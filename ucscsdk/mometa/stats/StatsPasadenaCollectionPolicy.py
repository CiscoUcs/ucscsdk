"""This module contains the general information for StatsPasadenaCollectionPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StatsPasadenaCollectionPolicyConsts():
    COLLECTION_INTERVAL_10MIN = "10min"
    COLLECTION_INTERVAL_15MIN = "15min"
    COLLECTION_INTERVAL_1MIN = "1min"
    COLLECTION_INTERVAL_2MIN = "2min"
    COLLECTION_INTERVAL_30MIN = "30min"
    COLLECTION_INTERVAL_5MIN = "5min"
    COLLECTION_INTERVAL_NEVER = "never"
    DAILY_RECORDS_1YEAR = "1year"
    DAILY_RECORDS_2WEEKS = "2weeks"
    DAILY_RECORDS_3MONTHS = "3months"
    DAILY_RECORDS_6MONTHS = "6months"
    DAILY_RECORDS_NONE = "none"
    DAILY_RECORDS_UNLIMITED = "unlimited"
    DOMAIN_UNKNOWN = "unknown"
    HOURLY_RECORDS_1WEEK = "1week"
    HOURLY_RECORDS_2WEEKS = "2weeks"
    HOURLY_RECORDS_4WEEKS = "4weeks"
    HOURLY_RECORDS_8WEEKS = "8weeks"
    HOURLY_RECORDS_NONE = "none"
    HOURLY_RECORDS_UNLIMITED = "unlimited"
    REALTIME_RECORDS_1WEEK = "1week"
    REALTIME_RECORDS_2WEEKS = "2weeks"
    REALTIME_RECORDS_4WEEKS = "4weeks"
    REALTIME_RECORDS_8WEEKS = "8weeks"
    REALTIME_RECORDS_NONE = "none"
    REALTIME_RECORDS_UNLIMITED = "unlimited"
    WEEKLY_RECORDS_1YEAR = "1year"
    WEEKLY_RECORDS_2WEEKS = "2weeks"
    WEEKLY_RECORDS_6MONTHS = "6months"
    WEEKLY_RECORDS_NONE = "none"
    WEEKLY_RECORDS_UNLIMITED = "unlimited"


class StatsPasadenaCollectionPolicy(ManagedObject):
    """This is StatsPasadenaCollectionPolicy class."""

    consts = StatsPasadenaCollectionPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("StatsPasadenaCollectionPolicy", "statsPasadenaCollectionPolicy", "pasadena-coll-policy", VersionMeta.Version111b, "InputOutput", 0x7ff, [], ["admin", "operations"], ['statsHolder'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "collection_interval": MoPropertyMeta("collection_interval", "collectionInterval", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["10min", "15min", "1min", "2min", "30min", "5min", "never"], []), 
        "daily_records": MoPropertyMeta("daily_records", "dailyRecords", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["1year", "2weeks", "3months", "6months", "none", "unlimited"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "domain": MoPropertyMeta("domain", "domain", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["unknown"], []), 
        "hourly_records": MoPropertyMeta("hourly_records", "hourlyRecords", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["1week", "2weeks", "4weeks", "8weeks", "none", "unlimited"], []), 
        "id": MoPropertyMeta("id", "id", "ushort", VersionMeta.Version111b, MoPropertyMeta.CREATE_ONLY, 0x40, None, None, None, [], []), 
        "realtime_records": MoPropertyMeta("realtime_records", "realtimeRecords", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["1week", "2weeks", "4weeks", "8weeks", "none", "unlimited"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "weekly_records": MoPropertyMeta("weekly_records", "weeklyRecords", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["1year", "2weeks", "6months", "none", "unlimited"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "collectionInterval": "collection_interval", 
        "dailyRecords": "daily_records", 
        "dn": "dn", 
        "domain": "domain", 
        "hourlyRecords": "hourly_records", 
        "id": "id", 
        "realtimeRecords": "realtime_records", 
        "rn": "rn", 
        "status": "status", 
        "weeklyRecords": "weekly_records", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.collection_interval = None
        self.daily_records = None
        self.domain = None
        self.hourly_records = None
        self.id = None
        self.realtime_records = None
        self.status = None
        self.weekly_records = None

        ManagedObject.__init__(self, "StatsPasadenaCollectionPolicy", parent_mo_or_dn, **kwargs)

