"""This module contains the general information for HcDriverInfoItem ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class HcDriverInfoItemConsts():
    pass


class HcDriverInfoItem(ManagedObject):
    """This is HcDriverInfoItem class."""

    consts = HcDriverInfoItemConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("HcDriverInfoItem", "hcDriverInfoItem", "driver-[id]", None, "InputOutput", 0x1ff, [], ["admin"], [u'hcHolder'], [], [None])

    prop_meta = {
        "adapter_pid": MoPropertyMeta("adapter_pid", "adapterPid", "string", None, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", None, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "protocol": MoPropertyMeta("protocol", "protocol", "string", None, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", None, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []), 
        "version": MoPropertyMeta("version", "version", "string", None, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], []), 
    }

    prop_map = {
        "adapterPid": "adapter_pid", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "protocol": "protocol", 
        "rn": "rn", 
        "status": "status", 
        "vendor": "vendor", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.adapter_pid = None
        self.child_action = None
        self.protocol = None
        self.status = None
        self.vendor = None
        self.version = None

        ManagedObject.__init__(self, "HcDriverInfoItem", parent_mo_or_dn, **kwargs)

