"""This module contains the general information for FirmwareInstallImpact ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareInstallImpactConsts():
    pass


class FirmwareInstallImpact(ManagedObject):
    """This is FirmwareInstallImpact class."""

    consts = FirmwareInstallImpactConsts()
    naming_props = set(['keyDn'])

    mo_meta = MoMeta("FirmwareInstallImpact", "firmwareInstallImpact", "fw-sys-InstallImpact-[key_dn]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin"], [], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "key_dn": MoPropertyMeta("key_dn", "keyDn", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "keyDn": "key_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, key_dn, **kwargs):
        self._dirty_mask = 0
        self.key_dn = key_dn
        self.child_action = None
        self.descr = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareInstallImpact", parent_mo_or_dn, **kwargs)

