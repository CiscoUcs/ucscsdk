"""This module contains the general information for ConfigSpotLightItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigSpotLightItemConsts():
    pass


class ConfigSpotLightItem(ManagedObject):
    """This is ConfigSpotLightItem class."""

    consts = ConfigSpotLightItemConsts()
    naming_props = set(['compositeId'])

    mo_meta = MoMeta("ConfigSpotLightItem", "configSpotLightItem", "spotlight-[composite_id]", VersionMeta.Version201b, "InputOutput", 0x1f, [], ["admin"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "composite_id": MoPropertyMeta("composite_id", "compositeId", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x2, 1, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "oper_category": MoPropertyMeta("oper_category", "operCategory", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_dn": MoPropertyMeta("oper_dn", "operDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_domain_dn": MoPropertyMeta("oper_domain_dn", "operDomainDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_domain_group_dn": MoPropertyMeta("oper_domain_group_dn", "operDomainGroupDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_id": MoPropertyMeta("oper_id", "operId", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_name": MoPropertyMeta("oper_name", "operName", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_org_dn": MoPropertyMeta("oper_org_dn", "operOrgDn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_search_field": MoPropertyMeta("oper_search_field", "operSearchField", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_sec_search_field": MoPropertyMeta("oper_sec_search_field", "operSecSearchField", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_src_dme": MoPropertyMeta("oper_src_dme", "operSrcDme", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_sub_type": MoPropertyMeta("oper_sub_type", "operSubType", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_third_search_field": MoPropertyMeta("oper_third_search_field", "operThirdSearchField", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_type": MoPropertyMeta("oper_type", "operType", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "score": MoPropertyMeta("score", "score", "float", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "compositeId": "composite_id", 
        "dn": "dn", 
        "operCategory": "oper_category", 
        "operDn": "oper_dn", 
        "operDomainDn": "oper_domain_dn", 
        "operDomainGroupDn": "oper_domain_group_dn", 
        "operId": "oper_id", 
        "operName": "oper_name", 
        "operOrgDn": "oper_org_dn", 
        "operSearchField": "oper_search_field", 
        "operSecSearchField": "oper_sec_search_field", 
        "operSrcDme": "oper_src_dme", 
        "operSubType": "oper_sub_type", 
        "operThirdSearchField": "oper_third_search_field", 
        "operType": "oper_type", 
        "rn": "rn", 
        "score": "score", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, composite_id, **kwargs):
        self._dirty_mask = 0
        self.composite_id = composite_id
        self.child_action = None
        self.oper_category = None
        self.oper_dn = None
        self.oper_domain_dn = None
        self.oper_domain_group_dn = None
        self.oper_id = None
        self.oper_name = None
        self.oper_org_dn = None
        self.oper_search_field = None
        self.oper_sec_search_field = None
        self.oper_src_dme = None
        self.oper_sub_type = None
        self.oper_third_search_field = None
        self.oper_type = None
        self.score = None
        self.status = None

        ManagedObject.__init__(self, "ConfigSpotLightItem", parent_mo_or_dn, **kwargs)

