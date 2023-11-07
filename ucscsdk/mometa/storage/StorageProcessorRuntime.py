"""This module contains the general information for StorageProcessorRuntime ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageProcessorRuntimeConsts():
    pass


class StorageProcessorRuntime(ManagedObject):
    """This is StorageProcessorRuntime class."""

    consts = StorageProcessorRuntimeConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageProcessorRuntime", "storageProcessorRuntime", "proc-runtime", VersionMeta.Version131a, "InputOutput", 0xf, [], ["read-only"], ['storageProcessor'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "unplanned_shutdown": MoPropertyMeta("unplanned_shutdown", "unplannedShutdown", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "unplannedShutdown": "unplanned_shutdown", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.unplanned_shutdown = None

        ManagedObject.__init__(self, "StorageProcessorRuntime", parent_mo_or_dn, **kwargs)

