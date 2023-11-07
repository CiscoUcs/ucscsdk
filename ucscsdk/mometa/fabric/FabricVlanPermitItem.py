"""This module contains the general information for FabricVlanPermitItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricVlanPermitItemConsts():
    SHARING_COMMUNITY = "community"
    SHARING_ISOLATED = "isolated"
    SHARING_NONE = "none"
    SHARING_PRIMARY = "primary"
    VLAN_STATUS_ASSIGNED = "assigned"
    VLAN_STATUS_AVAILABLE = "available"
    VLAN_STATUS_IN_USE = "in-use"
    VLAN_SWITCH_ID_A = "A"
    VLAN_SWITCH_ID_B = "B"
    VLAN_SWITCH_ID_NONE = "NONE"
    VLAN_SWITCH_ID_MGMT = "mgmt"


class FabricVlanPermitItem(ManagedObject):
    """This is FabricVlanPermitItem class."""

    consts = FabricVlanPermitItemConsts()
    naming_props = set(['vlanName'])

    mo_meta = MoMeta("FabricVlanPermitItem", "fabricVlanPermitItem", "vlan-permit-item-[vlan_name]", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["read-only"], [], ['configOrgItem'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_group_name": MoPropertyMeta("domain_group_name", "domainGroupName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "pub_nw_name": MoPropertyMeta("pub_nw_name", "pubNwName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "sharing": MoPropertyMeta("sharing", "sharing", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["community", "isolated", "none", "primary"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vlan_dn": MoPropertyMeta("vlan_dn", "vlanDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "vlan_id": MoPropertyMeta("vlan_id", "vlanId", "uint", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]), 
        "vlan_name": MoPropertyMeta("vlan_name", "vlanName", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "vlan_status": MoPropertyMeta("vlan_status", "vlanStatus", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["assigned", "available", "in-use"], []), 
        "vlan_switch_id": MoPropertyMeta("vlan_switch_id", "vlanSwitchId", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "domainGroupDn": "domain_group_dn", 
        "domainGroupName": "domain_group_name", 
        "pubNwName": "pub_nw_name", 
        "rn": "rn", 
        "sharing": "sharing", 
        "status": "status", 
        "vlanDn": "vlan_dn", 
        "vlanId": "vlan_id", 
        "vlanName": "vlan_name", 
        "vlanStatus": "vlan_status", 
        "vlanSwitchId": "vlan_switch_id", 
    }

    def __init__(self, parent_mo_or_dn, vlan_name, **kwargs):
        self._dirty_mask = 0
        self.vlan_name = vlan_name
        self.child_action = None
        self.domain_group_dn = None
        self.domain_group_name = None
        self.pub_nw_name = None
        self.sharing = None
        self.status = None
        self.vlan_dn = None
        self.vlan_id = None
        self.vlan_status = None
        self.vlan_switch_id = None

        ManagedObject.__init__(self, "FabricVlanPermitItem", parent_mo_or_dn, **kwargs)

