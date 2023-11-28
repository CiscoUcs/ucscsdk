"""This module contains the general information for HcOsInfoItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class HcOsInfoItemConsts():
    pass


class HcOsInfoItem(ManagedObject):
    """This is HcOsInfoItem class."""

    consts = HcOsInfoItemConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("HcOsInfoItem", "hcOsInfoItem", "os-[id]", VersionMeta.Version151a, "InputOutput", 0x7f, [], ["admin"], ['hcHolder'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "rn": "rn", 
        "status": "status", 
        "vendor": "vendor", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.status = None
        self.vendor = None
        self.version = None

        ManagedObject.__init__(self, "HcOsInfoItem", parent_mo_or_dn, **kwargs)

