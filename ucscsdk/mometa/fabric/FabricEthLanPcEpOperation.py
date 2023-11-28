"""This module contains the general information for FabricEthLanPcEpOperation ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricEthLanPcEpOperationConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    TRIGGER_STATUS_TRIGGER_ACKED = "trigger-acked"
    TRIGGER_STATUS_TRIGGER_FAILED = "trigger-failed"
    TRIGGER_STATUS_TRIGGERED = "triggered"
    TRIGGER_STATUS_UNKNOWN = "unknown"


class FabricEthLanPcEpOperation(ManagedObject):
    """This is FabricEthLanPcEpOperation class."""

    consts = FabricEthLanPcEpOperationConsts()
    naming_props = set(['slotId', 'portId'])

    mo_meta = MoMeta("FabricEthLanPcEpOperation", "fabricEthLanPcEpOperation", "remoper-ep-slot-[slot_id]-port-[port_id]", VersionMeta.Version141a, "InputOutput", 0x1ff, [], ["admin", "ext-lan-config", "ext-lan-policy"], ['fabricEthLanPcOperation', 'fabricSubGroup'], ['faultInst'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "eth_link_profile_name": MoPropertyMeta("eth_link_profile_name", "ethLinkProfileName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "last_modified": MoPropertyMeta("last_modified", "lastModified", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "oper_eth_link_profile_name": MoPropertyMeta("oper_eth_link_profile_name", "operEthLinkProfileName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-108"]), 
        "remote_error_code": MoPropertyMeta("remote_error_code", "remoteErrorCode", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "remote_error_descr": MoPropertyMeta("remote_error_descr", "remoteErrorDescr", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x40, None, None, None, [], ["1-5"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_status": MoPropertyMeta("trigger_status", "triggerStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["trigger-acked", "trigger-failed", "triggered", "unknown"], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "ethLinkProfileName": "eth_link_profile_name", 
        "lastModified": "last_modified", 
        "operEthLinkProfileName": "oper_eth_link_profile_name", 
        "portId": "port_id", 
        "remoteErrorCode": "remote_error_code", 
        "remoteErrorDescr": "remote_error_descr", 
        "rn": "rn", 
        "slotId": "slot_id", 
        "status": "status", 
        "triggerStatus": "trigger_status", 
    }

    def __init__(self, parent_mo_or_dn, slot_id, port_id, **kwargs):
        self._dirty_mask = 0
        self.slot_id = slot_id
        self.port_id = port_id
        self.admin_state = None
        self.child_action = None
        self.ep_dn = None
        self.eth_link_profile_name = None
        self.last_modified = None
        self.oper_eth_link_profile_name = None
        self.remote_error_code = None
        self.remote_error_descr = None
        self.status = None
        self.trigger_status = None

        ManagedObject.__init__(self, "FabricEthLanPcEpOperation", parent_mo_or_dn, **kwargs)

