"""This module contains the general information for ConfigDomainFilter ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigDomainFilterConsts():
    CONNECTION_STATE_CONNECTED = "connected"
    CONNECTION_STATE_LOST_CONNECTIVITY = "lost-connectivity"
    FAULT_LEVEL_CLEARED = "cleared"
    FAULT_LEVEL_CONDITION = "condition"
    FAULT_LEVEL_CRITICAL = "critical"
    FAULT_LEVEL_INFO = "info"
    FAULT_LEVEL_MAJOR = "major"
    FAULT_LEVEL_MINOR = "minor"
    FAULT_LEVEL_WARNING = "warning"
    FW_OPER_STATE_FAILED = "failed"
    FW_OPER_STATE_IN_PROGRESS = "in-progress"
    FW_OPER_STATE_PENDING_USER_ACK = "pending-user-ack"
    FW_OPER_STATE_READY = "ready"
    FW_OPER_STATE_SCHEDULED = "scheduled"
    FW_OPER_STATE_START_PENDING_EXT_PERMISSION = "start-pending-ext-permission"
    INVENTORY_STATUS_IN_PROGRESS = "in-progress"
    INVENTORY_STATUS_OK = "ok"
    INVENTORY_STATUS_THROTTLED = "throttled"
    LIC_STATE_LICENSE_EXPIRED = "license-expired"
    LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
    LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
    LIC_STATE_LICENSE_OK = "license-ok"
    LIC_STATE_NOT_APPLICABLE = "not-applicable"
    LIC_STATE_UNKNOWN = "unknown"
    OPER_STATE_LOST_VISIBILITY = "lost-visibility"
    OPER_STATE_REGISTERED = "registered"
    OPER_STATE_REGISTERING = "registering"
    OPER_STATE_SYNCHRONIZING = "synchronizing"
    OPER_STATE_UNREGISTERED = "unregistered"
    OPER_STATE_VERSION_MISMATCH = "version-mismatch"
    PRODUCT_FAMILY_UCS_CLASSIC = "ucs-classic"
    PRODUCT_FAMILY_UCS_CLASSIC_3GEN = "ucs-classic-3gen"
    PRODUCT_FAMILY_UCS_CLASSIC_4GEN = "ucs-classic-4gen"
    PRODUCT_FAMILY_UCS_CLASSIC_5GEN = "ucs-classic-5gen"
    PRODUCT_FAMILY_UCS_MINI = "ucs-mini"
    PRODUCT_FAMILY_UCS_X_SERIES_DIRECT = "ucs-x-series-direct"
    SUSPEND_STATE_OFF = "off"
    SUSPEND_STATE_ON = "on"


class ConfigDomainFilter(ManagedObject):
    """This is ConfigDomainFilter class."""

    consts = ConfigDomainFilterConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigDomainFilter", "configDomainFilter", "domain-filter", VersionMeta.Version131a, "InputOutput", 0x7fff, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "connection_state": MoPropertyMeta("connection_state", "connectionState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["connected", "lost-connectivity"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "fw_oper_state": MoPropertyMeta("fw_oper_state", "fwOperState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["failed", "in-progress", "pending-user-ack", "ready", "scheduled", "start-pending-ext-permission"], []), 
        "fw_package_version": MoPropertyMeta("fw_package_version", "fwPackageVersion", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []), 
        "fw_service_pack_version": MoPropertyMeta("fw_service_pack_version", "fwServicePackVersion", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []), 
        "inventory_status": MoPropertyMeta("inventory_status", "inventoryStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["in-progress", "ok", "throttled"], []), 
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "product_family": MoPropertyMeta("product_family", "productFamily", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["ucs-classic", "ucs-classic-3gen", "ucs-classic-4gen", "ucs-classic-5gen", "ucs-mini", "ucs-x-series-direct"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x1000, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspend_state": MoPropertyMeta("suspend_state", "suspendState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["off", "on"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "connectionState": "connection_state", 
        "dn": "dn", 
        "domainGroupDn": "domain_group_dn", 
        "faultLevel": "fault_level", 
        "fwOperState": "fw_oper_state", 
        "fwPackageVersion": "fw_package_version", 
        "fwServicePackVersion": "fw_service_pack_version", 
        "inventoryStatus": "inventory_status", 
        "licState": "lic_state", 
        "operState": "oper_state", 
        "productFamily": "product_family", 
        "rn": "rn", 
        "status": "status", 
        "suspendState": "suspend_state", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.connection_state = None
        self.domain_group_dn = None
        self.fault_level = None
        self.fw_oper_state = None
        self.fw_package_version = None
        self.fw_service_pack_version = None
        self.inventory_status = None
        self.lic_state = None
        self.oper_state = None
        self.product_family = None
        self.status = None
        self.suspend_state = None

        ManagedObject.__init__(self, "ConfigDomainFilter", parent_mo_or_dn, **kwargs)

