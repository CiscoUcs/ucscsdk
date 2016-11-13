"""This module contains the general information for IdentIdentCtx ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IdentIdentCtxConsts():
    CONS_TYPE_CHASSIS = "chassis"
    CONS_TYPE_SERVER = "server"
    CONS_TYPE_VHBA = "vhba"
    CONS_TYPE_VM = "vm"
    CONS_TYPE_VMNIC = "vmnic"
    CONS_TYPE_VNIC = "vnic"
    DEFINED_IN_IDM_NO = "no"
    DEFINED_IN_IDM_YES = "yes"
    GLOBAL_ASSIGNED_CNT_NOT_DEFINED_IN_POOL = "not-defined-in-pool"
    GLOBAL_DEFINED_CNT_NOT_DEFINED_IN_POOL = "not-defined-in-pool"
    IDENT_TYPE_IP_V4 = "ipV4"
    IDENT_TYPE_IP_V6 = "ipV6"
    IDENT_TYPE_IQN = "iqn"
    IDENT_TYPE_MAC = "mac"
    IDENT_TYPE_UUID = "uuid"
    IDENT_TYPE_VLAN = "vlan"
    IDENT_TYPE_WWNN = "wwnn"
    IDENT_TYPE_WWPN = "wwpn"
    INTENT_ADD_POOLED = "add-pooled"
    INTENT_ASSIGN = "assign"
    INTENT_CHECK_DUPLICATE_ID = "check-duplicate-id"
    INTENT_DELETE_POOLED = "delete-pooled"
    INTENT_RE_EVALUATE = "re-evaluate"
    INTENT_REQUISITION = "requisition"
    INTENT_SYNC = "sync"
    INTENT_UNASSIGN = "unassign"
    RET_STATUS_ASSIGNED_BY_OTHER = "assigned-by-other"
    RET_STATUS_FAILED = "failed"
    RET_STATUS_IN_TRANSIT = "in-transit"
    RET_STATUS_OUT_OF_SYNC = "out-of-sync"
    RET_STATUS_SUCCEEDED = "succeeded"
    RET_STATUS_SYNCED = "synced"
    USING_QUALIFIED_POOL_NO = "no"
    USING_QUALIFIED_POOL_YES = "yes"


class IdentIdentCtx(ManagedObject):
    """This is IdentIdentCtx class."""

    consts = IdentIdentCtxConsts()
    naming_props = set([u'seqNum'])

    mo_meta = MoMeta("IdentIdentCtx", "identIdentCtx", "IdCtx-[seq_num]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["read-only"], [u'identIdentRequest'], [], [None])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cons_dn": MoPropertyMeta("cons_dn", "consDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "cons_type": MoPropertyMeta("cons_type", "consType", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["chassis", "server", "vhba", "vm", "vmnic", "vnic"], []), 
        "default_ident_pool_name": MoPropertyMeta("default_ident_pool_name", "defaultIdentPoolName", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "defined_in_idm": MoPropertyMeta("defined_in_idm", "definedInIdm", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "global_assigned_cnt": MoPropertyMeta("global_assigned_cnt", "globalAssignedCnt", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-defined-in-pool"], ["0-4294967295"]), 
        "global_defined_cnt": MoPropertyMeta("global_defined_cnt", "globalDefinedCnt", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-defined-in-pool"], ["0-4294967295"]), 
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "ident_type": MoPropertyMeta("ident_type", "identType", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipV4", "ipV6", "iqn", "mac", "uuid", "vlan", "wwnn", "wwpn"], []), 
        "intent": MoPropertyMeta("intent", "intent", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["add-pooled", "assign", "check-duplicate-id", "delete-pooled", "re-evaluate", "requisition", "sync", "unassign"], []), 
        "pool_dn": MoPropertyMeta("pool_dn", "poolDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "pool_org_dn": MoPropertyMeta("pool_org_dn", "poolOrgDn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "pooled_id": MoPropertyMeta("pooled_id", "pooledId", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "replaced_acquirer": MoPropertyMeta("replaced_acquirer", "replacedAcquirer", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "ret_status": MoPropertyMeta("ret_status", "retStatus", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["assigned-by-other", "failed", "in-transit", "out-of-sync", "succeeded", "synced"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "seq_num": MoPropertyMeta("seq_num", "seqNum", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suppl_id1": MoPropertyMeta("suppl_id1", "supplId1", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "suppl_id2": MoPropertyMeta("suppl_id2", "supplId2", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "suppl_id3": MoPropertyMeta("suppl_id3", "supplId3", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "suppl_id4": MoPropertyMeta("suppl_id4", "supplId4", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "using_qualified_pool": MoPropertyMeta("using_qualified_pool", "usingQualifiedPool", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
    }

    prop_map = {
        "assigned": "assigned", 
        "childAction": "child_action", 
        "consDn": "cons_dn", 
        "consType": "cons_type", 
        "defaultIdentPoolName": "default_ident_pool_name", 
        "definedInIdm": "defined_in_idm", 
        "dn": "dn", 
        "globalAssignedCnt": "global_assigned_cnt", 
        "globalDefinedCnt": "global_defined_cnt", 
        "identPoolName": "ident_pool_name", 
        "identType": "ident_type", 
        "intent": "intent", 
        "poolDn": "pool_dn", 
        "poolOrgDn": "pool_org_dn", 
        "pooledId": "pooled_id", 
        "replacedAcquirer": "replaced_acquirer", 
        "retStatus": "ret_status", 
        "rn": "rn", 
        "seqNum": "seq_num", 
        "status": "status", 
        "supplId1": "suppl_id1", 
        "supplId2": "suppl_id2", 
        "supplId3": "suppl_id3", 
        "supplId4": "suppl_id4", 
        "usingQualifiedPool": "using_qualified_pool", 
    }

    def __init__(self, parent_mo_or_dn, seq_num, **kwargs):
        self._dirty_mask = 0
        self.seq_num = seq_num
        self.assigned = None
        self.child_action = None
        self.cons_dn = None
        self.cons_type = None
        self.default_ident_pool_name = None
        self.defined_in_idm = None
        self.global_assigned_cnt = None
        self.global_defined_cnt = None
        self.ident_pool_name = None
        self.ident_type = None
        self.intent = None
        self.pool_dn = None
        self.pool_org_dn = None
        self.pooled_id = None
        self.replaced_acquirer = None
        self.ret_status = None
        self.status = None
        self.suppl_id1 = None
        self.suppl_id2 = None
        self.suppl_id3 = None
        self.suppl_id4 = None
        self.using_qualified_pool = None

        ManagedObject.__init__(self, "IdentIdentCtx", parent_mo_or_dn, **kwargs)

