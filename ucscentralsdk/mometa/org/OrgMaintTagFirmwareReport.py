"""This module contains the general information for OrgMaintTagFirmwareReport ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class OrgMaintTagFirmwareReportConsts():
    pass


class OrgMaintTagFirmwareReport(ManagedObject):
    """This is OrgMaintTagFirmwareReport class."""

    consts = OrgMaintTagFirmwareReportConsts()
    naming_props = set([u'maintTag'])

    mo_meta = MoMeta("OrgMaintTagFirmwareReport", "orgMaintTagFirmwareReport", "firmware-report-[maint_tag]", None, "InputOutput", 0x1f, [], ["read-only"], [], [u'orgDomainFirmwareInfo'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "maint_tag": MoPropertyMeta("maint_tag", "maintTag", "string", None, MoPropertyMeta.NAMING, 0x4, 1, 64, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "maintTag": "maint_tag", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, maint_tag, **kwargs):
        self._dirty_mask = 0
        self.maint_tag = maint_tag
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "OrgMaintTagFirmwareReport", parent_mo_or_dn, **kwargs)

