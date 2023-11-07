"""This module contains the general information for ConfigOrgItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class ConfigOrgItemConsts():
    pass


class ConfigOrgItem(ManagedObject):
    """This is ConfigOrgItem class."""

    consts = ConfigOrgItemConsts()
    naming_props = set(['context'])

    mo_meta = MoMeta("ConfigOrgItem", "configOrgItem", "org-item-[context]", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["read-only"], ['fabricVlanPermitItem'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "context": MoPropertyMeta("context", "context", "string", VersionMeta.Version141a, MoPropertyMeta.NAMING, 0x2, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "org_dn": MoPropertyMeta("org_dn", "orgDn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "context": "context", 
        "dn": "dn", 
        "name": "name", 
        "orgDn": "org_dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, context, **kwargs):
        self._dirty_mask = 0
        self.context = context
        self.child_action = None
        self.name = None
        self.org_dn = None
        self.status = None

        ManagedObject.__init__(self, "ConfigOrgItem", parent_mo_or_dn, **kwargs)

