"""This module contains the general information for MgmtInterface ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtInterfaceConsts():
    CONFIG_STATE_INCOMPLETE = "incomplete"
    CONFIG_STATE_INVALID_PINNING = "invalidPinning"
    CONFIG_STATE_UNRESOLVED_VLAN = "unresolvedVlan"
    CONFIG_STATE_UNSUPPORTED_FIRMWARE = "unsupportedFirmware"
    CONFIG_STATE_UNSUPPORTED_SERVER = "unsupportedServer"
    CONFIG_STATE_UNSUPPORTED_VLAN = "unsupportedVlan"
    CONFIG_STATE_VALID = "valid"
    IP_V4_STATE_NONE = "none"
    IP_V4_STATE_POOLED = "pooled"
    IP_V4_STATE_STATIC = "static"
    IP_V6_STATE_NONE = "none"
    IP_V6_STATE_POOLED = "pooled"
    IP_V6_STATE_STATIC = "static"
    IS_DEFAULT_DERIVED_FALSE = "false"
    IS_DEFAULT_DERIVED_NO = "no"
    IS_DEFAULT_DERIVED_TRUE = "true"
    IS_DEFAULT_DERIVED_YES = "yes"
    MODE_IN_BAND = "in-band"
    OPER_STATE_DEPLOYED = "deployed"
    OPER_STATE_DOWN = "down"
    OPER_STATE_NOT_DEPLOYED = "notDeployed"
    OPER_STATE_UNKNOWN = "unknown"
    OPER_STATE_UP = "up"


class MgmtInterface(ManagedObject):
    """This is MgmtInterface class."""

    consts = MgmtInterfaceConsts()
    naming_props = set(['mode'])

    mo_meta = MoMeta("MgmtInterface", "mgmtInterface", "iface-[mode]", VersionMeta.Version112a, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], ['computeInstance', 'lsServer', 'mgmtController'], ['mgmtVnet'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_message": MoPropertyMeta("config_message", "configMessage", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["incomplete", "invalidPinning", "unresolvedVlan", "unsupportedFirmware", "unsupportedServer", "unsupportedVlan", "valid"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ip_v4_state": MoPropertyMeta("ip_v4_state", "ipV4State", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["none", "pooled", "static"], []), 
        "ip_v6_state": MoPropertyMeta("ip_v6_state", "ipV6State", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["none", "pooled", "static"], []), 
        "is_default_derived": MoPropertyMeta("is_default_derived", "isDefaultDerived", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["in-band"], []), 
        "monitor_interval": MoPropertyMeta("monitor_interval", "monitorInterval", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["deployed", "down", "notDeployed", "unknown", "up"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configMessage": "config_message", 
        "configState": "config_state", 
        "dn": "dn", 
        "ipV4State": "ip_v4_state", 
        "ipV6State": "ip_v6_state", 
        "isDefaultDerived": "is_default_derived", 
        "mode": "mode", 
        "monitorInterval": "monitor_interval", 
        "operState": "oper_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, mode, **kwargs):
        self._dirty_mask = 0
        self.mode = mode
        self.child_action = None
        self.config_message = None
        self.config_state = None
        self.ip_v4_state = None
        self.ip_v6_state = None
        self.is_default_derived = None
        self.monitor_interval = None
        self.oper_state = None
        self.status = None

        ManagedObject.__init__(self, "MgmtInterface", parent_mo_or_dn, **kwargs)

