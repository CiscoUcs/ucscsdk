"""This module contains the general information for OsController ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class OsControllerConsts():
    DEPLOY_STATE_COMPLETE = "complete"
    DEPLOY_STATE_FAILED = "failed"
    DEPLOY_STATE_IN_PROGRESS = "in-progress"
    DEPLOY_STATE_RETRY = "retry"
    DEPLOY_STATE_THROTTLED = "throttled"
    DEPLOY_STATE_UNDEFINED = "undefined"
    DEPLOY_STATE_UNDEPLOYED = "undeployed"
    TYPE_LINUX = "Linux"
    TYPE_PNU_OS = "PnuOS"
    TYPE_SOLARIS = "Solaris"
    TYPE_VMWARE_ESX = "VMWareESX"
    TYPE_WINDOWS = "Windows"
    TYPE_UNSPECIFIED = "unspecified"


class OsController(ManagedObject):
    """This is OsController class."""

    consts = OsControllerConsts()
    naming_props = set([])

    mo_meta = MoMeta("OsController", "osController", "os-ctrl", VersionMeta.Version131a, "InputOutput", 0xf, [], ["read-only"], ['storageProcessor'], ['firmwareBootDefinition', 'firmwareRunning'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "deploy_state": MoPropertyMeta("deploy_state", "deployState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["complete", "failed", "in-progress", "retry", "throttled", "undefined", "undeployed"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Linux", "PnuOS", "Solaris", "VMWareESX", "Windows", "unspecified"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "deployState": "deploy_state", 
        "dn": "dn", 
        "hostname": "hostname", 
        "name": "name", 
        "pnDn": "pn_dn", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.deploy_state = None
        self.hostname = None
        self.name = None
        self.pn_dn = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "OsController", parent_mo_or_dn, **kwargs)

