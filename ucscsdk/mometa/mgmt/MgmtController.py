"""This module contains the general information for MgmtController ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtControllerConsts():
    SUBJECT_ADAPTOR = "adaptor"
    SUBJECT_BLADE = "blade"
    SUBJECT_BOARD_CONTROLLER = "board-controller"
    SUBJECT_CHASSIS = "chassis"
    SUBJECT_CMC = "cmc"
    SUBJECT_IOCARD = "iocard"
    SUBJECT_SERVER_UNIT = "server-unit"
    SUBJECT_SWITCH = "switch"
    SUBJECT_SYSTEM = "system"
    SUBJECT_UNKNOWN = "unknown"


class MgmtController(ManagedObject):
    """This is MgmtController class."""

    consts = MgmtControllerConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtController", "mgmtController", "mgmt", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], [u'adaptorUnit', u'computeBlade', u'computeBoardController', u'computeRackUnit', u'computeServerUnit', u'computeSystem', u'equipmentChassis', u'equipmentIOCard', u'equipmentSharedIOModule', u'equipmentSwitchIOCard', u'equipmentSystemIOController', u'networkElement', u'storageController', u'storageSasExpander', u'topSystem'], [u'cimcvmediaActualMountList', u'firmwareRunning', u'mgmtCmcSecureBoot', u'mgmtConnection', u'mgmtIf', u'mgmtInterface', u'vnicIpV4PooledAddr', u'vnicIpV4ProfDerivedAddr', u'vnicIpV4StaticAddr'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_conn": MoPropertyMeta("oper_conn", "operConn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subject": MoPropertyMeta("subject", "subject", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["adaptor", "blade", "board-controller", "chassis", "cmc", "iocard", "server-unit", "switch", "system", "unknown"], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "guid": "guid", 
        "model": "model", 
        "operConn": "oper_conn", 
        "revision": "revision", 
        "rn": "rn", 
        "serial": "serial", 
        "status": "status", 
        "subject": "subject", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.guid = None
        self.model = None
        self.oper_conn = None
        self.revision = None
        self.serial = None
        self.status = None
        self.subject = None
        self.vendor = None

        ManagedObject.__init__(self, "MgmtController", parent_mo_or_dn, **kwargs)

