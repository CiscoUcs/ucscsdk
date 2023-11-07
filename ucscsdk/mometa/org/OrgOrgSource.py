"""This module contains the general information for OrgOrgSource ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class OrgOrgSourceConsts():
    pass


class OrgOrgSource(ManagedObject):
    """This is OrgOrgSource class."""

    consts = OrgOrgSourceConsts()
    naming_props = set(['clientId'])

    mo_meta = MoMeta("OrgOrgSource", "orgOrgSource", "org-source-[client_id]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["read-only"], ['orgOrg'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "client_id": MoPropertyMeta("client_id", "clientId", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x2, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "clientId": "client_id", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, client_id, **kwargs):
        self._dirty_mask = 0
        self.client_id = client_id
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "OrgOrgSource", parent_mo_or_dn, **kwargs)

