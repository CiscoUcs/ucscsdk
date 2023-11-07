"""This module contains the general information for FirmwareUpdatable ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareUpdatableConsts():
    ADMIN_STATE_FORCE_TRIGGER = "force-trigger"
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    DEPLOYMENT_BACKUP = "backup"
    DEPLOYMENT_BOOT_LOADER = "boot-loader"
    DEPLOYMENT_KERNEL = "kernel"
    DEPLOYMENT_PROVIDER = "provider"
    DEPLOYMENT_SERVICE_PACK = "service-pack"
    DEPLOYMENT_SYSTEM = "system"
    DEPLOYMENT_UNSPECIFIED = "unspecified"
    OPER_STATE_ACTIVATING = "activating"
    OPER_STATE_BAD_IMAGE = "bad-image"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_PENDING_NEXT_BOOT = "pending-next-boot"
    OPER_STATE_READY = "ready"
    OPER_STATE_REBOOTING = "rebooting"
    OPER_STATE_SCHEDULED = "scheduled"
    OPER_STATE_SET_STARTUP = "set-startup"
    OPER_STATE_THROTTLED = "throttled"
    OPER_STATE_UPDATING = "updating"
    OPER_STATE_UPGRADING = "upgrading"
    OPER_STATE_QUAL_BOOT_CONF_MISSING = "boot-conf-missing"
    OPER_STATE_QUAL_CHECKSUM_FAILURE = "checksum-failure"
    OPER_STATE_QUAL_CRC_FAILURE = "crc-failure"
    OPER_STATE_QUAL_FILESYSTEM_ERROR = "filesystem-error"
    OPER_STATE_QUAL_MGMT_CONNECT_ERROR = "mgmt-connect-error"
    OPER_STATE_QUAL_NONE = "none"
    OPER_STATE_QUAL_UNKNOWN_ERROR = "unknown-error"


class FirmwareUpdatable(ManagedObject):
    """This is FirmwareUpdatable class."""

    consts = FirmwareUpdatableConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareUpdatable", "firmwareUpdatable", "fw-updatable", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin"], ['equipmentPsu', 'storageOnboardDevice'], [], ["Get", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["force-trigger", "trigger", "triggered"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "deployment": MoPropertyMeta("deployment", "deployment", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["backup", "boot-loader", "kernel", "provider", "service-pack", "system", "unspecified"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating", "upgrading"], []), 
        "oper_state_qual": MoPropertyMeta("oper_state_qual", "operStateQual", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["boot-conf-missing", "checksum-failure", "crc-failure", "filesystem-error", "mgmt-connect-error", "none", "unknown-error"], []), 
        "prev_version": MoPropertyMeta("prev_version", "prevVersion", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "deployment": "deployment", 
        "dn": "dn", 
        "operState": "oper_state", 
        "operStateQual": "oper_state_qual", 
        "prevVersion": "prev_version", 
        "rn": "rn", 
        "status": "status", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.deployment = None
        self.oper_state = None
        self.oper_state_qual = None
        self.prev_version = None
        self.status = None
        self.version = None

        ManagedObject.__init__(self, "FirmwareUpdatable", parent_mo_or_dn, **kwargs)

