"""This module contains the general information for LsZoneInitiatorMember ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsZoneInitiatorMemberConsts():
    pass


class LsZoneInitiatorMember(ManagedObject):
    """This is LsZoneInitiatorMember class."""

    consts = LsZoneInitiatorMemberConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("LsZoneInitiatorMember", "lsZoneInitiatorMember", "initiator-[name]", VersionMeta.Version141a, "InputOutput", 0x3f, [], ["admin", "ls-storage"], ['lsFcZoneGroup'], ['lsFcZone'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "wwpn": MoPropertyMeta("wwpn", "wwpn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "usrLbl": "usr_lbl", 
        "wwpn": "wwpn", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.ep_dn = None
        self.status = None
        self.usr_lbl = None
        self.wwpn = None

        ManagedObject.__init__(self, "LsZoneInitiatorMember", parent_mo_or_dn, **kwargs)

