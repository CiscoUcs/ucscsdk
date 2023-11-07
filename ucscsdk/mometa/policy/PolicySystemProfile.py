"""This module contains the general information for PolicySystemProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicySystemProfileConsts():
    pass


class PolicySystemProfile(ManagedObject):
    """This is PolicySystemProfile class."""

    consts = PolicySystemProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("PolicySystemProfile", "policySystemProfile", "SystemProfile", VersionMeta.Version112a, "InputOutput", 0x1f, [], ["read-only"], ['orgOrg'], ['faultInst'], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version112a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "device_profile_ref": MoPropertyMeta("device_profile_ref", "deviceProfileRef", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "oper_device_profile_ref": MoPropertyMeta("oper_device_profile_ref", "operDeviceProfileRef", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "deviceProfileRef": "device_profile_ref", 
        "dn": "dn", 
        "operDeviceProfileRef": "oper_device_profile_ref", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.device_profile_ref = None
        self.oper_device_profile_ref = None
        self.status = None

        ManagedObject.__init__(self, "PolicySystemProfile", parent_mo_or_dn, **kwargs)

