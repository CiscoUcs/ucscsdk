"""This module contains the general information for HcSupportedAdapterFirmwareItem ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class HcSupportedAdapterFirmwareItemConsts():
    pass


class HcSupportedAdapterFirmwareItem(ManagedObject):
    """This is HcSupportedAdapterFirmwareItem class."""

    consts = HcSupportedAdapterFirmwareItemConsts()
    naming_props = set([u'itemId'])

    mo_meta = MoMeta("HcSupportedAdapterFirmwareItem", "hcSupportedAdapterFirmwareItem", "supported-adapter-firmware-[item_id]", None, "InputOutput", 0x3ff, [], ["admin"], [u'hcAdapterFirmwareItem'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "item_id": MoPropertyMeta("item_id", "itemId", "ulong", None, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "item_ref_dn": MoPropertyMeta("item_ref_dn", "itemRefDn", "string", None, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []), 
        "item_ref_id": MoPropertyMeta("item_ref_id", "itemRefId", "string", None, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, None, [], []), 
        "item_ref_model": MoPropertyMeta("item_ref_model", "itemRefModel", "string", None, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []), 
        "item_vendor": MoPropertyMeta("item_vendor", "itemVendor", "string", None, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []), 
        "item_version": MoPropertyMeta("item_version", "itemVersion", "string", None, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "itemId": "item_id", 
        "itemRefDn": "item_ref_dn", 
        "itemRefId": "item_ref_id", 
        "itemRefModel": "item_ref_model", 
        "itemVendor": "item_vendor", 
        "itemVersion": "item_version", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, item_id, **kwargs):
        self._dirty_mask = 0
        self.item_id = item_id
        self.child_action = None
        self.item_ref_dn = None
        self.item_ref_id = None
        self.item_ref_model = None
        self.item_vendor = None
        self.item_version = None
        self.status = None

        ManagedObject.__init__(self, "HcSupportedAdapterFirmwareItem", parent_mo_or_dn, **kwargs)

