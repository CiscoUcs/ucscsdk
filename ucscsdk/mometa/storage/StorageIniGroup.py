"""This module contains the general information for StorageIniGroup ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageIniGroupConsts():
    INT_ID_NONE = "none"
    OPER_PROTOCOL_DERIVED = "derived"
    OPER_PROTOCOL_FC = "fc"
    OPER_PROTOCOL_ISCSI = "iscsi"
    OPER_STATE_MISCONFIGURED = "misconfigured"
    OPER_STATE_OK = "ok"
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PROTOCOL_DERIVED = "derived"
    PROTOCOL_FC = "fc"
    PROTOCOL_ISCSI = "iscsi"


class StorageIniGroup(ManagedObject):
    """This is StorageIniGroup class."""

    consts = StorageIniGroupConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("StorageIniGroup", "storageIniGroup", "grp-[name]", VersionMeta.Version111a, "InputOutput", 0x3ff, [], ["admin", "ls-config", "ls-server", "ls-storage", "ls-storage-policy"], ['lsServer', 'vnicSanConnPolicy'], ['faultInst', 'storageInitiator', 'vnicFcGroupDef'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "group_policy_name": MoPropertyMeta("group_policy_name", "groupPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_protocol": MoPropertyMeta("oper_protocol", "operProtocol", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["derived", "fc", "iscsi"], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["misconfigured", "ok"], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_name": MoPropertyMeta("policy_name", "policyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version111a, MoPropertyMeta.CREATE_ONLY, 0x40, None, None, None, ["derived", "fc", "iscsi"], []), 
        "rmt_disk_cfg_name": MoPropertyMeta("rmt_disk_cfg_name", "rmtDiskCfgName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "groupPolicyName": "group_policy_name", 
        "intId": "int_id", 
        "name": "name", 
        "operProtocol": "oper_protocol", 
        "operState": "oper_state", 
        "owner": "owner", 
        "policyLevel": "policy_level", 
        "policyName": "policy_name", 
        "policyOwner": "policy_owner", 
        "protocol": "protocol", 
        "rmtDiskCfgName": "rmt_disk_cfg_name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.group_policy_name = None
        self.int_id = None
        self.oper_protocol = None
        self.oper_state = None
        self.owner = None
        self.policy_level = None
        self.policy_name = None
        self.policy_owner = None
        self.protocol = None
        self.rmt_disk_cfg_name = None
        self.status = None

        ManagedObject.__init__(self, "StorageIniGroup", parent_mo_or_dn, **kwargs)

