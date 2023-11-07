"""This module contains the general information for DomainFeatureCatalog ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class DomainFeatureCatalogConsts():
    pass


class DomainFeatureCatalog(ManagedObject):
    """This is DomainFeatureCatalog class."""

    consts = DomainFeatureCatalogConsts()
    naming_props = set(['version'])

    mo_meta = MoMeta("DomainFeatureCatalog", "domainFeatureCatalog", "catalog-[version]", VersionMeta.Version112a, "InputOutput", 0x1f, [], ["admin"], ['domainEp'], ['domainChassisFeature', 'domainChassisParam', 'domainEnvironmentFeature', 'domainEnvironmentParam', 'domainNetworkFeature', 'domainNetworkParam', 'domainServerFeature', 'domainServerParam', 'domainStorageFeature', 'domainStorageParam'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version112a, MoPropertyMeta.NAMING, 0x10, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "description": "description", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, version, **kwargs):
        self._dirty_mask = 0
        self.version = version
        self.child_action = None
        self.description = None
        self.status = None

        ManagedObject.__init__(self, "DomainFeatureCatalog", parent_mo_or_dn, **kwargs)

