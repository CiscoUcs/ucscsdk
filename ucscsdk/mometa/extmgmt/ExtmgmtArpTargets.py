"""This module contains the general information for ExtmgmtArpTargets ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ExtmgmtArpTargetsConsts():
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"


class ExtmgmtArpTargets(ManagedObject):
    """This is ExtmgmtArpTargets class."""

    consts = ExtmgmtArpTargetsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtmgmtArpTargets", "extmgmtArpTargets", "arp-target-policy", VersionMeta.Version101a, "InputOutput", 0x1ff, [], ["admin", "domain-group-management", "ext-lan-config"], ['extmgmtIfMonPolicy'], [], ["Add", "Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []), 
        "config_status_message": MoPropertyMeta("config_status_message", "configStatusMessage", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "max_deadline_timeout": MoPropertyMeta("max_deadline_timeout", "maxDeadlineTimeout", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["5-15"]), 
        "number_of_arp_requests": MoPropertyMeta("number_of_arp_requests", "numberOfArpRequests", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-5"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "target_ip1": MoPropertyMeta("target_ip1", "targetIp1", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "target_ip2": MoPropertyMeta("target_ip2", "targetIp2", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "target_ip3": MoPropertyMeta("target_ip3", "targetIp3", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configState": "config_state", 
        "configStatusMessage": "config_status_message", 
        "dn": "dn", 
        "maxDeadlineTimeout": "max_deadline_timeout", 
        "numberOfArpRequests": "number_of_arp_requests", 
        "rn": "rn", 
        "status": "status", 
        "targetIp1": "target_ip1", 
        "targetIp2": "target_ip2", 
        "targetIp3": "target_ip3", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_state = None
        self.config_status_message = None
        self.max_deadline_timeout = None
        self.number_of_arp_requests = None
        self.status = None
        self.target_ip1 = None
        self.target_ip2 = None
        self.target_ip3 = None

        ManagedObject.__init__(self, "ExtmgmtArpTargets", parent_mo_or_dn, **kwargs)

