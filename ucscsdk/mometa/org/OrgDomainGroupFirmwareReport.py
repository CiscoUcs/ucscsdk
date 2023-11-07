"""This module contains the general information for OrgDomainGroupFirmwareReport ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class OrgDomainGroupFirmwareReportConsts():
    pass


class OrgDomainGroupFirmwareReport(ManagedObject):
    """This is OrgDomainGroupFirmwareReport class."""

    consts = OrgDomainGroupFirmwareReportConsts()
    naming_props = set(['domainGroupDn'])

    mo_meta = MoMeta("OrgDomainGroupFirmwareReport", "orgDomainGroupFirmwareReport", "firmware-report-[domain_group_dn]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], [], ['orgFirmwareVersionCount'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "domainGroupDn": "domain_group_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, domain_group_dn, **kwargs):
        self._dirty_mask = 0
        self.domain_group_dn = domain_group_dn
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "OrgDomainGroupFirmwareReport", parent_mo_or_dn, **kwargs)

