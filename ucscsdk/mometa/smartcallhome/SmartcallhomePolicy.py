"""This module contains the general information for SmartcallhomePolicy ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SmartcallhomePolicyConsts():
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    CAUSE_CAPACITY_EXCEEDED = "capacity-exceeded"
    CAUSE_CLIENT_LOST_CONNECTIVITY = "client-lost-connectivity"
    CAUSE_CONTROLLER_LOST_CONNECTIVITY = "controller-lost-connectivity"
    CAUSE_CORE_FILE_GENERATED = "core-file-generated"
    CAUSE_DB_CONNECT_READ_WRITE_ERROR = "db-connect-read-write-error"
    CAUSE_DUPLICATED_ASSIGNED = "duplicated-assigned"
    CAUSE_INVALID_KEYRING_CERTIFICATE = "invalid-Keyring-certificate"
    CAUSE_INVALID_TRUSTPOINT_CERT_CHAIN = "invalid-trustpoint-cert-chain"
    CAUSE_NOT_IN_COMPLIANCE = "not-in-compliance"
    CAUSE_PROVIDER_LOST_CONNECTIVITY = "provider-lost-connectivity"
    CAUSE_REMOTE_FAILED = "remote-failed"
    CAUSE_UNSPECIFIED = "unspecified"


class SmartcallhomePolicy(ManagedObject):
    """This is SmartcallhomePolicy class."""

    consts = SmartcallhomePolicyConsts()
    naming_props = set(['cause'])

    mo_meta = MoMeta("SmartcallhomePolicy", "smartcallhomePolicy", "smart-policy-[cause]", VersionMeta.Version141a, "InputOutput", 0xff, [], ["admin", "fault"], ['callhomeEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "cause": MoPropertyMeta("cause", "cause", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x4, None, None, None, ["capacity-exceeded", "client-lost-connectivity", "controller-lost-connectivity", "core-file-generated", "db-connect-read-write-error", "duplicated-assigned", "invalid-Keyring-certificate", "invalid-trustpoint-cert-chain", "not-in-compliance", "provider-lost-connectivity", "remote-failed", "unspecified"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "cause": "cause", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, cause, **kwargs):
        self._dirty_mask = 0
        self.cause = cause
        self.admin_state = None
        self.child_action = None
        self.descr = None
        self.name = None
        self.status = None

        ManagedObject.__init__(self, "SmartcallhomePolicy", parent_mo_or_dn, **kwargs)

