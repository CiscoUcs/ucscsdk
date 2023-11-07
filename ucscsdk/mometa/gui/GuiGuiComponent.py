"""This module contains the general information for GuiGuiComponent ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GuiGuiComponentConsts():
    pass


class GuiGuiComponent(ManagedObject):
    """This is GuiGuiComponent class."""

    consts = GuiGuiComponentConsts()
    naming_props = set(['appId'])

    mo_meta = MoMeta("GuiGuiComponent", "guiGuiComponent", "gui-[app_id]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin"], ['guiGuiCont'], [], [None])

    prop_meta = {
        "app_id": MoPropertyMeta("app_id", "appId", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x2, 1, 510, None, [], []), 
        "app_type": MoPropertyMeta("app_type", "appType", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "parent_id": MoPropertyMeta("parent_id", "parentId", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "title": MoPropertyMeta("title", "title", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "uri": MoPropertyMeta("uri", "uri", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "weight": MoPropertyMeta("weight", "weight", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "appId": "app_id", 
        "appType": "app_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "parentId": "parent_id", 
        "rn": "rn", 
        "status": "status", 
        "title": "title", 
        "uri": "uri", 
        "weight": "weight", 
    }

    def __init__(self, parent_mo_or_dn, app_id, **kwargs):
        self._dirty_mask = 0
        self.app_id = app_id
        self.app_type = None
        self.child_action = None
        self.parent_id = None
        self.status = None
        self.title = None
        self.uri = None
        self.weight = None

        ManagedObject.__init__(self, "GuiGuiComponent", parent_mo_or_dn, **kwargs)

