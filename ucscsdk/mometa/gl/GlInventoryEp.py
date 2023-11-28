"""This module contains the general information for GlInventoryEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlInventoryEpConsts():
    TYPE_BOOT_MGR = "boot-mgr"
    TYPE_CENTRAL_MGR = "central-mgr"
    TYPE_IDENTIFIER_MGR = "identifier-mgr"
    TYPE_MANAGED_ENDPOINT = "managed-endpoint"
    TYPE_MGMT_CONTROLLER = "mgmt-controller"
    TYPE_OPERATION_MGR = "operation-mgr"
    TYPE_POLICY_MGR = "policy-mgr"
    TYPE_RESOURCE_AGGR = "resource-aggr"
    TYPE_RESOURCE_MGR = "resource-mgr"
    TYPE_SERVER_MGR = "server-mgr"
    TYPE_SERVICE_REG = "service-reg"
    TYPE_STATS_MGR = "stats-mgr"
    TYPE_STORAGE_BROKER = "storage-broker"
    TYPE_VIRTUAL_SWITCHING_MGR = "virtual-switching-mgr"
    TYPE_VM_MGR = "vm-mgr"


class GlInventoryEp(ManagedObject):
    """This is GlInventoryEp class."""

    consts = GlInventoryEpConsts()
    naming_props = set(['internalId'])

    mo_meta = MoMeta("GlInventoryEp", "glInventoryEp", "inv-[internal_id]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["read-only"], ['glPathEp', 'glRequest'], ['glPolicyInvEp', 'glPoolInvEp', 'glSPInvEp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "internal_id": MoPropertyMeta("internal_id", "internalId", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["boot-mgr", "central-mgr", "identifier-mgr", "managed-endpoint", "mgmt-controller", "operation-mgr", "policy-mgr", "resource-aggr", "resource-mgr", "server-mgr", "service-reg", "stats-mgr", "storage-broker", "virtual-switching-mgr", "vm-mgr"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "index": "index", 
        "internalId": "internal_id", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, internal_id, **kwargs):
        self._dirty_mask = 0
        self.internal_id = internal_id
        self.child_action = None
        self.index = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "GlInventoryEp", parent_mo_or_dn, **kwargs)

