"""This module contains the general information for LsbootUpgradeStatus ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsbootUpgradeStatusConsts():
    LEGACY_TO_ADVANCED_BOOT_ORDER_UPDATE_FALSE = "false"
    LEGACY_TO_ADVANCED_BOOT_ORDER_UPDATE_NO = "no"
    LEGACY_TO_ADVANCED_BOOT_ORDER_UPDATE_TRUE = "true"
    LEGACY_TO_ADVANCED_BOOT_ORDER_UPDATE_YES = "yes"


class LsbootUpgradeStatus(ManagedObject):
    """This is LsbootUpgradeStatus class."""

    consts = LsbootUpgradeStatusConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootUpgradeStatus", "lsbootUpgradeStatus", "UpgradeStatus", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["admin"], ['lsbootPolicy'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "legacy_to_advanced_boot_order_update": MoPropertyMeta("legacy_to_advanced_boot_order_update", "legacyToAdvancedBootOrderUpdate", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "legacyToAdvancedBootOrderUpdate": "legacy_to_advanced_boot_order_update", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.legacy_to_advanced_boot_order_update = None
        self.status = None

        ManagedObject.__init__(self, "LsbootUpgradeStatus", parent_mo_or_dn, **kwargs)

