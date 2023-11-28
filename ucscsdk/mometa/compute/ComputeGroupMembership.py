"""This module contains the general information for ComputeGroupMembership ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeGroupMembershipConsts():
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    CONFIG_STATE_OK = "ok"
    OWNER_MANAGEMENT = "management"
    OWNER_POLICY = "policy"


class ComputeGroupMembership(ManagedObject):
    """This is ComputeGroupMembership class."""

    consts = ComputeGroupMembershipConsts()
    naming_props = set(['ip'])

    mo_meta = MoMeta("ComputeGroupMembership", "computeGroupMembership", "membership-[ip]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin", "domain-group-management"], ['computeResourceAggrEp'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applied", "ok"], []), 
        "config_status_message": MoPropertyMeta("config_status_message", "configStatusMessage", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "group_dn": MoPropertyMeta("group_dn", "groupDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, None, [], []), 
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "oper_group_dn": MoPropertyMeta("oper_group_dn", "operGroupDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["management", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configState": "config_state", 
        "configStatusMessage": "config_status_message", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "groupDn": "group_dn", 
        "ip": "ip", 
        "operGroupDn": "oper_group_dn", 
        "owner": "owner", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, ip, **kwargs):
        self._dirty_mask = 0
        self.ip = ip
        self.child_action = None
        self.config_state = None
        self.config_status_message = None
        self.flt_aggr = None
        self.group_dn = None
        self.oper_group_dn = None
        self.owner = None
        self.status = None

        ManagedObject.__init__(self, "ComputeGroupMembership", parent_mo_or_dn, **kwargs)

