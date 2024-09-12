"""This module contains the general information for ExtpolVersionHolder ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ExtpolVersionHolderConsts():
    CONN_PROTOCOL_IPV4 = "ipv4"
    CONN_PROTOCOL_IPV6 = "ipv6"
    CONN_PROTOCOL_UNKNOWN = "unknown"
    OPERATION_ADD = "add"
    OPERATION_DELETE = "delete"
    OPERATION_NO_OPERATION = "noOperation"
    PRODUCT_FAMILY_UCS_CLASSIC = "ucs-classic"
    PRODUCT_FAMILY_UCS_CLASSIC_3GEN = "ucs-classic-3gen"
    PRODUCT_FAMILY_UCS_CLASSIC_4GEN = "ucs-classic-4gen"
    PRODUCT_FAMILY_UCS_CLASSIC_5GEN = "ucs-classic-5gen"
    PRODUCT_FAMILY_UCS_MINI = "ucs-mini"
    PRODUCT_FAMILY_UCS_X_SERIES_DIRECT = "ucs-x-series-direct"
    VERSION_HOLDER_FALSE = "false"
    VERSION_HOLDER_NO = "no"
    VERSION_HOLDER_TRUE = "true"
    VERSION_HOLDER_YES = "yes"
    VERSION_HOLDER_FLAG_FALSE = "false"
    VERSION_HOLDER_FLAG_NO = "no"
    VERSION_HOLDER_FLAG_TRUE = "true"
    VERSION_HOLDER_FLAG_YES = "yes"


class ExtpolVersionHolder(ManagedObject):
    """This is ExtpolVersionHolder class."""

    consts = ExtpolVersionHolderConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("ExtpolVersionHolder", "extpolVersionHolder", "versionHolder-[id]", VersionMeta.Version131a, "InputOutput", 0x1f, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "conn_protocol": MoPropertyMeta("conn_protocol", "connProtocol", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipv4", "ipv6", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "host": MoPropertyMeta("host", "host", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?$|^[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?(\.[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?)*(\.[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?)$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$""", [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "ipv4": MoPropertyMeta("ipv4", "ipv4", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "ipv6": MoPropertyMeta("ipv6", "ipv6", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "operation": MoPropertyMeta("operation", "operation", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["add", "delete", "noOperation"], []), 
        "product_family": MoPropertyMeta("product_family", "productFamily", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ucs-classic", "ucs-classic-3gen", "ucs-classic-4gen", "ucs-classic-5gen", "ucs-mini", "ucs-x-series-direct"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "version_holder": MoPropertyMeta("version_holder", "versionHolder", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "version_holder_flag": MoPropertyMeta("version_holder_flag", "versionHolderFlag", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "connProtocol": "conn_protocol", 
        "dn": "dn", 
        "guid": "guid", 
        "host": "host", 
        "id": "id", 
        "ipv4": "ipv4", 
        "ipv6": "ipv6", 
        "operation": "operation", 
        "productFamily": "product_family", 
        "rn": "rn", 
        "status": "status", 
        "versionHolder": "version_holder", 
        "versionHolderFlag": "version_holder_flag", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.conn_protocol = None
        self.guid = None
        self.host = None
        self.ipv4 = None
        self.ipv6 = None
        self.operation = None
        self.product_family = None
        self.status = None
        self.version_holder = None
        self.version_holder_flag = None

        ManagedObject.__init__(self, "ExtpolVersionHolder", parent_mo_or_dn, **kwargs)

