"""This module contains the general information for StatsInventoryMeta ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StatsInventoryMetaConsts():
    SUBSCRIBE_STATUS_OK = "ok"
    SUBSCRIBE_STATUS_PENDING = "pending"


class StatsInventoryMeta(ManagedObject):
    """This is StatsInventoryMeta class."""

    consts = StatsInventoryMetaConsts()
    naming_props = set([])

    mo_meta = MoMeta("StatsInventoryMeta", "statsInventoryMeta", "invMeta", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["admin"], ['extpolClient'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "last_subscribed_ts": MoPropertyMeta("last_subscribed_ts", "lastSubscribedTs", "ulong", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subscribe_status": MoPropertyMeta("subscribe_status", "subscribeStatus", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["ok", "pending"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "lastSubscribedTs": "last_subscribed_ts", 
        "rn": "rn", 
        "status": "status", 
        "subscribeStatus": "subscribe_status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.last_subscribed_ts = None
        self.status = None
        self.subscribe_status = None

        ManagedObject.__init__(self, "StatsInventoryMeta", parent_mo_or_dn, **kwargs)

