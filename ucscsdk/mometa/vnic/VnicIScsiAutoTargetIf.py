"""This module contains the general information for VnicIScsiAutoTargetIf ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicIScsiAutoTargetIfConsts():
    pass


class VnicIScsiAutoTargetIf(ManagedObject):
    """This is VnicIScsiAutoTargetIf class."""

    consts = VnicIScsiAutoTargetIfConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicIScsiAutoTargetIf", "vnicIScsiAutoTargetIf", "auto", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin", "ls-config", "ls-network", "ls-server", "ls-storage"], ['vnicIScsi', 'vnicIScsiBootVnic', 'vnicIScsiTargetParams', 'vnicVlan'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dhcp_vendor_id": MoPropertyMeta("dhcp_vendor_id", "dhcpVendorId", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, 0, 32, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dhcpVendorId": "dhcp_vendor_id", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.dhcp_vendor_id = None
        self.status = None

        ManagedObject.__init__(self, "VnicIScsiAutoTargetIf", parent_mo_or_dn, **kwargs)

