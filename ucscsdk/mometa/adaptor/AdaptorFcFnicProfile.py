"""This module contains the general information for AdaptorFcFnicProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorFcFnicProfileConsts():
    pass


class AdaptorFcFnicProfile(ManagedObject):
    """This is AdaptorFcFnicProfile class."""

    consts = AdaptorFcFnicProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcFnicProfile", "adaptorFcFnicProfile", "fc-fnic", VersionMeta.Version151a, "InputOutput", 0x3f, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage"], ['adaptorHostFcIfProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "io_retry_timeout": MoPropertyMeta("io_retry_timeout", "ioRetryTimeout", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1-59"]), 
        "lun_queue_depth": MoPropertyMeta("lun_queue_depth", "lunQueueDepth", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["1-254"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ioRetryTimeout": "io_retry_timeout", 
        "lunQueueDepth": "lun_queue_depth", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.io_retry_timeout = None
        self.lun_queue_depth = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorFcFnicProfile", parent_mo_or_dn, **kwargs)

