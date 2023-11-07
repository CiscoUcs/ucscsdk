"""This module contains the general information for GlDomainEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlDomainEpConsts():
    pass


class GlDomainEp(ManagedObject):
    """This is GlDomainEp class."""

    consts = GlDomainEpConsts()
    naming_props = set(['domainId'])

    mo_meta = MoMeta("GlDomainEp", "glDomainEp", "domain-[domain_id]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["read-only"], ['glEp'], ['glConflictResolutionRuleEp', 'glRequest'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_id": MoPropertyMeta("domain_id", "domainId", "uint", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "domainId": "domain_id", 
        "index": "index", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, domain_id, **kwargs):
        self._dirty_mask = 0
        self.domain_id = domain_id
        self.child_action = None
        self.index = None
        self.status = None

        ManagedObject.__init__(self, "GlDomainEp", parent_mo_or_dn, **kwargs)

