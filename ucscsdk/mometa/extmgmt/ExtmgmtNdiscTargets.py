"""This module contains the general information for ExtmgmtNdiscTargets ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ExtmgmtNdiscTargetsConsts():
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"


class ExtmgmtNdiscTargets(ManagedObject):
    """This is ExtmgmtNdiscTargets class."""

    consts = ExtmgmtNdiscTargetsConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtmgmtNdiscTargets", "extmgmtNdiscTargets", "ndisc-target-policy", VersionMeta.Version112a, "InputOutput", 0x1ff, [], ["admin", "domain-group-management", "ext-lan-config"], ['extmgmtIfMonPolicy'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []), 
        "config_status_message": MoPropertyMeta("config_status_message", "configStatusMessage", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ipv6_target1": MoPropertyMeta("ipv6_target1", "ipv6Target1", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, None, [], []), 
        "ipv6_target2": MoPropertyMeta("ipv6_target2", "ipv6Target2", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []), 
        "ipv6_target3": MoPropertyMeta("ipv6_target3", "ipv6Target3", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, None, [], []), 
        "max_deadline_timeout": MoPropertyMeta("max_deadline_timeout", "maxDeadlineTimeout", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["5-15"]), 
        "number_of_ndisc_requests": MoPropertyMeta("number_of_ndisc_requests", "numberOfNdiscRequests", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-5"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configState": "config_state", 
        "configStatusMessage": "config_status_message", 
        "dn": "dn", 
        "ipv6Target1": "ipv6_target1", 
        "ipv6Target2": "ipv6_target2", 
        "ipv6Target3": "ipv6_target3", 
        "maxDeadlineTimeout": "max_deadline_timeout", 
        "numberOfNdiscRequests": "number_of_ndisc_requests", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_state = None
        self.config_status_message = None
        self.ipv6_target1 = None
        self.ipv6_target2 = None
        self.ipv6_target3 = None
        self.max_deadline_timeout = None
        self.number_of_ndisc_requests = None
        self.status = None

        ManagedObject.__init__(self, "ExtmgmtNdiscTargets", parent_mo_or_dn, **kwargs)

