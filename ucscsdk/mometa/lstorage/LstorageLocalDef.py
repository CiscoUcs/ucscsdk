"""This module contains the general information for LstorageLocalDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LstorageLocalDefConsts():
    pass


class LstorageLocalDef(ManagedObject):
    """This is LstorageLocalDef class."""

    consts = LstorageLocalDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageLocalDef", "lstorageLocalDef", "local-def", VersionMeta.Version201b, "InputOutput", 0xf, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], ['computeBoard'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "deployed_security_key": MoPropertyMeta("deployed_security_key", "deployedSecurityKey", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 32, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "security_key": MoPropertyMeta("security_key", "securityKey", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 32, 32, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "deployedSecurityKey": "deployed_security_key", 
        "dn": "dn", 
        "rn": "rn", 
        "securityKey": "security_key", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.deployed_security_key = None
        self.security_key = None
        self.status = None

        ManagedObject.__init__(self, "LstorageLocalDef", parent_mo_or_dn, **kwargs)

