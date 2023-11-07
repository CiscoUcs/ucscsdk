"""This module contains the general information for StorageMeta ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StorageMetaConsts():
    pass


class StorageMeta(ManagedObject):
    """This is StorageMeta class."""

    consts = StorageMetaConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageMeta", "storageMeta", "meta", VersionMeta.Version131a, "InputOutput", 0xf, [], ["admin"], ['storageBlade'], ['faultInst'], [None])

    prop_meta = {
        "ucs_domain_name": MoPropertyMeta("ucs_domain_name", "UCSDomainName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|storage-blade-not-in-discovery-mode|missing-qualifier|global-array-storageArray-not-opted|domain-group-missing|matching-qualifier-error|missing-arrayAutoConfigRef|storage-blade-already-in-use|missing-arrayAutoConfigPolicy),){0,9}(defaultValue|not-applicable|storage-blade-not-in-discovery-mode|missing-qualifier|global-array-storageArray-not-opted|domain-group-missing|matching-qualifier-error|missing-arrayAutoConfigRef|storage-blade-already-in-use|missing-arrayAutoConfigPolicy){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "group_dn": MoPropertyMeta("group_dn", "groupDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "num_of_missing_policies": MoPropertyMeta("num_of_missing_policies", "numOfMissingPolicies", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_missingualifying_policies": MoPropertyMeta("num_of_missingualifying_policies", "numOfMissingualifyingPolicies", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_unqualifying_policies": MoPropertyMeta("num_of_unqualifying_policies", "numOfUnqualifyingPolicies", "ulong", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "UCSDomainName": "ucs_domain_name", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "dn": "dn", 
        "groupDn": "group_dn", 
        "numOfMissingPolicies": "num_of_missing_policies", 
        "numOfMissingualifyingPolicies": "num_of_missingualifying_policies", 
        "numOfUnqualifyingPolicies": "num_of_unqualifying_policies", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.ucs_domain_name = None
        self.child_action = None
        self.config_qualifier = None
        self.group_dn = None
        self.num_of_missing_policies = None
        self.num_of_missingualifying_policies = None
        self.num_of_unqualifying_policies = None
        self.status = None

        ManagedObject.__init__(self, "StorageMeta", parent_mo_or_dn, **kwargs)

