"""This module contains the general information for TrigTokenRequestor ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class TrigTokenRequestorConsts():
    ADMIN_STATE_AUTO_SCHED = "auto-sched"
    ADMIN_STATE_FORCE_ACK = "force-ack"
    ADMIN_STATE_SCHED_ACK = "sched-ack"
    OPER_STATE_CAP_REACHED = "cap-reached"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_IN_PROGRESS = "in-progress"
    OPER_STATE_PENDING = "pending"
    OPER_STATE_PENDING_ACK = "pending-ack"
    OPER_STATE_TRIGGERED = "triggered"


class TrigTokenRequestor(ManagedObject):
    """This is TrigTokenRequestor class."""

    consts = TrigTokenRequestorConsts()
    naming_props = set(['id', 'name'])

    mo_meta = MoMeta("TrigTokenRequestor", "trigTokenRequestor", "tokenreq-[id]-[name]", VersionMeta.Version101a, "InputOutput", 0x7f, [], ["admin", "domain-group-management", "ls-compute", "ls-config", "ls-server"], ['trigMeta'], [], ["Get", "Set"])

    prop_meta = {
        "activity_ts": MoPropertyMeta("activity_ts", "activityTs", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["auto-sched", "force-ack", "sched-ack"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cap-reached", "failed", "in-progress", "pending", "pending-ack", "triggered"], []), 
        "owner_dn": MoPropertyMeta("owner_dn", "ownerDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "owner_ip": MoPropertyMeta("owner_ip", "ownerIp", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "owner_ipv4v6_addr": MoPropertyMeta("owner_ipv4v6_addr", "ownerIpv4v6Addr", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$|[a-fA-F0-9:\[\]]{1,39}""", [], []), 
        "owner_name": MoPropertyMeta("owner_name", "ownerName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "token_dn": MoPropertyMeta("token_dn", "tokenDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "triggerable_dn": MoPropertyMeta("triggerable_dn", "triggerableDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
    }

    prop_map = {
        "activityTs": "activity_ts", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "name": "name", 
        "operState": "oper_state", 
        "ownerDn": "owner_dn", 
        "ownerIp": "owner_ip", 
        "ownerIpv4v6Addr": "owner_ipv4v6_addr", 
        "ownerName": "owner_name", 
        "rn": "rn", 
        "status": "status", 
        "tokenDn": "token_dn", 
        "triggerableDn": "triggerable_dn", 
    }

    def __init__(self, parent_mo_or_dn, id, name, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.name = name
        self.activity_ts = None
        self.admin_state = None
        self.child_action = None
        self.oper_state = None
        self.owner_dn = None
        self.owner_ip = None
        self.owner_ipv4v6_addr = None
        self.owner_name = None
        self.status = None
        self.token_dn = None
        self.triggerable_dn = None

        ManagedObject.__init__(self, "TrigTokenRequestor", parent_mo_or_dn, **kwargs)

