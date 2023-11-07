"""This module contains the general information for SmartcallhomeTransportGateway ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SmartcallhomeTransportGatewayConsts():
    ENABLED_FALSE = "false"
    ENABLED_NO = "no"
    ENABLED_TRUE = "true"
    ENABLED_YES = "yes"


class SmartcallhomeTransportGateway(ManagedObject):
    """This is SmartcallhomeTransportGateway class."""

    consts = SmartcallhomeTransportGatewayConsts()
    naming_props = set([])

    mo_meta = MoMeta("SmartcallhomeTransportGateway", "smartcallhomeTransportGateway", "transport-gateway", VersionMeta.Version141a, "InputOutput", 0x7f, [], ["admin", "operations"], ['callhomeEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "cert_chain": MoPropertyMeta("cert_chain", "certChain", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "enabled": MoPropertyMeta("enabled", "enabled", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["false", "no", "true", "yes"], []), 
        "old_cert_chain": MoPropertyMeta("old_cert_chain", "oldCertChain", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "url": MoPropertyMeta("url", "url", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []), 
    }

    prop_map = {
        "certChain": "cert_chain", 
        "childAction": "child_action", 
        "dn": "dn", 
        "enabled": "enabled", 
        "oldCertChain": "old_cert_chain", 
        "rn": "rn", 
        "status": "status", 
        "url": "url", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.cert_chain = None
        self.child_action = None
        self.enabled = None
        self.old_cert_chain = None
        self.status = None
        self.url = None

        ManagedObject.__init__(self, "SmartcallhomeTransportGateway", parent_mo_or_dn, **kwargs)

