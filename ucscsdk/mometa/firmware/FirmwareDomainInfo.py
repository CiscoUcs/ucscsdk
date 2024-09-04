"""This module contains the general information for FirmwareDomainInfo ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareDomainInfoConsts():
    CONNECTION_STATE_CONNECTED = "connected"
    CONNECTION_STATE_LOST_CONNECTIVITY = "lost-connectivity"
    OPER_STATE_LOST_VISIBILITY = "lost-visibility"
    OPER_STATE_REGISTERED = "registered"
    OPER_STATE_REGISTERING = "registering"
    OPER_STATE_SYNCHRONIZING = "synchronizing"
    OPER_STATE_UNREGISTERED = "unregistered"
    OPER_STATE_VERSION_MISMATCH = "version-mismatch"
    PRODUCT_FAMILY_UCS_CLASSIC = "ucs-classic"
    PRODUCT_FAMILY_UCS_CLASSIC_3GEN = "ucs-classic-3gen"
    PRODUCT_FAMILY_UCS_CLASSIC_4GEN = "ucs-classic-4gen"
    PRODUCT_FAMILY_UCS_CLASSIC_5GEN = "ucs-classic-5gen"
    PRODUCT_FAMILY_UCS_MINI = "ucs-mini"
    PRODUCT_FAMILY_UCS_X_SERIES_DIRECT = "ucs-x-series-direct"
    SUSPEND_STATE_OFF = "off"
    SUSPEND_STATE_ON = "on"


class FirmwareDomainInfo(ManagedObject):
    """This is FirmwareDomainInfo class."""

    consts = FirmwareDomainInfoConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("FirmwareDomainInfo", "firmwareDomainInfo", "domain-info-[id]", VersionMeta.Version151a, "InputOutput", 0x1f, [], ["admin", "operations"], ['firmwareDomainInfraProfile'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "connection_state": MoPropertyMeta("connection_state", "connectionState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "lost-connectivity"], []), 
        "context": MoPropertyMeta("context", "context", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "maint_grp_tag": MoPropertyMeta("maint_grp_tag", "maintGrpTag", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 64, r"""[a-zA-Z0-9=\[\]!#$%()*+\\,-./:;@_\s{|}~?]+""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "product_family": MoPropertyMeta("product_family", "productFamily", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ucs-classic", "ucs-classic-3gen", "ucs-classic-4gen", "ucs-classic-5gen", "ucs-mini", "ucs-x-series-direct"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspend_state": MoPropertyMeta("suspend_state", "suspendState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "connectionState": "connection_state", 
        "context": "context", 
        "descr": "descr", 
        "dn": "dn", 
        "id": "id", 
        "ip": "ip", 
        "maintGrpTag": "maint_grp_tag", 
        "name": "name", 
        "operState": "oper_state", 
        "productFamily": "product_family", 
        "rn": "rn", 
        "status": "status", 
        "suspendState": "suspend_state", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.connection_state = None
        self.context = None
        self.descr = None
        self.ip = None
        self.maint_grp_tag = None
        self.name = None
        self.oper_state = None
        self.product_family = None
        self.status = None
        self.suspend_state = None

        ManagedObject.__init__(self, "FirmwareDomainInfo", parent_mo_or_dn, **kwargs)

