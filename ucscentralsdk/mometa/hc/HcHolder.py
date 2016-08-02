"""This module contains the general information for HcHolder ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class HcHolderConsts():
    pass


class HcHolder(ManagedObject):
    """This is HcHolder class."""

    consts = HcHolderConsts()
    naming_props = set([])

    mo_meta = MoMeta("HcHolder", "hcHolder", "hc-ep", None, "InputOutput", 0xf, [], ["read-only"], [u'topRoot'], [u'hcAdmin', u'hcCatalog', u'hcCatalogList', u'hcCatalogVersion', u'hcDownloader', u'hcDriverInfoItem', u'hcOsInfoItem', u'hcReport', u'hcUcsVersionItem'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "HcHolder", **kwargs)

