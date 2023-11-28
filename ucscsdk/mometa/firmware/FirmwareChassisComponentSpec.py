"""This module contains the general information for FirmwareChassisComponentSpec ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareChassisComponentSpecConsts():
    EXCLUDE_BY_DEFAULT_FALSE = "false"
    EXCLUDE_BY_DEFAULT_NO = "no"
    EXCLUDE_BY_DEFAULT_TRUE = "true"
    EXCLUDE_BY_DEFAULT_YES = "yes"
    TYPE_CHASSIS_BOARD_CONTROLLER = "chassis-board-controller"
    TYPE_CMC = "cmc"
    TYPE_IOCARD = "iocard"
    TYPE_LOCAL_DISK = "local-disk"
    TYPE_SAS_EXPANDER = "sas-expander"
    TYPE_STORAGE_CONTROLLER = "storage-controller"
    TYPE_UNSPECIFIED = "unspecified"


class FirmwareChassisComponentSpec(ManagedObject):
    """This is FirmwareChassisComponentSpec class."""

    consts = FirmwareChassisComponentSpecConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("FirmwareChassisComponentSpec", "firmwareChassisComponentSpec", "chassis-component-spec-[type]", VersionMeta.Version151a, "InputOutput", 0x1f, [], [""], ['firmwareBundleTypeCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "exclude_by_default": MoPropertyMeta("exclude_by_default", "excludeByDefault", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x10, None, None, None, ["chassis-board-controller", "cmc", "iocard", "local-disk", "sas-expander", "storage-controller", "unspecified"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "excludeByDefault": "exclude_by_default", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.exclude_by_default = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareChassisComponentSpec", parent_mo_or_dn, **kwargs)

