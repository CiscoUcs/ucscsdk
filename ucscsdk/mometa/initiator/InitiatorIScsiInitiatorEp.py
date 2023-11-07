"""This module contains the general information for InitiatorIScsiInitiatorEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class InitiatorIScsiInitiatorEpConsts():
    PROT_DERIVED = "derived"
    PROT_FC = "fc"
    PROT_ISCSI = "iscsi"


class InitiatorIScsiInitiatorEp(ManagedObject):
    """This is InitiatorIScsiInitiatorEp class."""

    consts = InitiatorIScsiInitiatorEpConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("InitiatorIScsiInitiatorEp", "initiatorIScsiInitiatorEp", "scsi-ini-[name]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], ['initiatorGroupEp'], ['storageEpUser'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "iqn": MoPropertyMeta("iqn", "iqn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[0-9a-zA-Z\.:-]*$""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "pref": MoPropertyMeta("pref", "pref", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "prot": MoPropertyMeta("prot", "prot", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["derived", "fc", "iscsi"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "id": "id", 
        "iqn": "iqn", 
        "name": "name", 
        "pref": "pref", 
        "prot": "prot", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.ep_dn = None
        self.id = None
        self.iqn = None
        self.pref = None
        self.prot = None
        self.status = None

        ManagedObject.__init__(self, "InitiatorIScsiInitiatorEp", parent_mo_or_dn, **kwargs)

