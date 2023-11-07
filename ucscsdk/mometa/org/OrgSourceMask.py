"""This module contains the general information for OrgSourceMask ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class OrgSourceMaskConsts():
    DELETE_SOURCE_NOT_DELETING = "not-deleting"
    DELETE_SOURCE_POLICY_MGR = "policy-mgr"
    DELETE_SOURCE_RESOURCE_MGR = "resource-mgr"


class OrgSourceMask(ManagedObject):
    """This is OrgSourceMask class."""

    consts = OrgSourceMaskConsts()
    naming_props = set([])

    mo_meta = MoMeta("OrgSourceMask", "orgSourceMask", "src-mask", VersionMeta.Version101a, "InputOutput", 0xf, [], ["read-only"], ['orgOrg'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "delete_source": MoPropertyMeta("delete_source", "deleteSource", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-deleting", "policy-mgr", "resource-mgr"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "mask": MoPropertyMeta("mask", "mask", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|policy-mgr|managed-endpoint|local|global),){0,4}(defaultValue|policy-mgr|managed-endpoint|local|global){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "deleteSource": "delete_source", 
        "dn": "dn", 
        "mask": "mask", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.delete_source = None
        self.mask = None
        self.status = None

        ManagedObject.__init__(self, "OrgSourceMask", parent_mo_or_dn, **kwargs)

