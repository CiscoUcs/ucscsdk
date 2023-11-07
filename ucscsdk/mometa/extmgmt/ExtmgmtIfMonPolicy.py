"""This module contains the general information for ExtmgmtIfMonPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ExtmgmtIfMonPolicyConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    ENABLE_HAFAILOVER_FALSE = "false"
    ENABLE_HAFAILOVER_NO = "no"
    ENABLE_HAFAILOVER_TRUE = "true"
    ENABLE_HAFAILOVER_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class ExtmgmtIfMonPolicy(ManagedObject):
    """This is ExtmgmtIfMonPolicy class."""

    consts = ExtmgmtIfMonPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtmgmtIfMonPolicy", "extmgmtIfMonPolicy", "extmgmt-intf-monitor-policy", VersionMeta.Version101a, "InputOutput", 0x7ff, [], ["admin", "domain-group-management", "ext-lan-config"], ['orgDomainGroup', 'policyDeviceProfile'], ['extmgmtArpTargets', 'extmgmtGatewayPing', 'extmgmtMiiStatus', 'extmgmtNdiscTargets'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "enable_ha_failover": MoPropertyMeta("enable_ha_failover", "enableHAFailover", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "max_fail_report_count": MoPropertyMeta("max_fail_report_count", "maxFailReportCount", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["2-5"]), 
        "monitor_mechanism": MoPropertyMeta("monitor_mechanism", "monitorMechanism", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "poll_interval": MoPropertyMeta("poll_interval", "pollInterval", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["90-300"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "enableHAFailover": "enable_ha_failover", 
        "intId": "int_id", 
        "maxFailReportCount": "max_fail_report_count", 
        "monitorMechanism": "monitor_mechanism", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "pollInterval": "poll_interval", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.enable_ha_failover = None
        self.int_id = None
        self.max_fail_report_count = None
        self.monitor_mechanism = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.poll_interval = None
        self.status = None

        ManagedObject.__init__(self, "ExtmgmtIfMonPolicy", parent_mo_or_dn, **kwargs)

