"""This module contains the general information for OrgDomainFirmwareInfo ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class OrgDomainFirmwareInfoConsts():
    CONNECTION_STATE_CONNECTED = "connected"
    CONNECTION_STATE_LOST_CONNECTIVITY = "lost-connectivity"
    FIRMWARE_OPER_STATE_FAILED = "failed"
    FIRMWARE_OPER_STATE_IN_PROGRESS = "in-progress"
    FIRMWARE_OPER_STATE_PENDING_USER_ACK = "pending-user-ack"
    FIRMWARE_OPER_STATE_READY = "ready"
    FIRMWARE_OPER_STATE_SCHEDULED = "scheduled"
    FIRMWARE_OPER_STATE_START_PENDING_EXT_PERMISSION = "start-pending-ext-permission"
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


class OrgDomainFirmwareInfo(ManagedObject):
    """This is OrgDomainFirmwareInfo class."""

    consts = OrgDomainFirmwareInfoConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("OrgDomainFirmwareInfo", "orgDomainFirmwareInfo", "domain-fw-info-[id]", VersionMeta.Version151a, "InputOutput", 0x1f, [], ["read-only"], ['orgMaintTagFirmwareReport'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "connection_state": MoPropertyMeta("connection_state", "connectionState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "lost-connectivity"], []), 
        "context": MoPropertyMeta("context", "context", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "firmware_oper_state": MoPropertyMeta("firmware_oper_state", "firmwareOperState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "in-progress", "pending-user-ack", "ready", "scheduled", "start-pending-ext-permission"], []), 
        "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "fw_service_pack_version": MoPropertyMeta("fw_service_pack_version", "fwServicePackVersion", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "product_family": MoPropertyMeta("product_family", "productFamily", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ucs-classic", "ucs-classic-3gen", "ucs-classic-4gen", "ucs-classic-5gen", "ucs-mini", "ucs-x-series-direct"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspend_state": MoPropertyMeta("suspend_state", "suspendState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []), 
        "ucsm_running_version": MoPropertyMeta("ucsm_running_version", "ucsmRunningVersion", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "connectionState": "connection_state", 
        "context": "context", 
        "dn": "dn", 
        "firmwareOperState": "firmware_oper_state", 
        "firmwareVersion": "firmware_version", 
        "fwServicePackVersion": "fw_service_pack_version", 
        "id": "id", 
        "ip": "ip", 
        "name": "name", 
        "operState": "oper_state", 
        "productFamily": "product_family", 
        "rn": "rn", 
        "status": "status", 
        "suspendState": "suspend_state", 
        "ucsmRunningVersion": "ucsm_running_version", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.connection_state = None
        self.context = None
        self.firmware_oper_state = None
        self.firmware_version = None
        self.fw_service_pack_version = None
        self.ip = None
        self.name = None
        self.oper_state = None
        self.product_family = None
        self.status = None
        self.suspend_state = None
        self.ucsm_running_version = None

        ManagedObject.__init__(self, "OrgDomainFirmwareInfo", parent_mo_or_dn, **kwargs)

