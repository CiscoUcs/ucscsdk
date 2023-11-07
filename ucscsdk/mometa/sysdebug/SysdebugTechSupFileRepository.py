"""This module contains the general information for SysdebugTechSupFileRepository ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SysdebugTechSupFileRepositoryConsts():
    pass


class SysdebugTechSupFileRepository(ManagedObject):
    """This is SysdebugTechSupFileRepository class."""

    consts = SysdebugTechSupFileRepositoryConsts()
    naming_props = set([])

    mo_meta = MoMeta("SysdebugTechSupFileRepository", "sysdebugTechSupFileRepository", "tech-support-files", VersionMeta.Version101a, "InputOutput", 0xf, [], ["admin", "operations"], ['computeSystem', 'topSystem'], ['sysdebugTechSupport', 'sysdebugTechSupportOp', 'sysdebugTechSupportOperation'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "SysdebugTechSupFileRepository", parent_mo_or_dn, **kwargs)

