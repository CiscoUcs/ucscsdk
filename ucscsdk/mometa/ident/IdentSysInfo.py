"""This module contains the general information for IdentSysInfo ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IdentSysInfoConsts():
    IS_FIRST_SYNC_FALSE = "false"
    IS_FIRST_SYNC_NO = "no"
    IS_FIRST_SYNC_TRUE = "true"
    IS_FIRST_SYNC_YES = "yes"
    IS_SYNC_FALSE = "false"
    IS_SYNC_NO = "no"
    IS_SYNC_TRUE = "true"
    IS_SYNC_YES = "yes"
    IS_SYNC_ALLOWED_FALSE = "false"
    IS_SYNC_ALLOWED_NO = "no"
    IS_SYNC_ALLOWED_TRUE = "true"
    IS_SYNC_ALLOWED_YES = "yes"
    TXN_TYPE_CONF_RENAME = "conf-rename"
    TXN_TYPE_REGULAR = "regular"


class IdentSysInfo(ManagedObject):
    """This is IdentSysInfo class."""

    consts = IdentSysInfoConsts()
    naming_props = set([])

    mo_meta = MoMeta("IdentSysInfo", "identSysInfo", "", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "generation": MoPropertyMeta("generation", "generation", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "is_first_sync": MoPropertyMeta("is_first_sync", "isFirstSync", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_sync": MoPropertyMeta("is_sync", "isSync", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_sync_allowed": MoPropertyMeta("is_sync_allowed", "isSyncAllowed", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "txn_type": MoPropertyMeta("txn_type", "txnType", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conf-rename", "regular"], []), 
        "ucsc_generation": MoPropertyMeta("ucsc_generation", "ucscGeneration", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "generation": "generation", 
        "isFirstSync": "is_first_sync", 
        "isSync": "is_sync", 
        "isSyncAllowed": "is_sync_allowed", 
        "rn": "rn", 
        "status": "status", 
        "txnType": "txn_type", 
        "ucscGeneration": "ucsc_generation", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.generation = None
        self.is_first_sync = None
        self.is_sync = None
        self.is_sync_allowed = None
        self.status = None
        self.txn_type = None
        self.ucsc_generation = None

        ManagedObject.__init__(self, "IdentSysInfo", parent_mo_or_dn, **kwargs)

