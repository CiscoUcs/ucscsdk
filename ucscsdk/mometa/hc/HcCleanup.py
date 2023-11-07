"""This module contains the general information for HcCleanup ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class HcCleanupConsts():
    pass


class HcCleanup(ManagedObject):
    """This is HcCleanup class."""

    consts = HcCleanupConsts()
    naming_props = set(['refDn'])

    mo_meta = MoMeta("HcCleanup", "hcCleanup", "cleanup-[ref_dn]", VersionMeta.Version151a, "InputOutput", 0x1f, [], ["read-only"], ['hcAdmin'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ref_dn": MoPropertyMeta("ref_dn", "refDn", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "refDn": "ref_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, ref_dn, **kwargs):
        self._dirty_mask = 0
        self.ref_dn = ref_dn
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "HcCleanup", parent_mo_or_dn, **kwargs)

