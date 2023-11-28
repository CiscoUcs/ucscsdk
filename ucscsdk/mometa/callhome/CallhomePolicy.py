"""This module contains the general information for CallhomePolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class CallhomePolicyConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CAUSE_ARP_TARGETS_CONFIG_ERROR = "arp-targets-config-error"
    CAUSE_ASSOCIATION_FAILED = "association-failed"
    CAUSE_CONFIGURATION_FAILURE = "configuration-failure"
    CAUSE_CONNECTIVITY_PROBLEM = "connectivity-problem"
    CAUSE_ELECTION_FAILURE = "election-failure"
    CAUSE_EQUIPMENT_DISABLED = "equipment-disabled"
    CAUSE_EQUIPMENT_INACCESSIBLE = "equipment-inaccessible"
    CAUSE_EQUIPMENT_INOPERABLE = "equipment-inoperable"
    CAUSE_EQUIPMENT_OFFLINE = "equipment-offline"
    CAUSE_EQUIPMENT_PROBLEM = "equipment-problem"
    CAUSE_FRU_PROBLEM = "fru-problem"
    CAUSE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CAUSE_INVENTORY_FAILED = "inventory-failed"
    CAUSE_LICENSE_GRACEPERIOD_EXPIRED = "license-graceperiod-expired"
    CAUSE_LIMIT_REACHED = "limit-reached"
    CAUSE_LINK_DOWN = "link-down"
    CAUSE_MANAGEMENT_SERVICES_FAILURE = "management-services-failure"
    CAUSE_MANAGEMENT_SERVICES_UNRESPONSIVE = "management-services-unresponsive"
    CAUSE_MGMTIF_DOWN = "mgmtif-down"
    CAUSE_PORT_FAILED = "port-failed"
    CAUSE_POWER_PROBLEM = "power-problem"
    CAUSE_THERMAL_PROBLEM = "thermal-problem"
    CAUSE_UNSPECIFIED = "unspecified"
    CAUSE_VERSION_INCOMPATIBLE = "version-incompatible"
    CAUSE_VIF_IDS_MISMATCH = "vif-ids-mismatch"
    CAUSE_VOLTAGE_PROBLEM = "voltage-problem"


class CallhomePolicy(ManagedObject):
    """This is CallhomePolicy class."""

    consts = CallhomePolicyConsts()
    naming_props = set(['cause'])

    mo_meta = MoMeta("CallhomePolicy", "callhomePolicy", "policy-[cause]", VersionMeta.Version101a, "InputOutput", 0xff, [], ["admin", "fault"], ['callhomeEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "cause": MoPropertyMeta("cause", "cause", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, None, None, None, ["arp-targets-config-error", "association-failed", "configuration-failure", "connectivity-problem", "election-failure", "equipment-disabled", "equipment-inaccessible", "equipment-inoperable", "equipment-offline", "equipment-problem", "fru-problem", "identity-unestablishable", "inventory-failed", "license-graceperiod-expired", "limit-reached", "link-down", "management-services-failure", "management-services-unresponsive", "mgmtif-down", "port-failed", "power-problem", "thermal-problem", "unspecified", "version-incompatible", "vif-ids-mismatch", "voltage-problem"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "cause": "cause", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, cause, **kwargs):
        self._dirty_mask = 0
        self.cause = cause
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.name = None
        self.status = None

        ManagedObject.__init__(self, "CallhomePolicy", parent_mo_or_dn, **kwargs)

