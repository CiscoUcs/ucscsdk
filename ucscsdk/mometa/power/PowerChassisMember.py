"""This module contains the general information for PowerChassisMember ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PowerChassisMemberConsts():
    OPER_STATE_CAP_INSUFFICIENT = "cap-insufficient"
    OPER_STATE_CAP_OK = "cap-ok"
    OPER_STATE_FW_MISMATCH = "fw-mismatch"
    OPER_STATE_PSU_INSUFFICIENT = "psu-insufficient"
    OPER_STATE_PSU_REDUNDANCY_FAILED = "psu-redundancy-failed"
    OPER_STATE_UNINITIALIZED = "uninitialized"


class PowerChassisMember(ManagedObject):
    """This is PowerChassisMember class."""

    consts = PowerChassisMemberConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("PowerChassisMember", "powerChassisMember", "ch-member-[id]", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["admin", "power-mgmt", "read-only"], ['powerGroup'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cap-insufficient", "cap-ok", "fw-mismatch", "psu-insufficient", "psu-redundancy-failed", "uninitialized"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "operState": "oper_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.oper_state = None
        self.status = None

        ManagedObject.__init__(self, "PowerChassisMember", parent_mo_or_dn, **kwargs)

