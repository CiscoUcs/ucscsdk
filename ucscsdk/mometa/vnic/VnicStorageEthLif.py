"""This module contains the general information for VnicStorageEthLif ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicStorageEthLifConsts():
    OPER_STATE_DOWN = "down"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_UP = "up"
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"
    SHARING_COMMUNITY = "community"
    SHARING_ISOLATED = "isolated"
    SHARING_NONE = "none"
    SHARING_PRIMARY = "primary"
    SWITCH_ID_A = "A"
    SWITCH_ID_A_B = "A-B"
    SWITCH_ID_AB = "AB"
    SWITCH_ID_B = "B"
    SWITCH_ID_B_A = "B-A"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_DUAL = "dual"
    SWITCH_ID_MGMT = "mgmt"
    TYPE_ETHER = "ether"
    TYPE_FC = "fc"
    TYPE_IPC = "ipc"
    TYPE_SCSI = "scsi"
    TYPE_UNKNOWN = "unknown"


class VnicStorageEthLif(ManagedObject):
    """This is VnicStorageEthLif class."""

    consts = VnicStorageEthLifConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("VnicStorageEthLif", "vnicStorageEthLif", "eth-lif-[name]", VersionMeta.Version131a, "InputOutput", 0xff, [], ["admin", "ls-config", "ls-network", "ls-server", "ls-storage"], [], ['faultInst', 'vnicFault', 'vnicIPv4If'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|unsupported-azurestackqos-geneve|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unsupported-adaptor-for-vnic-cdn|misconfigured-net-san-group|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|redundancy-vnicpair-not-in-sync|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|unsupported-roce-properties|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|duplicate-vnic-cdn-name|overlapping-vlans|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|unsupported-adaptor-for-vnic-oracle-rac|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-roce-sriov|unsupported-geneve-usnic-vmq|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|insufficient-roce-resources|unsupported-azurestackqos-vmmq-geneve-advfilters|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unsupported-roce-nvgre|unresolved-net-san-group|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-roce-vxlan|unsupported-vxlan-vmq|redundancy-vnic-not-in-pair|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig|unsupported-vmq-resources),){0,67}(defaultValue|not-applicable|unsupported-azurestackqos-geneve|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unsupported-adaptor-for-vnic-cdn|misconfigured-net-san-group|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|redundancy-vnicpair-not-in-sync|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|unsupported-roce-properties|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|duplicate-vnic-cdn-name|overlapping-vlans|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|unsupported-adaptor-for-vnic-oracle-rac|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-roce-sriov|unsupported-geneve-usnic-vmq|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|insufficient-roce-resources|unsupported-azurestackqos-vmmq-geneve-advfilters|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unsupported-roce-nvgre|unresolved-net-san-group|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-roce-vxlan|unsupported-vxlan-vmq|redundancy-vnic-not-in-pair|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig|unsupported-vmq-resources){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version131a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_primary_vnet_dn": MoPropertyMeta("oper_primary_vnet_dn", "operPrimaryVnetDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_primary_vnet_name": MoPropertyMeta("oper_primary_vnet_name", "operPrimaryVnetName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["down", "failed", "indeterminate", "up"], []), 
        "oper_vlan_name": MoPropertyMeta("oper_vlan_name", "operVlanName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_vnet_dn": MoPropertyMeta("oper_vnet_dn", "operVnetDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_vnet_name": MoPropertyMeta("oper_vnet_name", "operVnetName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []), 
        "pub_nw_id": MoPropertyMeta("pub_nw_id", "pubNwId", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "role": MoPropertyMeta("role", "role", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((defaultValue|none|nfs|node-mgmt|node-ha-state|cifs|data-protection|iscsi),){0,7}(defaultValue|none|nfs|node-mgmt|node-ha-state|cifs|data-protection|iscsi){0,1}""", [], []), 
        "sharing": MoPropertyMeta("sharing", "sharing", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["community", "isolated", "none", "primary"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["A", "A-B", "AB", "B", "B-A", "NONE", "dual", "mgmt"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], []), 
        "vlan_name": MoPropertyMeta("vlan_name", "vlanName", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []), 
        "vnet": MoPropertyMeta("vnet", "vnet", "uint", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "dn": "dn", 
        "name": "name", 
        "operPrimaryVnetDn": "oper_primary_vnet_dn", 
        "operPrimaryVnetName": "oper_primary_vnet_name", 
        "operState": "oper_state", 
        "operVlanName": "oper_vlan_name", 
        "operVnetDn": "oper_vnet_dn", 
        "operVnetName": "oper_vnet_name", 
        "owner": "owner", 
        "pubNwId": "pub_nw_id", 
        "rn": "rn", 
        "role": "role", 
        "sharing": "sharing", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
        "vlanName": "vlan_name", 
        "vnet": "vnet", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config_qualifier = None
        self.oper_primary_vnet_dn = None
        self.oper_primary_vnet_name = None
        self.oper_state = None
        self.oper_vlan_name = None
        self.oper_vnet_dn = None
        self.oper_vnet_name = None
        self.owner = None
        self.pub_nw_id = None
        self.role = None
        self.sharing = None
        self.status = None
        self.switch_id = None
        self.type = None
        self.vlan_name = None
        self.vnet = None

        ManagedObject.__init__(self, "VnicStorageEthLif", parent_mo_or_dn, **kwargs)

