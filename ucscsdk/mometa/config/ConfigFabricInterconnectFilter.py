"""This module contains the general information for ConfigFabricInterconnectFilter ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigFabricInterconnectFilterConsts():
    FAULT_LEVEL_CLEARED = "cleared"
    FAULT_LEVEL_CONDITION = "condition"
    FAULT_LEVEL_CRITICAL = "critical"
    FAULT_LEVEL_INFO = "info"
    FAULT_LEVEL_MAJOR = "major"
    FAULT_LEVEL_MINOR = "minor"
    FAULT_LEVEL_WARNING = "warning"
    FW_OPER_STATE_ACTIVATING = "activating"
    FW_OPER_STATE_BAD_IMAGE = "bad-image"
    FW_OPER_STATE_FAILED = "failed"
    FW_OPER_STATE_PENDING_NEXT_BOOT = "pending-next-boot"
    FW_OPER_STATE_READY = "ready"
    FW_OPER_STATE_REBOOTING = "rebooting"
    FW_OPER_STATE_SCHEDULED = "scheduled"
    FW_OPER_STATE_SET_STARTUP = "set-startup"
    FW_OPER_STATE_THROTTLED = "throttled"
    FW_OPER_STATE_UPDATING = "updating"
    FW_OPER_STATE_UPGRADING = "upgrading"


class ConfigFabricInterconnectFilter(ManagedObject):
    """This is ConfigFabricInterconnectFilter class."""

    consts = ConfigFabricInterconnectFilterConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigFabricInterconnectFilter", "configFabricInterconnectFilter", "fabric-interconnect-filter", VersionMeta.Version131a, "InputOutput", 0x1fff, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_dn": MoPropertyMeta("domain_dn", "domainDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "fw_oper_state": MoPropertyMeta("fw_oper_state", "fwOperState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating", "upgrading"], []), 
        "fw_service_pack_version": MoPropertyMeta("fw_service_pack_version", "fwServicePackVersion", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []), 
        "fw_version": MoPropertyMeta("fw_version", "fwVersion", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], []), 
        "operability": MoPropertyMeta("operability", "operability", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x800, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "domainDn": "domain_dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainName": "domain_name", 
        "faultLevel": "fault_level", 
        "fwOperState": "fw_oper_state", 
        "fwServicePackVersion": "fw_service_pack_version", 
        "fwVersion": "fw_version", 
        "model": "model", 
        "operability": "operability", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.domain_dn = None
        self.domain_group_dn = None
        self.domain_name = None
        self.fault_level = None
        self.fw_oper_state = None
        self.fw_service_pack_version = None
        self.fw_version = None
        self.model = None
        self.operability = None
        self.status = None

        ManagedObject.__init__(self, "ConfigFabricInterconnectFilter", parent_mo_or_dn, **kwargs)

