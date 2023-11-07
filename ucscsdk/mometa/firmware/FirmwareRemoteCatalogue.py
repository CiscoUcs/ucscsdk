"""This module contains the general information for FirmwareRemoteCatalogue ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FirmwareRemoteCatalogueConsts():
    pass


class FirmwareRemoteCatalogue(ManagedObject):
    """This is FirmwareRemoteCatalogue class."""

    consts = FirmwareRemoteCatalogueConsts()
    naming_props = set(['server'])

    mo_meta = MoMeta("FirmwareRemoteCatalogue", "firmwareRemoteCatalogue", "remote-fw-catalogue-[server]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["read-only"], ['topSystem'], ['firmwareCompSource', 'firmwareDistributable', 'firmwareImage'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "server": MoPropertyMeta("server", "server", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "server": "server", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, server, **kwargs):
        self._dirty_mask = 0
        self.server = server
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareRemoteCatalogue", parent_mo_or_dn, **kwargs)

