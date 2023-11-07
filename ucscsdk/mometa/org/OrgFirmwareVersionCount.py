"""This module contains the general information for OrgFirmwareVersionCount ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class OrgFirmwareVersionCountConsts():
    pass


class OrgFirmwareVersionCount(ManagedObject):
    """This is OrgFirmwareVersionCount class."""

    consts = OrgFirmwareVersionCountConsts()
    naming_props = set(['firmwareVersion'])

    mo_meta = MoMeta("OrgFirmwareVersionCount", "orgFirmwareVersionCount", "fw-version-count-[firmware_version]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['orgDomainGroupFirmwareReport'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "count": MoPropertyMeta("count", "count", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "firmware_version": MoPropertyMeta("firmware_version", "firmwareVersion", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "count": "count", 
        "dn": "dn", 
        "firmwareVersion": "firmware_version", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, firmware_version, **kwargs):
        self._dirty_mask = 0
        self.firmware_version = firmware_version
        self.child_action = None
        self.count = None
        self.status = None

        ManagedObject.__init__(self, "OrgFirmwareVersionCount", parent_mo_or_dn, **kwargs)

