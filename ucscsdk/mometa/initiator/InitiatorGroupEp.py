"""This module contains the general information for InitiatorGroupEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class InitiatorGroupEpConsts():
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"


class InitiatorGroupEp(ManagedObject):
    """This is InitiatorGroupEp class."""

    consts = InitiatorGroupEpConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("InitiatorGroupEp", "initiatorGroupEp", "grp-[name]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['initiatorRequestorEp'], ['initiatorFcInitiatorEp', 'initiatorIScsiInitiatorEp', 'initiatorStoreEp', 'storageIScsiInitiatorEp', 'storageNodeEp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "pol_name": MoPropertyMeta("pol_name", "polName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rmt_disk_cfg_name": MoPropertyMeta("rmt_disk_cfg_name", "rmtDiskCfgName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "id": "id", 
        "lc": "lc", 
        "name": "name", 
        "polName": "pol_name", 
        "rmtDiskCfgName": "rmt_disk_cfg_name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.ep_dn = None
        self.id = None
        self.lc = None
        self.pol_name = None
        self.rmt_disk_cfg_name = None
        self.status = None

        ManagedObject.__init__(self, "InitiatorGroupEp", parent_mo_or_dn, **kwargs)

