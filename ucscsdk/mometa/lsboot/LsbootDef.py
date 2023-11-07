"""This module contains the general information for LsbootDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsbootDefConsts():
    ADV_BOOT_ORDER_APPLICABLE_FALSE = "false"
    ADV_BOOT_ORDER_APPLICABLE_NO = "no"
    ADV_BOOT_ORDER_APPLICABLE_TRUE = "true"
    ADV_BOOT_ORDER_APPLICABLE_YES = "yes"
    ENFORCE_VNIC_NAME_FALSE = "false"
    ENFORCE_VNIC_NAME_NO = "no"
    ENFORCE_VNIC_NAME_TRUE = "true"
    ENFORCE_VNIC_NAME_YES = "yes"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    PURPOSE_OPERATIONAL = "operational"
    PURPOSE_UTILITY = "utility"
    REBOOT_ON_UPDATE_FALSE = "false"
    REBOOT_ON_UPDATE_NO = "no"
    REBOOT_ON_UPDATE_TRUE = "true"
    REBOOT_ON_UPDATE_YES = "yes"


class LsbootDef(ManagedObject):
    """This is LsbootDef class."""

    consts = LsbootDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootDef", "lsbootDef", "boot-policy", VersionMeta.Version111a, "InputOutput", 0x1ff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], ['computeBlade', 'computeRackUnit', 'computeServerUnit', 'lsServer'], ['lsbootBootSecurity', 'lsbootEFIShell', 'lsbootIScsi', 'lsbootLan', 'lsbootSan', 'lsbootStorage', 'lsbootVirtualMedia'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "adv_boot_order_applicable": MoPropertyMeta("adv_boot_order_applicable", "advBootOrderApplicable", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["false", "no", "true", "yes"], []), 
        "boot_mode": MoPropertyMeta("boot_mode", "bootMode", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "enforce_vnic_name": MoPropertyMeta("enforce_vnic_name", "enforceVnicName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["false", "no", "true", "yes"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["operational", "utility"], []), 
        "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "advBootOrderApplicable": "adv_boot_order_applicable", 
        "bootMode": "boot_mode", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "enforceVnicName": "enforce_vnic_name", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "purpose": "purpose", 
        "rebootOnUpdate": "reboot_on_update", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.adv_boot_order_applicable = None
        self.boot_mode = None
        self.child_action = None
        self.descr = None
        self.enforce_vnic_name = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.purpose = None
        self.reboot_on_update = None
        self.status = None

        ManagedObject.__init__(self, "LsbootDef", parent_mo_or_dn, **kwargs)

