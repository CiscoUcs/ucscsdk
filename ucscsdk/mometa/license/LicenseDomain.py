"""This module contains the general information for LicenseDomain ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LicenseDomainConsts():
    pass


class LicenseDomain(ManagedObject):
    """This is LicenseDomain class."""

    consts = LicenseDomainConsts()
    naming_props = set(['guid'])

    mo_meta = MoMeta("LicenseDomain", "licenseDomain", "Domain-[guid]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin"], ['licenseEp'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "grace_period_used": MoPropertyMeta("grace_period_used", "gracePeriodUsed", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "gracePeriodUsed": "grace_period_used", 
        "guid": "guid", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, guid, **kwargs):
        self._dirty_mask = 0
        self.guid = guid
        self.child_action = None
        self.grace_period_used = None
        self.status = None

        ManagedObject.__init__(self, "LicenseDomain", parent_mo_or_dn, **kwargs)

