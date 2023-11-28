"""This module contains the general information for BiosTokenSettings ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosTokenSettingsConsts():
    IS_ASSIGNED_FALSE = "false"
    IS_ASSIGNED_NO = "no"
    IS_ASSIGNED_TRUE = "true"
    IS_ASSIGNED_YES = "yes"


class BiosTokenSettings(ManagedObject):
    """This is BiosTokenSettings class."""

    consts = BiosTokenSettingsConsts()
    naming_props = set(['settingsMoRn'])

    mo_meta = MoMeta("BiosTokenSettings", "biosTokenSettings", "tokn-setng-[settings_mo_rn]", VersionMeta.Version201b, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], ['biosTokenParam'], [], [None])

    prop_meta = {
        "maximum": MoPropertyMeta("maximum", "Maximum", "string", VersionMeta.Version201k, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "minimum": MoPropertyMeta("minimum", "Minimum", "string", VersionMeta.Version201k, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "step": MoPropertyMeta("step", "Step", "string", VersionMeta.Version201k, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "unit": MoPropertyMeta("unit", "Unit", "string", VersionMeta.Version201k, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "bios_ret_setting_name": MoPropertyMeta("bios_ret_setting_name", "biosRetSettingName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "is_assigned": MoPropertyMeta("is_assigned", "isAssigned", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []), 
        "legacy_prop_val": MoPropertyMeta("legacy_prop_val", "legacyPropVal", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "settings_mo_rn": MoPropertyMeta("settings_mo_rn", "settingsMoRn", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "target_token_value": MoPropertyMeta("target_token_value", "targetTokenValue", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "Maximum": "maximum", 
        "Minimum": "minimum", 
        "Step": "step", 
        "Unit": "unit", 
        "biosRetSettingName": "bios_ret_setting_name", 
        "childAction": "child_action", 
        "dn": "dn", 
        "isAssigned": "is_assigned", 
        "legacyPropVal": "legacy_prop_val", 
        "rn": "rn", 
        "settingsMoRn": "settings_mo_rn", 
        "status": "status", 
        "targetTokenValue": "target_token_value", 
    }

    def __init__(self, parent_mo_or_dn, settings_mo_rn, **kwargs):
        self._dirty_mask = 0
        self.settings_mo_rn = settings_mo_rn
        self.maximum = None
        self.minimum = None
        self.step = None
        self.unit = None
        self.bios_ret_setting_name = None
        self.child_action = None
        self.is_assigned = None
        self.legacy_prop_val = None
        self.status = None
        self.target_token_value = None

        ManagedObject.__init__(self, "BiosTokenSettings", parent_mo_or_dn, **kwargs)

