"""This module contains the general information for FcpoolFormat ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FcpoolFormatConsts():
    MASK_FF_FF_FF_FF_FF_FF_FF_FX = "FF:FF:FF:FF:FF:FF:FF:Fx"
    MASK_FF_FF_FF_FF_FF_FF_FF_XX = "FF:FF:FF:FF:FF:FF:FF:xx"
    MASK_FF_FF_FF_FF_FF_FF_FX_XX = "FF:FF:FF:FF:FF:FF:Fx:xx"
    MASK_FF_FF_FF_FF_FF_FF_XX_XX = "FF:FF:FF:FF:FF:FF:xx:xx"
    MASK_FF_FF_FF_FF_FF_FX_XX_XX = "FF:FF:FF:FF:FF:Fx:xx:xx"
    MASK_FF_FF_FF_FF_FF_XX_XX_XX = "FF:FF:FF:FF:FF:xx:xx:xx"
    MASK_FF_FF_FF_FF_FX_XX_XX_XX = "FF:FF:FF:FF:Fx:xx:xx:xx"
    MASK_FF_FF_FF_FF_XX_XX_XX_XX = "FF:FF:FF:FF:xx:xx:xx:xx"
    MASK_FF_FF_FF_FX_XX_XX_XX_XX = "FF:FF:FF:Fx:xx:xx:xx:xx"
    MASK_FF_FF_FF_XX_XX_XX_XX_XX = "FF:FF:FF:xx:xx:xx:xx:xx"
    MASK_FF_FF_FX_XX_XX_XX_XX_XX = "FF:FF:Fx:xx:xx:xx:xx:xx"
    MASK_FF_FF_XX_XX_XX_XX_XX_XX = "FF:FF:xx:xx:xx:xx:xx:xx"
    MASK_FF_FX_XX_XX_XX_XX_XX_XX = "FF:Fx:xx:xx:xx:xx:xx:xx"
    MASK_FF_XX_XX_XX_XX_XX_XX_XX = "FF:xx:xx:xx:xx:xx:xx:xx"
    MASK_FX_XX_XX_XX_XX_XX_XX_XX = "Fx:xx:xx:xx:xx:xx:xx:xx"


class FcpoolFormat(ManagedObject):
    """This is FcpoolFormat class."""

    consts = FcpoolFormatConsts()
    naming_props = set(['format', 'mask'])

    mo_meta = MoMeta("FcpoolFormat", "fcpoolFormat", "format-[format]-[mask]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin", "ext-san-config", "ext-san-policy", "ls-storage", "ls-storage-policy"], ['fcpoolUniverse'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "format": MoPropertyMeta("format", "format", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
        "mask": MoPropertyMeta("mask", "mask", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, None, None, None, ["FF:FF:FF:FF:FF:FF:FF:Fx", "FF:FF:FF:FF:FF:FF:FF:xx", "FF:FF:FF:FF:FF:FF:Fx:xx", "FF:FF:FF:FF:FF:FF:xx:xx", "FF:FF:FF:FF:FF:Fx:xx:xx", "FF:FF:FF:FF:FF:xx:xx:xx", "FF:FF:FF:FF:Fx:xx:xx:xx", "FF:FF:FF:FF:xx:xx:xx:xx", "FF:FF:FF:Fx:xx:xx:xx:xx", "FF:FF:FF:xx:xx:xx:xx:xx", "FF:FF:Fx:xx:xx:xx:xx:xx", "FF:FF:xx:xx:xx:xx:xx:xx", "FF:Fx:xx:xx:xx:xx:xx:xx", "FF:xx:xx:xx:xx:xx:xx:xx", "Fx:xx:xx:xx:xx:xx:xx:xx"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "format": "format", 
        "mask": "mask", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, format, mask, **kwargs):
        self._dirty_mask = 0
        self.format = format
        self.mask = mask
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "FcpoolFormat", parent_mo_or_dn, **kwargs)

