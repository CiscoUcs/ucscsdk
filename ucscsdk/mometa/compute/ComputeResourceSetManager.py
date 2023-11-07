"""This module contains the general information for ComputeResourceSetManager ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ComputeResourceSetManagerConsts():
    POLLING_STATE_COMPLETE = "complete"
    POLLING_STATE_INIT_DONE = "init-done"
    POLLING_STATE_PENDING_REBALANCE = "pending-rebalance"
    POLLING_STATE_REBALANCING = "rebalancing"
    POLLING_STATE_STARTED = "started"
    POLLING_STATE_SYSTEM_INIT = "system-init"


class ComputeResourceSetManager(ManagedObject):
    """This is ComputeResourceSetManager class."""

    consts = ComputeResourceSetManagerConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeResourceSetManager", "computeResourceSetManager", "rsrc-set-mgr", VersionMeta.Version101a, "InputOutput", 0xf, [], ["admin"], ['computeResourceAggrEp'], ['computeResourceSet'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "current_set_in_polling": MoPropertyMeta("current_set_in_polling", "currentSetInPolling", "ushort", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "polling_state": MoPropertyMeta("polling_state", "pollingState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["complete", "init-done", "pending-rebalance", "rebalancing", "started", "system-init"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "currentSetInPolling": "current_set_in_polling", 
        "dn": "dn", 
        "pollingState": "polling_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.current_set_in_polling = None
        self.polling_state = None
        self.status = None

        ManagedObject.__init__(self, "ComputeResourceSetManager", parent_mo_or_dn, **kwargs)

