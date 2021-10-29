"""This module contains the general information for FirmwareSource ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareSourceConsts():
    DOWNLOAD_STATUS_FAILED = "failed"
    DOWNLOAD_STATUS_IDLE = "idle"
    DOWNLOAD_STATUS_INPROGRESS = "inprogress"
    LAST_DOWNLOAD_NEVER = "never"
    TRIGGER_STATE_NONE = "none"
    TRIGGER_STATE_TRIGGER_DELETE = "trigger-delete"
    TRIGGER_STATE_TRIGGER_DOWNLOAD = "trigger-download"
    TYPE_CISCO = "Cisco"
    TYPE_LOCAL = "local"


class FirmwareSource(ManagedObject):
    """This is FirmwareSource class."""

    consts = FirmwareSourceConsts()
    naming_props = set([u'type'])

    mo_meta = MoMeta("FirmwareSource", "firmwareSource", "source-[type]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin"], [u'firmwareCatalogue'], [u'faultInst', u'firmwareDownloadPolicy'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "download_error": MoPropertyMeta("download_error", "downloadError", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "download_status": MoPropertyMeta("download_status", "downloadStatus", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed", "idle", "inprogress"], []), 
        "last_download": MoPropertyMeta("last_download", "lastDownload", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "trigger_state": MoPropertyMeta("trigger_state", "triggerState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["none", "trigger-delete", "trigger-download"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, None, None, None, ["Cisco", "local"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "downloadError": "download_error", 
        "downloadStatus": "download_status", 
        "lastDownload": "last_download", 
        "rn": "rn", 
        "status": "status", 
        "triggerState": "trigger_state", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.download_error = None
        self.download_status = None
        self.last_download = None
        self.status = None
        self.trigger_state = None

        ManagedObject.__init__(self, "FirmwareSource", parent_mo_or_dn, **kwargs)

