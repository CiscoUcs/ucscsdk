"""This module contains the general information for AdaptorHostScsiLunRef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorHostScsiLunRefConsts():
    BOOT_DEV_DISABLED = "disabled"
    BOOT_DEV_ENABLED = "enabled"
    LUN_ORDER_NOT_APPLICABLE = "not-applicable"


class AdaptorHostScsiLunRef(ManagedObject):
    """This is AdaptorHostScsiLunRef class."""

    consts = AdaptorHostScsiLunRefConsts()
    naming_props = set(['lunOrder'])

    mo_meta = MoMeta("AdaptorHostScsiLunRef", "adaptorHostScsiLunRef", "host-scsi-lun-[lun_order]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['adaptorHostScsiIf'], [], ["Get"])

    prop_meta = {
        "boot_dev": MoPropertyMeta("boot_dev", "bootDev", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "lun_id": MoPropertyMeta("lun_id", "lunId", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lun_order": MoPropertyMeta("lun_order", "lunOrder", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, None, ["not-applicable"], ["0-64"]), 
        "oper_lun_id": MoPropertyMeta("oper_lun_id", "operLunId", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "bootDev": "boot_dev", 
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "lunId": "lun_id", 
        "lunOrder": "lun_order", 
        "operLunId": "oper_lun_id", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, lun_order, **kwargs):
        self._dirty_mask = 0
        self.lun_order = lun_order
        self.boot_dev = None
        self.child_action = None
        self.flt_aggr = None
        self.lun_id = None
        self.oper_lun_id = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorHostScsiLunRef", parent_mo_or_dn, **kwargs)

