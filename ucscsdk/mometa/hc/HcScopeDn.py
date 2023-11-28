"""This module contains the general information for HcScopeDn ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class HcScopeDnConsts():
    REF_DN_TYPE_DOMAIN = "domain"
    REF_DN_TYPE_DOMAIN_GROUP = "domainGroup"
    REF_DN_TYPE_EQUIPMENT = "equipment"
    REF_DN_TYPE_HOST_FIRMWARE_POLICY = "hostFirmwarePolicy"
    REF_DN_TYPE_PROFILE = "profile"
    REF_DN_TYPE_UNKNOWN = "unknown"


class HcScopeDn(ManagedObject):
    """This is HcScopeDn class."""

    consts = HcScopeDnConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("HcScopeDn", "hcScopeDn", "scope-dn-[id]", VersionMeta.Version151a, "InputOutput", 0x7f, [], ["admin"], ['hcReport'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "ref_dn": MoPropertyMeta("ref_dn", "refDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []), 
        "ref_dn_type": MoPropertyMeta("ref_dn_type", "refDnType", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["domain", "domainGroup", "equipment", "hostFirmwarePolicy", "profile", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "refDn": "ref_dn", 
        "refDnType": "ref_dn_type", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.ref_dn = None
        self.ref_dn_type = None
        self.status = None

        ManagedObject.__init__(self, "HcScopeDn", parent_mo_or_dn, **kwargs)

