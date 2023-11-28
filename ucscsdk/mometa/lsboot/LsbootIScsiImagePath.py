"""This module contains the general information for LsbootIScsiImagePath ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsbootIScsiImagePathConsts():
    pass


class LsbootIScsiImagePath(ManagedObject):
    """This is LsbootIScsiImagePath class."""

    consts = LsbootIScsiImagePathConsts()
    naming_props = set(['type'])

    mo_meta = MoMeta("LsbootIScsiImagePath", "lsbootIScsiImagePath", "path-[type]", VersionMeta.Version111a, "InputOutput", 0xff, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], ['lsbootIScsi'], ['lsbootUEFIBootParam', 'vnicIScsiTargetParams'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "i_scsi_vnic_name": MoPropertyMeta("i_scsi_vnic_name", "iSCSIVnicName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "ip_addr_type": MoPropertyMeta("ip_addr_type", "ipAddrType", "string", VersionMeta.Version201f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []), 
        "vnic_name": MoPropertyMeta("vnic_name", "vnicName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "iSCSIVnicName": "i_scsi_vnic_name", 
        "ipAddrType": "ip_addr_type", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "vnicName": "vnic_name", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.i_scsi_vnic_name = None
        self.ip_addr_type = None
        self.status = None
        self.vnic_name = None

        ManagedObject.__init__(self, "LsbootIScsiImagePath", parent_mo_or_dn, **kwargs)

