"""This module contains the general information for VnicIScsiStaticTargetIf ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicIScsiStaticTargetIfConsts():
    OWNER_TYPE_MANAGED = "managed"
    OWNER_TYPE_UNMANAGED = "unmanaged"
    OWNER_TYPE_UNSPECIFIED = "unspecified"


class VnicIScsiStaticTargetIf(ManagedObject):
    """This is VnicIScsiStaticTargetIf class."""

    consts = VnicIScsiStaticTargetIfConsts()
    naming_props = set(['priority'])

    mo_meta = MoMeta("VnicIScsiStaticTargetIf", "vnicIScsiStaticTargetIf", "[priority]", VersionMeta.Version111a, "InputOutput", 0x1ff, [], ["admin", "ls-config", "ls-network", "ls-server", "ls-storage"], ['vnicIScsi', 'vnicIScsiBootVnic', 'vnicIScsiTargetParams', 'vnicVlan'], ['faultInst', 'vnicLun'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "auth_profile_name": MoPropertyMeta("auth_profile_name", "authProfileName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "ip_address": MoPropertyMeta("ip_address", "ipAddress", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[0-9a-zA-Z\.:-]{0,223}""", [], []), 
        "oper_auth_profile_name": MoPropertyMeta("oper_auth_profile_name", "operAuthProfileName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "owner_type": MoPropertyMeta("owner_type", "ownerType", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["managed", "unmanaged", "unspecified"], []), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["1-65535"]), 
        "priority": MoPropertyMeta("priority", "priority", "ushort", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x40, None, None, None, [], ["1-2"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "authProfileName": "auth_profile_name", 
        "childAction": "child_action", 
        "dn": "dn", 
        "ipAddress": "ip_address", 
        "name": "name", 
        "operAuthProfileName": "oper_auth_profile_name", 
        "ownerType": "owner_type", 
        "port": "port", 
        "priority": "priority", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, priority, **kwargs):
        self._dirty_mask = 0
        self.priority = priority
        self.auth_profile_name = None
        self.child_action = None
        self.ip_address = None
        self.name = None
        self.oper_auth_profile_name = None
        self.owner_type = None
        self.port = None
        self.status = None

        ManagedObject.__init__(self, "VnicIScsiStaticTargetIf", parent_mo_or_dn, **kwargs)

