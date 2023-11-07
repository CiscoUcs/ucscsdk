"""This module contains the general information for BiosVfDDR3VoltageSelection ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfDDR3VoltageSelectionConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_DDR3_VOLTAGE_SELECTION_DDR3_1350MV = "ddr3-1350mv"
    VP_DDR3_VOLTAGE_SELECTION_DDR3_1500MV = "ddr3-1500mv"
    VP_DDR3_VOLTAGE_SELECTION_PLATFORM_DEFAULT = "platform-default"
    VP_DDR3_VOLTAGE_SELECTION_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfDDR3VoltageSelection(ManagedObject):
    """This is BiosVfDDR3VoltageSelection class."""

    consts = BiosVfDDR3VoltageSelectionConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfDDR3VoltageSelection", "biosVfDDR3VoltageSelection", "DDR3-Voltage-Selection", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_dd_r3_voltage_selection": MoPropertyMeta("vp_dd_r3_voltage_selection", "vpDDR3VoltageSelection", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["ddr3-1350mv", "ddr3-1500mv", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpDDR3VoltageSelection": "vp_dd_r3_voltage_selection", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_dd_r3_voltage_selection = None

        ManagedObject.__init__(self, "BiosVfDDR3VoltageSelection", parent_mo_or_dn, **kwargs)

