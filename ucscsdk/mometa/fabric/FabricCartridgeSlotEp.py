"""This module contains the general information for FabricCartridgeSlotEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricCartridgeSlotEpConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    AUTO_NEGOTIATE_FALSE = "false"
    AUTO_NEGOTIATE_NO = "no"
    AUTO_NEGOTIATE_TRUE = "true"
    AUTO_NEGOTIATE_YES = "yes"
    CHASSIS_ID_N_A = "N/A"
    IF_ROLE_DIAG = "diag"
    IF_ROLE_FCOE_NAS_STORAGE = "fcoe-nas-storage"
    IF_ROLE_FCOE_STORAGE = "fcoe-storage"
    IF_ROLE_FCOE_UPLINK = "fcoe-uplink"
    IF_ROLE_MGMT = "mgmt"
    IF_ROLE_MONITOR = "monitor"
    IF_ROLE_NAS_STORAGE = "nas-storage"
    IF_ROLE_NETWORK = "network"
    IF_ROLE_NETWORK_FCOE_UPLINK = "network-fcoe-uplink"
    IF_ROLE_SERVER = "server"
    IF_ROLE_SERVICE = "service"
    IF_ROLE_STORAGE = "storage"
    IF_ROLE_UNKNOWN = "unknown"
    IF_TYPE_AGGREGATION = "aggregation"
    IF_TYPE_PHYSICAL = "physical"
    IF_TYPE_UNKNOWN = "unknown"
    IF_TYPE_VIRTUAL = "virtual"
    LIC_STATE_LICENSE_EXPIRED = "license-expired"
    LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
    LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
    LIC_STATE_LICENSE_OK = "license-ok"
    LIC_STATE_NOT_APPLICABLE = "not-applicable"
    LIC_STATE_UNKNOWN = "unknown"
    MANAGING_INST_A = "A"
    MANAGING_INST_B = "B"
    MANAGING_INST_NONE = "NONE"
    MANAGING_INST_MGMT = "mgmt"
    OPER_STATE_DOWN = "down"
    OPER_STATE_ERROR_MISCONFIGURED = "error-misconfigured"
    OPER_STATE_ERROR_UNSUPPORTED_MINI_SERVER_PORT = "error-unsupported-mini-server-port"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UP = "up"
    PEER_CHASSIS_ID_N_A = "N/A"
    PRESENCE_EMPTY = "empty"
    PRESENCE_EQUIPPED = "equipped"
    PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    PRESENCE_EQUIPPED_SLAVE = "equipped-slave"
    PRESENCE_EQUIPPED_UNSUPPORTED = "equipped-unsupported"
    PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    PRESENCE_INACCESSIBLE = "inaccessible"
    PRESENCE_MISMATCH = "mismatch"
    PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    PRESENCE_MISMATCH_SLAVE = "mismatch-slave"
    PRESENCE_MISSING = "missing"
    PRESENCE_MISSING_SLAVE = "missing-slave"
    PRESENCE_UNAUTHORIZED = "unauthorized"
    PRESENCE_UNKNOWN = "unknown"
    SLOT_ADMIN_STATE_ACKNOWLEDGED = "acknowledged"
    SLOT_ADMIN_STATE_REACKNOWLEDGE = "reacknowledge"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"


class FabricCartridgeSlotEp(ManagedObject):
    """This is FabricCartridgeSlotEp class."""

    consts = FabricCartridgeSlotEpConsts()
    naming_props = set(['slotId'])

    mo_meta = MoMeta("FabricCartridgeSlotEp", "fabricCartridgeSlotEp", "cart-slot-[slot_id]", VersionMeta.Version131a, "InputOutput", 0x7ff, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['fabricChassisEp'], ['fabricCartridgeSlotEpOperation', 'fabricComputeMSlotEp'], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "auto_negotiate": MoPropertyMeta("auto_negotiate", "autoNegotiate", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["false", "no", "true", "yes"], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["N/A"], ["1-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "conn_path": MoPropertyMeta("conn_path", "connPath", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "conn_status": MoPropertyMeta("conn_status", "connStatus", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "discovery_status": MoPropertyMeta("discovery_status", "discoveryStatus", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|A|B),){0,3}(defaultValue|unknown|A|B){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []), 
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []), 
        "lic_gp": MoPropertyMeta("lic_gp", "licGP", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []), 
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []), 
        "managing_inst": MoPropertyMeta("managing_inst", "managingInst", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["down", "error-misconfigured", "error-unsupported-mini-server-port", "failed", "unknown", "up"], []), 
        "oper_state_reason": MoPropertyMeta("oper_state_reason", "operStateReason", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "peer_aggr_port_id": MoPropertyMeta("peer_aggr_port_id", "peerAggrPortId", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "peer_chassis_id": MoPropertyMeta("peer_chassis_id", "peerChassisId", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "peer_port_id": MoPropertyMeta("peer_port_id", "peerPortId", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "peer_slot_id": MoPropertyMeta("peer_slot_id", "peerSlotId", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-48"]), 
        "presence": MoPropertyMeta("presence", "presence", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-slave", "equipped-unsupported", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "mismatch-slave", "missing", "missing-slave", "unauthorized", "unknown"], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "slot_admin_state": MoPropertyMeta("slot_admin_state", "slotAdminState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["acknowledged", "reacknowledge"], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x100, None, None, None, [], ["1-8"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "aggrPortId": "aggr_port_id", 
        "autoNegotiate": "auto_negotiate", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "connPath": "conn_path", 
        "connStatus": "conn_status", 
        "discoveryStatus": "discovery_status", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "fltAggr": "flt_aggr", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "licGP": "lic_gp", 
        "licState": "lic_state", 
        "locale": "locale", 
        "managingInst": "managing_inst", 
        "model": "model", 
        "name": "name", 
        "operState": "oper_state", 
        "operStateReason": "oper_state_reason", 
        "peerAggrPortId": "peer_aggr_port_id", 
        "peerChassisId": "peer_chassis_id", 
        "peerDn": "peer_dn", 
        "peerPortId": "peer_port_id", 
        "peerSlotId": "peer_slot_id", 
        "portId": "port_id", 
        "presence": "presence", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "slotAdminState": "slot_admin_state", 
        "slotId": "slot_id", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
        "usrLbl": "usr_lbl", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.admin_state = None
        self.aggr_port_id = None
        self.auto_negotiate = None
        self.chassis_id = None
        self.child_action = None
        self.conn_path = None
        self.conn_status = None
        self.discovery_status = None
        self.ep_dn = None
        self.flt_aggr = None
        self.if_role = None
        self.if_type = None
        self.lic_gp = None
        self.lic_state = None
        self.locale = None
        self.managing_inst = None
        self.model = None
        self.name = None
        self.oper_state = None
        self.oper_state_reason = None
        self.peer_aggr_port_id = None
        self.peer_chassis_id = None
        self.peer_dn = None
        self.peer_port_id = None
        self.peer_slot_id = None
        self.port_id = None
        self.presence = None
        self.revision = None
        self.serial = None
        self.slot_admin_state = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None
        self.usr_lbl = None
        self.vendor = None

        ManagedObject.__init__(self, "FabricCartridgeSlotEp", parent_mo_or_dn, **kwargs)

