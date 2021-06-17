"""This module contains the general information for FcPIo ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FcPIoConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CHASSIS_ID_N_A = "N/A"
    ENCAP_DOT1Q = "dot1q"
    ENCAP_ISL = "isl"
    ENCAP_NEGOTIATE = "negotiate"
    ENCAP_PROPRIETARY = "proprietary"
    ENCAP_UNKNOWN = "unknown"
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
    IS_BREAKOUT_XCVR_FALSE = "false"
    IS_BREAKOUT_XCVR_NO = "no"
    IS_BREAKOUT_XCVR_TRUE = "true"
    IS_BREAKOUT_XCVR_YES = "yes"
    IS_PORT_CHANNEL_MEMBER_FALSE = "false"
    IS_PORT_CHANNEL_MEMBER_NO = "no"
    IS_PORT_CHANNEL_MEMBER_TRUE = "true"
    IS_PORT_CHANNEL_MEMBER_YES = "yes"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    LIC_STATE_LICENSE_EXPIRED = "license-expired"
    LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
    LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
    LIC_STATE_LICENSE_OK = "license-ok"
    LIC_STATE_NOT_APPLICABLE = "not-applicable"
    LIC_STATE_UNKNOWN = "unknown"
    MAX_SPEED_16GBPS = "16gbps"
    MAX_SPEED_1GBPS = "1gbps"
    MAX_SPEED_2GBPS = "2gbps"
    MAX_SPEED_32GBPS = "32gbps"
    MAX_SPEED_4GBPS = "4gbps"
    MAX_SPEED_8GBPS = "8gbps"
    MAX_SPEED_AUTO = "auto"
    MAX_SPEED_INDETERMINATE = "indeterminate"
    MODE_E = "E"
    MODE_F = "F"
    MODE_SD = "SD"
    MODE_ACCESS = "access"
    MODE_FABRIC = "fabric"
    MODE_N_PROXY = "n_proxy"
    MODE_PROMISCUOUS_ACCESS = "promiscuousAccess"
    MODE_PROMISCUOUS_TRUNK = "promiscuousTrunk"
    MODE_TRUNK = "trunk"
    MODE_UNKNOWN = "unknown"
    MODE_VNTAG = "vntag"
    OPER_SPEED_16GBPS = "16gbps"
    OPER_SPEED_1GBPS = "1gbps"
    OPER_SPEED_2GBPS = "2gbps"
    OPER_SPEED_32GBPS = "32gbps"
    OPER_SPEED_4GBPS = "4gbps"
    OPER_SPEED_8GBPS = "8gbps"
    OPER_SPEED_AUTO = "auto"
    OPER_SPEED_INDETERMINATE = "indeterminate"
    OPER_STATE_ADMIN_DOWN = "admin-down"
    OPER_STATE_DOWN = "down"
    OPER_STATE_ERROR_DISABLED = "error-disabled"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_HARDWARE_FAILURE = "hardware-failure"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_LINK_DOWN = "link-down"
    OPER_STATE_LINK_UP = "link-up"
    OPER_STATE_NO_LICENSE = "no-license"
    OPER_STATE_SFP_NOT_PRESENT = "sfp-not-present"
    OPER_STATE_SOFTWARE_FAILURE = "software-failure"
    OPER_STATE_UDLD_AGGR_DOWN = "udld-aggr-down"
    OPER_STATE_UP = "up"
    PEER_CHASSIS_ID_N_A = "N/A"
    PORT_CAPABILITY_ETH_APPLIANT_PORT = "ethAppliantPort"
    PORT_CAPABILITY_ETH_FEX_SERVER_PORT = "ethFexServerPort"
    PORT_CAPABILITY_ETH_RACK_SERVER_PORT = "ethRackServerPort"
    PORT_CAPABILITY_ETH_UPLINK_PORT = "ethUplinkPort"
    PORT_CAPABILITY_UNKNOWN = "unknown"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"
    UNIFIED_PORT_FALSE = "false"
    UNIFIED_PORT_NO = "no"
    UNIFIED_PORT_TRUE = "true"
    UNIFIED_PORT_YES = "yes"
    XCVR_TYPE_1000BASECX = "1000basecx"
    XCVR_TYPE_1000BASELH = "1000baselh"
    XCVR_TYPE_1000BASELX = "1000baselx"
    XCVR_TYPE_1000BASESX = "1000basesx"
    XCVR_TYPE_1000BASET = "1000baset"
    XCVR_TYPE_1000BASEUNKNOWN = "1000baseunknown"
    XCVR_TYPE_1000BASEVX = "1000basevx"
    XCVR_TYPE_1000BASEX = "1000basex"
    XCVR_TYPE_1000BASEZX = "1000basezx"
    XCVR_TYPE_10GBASEER = "10gbaseer"
    XCVR_TYPE_10GBASELR = "10gbaselr"
    XCVR_TYPE_10GBASELRM = "10gbaselrm"
    XCVR_TYPE_10GBASESR = "10gbasesr"
    XCVR_TYPE_10GBASEZR = "10gbasezr"
    XCVR_TYPE_CWDM1471 = "cwdm1471"
    XCVR_TYPE_CWDM1531 = "cwdm1531"
    XCVR_TYPE_CWDM1551 = "cwdm1551"
    XCVR_TYPE_DWDMSFP = "dwdmsfp"
    XCVR_TYPE_FET = "fet"
    XCVR_TYPE_H10GACU10M = "h10gacu10m"
    XCVR_TYPE_H10GACU15M = "h10gacu15m"
    XCVR_TYPE_H10GACU1M = "h10gacu1m"
    XCVR_TYPE_H10GACU3M = "h10gacu3m"
    XCVR_TYPE_H10GACU5M = "h10gacu5m"
    XCVR_TYPE_H10GACU7M = "h10gacu7m"
    XCVR_TYPE_H10GACUAOC10M = "h10gacuaoc10m"
    XCVR_TYPE_H10GACUAOC15M = "h10gacuaoc15m"
    XCVR_TYPE_H10GACUAOC1M = "h10gacuaoc1m"
    XCVR_TYPE_H10GACUAOC2M = "h10gacuaoc2m"
    XCVR_TYPE_H10GACUAOC3M = "h10gacuaoc3m"
    XCVR_TYPE_H10GACUAOC5M = "h10gacuaoc5m"
    XCVR_TYPE_H10GACUAOC7M = "h10gacuaoc7m"
    XCVR_TYPE_H10GAOC10M = "h10gaoc10m"
    XCVR_TYPE_H10GAOC1M = "h10gaoc1m"
    XCVR_TYPE_H10GAOC2M = "h10gaoc2m"
    XCVR_TYPE_H10GAOC3M = "h10gaoc3m"
    XCVR_TYPE_H10GAOC5M = "h10gaoc5m"
    XCVR_TYPE_H10GAOC7M = "h10gaoc7m"
    XCVR_TYPE_H10GCU10M = "h10gcu10m"
    XCVR_TYPE_H10GCU1M = "h10gcu1m"
    XCVR_TYPE_H10GCU2M = "h10gcu2m"
    XCVR_TYPE_H10GCU3M = "h10gcu3m"
    XCVR_TYPE_H10GCU5M = "h10gcu5m"
    XCVR_TYPE_H10GCU7M = "h10gcu7m"
    XCVR_TYPE_H10GLRMSM = "h10glrmsm"
    XCVR_TYPE_H10GUSR = "h10gusr"
    XCVR_TYPE_QSFP40GCR4 = "qsfp40gcr4"
    XCVR_TYPE_QSFP40GCSR4 = "qsfp40gcsr4"
    XCVR_TYPE_QSFP40GFET = "qsfp40gfet"
    XCVR_TYPE_QSFP40GLR4 = "qsfp40glr4"
    XCVR_TYPE_QSFP40GSR4 = "qsfp40gsr4"
    XCVR_TYPE_QSFP40GSRBD = "qsfp40gsrbd"
    XCVR_TYPE_QSFP4SFP10GCU1M = "qsfp4sfp10gcu1m"
    XCVR_TYPE_QSFP4SFP10GCU2M = "qsfp4sfp10gcu2m"
    XCVR_TYPE_QSFP4SFP10GCU3M = "qsfp4sfp10gcu3m"
    XCVR_TYPE_QSFP4SFP10GCU5M = "qsfp4sfp10gcu5m"
    XCVR_TYPE_QSFP4X10GA0C10M = "qsfp4x10ga0c10m"
    XCVR_TYPE_QSFP4X10GA0C1M = "qsfp4x10ga0c1m"
    XCVR_TYPE_QSFP4X10GA0C2M = "qsfp4x10ga0c2m"
    XCVR_TYPE_QSFP4X10GA0C3M = "qsfp4x10ga0c3m"
    XCVR_TYPE_QSFP4X10GA0C5M = "qsfp4x10ga0c5m"
    XCVR_TYPE_QSFP4X10GA0C7M = "qsfp4x10ga0c7m"
    XCVR_TYPE_QSFP4X10GA0CUNKNOWN = "qsfp4x10ga0cunknown"
    XCVR_TYPE_QSFP4X10GAC10M = "qsfp4x10gac10m"
    XCVR_TYPE_QSFP4X10GAC1M = "qsfp4x10gac1m"
    XCVR_TYPE_QSFP4X10GAC3M = "qsfp4x10gac3m"
    XCVR_TYPE_QSFP4X10GAC5M = "qsfp4x10gac5m"
    XCVR_TYPE_QSFP4X10GAC7M = "qsfp4x10gac7m"
    XCVR_TYPE_QSFP4X10GLR = "qsfp4x10glr"
    XCVR_TYPE_QSFPH40GACU10M = "qsfph40gacu10m"
    XCVR_TYPE_QSFPH40GACU1M = "qsfph40gacu1m"
    XCVR_TYPE_QSFPH40GACU3M = "qsfph40gacu3m"
    XCVR_TYPE_QSFPH40GACU5M = "qsfph40gacu5m"
    XCVR_TYPE_QSFPH40GACU7M = "qsfph40gacu7m"
    XCVR_TYPE_QSFPH40GAOC10M = "qsfph40gaoc10m"
    XCVR_TYPE_QSFPH40GAOC15M = "qsfph40gaoc15m"
    XCVR_TYPE_QSFPH40GAOC1M = "qsfph40gaoc1m"
    XCVR_TYPE_QSFPH40GAOC2M = "qsfph40gaoc2m"
    XCVR_TYPE_QSFPH40GAOC3M = "qsfph40gaoc3m"
    XCVR_TYPE_QSFPH40GAOC5M = "qsfph40gaoc5m"
    XCVR_TYPE_QSFPH40GAOC7M = "qsfph40gaoc7m"
    XCVR_TYPE_QSFPH40GAOCUNKNOWN = "qsfph40gaocunknown"
    XCVR_TYPE_QSFPH40GCU1M = "qsfph40gcu1m"
    XCVR_TYPE_QSFPH40GCU2M = "qsfph40gcu2m"
    XCVR_TYPE_QSFPH40GCU3M = "qsfph40gcu3m"
    XCVR_TYPE_QSFPH40GCU5M = "qsfph40gcu5m"
    XCVR_TYPE_QSFPLOOP = "qsfploop"
    XCVR_TYPE_QSFPQSA = "qsfpqsa"
    XCVR_TYPE_QSFPUNKNOWN = "qsfpunknown"
    XCVR_TYPE_SFP = "sfp"
    XCVR_TYPE_UNKNOWN = "unknown"
    XCVR_TYPE_X2 = "x2"


class FcPIo(ManagedObject):
    """This is FcPIo class."""

    consts = FcPIoConsts()
    naming_props = set([u'portId'])

    mo_meta = MoMeta("FcPIo", "fcPIo", "port-[port_id]", VersionMeta.Version111a, "InputOutput", 0x7f, [], ["read-only"], [u'portGroup', u'portSubGroup'], [u'equipmentXcvr'], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
        "admin_transport": MoPropertyMeta("admin_transport", "adminTransport", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []), 
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "encap": MoPropertyMeta("encap", "encap", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["dot1q", "isl", "negotiate", "proprietary", "unknown"], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []), 
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []), 
        "is_breakout_xcvr": MoPropertyMeta("is_breakout_xcvr", "isBreakoutXcvr", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_port_channel_member": MoPropertyMeta("is_port_channel_member", "isPortChannelMember", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "lic_gp": MoPropertyMeta("lic_gp", "licGP", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []), 
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []), 
        "max_speed": MoPropertyMeta("max_speed", "maxSpeed", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["16gbps", "1gbps", "2gbps", "32gbps", "4gbps", "8gbps", "auto", "indeterminate"], []), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["E", "F", "SD", "access", "fabric", "n_proxy", "promiscuousAccess", "promiscuousTrunk", "trunk", "unknown", "vntag"], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_speed": MoPropertyMeta("oper_speed", "operSpeed", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["16gbps", "1gbps", "2gbps", "32gbps", "4gbps", "8gbps", "auto", "indeterminate"], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error-disabled", "failed", "hardware-failure", "indeterminate", "link-down", "link-up", "no-license", "sfp-not-present", "software-failure", "udld-aggr-down", "up"], []), 
        "peer_aggr_port_id": MoPropertyMeta("peer_aggr_port_id", "peerAggrPortId", "uint", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "peer_chassis_id": MoPropertyMeta("peer_chassis_id", "peerChassisId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["N/A"], ["0-255"]), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "peer_port_id": MoPropertyMeta("peer_port_id", "peerPortId", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "peer_slot_id": MoPropertyMeta("peer_slot_id", "peerSlotId", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "port_capability": MoPropertyMeta("port_capability", "portCapability", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ethAppliantPort", "ethFexServerPort", "ethRackServerPort", "ethUplinkPort", "unknown"], []), 
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "state_qual": MoPropertyMeta("state_qual", "stateQual", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []), 
        "ts": MoPropertyMeta("ts", "ts", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
        "unified_port": MoPropertyMeta("unified_port", "unifiedPort", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "wwn": MoPropertyMeta("wwn", "wwn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
        "xcvr_type": MoPropertyMeta("xcvr_type", "xcvrType", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1000basecx", "1000baselh", "1000baselx", "1000basesx", "1000baset", "1000baseunknown", "1000basevx", "1000basex", "1000basezx", "10gbaseer", "10gbaselr", "10gbaselrm", "10gbasesr", "10gbasezr", "cwdm1471", "cwdm1531", "cwdm1551", "dwdmsfp", "fet", "h10gacu10m", "h10gacu15m", "h10gacu1m", "h10gacu3m", "h10gacu5m", "h10gacu7m", "h10gacuaoc10m", "h10gacuaoc15m", "h10gacuaoc1m", "h10gacuaoc2m", "h10gacuaoc3m", "h10gacuaoc5m", "h10gacuaoc7m", "h10gaoc10m", "h10gaoc1m", "h10gaoc2m", "h10gaoc3m", "h10gaoc5m", "h10gaoc7m", "h10gcu10m", "h10gcu1m", "h10gcu2m", "h10gcu3m", "h10gcu5m", "h10gcu7m", "h10glrmsm", "h10gusr", "qsfp40gcr4", "qsfp40gcsr4", "qsfp40gfet", "qsfp40glr4", "qsfp40gsr4", "qsfp40gsrbd", "qsfp4sfp10gcu1m", "qsfp4sfp10gcu2m", "qsfp4sfp10gcu3m", "qsfp4sfp10gcu5m", "qsfp4x10ga0c10m", "qsfp4x10ga0c1m", "qsfp4x10ga0c2m", "qsfp4x10ga0c3m", "qsfp4x10ga0c5m", "qsfp4x10ga0c7m", "qsfp4x10ga0cunknown", "qsfp4x10gac10m", "qsfp4x10gac1m", "qsfp4x10gac3m", "qsfp4x10gac5m", "qsfp4x10gac7m", "qsfp4x10glr", "qsfph40gacu10m", "qsfph40gacu1m", "qsfph40gacu3m", "qsfph40gacu5m", "qsfph40gacu7m", "qsfph40gaoc10m", "qsfph40gaoc15m", "qsfph40gaoc1m", "qsfph40gaoc2m", "qsfph40gaoc3m", "qsfph40gaoc5m", "qsfph40gaoc7m", "qsfph40gaocunknown", "qsfph40gcu1m", "qsfph40gcu2m", "qsfph40gcu3m", "qsfph40gcu5m", "qsfploop", "qsfpqsa", "qsfpunknown", "sfp", "unknown", "x2"], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "adminTransport": "admin_transport", 
        "aggrPortId": "aggr_port_id", 
        "chassisId": "chassis_id", 
        "childAction": "child_action", 
        "dn": "dn", 
        "encap": "encap", 
        "epDn": "ep_dn", 
        "fltAggr": "flt_aggr", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "isBreakoutXcvr": "is_breakout_xcvr", 
        "isPortChannelMember": "is_port_channel_member", 
        "lc": "lc", 
        "licGP": "lic_gp", 
        "licState": "lic_state", 
        "locale": "locale", 
        "maxSpeed": "max_speed", 
        "mode": "mode", 
        "model": "model", 
        "name": "name", 
        "operSpeed": "oper_speed", 
        "operState": "oper_state", 
        "peerAggrPortId": "peer_aggr_port_id", 
        "peerChassisId": "peer_chassis_id", 
        "peerDn": "peer_dn", 
        "peerPortId": "peer_port_id", 
        "peerSlotId": "peer_slot_id", 
        "portCapability": "port_capability", 
        "portId": "port_id", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "slotId": "slot_id", 
        "stateQual": "state_qual", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "ts": "ts", 
        "type": "type", 
        "unifiedPort": "unified_port", 
        "usrLbl": "usr_lbl", 
        "vendor": "vendor", 
        "wwn": "wwn", 
        "xcvrType": "xcvr_type", 
    }

    def __init__(self, parent_mo_or_dn, port_id, **kwargs):
        self._dirty_mask = 0
        self.port_id = port_id
        self.admin_state = None
        self.admin_transport = None
        self.aggr_port_id = None
        self.chassis_id = None
        self.child_action = None
        self.encap = None
        self.ep_dn = None
        self.flt_aggr = None
        self.if_role = None
        self.if_type = None
        self.is_breakout_xcvr = None
        self.is_port_channel_member = None
        self.lc = None
        self.lic_gp = None
        self.lic_state = None
        self.locale = None
        self.max_speed = None
        self.mode = None
        self.model = None
        self.name = None
        self.oper_speed = None
        self.oper_state = None
        self.peer_aggr_port_id = None
        self.peer_chassis_id = None
        self.peer_dn = None
        self.peer_port_id = None
        self.peer_slot_id = None
        self.port_capability = None
        self.revision = None
        self.serial = None
        self.slot_id = None
        self.state_qual = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.ts = None
        self.type = None
        self.unified_port = None
        self.usr_lbl = None
        self.vendor = None
        self.wwn = None
        self.xcvr_type = None

        ManagedObject.__init__(self, "FcPIo", parent_mo_or_dn, **kwargs)

