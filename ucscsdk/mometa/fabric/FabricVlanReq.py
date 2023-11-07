"""This module contains the general information for FabricVlanReq ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FabricVlanReqConsts():
    TYPE_LAN = "lan"
    TYPE_SAN = "san"


class FabricVlanReq(ManagedObject):
    """This is FabricVlanReq class."""

    consts = FabricVlanReqConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FabricVlanReq", "fabricVlanReq", "vlan-req-[name]", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin", "ext-lan-config", "ext-lan-policy", "ls-network"], ['orgOrg'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_issues": MoPropertyMeta("config_issues", "configIssues", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|permit-unresolved),){0,2}(defaultValue|not-applicable|permit-unresolved){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lan", "san"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configIssues": "config_issues", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config_issues = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "FabricVlanReq", parent_mo_or_dn, **kwargs)

