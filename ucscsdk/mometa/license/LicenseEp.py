"""This module contains the general information for LicenseEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LicenseEpConsts():
    INITIALIZATION_STATE_INITIALIZED = "initialized"
    INITIALIZATION_STATE_UNINITIALIZED = "uninitialized"


class LicenseEp(ManagedObject):
    """This is LicenseEp class."""

    consts = LicenseEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("LicenseEp", "licenseEp", "license", VersionMeta.Version101a, "InputOutput", 0xf, [], ["admin"], ['topSystem'], ['licenseDomain', 'licenseDownloader', 'licenseFeature', 'licenseFile', 'licenseServerHostId'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "initialization_state": MoPropertyMeta("initialization_state", "initializationState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["initialized", "uninitialized"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "initializationState": "initialization_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.flt_aggr = None
        self.initialization_state = None
        self.status = None

        ManagedObject.__init__(self, "LicenseEp", parent_mo_or_dn, **kwargs)

