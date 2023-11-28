"""This module contains the general information for SmartlicenseEntitlement ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SmartlicenseEntitlementConsts():
    ENFORCE_MODE_AUTHORIZATION_EXPIRED = "authorization-expired"
    ENFORCE_MODE_COMPLIANCE = "compliance"
    ENFORCE_MODE_DISABLED = "disabled"
    ENFORCE_MODE_EVAL = "eval"
    ENFORCE_MODE_EXPIRED = "expired"
    ENFORCE_MODE_GRACE_PERIOD = "grace-period"
    ENFORCE_MODE_GRACE_PERIOD_EXPIRED = "grace-period-expired"
    ENFORCE_MODE_INIT = "init"
    ENFORCE_MODE_INVALID = "invalid"
    ENFORCE_MODE_INVALID_TAG = "invalid-tag"
    ENFORCE_MODE_MAX = "max"
    ENFORCE_MODE_OUT_OF_COMPLIANCE = "out-of-compliance"
    ENFORCE_MODE_OVERAGE = "overage"
    ENFORCE_MODE_WAITING = "waiting"


class SmartlicenseEntitlement(ManagedObject):
    """This is SmartlicenseEntitlement class."""

    consts = SmartlicenseEntitlementConsts()
    naming_props = set(['tag'])

    mo_meta = MoMeta("SmartlicenseEntitlement", "smartlicenseEntitlement", "entitlement[tag]", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["admin"], ['smartlicenseEntitlementEp', 'smartlicenseHolder'], ['faultInst'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "counter": MoPropertyMeta("counter", "counter", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "enforce_mode": MoPropertyMeta("enforce_mode", "enforceMode", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["authorization-expired", "compliance", "disabled", "eval", "expired", "grace-period", "grace-period-expired", "init", "invalid", "invalid-tag", "max", "out-of-compliance", "overage", "waiting"], []), 
        "feature_name": MoPropertyMeta("feature_name", "featureName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "last_reported_counter": MoPropertyMeta("last_reported_counter", "lastReportedCounter", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "mode_time": MoPropertyMeta("mode_time", "modeTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "requested_time": MoPropertyMeta("requested_time", "requestedTime", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tag": MoPropertyMeta("tag", "tag", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x10, 1, 128, None, [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 1, 64, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "counter": "counter", 
        "description": "description", 
        "dn": "dn", 
        "enforceMode": "enforce_mode", 
        "featureName": "feature_name", 
        "fltAggr": "flt_aggr", 
        "lastReportedCounter": "last_reported_counter", 
        "modeTime": "mode_time", 
        "requestedTime": "requested_time", 
        "rn": "rn", 
        "status": "status", 
        "tag": "tag", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, tag, **kwargs):
        self._dirty_mask = 0
        self.tag = tag
        self.child_action = None
        self.counter = None
        self.description = None
        self.enforce_mode = None
        self.feature_name = None
        self.flt_aggr = None
        self.last_reported_counter = None
        self.mode_time = None
        self.requested_time = None
        self.status = None
        self.version = None

        ManagedObject.__init__(self, "SmartlicenseEntitlement", parent_mo_or_dn, **kwargs)

