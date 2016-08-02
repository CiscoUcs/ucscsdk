"""This module contains the general information for MgmtCmcSecureBoot ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class MgmtCmcSecureBootConsts():
    ADMIN_STATE_DISABLE = "disable"
    ADMIN_STATE_ENABLE = "enable"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_ENABLED = "enabled"
    OPER_STATE_ENABLING = "enabling"
    OPER_STATE_UNSUPPORTED = "unsupported"


class MgmtCmcSecureBoot(ManagedObject):
    """This is MgmtCmcSecureBoot class."""

    consts = MgmtCmcSecureBootConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtCmcSecureBoot", "mgmtCmcSecureBoot", "mgmt-cmc-secure-boot", None, "InputOutput", 0x1f, [], ["admin", "ls-compute"], [u'mgmtController'], [u'mgmtCmcSecureBootOperation'], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", None, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disable", "enable"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled", "enabling", "unsupported"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "operState": "oper_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.oper_state = None
        self.status = None

        ManagedObject.__init__(self, "MgmtCmcSecureBoot", parent_mo_or_dn, **kwargs)

