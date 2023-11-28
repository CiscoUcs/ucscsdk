"""This module contains the general information for HcDownloader ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class HcDownloaderConsts():
    ADMIN_STATE_IDLE = "idle"
    ADMIN_STATE_RESTART = "restart"
    OWNER_MANAGEMENT = "management"
    OWNER_POLICY = "policy"
    PROTOCOL_FTP = "ftp"
    PROTOCOL_HTTP = "http"
    PROTOCOL_LOCAL = "local"
    PROTOCOL_SCP = "scp"
    PROTOCOL_SFTP = "sftp"
    PROTOCOL_TFTP = "tftp"
    TRANSFER_STATE_DOWNLOAD_FAILED = "download-failed"
    TRANSFER_STATE_DOWNLOADED = "downloaded"
    TRANSFER_STATE_DOWNLOADING = "downloading"
    TRANSFER_STATE_IMPORT_FAILED = "import-failed"
    TRANSFER_STATE_IMPORTED = "imported"
    TRANSFER_STATE_IMPORTING = "importing"
    TRANSFER_STATE_INIT = "init"
    TRANSFER_STATE_UPTODATE = "uptodate"


class HcDownloader(ManagedObject):
    """This is HcDownloader class."""

    consts = HcDownloaderConsts()
    naming_props = set(['fileName'])

    mo_meta = MoMeta("HcDownloader", "hcDownloader", "dnld-[file_name]", VersionMeta.Version151a, "InputOutput", 0xfff, [], ["admin"], ['hcHolder'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["idle", "restart"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "file_name": MoPropertyMeta("file_name", "fileName", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x8, 1, 64, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "image_size": MoPropertyMeta("image_size", "imageSize", "uint", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "image_url": MoPropertyMeta("image_url", "imageUrl", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["management", "policy"], []), 
        "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["ftp", "http", "local", "scp", "sftp", "tftp"], []), 
        "proxy_pwd": MoPropertyMeta("proxy_pwd", "proxyPwd", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "proxy_url": MoPropertyMeta("proxy_url", "proxyUrl", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "proxy_user": MoPropertyMeta("proxy_user", "proxyUser", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []), 
        "remote_path": MoPropertyMeta("remote_path", "remotePath", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "server": MoPropertyMeta("server", "server", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x200, 0, 64, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "transfer_state": MoPropertyMeta("transfer_state", "transferState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["download-failed", "downloaded", "downloading", "import-failed", "imported", "importing", "init", "uptodate"], []), 
        "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "fileName": "file_name", 
        "fltAggr": "flt_aggr", 
        "imageSize": "image_size", 
        "imageUrl": "image_url", 
        "owner": "owner", 
        "protocol": "protocol", 
        "proxyPwd": "proxy_pwd", 
        "proxyUrl": "proxy_url", 
        "proxyUser": "proxy_user", 
        "pwd": "pwd", 
        "remotePath": "remote_path", 
        "rn": "rn", 
        "server": "server", 
        "status": "status", 
        "transferState": "transfer_state", 
        "user": "user", 
    }

    def __init__(self, parent_mo_or_dn, file_name, **kwargs):
        self._dirty_mask = 0
        self.file_name = file_name
        self.admin_state = None
        self.child_action = None
        self.flt_aggr = None
        self.image_size = None
        self.image_url = None
        self.owner = None
        self.protocol = None
        self.proxy_pwd = None
        self.proxy_url = None
        self.proxy_user = None
        self.pwd = None
        self.remote_path = None
        self.server = None
        self.status = None
        self.transfer_state = None
        self.user = None

        ManagedObject.__init__(self, "HcDownloader", parent_mo_or_dn, **kwargs)

