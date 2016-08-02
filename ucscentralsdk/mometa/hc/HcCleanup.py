"""This module contains the general information for HcCleanup ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class HcCleanupConsts():
    pass


class HcCleanup(ManagedObject):
    """This is HcCleanup class."""

    consts = HcCleanupConsts()
    naming_props = set([u'refDn'])

    mo_meta = MoMeta("HcCleanup", "hcCleanup", "cleanup-[ref_dn]", None, "InputOutput", 0x1f, [], ["read-only"], [u'hcAdmin'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ref_dn": MoPropertyMeta("ref_dn", "refDn", "string", None, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
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

