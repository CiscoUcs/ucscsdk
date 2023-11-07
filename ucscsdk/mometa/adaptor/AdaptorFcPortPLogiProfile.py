"""This module contains the general information for AdaptorFcPortPLogiProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorFcPortPLogiProfileConsts():
    pass


class AdaptorFcPortPLogiProfile(ManagedObject):
    """This is AdaptorFcPortPLogiProfile class."""

    consts = AdaptorFcPortPLogiProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcPortPLogiProfile", "adaptorFcPortPLogiProfile", "fc-port-plogi", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage"], ['adaptorHostFcIfProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "retries": MoPropertyMeta("retries", "retries", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["0-255"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "timeout": MoPropertyMeta("timeout", "timeout", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1000-255000"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "retries": "retries", 
        "rn": "rn", 
        "status": "status", 
        "timeout": "timeout", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.retries = None
        self.status = None
        self.timeout = None

        ManagedObject.__init__(self, "AdaptorFcPortPLogiProfile", parent_mo_or_dn, **kwargs)

