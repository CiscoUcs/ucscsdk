"""This module contains the general information for SesEnclosure ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class SesEnclosureConsts():
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"


class SesEnclosure(ManagedObject):
    """This is SesEnclosure class."""

    consts = SesEnclosureConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("SesEnclosure", "sesEnclosure", "ses-enc-[id]", None, "InputOutput", 0x3f, [], ["read-only"], [u'equipmentChassis'], [u'sesDiskSlotEp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", None, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "elid": MoPropertyMeta("elid", "elid", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", None, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "elid": "elid", 
        "id": "id", 
        "lc": "lc", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.descr = None
        self.elid = None
        self.lc = None
        self.status = None

        ManagedObject.__init__(self, "SesEnclosure", parent_mo_or_dn, **kwargs)

