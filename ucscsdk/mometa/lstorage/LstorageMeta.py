"""This module contains the general information for LstorageMeta ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LstorageMetaConsts():
    pass


class LstorageMeta(ManagedObject):
    """This is LstorageMeta class."""

    consts = LstorageMetaConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageMeta", "lstorageMeta", "meta", VersionMeta.Version131a, "InputOutput", 0x3f, [], ["admin"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "client_array_destination_dn": MoPropertyMeta("client_array_destination_dn", "clientArrayDestinationDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x2, 0, 256, None, [], []), 
        "client_blade_location_dn": MoPropertyMeta("client_blade_location_dn", "clientBladeLocationDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x4, 0, 256, None, [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|ungrouped-domain),){0,2}(defaultValue|not-applicable|ungrouped-domain){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "clientArrayDestinationDn": "client_array_destination_dn", 
        "clientBladeLocationDn": "client_blade_location_dn", 
        "configQualifier": "config_qualifier", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.client_array_destination_dn = None
        self.client_blade_location_dn = None
        self.config_qualifier = None
        self.status = None

        ManagedObject.__init__(self, "LstorageMeta", parent_mo_or_dn, **kwargs)

