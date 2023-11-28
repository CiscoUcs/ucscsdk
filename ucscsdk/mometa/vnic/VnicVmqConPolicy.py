"""This module contains the general information for VnicVmqConPolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicVmqConPolicyConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class VnicVmqConPolicy(ManagedObject):
    """This is VnicVmqConPolicy class."""

    consts = VnicVmqConPolicyConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicVmqConPolicy", "vnicVmqConPolicy", "vmq-con-[name]", VersionMeta.Version112a, "InputOutput", 0x7ff, [], ["admin", "ls-compute", "ls-network", "ls-network-policy", "ls-server"], ['orgOrg'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version201f, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "intr_count": MoPropertyMeta("intr_count", "intrCount", "ushort", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-128"]), 
        "multi_queue": MoPropertyMeta("multi_queue", "multiQueue", "string", VersionMeta.Version201f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vmmq_sub_vnics": MoPropertyMeta("vmmq_sub_vnics", "vmmqSubVnics", "ushort", VersionMeta.Version201f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["1-256"]), 
        "vmq_count": MoPropertyMeta("vmq_count", "vmqCount", "ushort", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], ["1-128"]), 
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "intrCount": "intr_count", 
        "multiQueue": "multi_queue", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
        "vmmqSubVnics": "vmmq_sub_vnics", 
        "vmqCount": "vmq_count", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.adaptor_profile_name = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.intr_count = None
        self.multi_queue = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None
        self.vmmq_sub_vnics = None
        self.vmq_count = None

        ManagedObject.__init__(self, "VnicVmqConPolicy", parent_mo_or_dn, **kwargs)

