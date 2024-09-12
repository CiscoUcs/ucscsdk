"""This module contains the general information for ExtpolDomain ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ExtpolDomainConsts():
    PRODUCT_FAMILY_UCS_CLASSIC = "ucs-classic"
    PRODUCT_FAMILY_UCS_CLASSIC_3GEN = "ucs-classic-3gen"
    PRODUCT_FAMILY_UCS_CLASSIC_4GEN = "ucs-classic-4gen"
    PRODUCT_FAMILY_UCS_CLASSIC_5GEN = "ucs-classic-5gen"
    PRODUCT_FAMILY_UCS_MINI = "ucs-mini"
    PRODUCT_FAMILY_UCS_X_SERIES_DIRECT = "ucs-x-series-direct"


class ExtpolDomain(ManagedObject):
    """This is ExtpolDomain class."""

    consts = ExtpolDomainConsts()
    naming_props = set(['guid'])

    mo_meta = MoMeta("ExtpolDomain", "extpolDomain", "domain-[guid]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['extpolClientCont'], ['changeEp', 'computeChassisFeatMask', 'computeEnvFeatMask', 'computeNetworkFeatMask', 'computeServerFeatMask', 'computeStorageFeatMask', 'domainChassisFeature', 'domainEnvironmentFeature', 'domainNetworkFeature', 'domainServerFeature', 'domainStorageFeature', 'lstorageBlade'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, 1, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "product_family": MoPropertyMeta("product_family", "productFamily", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ucs-classic", "ucs-classic-3gen", "ucs-classic-4gen", "ucs-classic-5gen", "ucs-mini", "ucs-x-series-direct"], []), 
        "reg_count": MoPropertyMeta("reg_count", "regCount", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "guid": "guid", 
        "id": "id", 
        "productFamily": "product_family", 
        "regCount": "reg_count", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, guid, **kwargs):
        self._dirty_mask = 0
        self.guid = guid
        self.child_action = None
        self.id = None
        self.product_family = None
        self.reg_count = None
        self.status = None

        ManagedObject.__init__(self, "ExtpolDomain", parent_mo_or_dn, **kwargs)

