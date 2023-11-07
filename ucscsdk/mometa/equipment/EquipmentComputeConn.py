"""This module contains the general information for EquipmentComputeConn ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentComputeConnConsts():
    SERVER_SIOC_CONNECTIVITY_SINGLE_SERVER_DUAL_SIOC = "single-server-dual-sioc"
    SERVER_SIOC_CONNECTIVITY_SINGLE_SERVER_SINGLE_SIOC = "single-server-single-sioc"


class EquipmentComputeConn(ManagedObject):
    """This is EquipmentComputeConn class."""

    consts = EquipmentComputeConnConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentComputeConn", "equipmentComputeConn", "compute-conn", VersionMeta.Version201b, "InputOutput", 0xf, [], [""], ['equipmentChassis'], [], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "server_sioc_connectivity": MoPropertyMeta("server_sioc_connectivity", "serverSiocConnectivity", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["single-server-dual-sioc", "single-server-single-sioc"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "serverSiocConnectivity": "server_sioc_connectivity", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.server_sioc_connectivity = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentComputeConn", parent_mo_or_dn, **kwargs)

