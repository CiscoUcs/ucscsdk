"""This module contains the general information for EquipmentChassisStatsHist ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentChassisStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class EquipmentChassisStatsHist(ManagedObject):
    """This is EquipmentChassisStatsHist class."""

    consts = EquipmentChassisStatsHistConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("EquipmentChassisStatsHist", "equipmentChassisStatsHist", "[id]", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["read-only"], ['equipmentChassisStats'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111a, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "input_power": MoPropertyMeta("input_power", "inputPower", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "input_power_avg": MoPropertyMeta("input_power_avg", "inputPowerAvg", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "input_power_max": MoPropertyMeta("input_power_max", "inputPowerMax", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "input_power_min": MoPropertyMeta("input_power_min", "inputPowerMin", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "output_power": MoPropertyMeta("output_power", "outputPower", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "output_power_avg": MoPropertyMeta("output_power_avg", "outputPowerAvg", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "output_power_max": MoPropertyMeta("output_power_max", "outputPowerMax", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "output_power_min": MoPropertyMeta("output_power_min", "outputPowerMin", "float", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "inputPower": "input_power", 
        "inputPowerAvg": "input_power_avg", 
        "inputPowerMax": "input_power_max", 
        "inputPowerMin": "input_power_min", 
        "mostRecent": "most_recent", 
        "outputPower": "output_power", 
        "outputPowerAvg": "output_power_avg", 
        "outputPowerMax": "output_power_max", 
        "outputPowerMin": "output_power_min", 
        "rn": "rn", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.input_power = None
        self.input_power_avg = None
        self.input_power_max = None
        self.input_power_min = None
        self.most_recent = None
        self.output_power = None
        self.output_power_avg = None
        self.output_power_max = None
        self.output_power_min = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "EquipmentChassisStatsHist", parent_mo_or_dn, **kwargs)

