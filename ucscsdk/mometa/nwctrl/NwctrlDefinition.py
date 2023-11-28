"""This module contains the general information for NwctrlDefinition ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class NwctrlDefinitionConsts():
    CDP_DISABLED = "disabled"
    CDP_ENABLED = "enabled"
    INT_ID_NONE = "none"
    LLDP_RECEIVE_DISABLED = "disabled"
    LLDP_RECEIVE_ENABLED = "enabled"
    LLDP_TRANSMIT_DISABLED = "disabled"
    LLDP_TRANSMIT_ENABLED = "enabled"
    MAC_REGISTER_MODE_ALL_HOST_VLANS = "all-host-vlans"
    MAC_REGISTER_MODE_ONLY_NATIVE_VLAN = "only-native-vlan"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    UPLINK_FAIL_ACTION_LINK_DOWN = "link-down"
    UPLINK_FAIL_ACTION_WARNING = "warning"


class NwctrlDefinition(ManagedObject):
    """This is NwctrlDefinition class."""

    consts = NwctrlDefinitionConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("NwctrlDefinition", "nwctrlDefinition", "nwctrl-[name]", VersionMeta.Version111a, "InputOutput", 0x7ff, [], ["read-only"], ['fabricEthEstcCloud', 'orgDomainGroup', 'orgOrg', 'policySystemEp'], ['dpsecMac'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "cdp": MoPropertyMeta("cdp", "cdp", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "lldp_receive": MoPropertyMeta("lldp_receive", "lldpReceive", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled"], []), 
        "lldp_transmit": MoPropertyMeta("lldp_transmit", "lldpTransmit", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled"], []), 
        "mac_register_mode": MoPropertyMeta("mac_register_mode", "macRegisterMode", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["all-host-vlans", "only-native-vlan"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "uplink_fail_action": MoPropertyMeta("uplink_fail_action", "uplinkFailAction", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["link-down", "warning"], []), 
    }

    prop_map = {
        "cdp": "cdp", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "lldpReceive": "lldp_receive", 
        "lldpTransmit": "lldp_transmit", 
        "macRegisterMode": "mac_register_mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
        "uplinkFailAction": "uplink_fail_action", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.cdp = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.lldp_receive = None
        self.lldp_transmit = None
        self.mac_register_mode = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None
        self.uplink_fail_action = None

        ManagedObject.__init__(self, "NwctrlDefinition", parent_mo_or_dn, **kwargs)

