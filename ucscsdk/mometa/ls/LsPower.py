"""This module contains the general information for LsPower ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsPowerConsts():
    STATE_ADMIN_DOWN = "admin-down"
    STATE_ADMIN_UP = "admin-up"
    STATE_BMC_RESET_IMMEDIATE = "bmc-reset-immediate"
    STATE_BMC_RESET_WAIT = "bmc-reset-wait"
    STATE_CMOS_RESET_IMMEDIATE = "cmos-reset-immediate"
    STATE_CYCLE_IMMEDIATE = "cycle-immediate"
    STATE_CYCLE_WAIT = "cycle-wait"
    STATE_DIAGNOSTIC_INTERRUPT = "diagnostic-interrupt"
    STATE_DOWN = "down"
    STATE_HARD_RESET_IMMEDIATE = "hard-reset-immediate"
    STATE_HARD_RESET_WAIT = "hard-reset-wait"
    STATE_IPMI_RESET = "ipmi-reset"
    STATE_KVM_RESET = "kvm-reset"
    STATE_SOFT_SHUT_DOWN = "soft-shut-down"
    STATE_SOFT_SHUT_DOWN_ONLY = "soft-shut-down-only"
    STATE_UP = "up"


class LsPower(ManagedObject):
    """This is LsPower class."""

    consts = LsPowerConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsPower", "lsPower", "power", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-oper", "ls-server-policy"], [u'computeInstance', u'lsServer'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["admin-down", "admin-up", "bmc-reset-immediate", "bmc-reset-wait", "cmos-reset-immediate", "cycle-immediate", "cycle-wait", "diagnostic-interrupt", "down", "hard-reset-immediate", "hard-reset-wait", "ipmi-reset", "kvm-reset", "soft-shut-down", "soft-shut-down-only", "up"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "state": "state", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.state = None
        self.status = None

        ManagedObject.__init__(self, "LsPower", parent_mo_or_dn, **kwargs)

