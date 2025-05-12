"""This module contains the general information for ConfigDomainItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigDomainItemConsts():
    CONN_PROTOCOL_IPV4 = "ipv4"
    CONN_PROTOCOL_IPV6 = "ipv6"
    CONN_PROTOCOL_UNKNOWN = "unknown"
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
    IS_HA_FALSE = "false"
    IS_HA_NO = "no"
    IS_HA_TRUE = "true"
    IS_HA_YES = "yes"
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


class ConfigDomainItem(ManagedObject):
    """This is ConfigDomainItem class."""

    consts = ConfigDomainItemConsts()
    naming_props = set([])

    mo_meta = MoMeta("ConfigDomainItem", "configDomainItem", "domain-item", VersionMeta.Version131a, "InputOutput", 0xf, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "conn_protocol": MoPropertyMeta("conn_protocol", "connProtocol", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipv4", "ipv6", "unknown"], []), 
        "connection_state": MoPropertyMeta("connection_state", "connectionState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "lost-connectivity"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_dn": MoPropertyMeta("domain_dn", "domainDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_name": MoPropertyMeta("domain_name", "domainName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "fabric_interconnect_model": MoPropertyMeta("fabric_interconnect_model", "fabricInterconnectModel", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "fault_level": MoPropertyMeta("fault_level", "faultLevel", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], []), 
        "fw_oper_state": MoPropertyMeta("fw_oper_state", "fwOperState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "in-progress", "pending-user-ack", "ready", "scheduled", "start-pending-ext-permission"], []), 
        "fw_package_version": MoPropertyMeta("fw_package_version", "fwPackageVersion", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "fw_service_pack_version": MoPropertyMeta("fw_service_pack_version", "fwServicePackVersion", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "inventory_status": MoPropertyMeta("inventory_status", "inventoryStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["in-progress", "ok", "throttled"], []), 
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "ipv6": MoPropertyMeta("ipv6", "ipv6", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "is_ha": MoPropertyMeta("is_ha", "isHA", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []), 
        "num_of_blades": MoPropertyMeta("num_of_blades", "numOfBlades", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_cartridges": MoPropertyMeta("num_of_cartridges", "numOfCartridges", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_chassis": MoPropertyMeta("num_of_chassis", "numOfChassis", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_fex": MoPropertyMeta("num_of_fex", "numOfFex", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_racks": MoPropertyMeta("num_of_racks", "numOfRacks", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_storage_blades": MoPropertyMeta("num_of_storage_blades", "numOfStorageBlades", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "product_family": MoPropertyMeta("product_family", "productFamily", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ucs-classic", "ucs-classic-3gen", "ucs-classic-4gen", "ucs-classic-5gen", "ucs-mini", "ucs-x-series-direct"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "site": MoPropertyMeta("site", "site", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspend_state": MoPropertyMeta("suspend_state", "suspendState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "connProtocol": "conn_protocol", 
        "connectionState": "connection_state", 
        "dn": "dn", 
        "domainDn": "domain_dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainName": "domain_name", 
        "fabricInterconnectModel": "fabric_interconnect_model", 
        "faultLevel": "fault_level", 
        "fwOperState": "fw_oper_state", 
        "fwPackageVersion": "fw_package_version", 
        "fwServicePackVersion": "fw_service_pack_version", 
        "inventoryStatus": "inventory_status", 
        "ip": "ip", 
        "ipv6": "ipv6", 
        "isHA": "is_ha", 
        "licState": "lic_state", 
        "numOfBlades": "num_of_blades", 
        "numOfCartridges": "num_of_cartridges", 
        "numOfChassis": "num_of_chassis", 
        "numOfFex": "num_of_fex", 
        "numOfRacks": "num_of_racks", 
        "numOfStorageBlades": "num_of_storage_blades", 
        "operState": "oper_state", 
        "owner": "owner", 
        "productFamily": "product_family", 
        "rn": "rn", 
        "site": "site", 
        "status": "status", 
        "suspendState": "suspend_state", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.conn_protocol = None
        self.connection_state = None
        self.domain_dn = None
        self.domain_group_dn = None
        self.domain_name = None
        self.fabric_interconnect_model = None
        self.fault_level = None
        self.fw_oper_state = None
        self.fw_package_version = None
        self.fw_service_pack_version = None
        self.inventory_status = None
        self.ip = None
        self.ipv6 = None
        self.is_ha = None
        self.lic_state = None
        self.num_of_blades = None
        self.num_of_cartridges = None
        self.num_of_chassis = None
        self.num_of_fex = None
        self.num_of_racks = None
        self.num_of_storage_blades = None
        self.oper_state = None
        self.owner = None
        self.product_family = None
        self.site = None
        self.status = None
        self.suspend_state = None

        ManagedObject.__init__(self, "ConfigDomainItem", parent_mo_or_dn, **kwargs)

