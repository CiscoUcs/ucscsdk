"""This module contains the general information for MgmtConnection ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtConnectionConsts():
    ACK_ACKNOWLEDGED = "acknowledged"
    ACK_UN_INITIALIZED = "un-initialized"
    ACK_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    OPER_STATE_ACKNOWLEDGED = "acknowledged"
    OPER_STATE_UN_INITIALIZED = "un-initialized"
    OPER_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    TYPE_SHARED_LOM = "shared-lom"
    TYPE_SIDEBAND = "sideband"
    TYPE_UNSPECIFIED = "unspecified"


class MgmtConnection(ManagedObject):
    """This is MgmtConnection class."""

    consts = MgmtConnectionConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("MgmtConnection", "mgmtConnection", "mgmt-connection-[type]", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["admin"], ['mgmtController'], [], ["Get", "Set"])

    prop_meta = {
        "ack": MoPropertyMeta("ack", "ack", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["acknowledged", "un-initialized", "unsupported-connectivity"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["acknowledged", "un-initialized", "unsupported-connectivity"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x20, None, None, None, ["shared-lom", "sideband", "unspecified"], []), 
    }

    prop_map = {
        "ack": "ack", 
        "childAction": "child_action", 
        "dn": "dn", 
        "operState": "oper_state", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.ack = None
        self.child_action = None
        self.oper_state = None
        self.status = None

        ManagedObject.__init__(self, "MgmtConnection", parent_mo_or_dn, **kwargs)

