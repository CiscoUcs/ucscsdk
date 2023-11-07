"""This module contains the general information for ExtmgmtMiiStatus ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ExtmgmtMiiStatusConsts():
    pass


class ExtmgmtMiiStatus(ManagedObject):
    """This is ExtmgmtMiiStatus class."""

    consts = ExtmgmtMiiStatusConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtmgmtMiiStatus", "extmgmtMiiStatus", "mii-status-policy", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin", "domain-group-management", "ext-lan-config"], ['extmgmtIfMonPolicy'], [], ["Add", "Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "max_retry_count": MoPropertyMeta("max_retry_count", "maxRetryCount", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-3"]), 
        "retry_interval": MoPropertyMeta("retry_interval", "retryInterval", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["3-10"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maxRetryCount": "max_retry_count", 
        "retryInterval": "retry_interval", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.max_retry_count = None
        self.retry_interval = None
        self.status = None

        ManagedObject.__init__(self, "ExtmgmtMiiStatus", parent_mo_or_dn, **kwargs)

