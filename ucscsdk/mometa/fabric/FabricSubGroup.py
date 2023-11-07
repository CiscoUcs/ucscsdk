"""This module contains the general information for FabricSubGroup ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricSubGroupConsts():
    CONFIG_STATE_DISABLED = "disabled"
    CONFIG_STATE_ENABLED = "enabled"
    LIC_STATE_LICENSE_EXPIRED = "license-expired"
    LIC_STATE_LICENSE_GRACEPERIOD = "license-graceperiod"
    LIC_STATE_LICENSE_INSUFFICIENT = "license-insufficient"
    LIC_STATE_LICENSE_OK = "license-ok"
    LIC_STATE_NOT_APPLICABLE = "not-applicable"
    LIC_STATE_UNKNOWN = "unknown"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"


class FabricSubGroup(ManagedObject):
    """This is FabricSubGroup class."""

    consts = FabricSubGroupConsts()
    naming_props = set(['slotId', 'aggrPortId'])

    mo_meta = MoMeta("FabricSubGroup", "fabricSubGroup", "slot-[slot_id]-aggr-port-[aggr_port_id]", VersionMeta.Version121a, "InputOutput", 0x7f, [], ["admin", "ext-lan-config", "ext-lan-policy", "ext-san-config", "ext-san-policy", "ls-network", "ls-network-policy"], ['fabricDceSwSrv', 'fabricDceSwSrvPc', 'fabricDceSwSrvPcOperation', 'fabricEthEstc', 'fabricEthEstcPc', 'fabricEthEstcPcOperation', 'fabricEthLan', 'fabricEthLanPc', 'fabricEthLanPcOperation', 'fabricEthMon', 'fabricEthMonOperation', 'fabricFcEstc', 'fabricFcMon', 'fabricFcMonOperation', 'fabricFcSan', 'fabricFcoeSanPc', 'fabricFcoeSanPcOperation'], ['fabricDceSwSrvEp', 'fabricDceSwSrvEpOperation', 'fabricDceSwSrvPcEp', 'fabricDceSwSrvPcEpOperation', 'fabricEthEstcEp', 'fabricEthEstcEpOperation', 'fabricEthEstcPcEp', 'fabricEthEstcPcEpOperation', 'fabricEthLanEp', 'fabricEthLanEpOperation', 'fabricEthLanPcEp', 'fabricEthLanPcEpOperation', 'fabricEthMonDestEp', 'fabricEthMonDestEpOperation', 'fabricFcMonDestEpOperation', 'fabricFcoeEstcEp', 'fabricFcoeEstcEpOperation', 'fabricFcoeSanEp', 'fabricFcoeSanEpOperation', 'fabricFcoeSanPcEp', 'fabricFcoeSanPcEpOperation'], ["Get", "Set"])

    prop_meta = {
        "aggr_port_id": MoPropertyMeta("aggr_port_id", "aggrPortId", "uint", VersionMeta.Version121a, MoPropertyMeta.NAMING, 0x2, None, None, None, [], ["1-108"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "lic_gp": MoPropertyMeta("lic_gp", "licGP", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "lic_state": MoPropertyMeta("lic_state", "licState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["license-expired", "license-graceperiod", "license-insufficient", "license-ok", "not-applicable", "unknown"], []), 
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version121a, MoPropertyMeta.NAMING, 0x20, None, None, None, [], ["1-4"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
    }

    prop_map = {
        "aggrPortId": "aggr_port_id", 
        "childAction": "child_action", 
        "configState": "config_state", 
        "dn": "dn", 
        "licGP": "lic_gp", 
        "licState": "lic_state", 
        "locale": "locale", 
        "name": "name", 
        "rn": "rn", 
        "slotId": "slot_id", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, aggr_port_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.aggr_port_id = aggr_port_id
        self.child_action = None
        self.config_state = None
        self.lic_gp = None
        self.lic_state = None
        self.locale = None
        self.name = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricSubGroup", parent_mo_or_dn, **kwargs)

