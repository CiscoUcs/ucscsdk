"""This module contains the general information for ComputeRemoteOpStatus ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeRemoteOpStatusConsts():
    OP_STATUS_FAIL = "fail"
    OP_STATUS_NOP = "nop"
    OP_STATUS_SUCCESS = "success"
    OP_TYPE_BACKUP = "backup"
    OP_TYPE_UNKNOWN = "unknown"


class ComputeRemoteOpStatus(ManagedObject):
    """This is ComputeRemoteOpStatus class."""

    consts = ComputeRemoteOpStatusConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeRemoteOpStatus", "computeRemoteOpStatus", "remote-op-status", VersionMeta.Version121a, "InputOutput", 0xf, [], ["read-only"], ['mgmtBackup'], ['faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "op_status": MoPropertyMeta("op_status", "opStatus", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "nop", "success"], []), 
        "op_type": MoPropertyMeta("op_type", "opType", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["backup", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "opStatus": "op_status", 
        "opType": "op_type", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.op_status = None
        self.op_type = None
        self.status = None

        ManagedObject.__init__(self, "ComputeRemoteOpStatus", parent_mo_or_dn, **kwargs)

