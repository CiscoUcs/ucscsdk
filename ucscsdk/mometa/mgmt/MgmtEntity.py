"""This module contains the general information for MgmtEntity ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtEntityConsts():
    CHASSIS_DEVICE_IO_STATE1_OK = "ok"
    CHASSIS_DEVICE_IO_STATE1_OPEN_ERROR = "openError"
    CHASSIS_DEVICE_IO_STATE1_READ_ERROR = "readError"
    CHASSIS_DEVICE_IO_STATE1_UNKNOWN = "unknown"
    CHASSIS_DEVICE_IO_STATE1_WRITE_ERROR = "writeError"
    CHASSIS_DEVICE_IO_STATE2_OK = "ok"
    CHASSIS_DEVICE_IO_STATE2_OPEN_ERROR = "openError"
    CHASSIS_DEVICE_IO_STATE2_READ_ERROR = "readError"
    CHASSIS_DEVICE_IO_STATE2_UNKNOWN = "unknown"
    CHASSIS_DEVICE_IO_STATE2_WRITE_ERROR = "writeError"
    CHASSIS_DEVICE_IO_STATE3_OK = "ok"
    CHASSIS_DEVICE_IO_STATE3_OPEN_ERROR = "openError"
    CHASSIS_DEVICE_IO_STATE3_READ_ERROR = "readError"
    CHASSIS_DEVICE_IO_STATE3_UNKNOWN = "unknown"
    CHASSIS_DEVICE_IO_STATE3_WRITE_ERROR = "writeError"
    HA_READY_FALSE = "false"
    HA_READY_NO = "no"
    HA_READY_TRUE = "true"
    HA_READY_YES = "yes"
    ID_A = "A"
    ID_B = "B"
    ID_NONE = "NONE"
    ID_MGMT = "mgmt"
    LEAD_ID_FOR_AUTO_INSTALL_A = "A"
    LEAD_ID_FOR_AUTO_INSTALL_B = "B"
    LEAD_ID_FOR_AUTO_INSTALL_NONE = "NONE"
    LEAD_ID_FOR_AUTO_INSTALL_MGMT = "mgmt"
    SSH_KEY_STATUS_MATCHED = "matched"
    SSH_KEY_STATUS_MISMATCHED = "mismatched"
    SSH_KEY_STATUS_NONE = "none"
    VERSION_MISMATCH_FALSE = "false"
    VERSION_MISMATCH_NO = "no"
    VERSION_MISMATCH_TRUE = "true"
    VERSION_MISMATCH_YES = "yes"


class MgmtEntity(ManagedObject):
    """This is MgmtEntity class."""

    consts = MgmtEntityConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("MgmtEntity", "mgmtEntity", "mgmt-entity-[id]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['computeSystem', 'topSystem'], [], ["Get"])

    prop_meta = {
        "chassis1": MoPropertyMeta("chassis1", "chassis1", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "chassis2": MoPropertyMeta("chassis2", "chassis2", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "chassis3": MoPropertyMeta("chassis3", "chassis3", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "chassis_device_io_state1": MoPropertyMeta("chassis_device_io_state1", "chassisDeviceIoState1", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ok", "openError", "readError", "unknown", "writeError"], []), 
        "chassis_device_io_state2": MoPropertyMeta("chassis_device_io_state2", "chassisDeviceIoState2", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ok", "openError", "readError", "unknown", "writeError"], []), 
        "chassis_device_io_state3": MoPropertyMeta("chassis_device_io_state3", "chassisDeviceIoState3", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ok", "openError", "readError", "unknown", "writeError"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "ha_failure_reason": MoPropertyMeta("ha_failure_reason", "haFailureReason", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ha_readiness": MoPropertyMeta("ha_readiness", "haReadiness", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ha_ready": MoPropertyMeta("ha_ready", "haReady", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "lead_id_for_auto_install": MoPropertyMeta("lead_id_for_auto_install", "leadIdForAutoInstall", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "leadership": MoPropertyMeta("leadership", "leadership", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mgmt_services_state": MoPropertyMeta("mgmt_services_state", "mgmtServicesState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "problems": MoPropertyMeta("problems", "problems", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "ssh_auth_keys_csum": MoPropertyMeta("ssh_auth_keys_csum", "sshAuthKeysCsum", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "ssh_auth_keys_size": MoPropertyMeta("ssh_auth_keys_size", "sshAuthKeysSize", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "ssh_key_status": MoPropertyMeta("ssh_key_status", "sshKeyStatus", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["matched", "mismatched", "none"], ["0-4294967295"]), 
        "ssh_root_pub_key_csum": MoPropertyMeta("ssh_root_pub_key_csum", "sshRootPubKeyCsum", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "ssh_root_pub_key_size": MoPropertyMeta("ssh_root_pub_key_size", "sshRootPubKeySize", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "umbilical_state": MoPropertyMeta("umbilical_state", "umbilicalState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "version_mismatch": MoPropertyMeta("version_mismatch", "versionMismatch", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "chassis1": "chassis1", 
        "chassis2": "chassis2", 
        "chassis3": "chassis3", 
        "chassisDeviceIoState1": "chassis_device_io_state1", 
        "chassisDeviceIoState2": "chassis_device_io_state2", 
        "chassisDeviceIoState3": "chassis_device_io_state3", 
        "childAction": "child_action", 
        "dn": "dn", 
        "haFailureReason": "ha_failure_reason", 
        "haReadiness": "ha_readiness", 
        "haReady": "ha_ready", 
        "id": "id", 
        "leadIdForAutoInstall": "lead_id_for_auto_install", 
        "leadership": "leadership", 
        "mgmtServicesState": "mgmt_services_state", 
        "problems": "problems", 
        "rn": "rn", 
        "sshAuthKeysCsum": "ssh_auth_keys_csum", 
        "sshAuthKeysSize": "ssh_auth_keys_size", 
        "sshKeyStatus": "ssh_key_status", 
        "sshRootPubKeyCsum": "ssh_root_pub_key_csum", 
        "sshRootPubKeySize": "ssh_root_pub_key_size", 
        "state": "state", 
        "status": "status", 
        "umbilicalState": "umbilical_state", 
        "versionMismatch": "version_mismatch", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.chassis1 = None
        self.chassis2 = None
        self.chassis3 = None
        self.chassis_device_io_state1 = None
        self.chassis_device_io_state2 = None
        self.chassis_device_io_state3 = None
        self.child_action = None
        self.ha_failure_reason = None
        self.ha_readiness = None
        self.ha_ready = None
        self.lead_id_for_auto_install = None
        self.leadership = None
        self.mgmt_services_state = None
        self.problems = None
        self.ssh_auth_keys_csum = None
        self.ssh_auth_keys_size = None
        self.ssh_key_status = None
        self.ssh_root_pub_key_csum = None
        self.ssh_root_pub_key_size = None
        self.state = None
        self.status = None
        self.umbilical_state = None
        self.version_mismatch = None

        ManagedObject.__init__(self, "MgmtEntity", parent_mo_or_dn, **kwargs)

