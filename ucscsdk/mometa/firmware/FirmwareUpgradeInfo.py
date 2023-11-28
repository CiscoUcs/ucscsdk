"""This module contains the general information for FirmwareUpgradeInfo ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareUpgradeInfoConsts():
    TIME_STAMP_NEVER = "never"
    VALIDATE_STATUS_FAILED = "failed"
    VALIDATE_STATUS_IN_PROGRESS = "in-progress"
    VALIDATE_STATUS_SKIPPED = "skipped"
    VALIDATE_STATUS_SUCCESS = "success"
    VALIDATE_STATUS_UNKNOWN = "unknown"
    VALIDATE_STATUS_WARNINGS = "warnings"


class FirmwareUpgradeInfo(ManagedObject):
    """This is FirmwareUpgradeInfo class."""

    consts = FirmwareUpgradeInfoConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareUpgradeInfo", "firmwareUpgradeInfo", "validate-upgrade", VersionMeta.Version141a, "InputOutput", 0xf, [], ["admin"], ['computeSystem'], ['firmwareUpgradeDetail'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "message": MoPropertyMeta("message", "message", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "time_stamp": MoPropertyMeta("time_stamp", "timeStamp", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "validate_status": MoPropertyMeta("validate_status", "validateStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "in-progress", "skipped", "success", "unknown", "warnings"], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "message": "message", 
        "rn": "rn", 
        "status": "status", 
        "timeStamp": "time_stamp", 
        "validateStatus": "validate_status", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.message = None
        self.status = None
        self.time_stamp = None
        self.validate_status = None
        self.version = None

        ManagedObject.__init__(self, "FirmwareUpgradeInfo", parent_mo_or_dn, **kwargs)

