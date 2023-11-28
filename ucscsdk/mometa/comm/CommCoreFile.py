"""This module contains the general information for CommCoreFile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class CommCoreFileConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    FILE_TRANSFER_PROTO_FTP = "ftp"
    FILE_TRANSFER_PROTO_HTTP = "http"
    FILE_TRANSFER_PROTO_NFS_COPY = "nfs-copy"
    FILE_TRANSFER_PROTO_NONE = "none"
    FILE_TRANSFER_PROTO_SCP = "scp"
    FILE_TRANSFER_PROTO_SFTP = "sftp"
    FILE_TRANSFER_PROTO_TFTP = "tftp"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PROTO_ALL = "all"
    PROTO_NONE = "none"
    PROTO_TCP = "tcp"
    PROTO_UDP = "udp"


class CommCoreFile(ManagedObject):
    """This is CommCoreFile class."""

    consts = CommCoreFileConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("CommCoreFile", "commCoreFile", "core-file-[name]", VersionMeta.Version101a, "InputOutput", 0x3ff, [], ["admin"], ['orgDomainGroup', 'orgOrg', 'policyDeviceProfile'], [], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "file_transfer_proto": MoPropertyMeta("file_transfer_proto", "fileTransferProto", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ftp", "http", "nfs-copy", "none", "scp", "sftp", "tftp"], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""^[A-Za-z]([A-Za-z0-9_.-]*[A-Za-z0-9])?([A-Za-z]([A-Za-z0-9._-]*[A-Za-z0-9])?)*$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_port": MoPropertyMeta("oper_port", "operPort", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]), 
        "path": MoPropertyMeta("path", "path", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["1-65535"]), 
        "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fileTransferProto": "file_transfer_proto", 
        "hostname": "hostname", 
        "intId": "int_id", 
        "name": "name", 
        "operPort": "oper_port", 
        "path": "path", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "port": "port", 
        "proto": "proto", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.file_transfer_proto = None
        self.hostname = None
        self.int_id = None
        self.oper_port = None
        self.path = None
        self.policy_level = None
        self.policy_owner = None
        self.port = None
        self.proto = None
        self.status = None

        ManagedObject.__init__(self, "CommCoreFile", parent_mo_or_dn, **kwargs)

