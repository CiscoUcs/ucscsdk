"""This module contains the general information for EquipmentUnifiedPortCapProvider ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentUnifiedPortCapProviderConsts():
    LIC_STATE_LICENSE_EXPIRED = "license-expired"
    LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
    LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
    LIC_STATE_LICENSE_OK = "license-ok"
    LIC_STATE_NOT_APPLICABLE = "not-applicable"
    LIC_STATE_UNKNOWN = "unknown"
    SUPPORTED_ALGORITHM_NONE = "none"
    SUPPORTED_ALGORITHM_SLIDE_RULE = "slide-rule"
    SUPPORTED_ALGORITHM_SLIDE_RULE_ETH_FIRST_DOUBLE_ROW = "slide-rule-eth-first-double-row"
    SUPPORTED_ALGORITHM_SLIDE_RULE_ETH_FIRST_SINGLE_ROW = "slide-rule-eth-first-single-row"
    SUPPORTED_ALGORITHM_SLIDE_RULE_FC_FIRST_3GFI_ROW = "slide-rule-fc-first-3gfi-row"
    SUPPORTED_ALGORITHM_SLIDE_RULE_FC_FIRST_4GFI_ROW = "slide-rule-fc-first-4gfi-row"
    SUPPORTED_ALGORITHM_SLIDE_RULE_FC_FIRST_5GFI_ROW = "slide-rule-fc-first-5gfi-row"
    SUPPORTED_ALGORITHM_SLIDE_RULE_FC_FIRST_DOUBLE_ROW = "slide-rule-fc-first-double-row"
    SUPPORTED_ALGORITHM_SLIDE_RULE_FC_FIRST_SINGLE_ROW = "slide-rule-fc-first-single-row"
    SUPPORTED_ALGORITHM_SLIDE_RULE_FC_FIRST_UCSX_DIRECT_ROW = "slide-rule-fc-first-ucsx-direct-row"
    SUPPORTED_ALGORITHM_UNRESTRICTED = "unrestricted"


class EquipmentUnifiedPortCapProvider(ManagedObject):
    """This is EquipmentUnifiedPortCapProvider class."""

    consts = EquipmentUnifiedPortCapProviderConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentUnifiedPortCapProvider", "equipmentUnifiedPortCapProvider", "unified-port-cap", VersionMeta.Version131a, "InputOutput", 0x1f, [], [""], ['equipmentGemCapProvider', 'equipmentSwitchCapProvider', 'equipmentSwitchIOCardCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "end_port_id": MoPropertyMeta("end_port_id", "endPortId", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lic_gp": MoPropertyMeta("lic_gp", "licGP", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "start_port_id": MoPropertyMeta("start_port_id", "startPortId", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_algorithm": MoPropertyMeta("supported_algorithm", "supportedAlgorithm", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "slide-rule", "slide-rule-eth-first-double-row", "slide-rule-eth-first-single-row", "slide-rule-fc-first-3gfi-row", "slide-rule-fc-first-4gfi-row", "slide-rule-fc-first-5gfi-row", "slide-rule-fc-first-double-row", "slide-rule-fc-first-single-row", "slide-rule-fc-first-ucsx-direct-row", "unrestricted"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "endPortId": "end_port_id", 
        "licGP": "lic_gp", 
        "licState": "lic_state", 
        "name": "name", 
        "rn": "rn", 
        "startPortId": "start_port_id", 
        "status": "status", 
        "supportedAlgorithm": "supported_algorithm", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.end_port_id = None
        self.lic_gp = None
        self.lic_state = None
        self.name = None
        self.start_port_id = None
        self.status = None
        self.supported_algorithm = None

        ManagedObject.__init__(self, "EquipmentUnifiedPortCapProvider", parent_mo_or_dn, **kwargs)

