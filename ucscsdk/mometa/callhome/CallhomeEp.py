"""This module contains the general information for CallhomeEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class CallhomeEpConsts():
    ADMIN_STATE_OFF = "off"
    ADMIN_STATE_ON = "on"
    ALERT_THROTTLING_ADMIN_STATE_OFF = "off"
    ALERT_THROTTLING_ADMIN_STATE_ON = "on"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class CallhomeEp(ManagedObject):
    """This is CallhomeEp class."""

    consts = CallhomeEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("CallhomeEp", "callhomeEp", "call-home", VersionMeta.Version101a, "InputOutput", 0xff, [], ["admin", "operations"], ['callhomeHolder', 'orgDomainGroup', 'orgOrg', 'policyDeviceProfile', 'smartlicenseHolder'], ['callhomeFaultInst', 'callhomeHttp', 'callhomePeriodicSystemInventory', 'callhomePolicy', 'callhomeProfile', 'callhomeSmtp', 'callhomeSource', 'callhomeTestAlert', 'smartcallhomeHttpProxy', 'smartcallhomePeriodicSystemInventory', 'smartcallhomePolicy', 'smartcallhomeProfile', 'smartcallhomeSource', 'smartcallhomeTransportGateway'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["off", "on"], []), 
        "alert_throttling_admin_state": MoPropertyMeta("alert_throttling_admin_state", "alertThrottlingAdminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["off", "on"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "alertThrottlingAdminState": "alert_throttling_admin_state", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.alert_throttling_admin_state = None
        self.child_action = None
        self.config_state = None
        self.descr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None

        ManagedObject.__init__(self, "CallhomeEp", parent_mo_or_dn, **kwargs)

