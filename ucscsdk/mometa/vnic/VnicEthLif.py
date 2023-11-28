"""This module contains the general information for VnicEthLif ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicEthLifConsts():
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"
    TYPE_ETHER = "ether"
    TYPE_FC = "fc"
    TYPE_IPC = "ipc"
    TYPE_SCSI = "scsi"
    TYPE_UNKNOWN = "unknown"


class VnicEthLif(ManagedObject):
    """This is VnicEthLif class."""

    consts = VnicEthLifConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicEthLif", "vnicEthLif", "eth-lif-[name]", VersionMeta.Version131a, "InputOutput", 0x1ff, [], ["admin", "ls-storage"], [], [], ["Get"])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "nic_dn": MoPropertyMeta("nic_dn", "nicDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], []), 
        "vnic_dn": MoPropertyMeta("vnic_dn", "vnicDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x100, 0, 256, None, [], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "nicDn": "nic_dn", 
        "owner": "owner", 
        "rn": "rn", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
        "vnicDn": "vnic_dn", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.addr = None
        self.child_action = None
        self.nic_dn = None
        self.owner = None
        self.status = None
        self.switch_id = None
        self.type = None
        self.vnic_dn = None

        ManagedObject.__init__(self, "VnicEthLif", parent_mo_or_dn, **kwargs)

