"""This module contains the general information for DomainChassisFeature ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class DomainChassisFeatureConsts():
    FUNCTIONAL_STATE_DISABLED = "disabled"
    FUNCTIONAL_STATE_ENABLED = "enabled"
    TYPE_MAJOR = "major"
    TYPE_MINOR = "minor"


class DomainChassisFeature(ManagedObject):
    """This is DomainChassisFeature class."""

    consts = DomainChassisFeatureConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("DomainChassisFeature", "domainChassisFeature", "chassis-feature-[name]", VersionMeta.Version201b, "InputOutput", 0x3f, [], [""], ['computeSystem', 'domainFeatureCatalog', 'extpolDomain'], ['domainChassisParam', 'domainEnvironmentParam', 'domainNetworkParam', 'domainServerParam', 'domainStorageParam'], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "functional_state": MoPropertyMeta("functional_state", "functionalState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["disabled", "enabled"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["major", "minor"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "functionalState": "functional_state", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.flt_aggr = None
        self.functional_state = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "DomainChassisFeature", parent_mo_or_dn, **kwargs)

