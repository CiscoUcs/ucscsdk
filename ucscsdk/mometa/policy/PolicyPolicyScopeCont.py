"""This module contains the general information for PolicyPolicyScopeCont ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class PolicyPolicyScopeContConsts():
    NEED_RECOVERY_FALSE = "false"
    NEED_RECOVERY_NO = "no"
    NEED_RECOVERY_TRUE = "true"
    NEED_RECOVERY_YES = "yes"


class PolicyPolicyScopeCont(ManagedObject):
    """This is PolicyPolicyScopeCont class."""

    consts = PolicyPolicyScopeContConsts()
    naming_props = set(['appType'])

    mo_meta = MoMeta("PolicyPolicyScopeCont", "policyPolicyScopeCont", "scope-cont-[app_type]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin"], ['extpolClient', 'extpolController', 'extpolProvider', 'extpolRegistry', 'policyPolicyEp'], ['policyPolicyScopeContext'], [None])

    prop_meta = {
        "app_type": MoPropertyMeta("app_type", "appType", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x2, 1, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "gen_num": MoPropertyMeta("gen_num", "genNum", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "need_recovery": MoPropertyMeta("need_recovery", "needRecovery", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "appType": "app_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "genNum": "gen_num", 
        "needRecovery": "need_recovery", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, app_type, **kwargs):
        self._dirty_mask = 0
        self.app_type = app_type
        self.child_action = None
        self.gen_num = None
        self.need_recovery = None
        self.status = None

        ManagedObject.__init__(self, "PolicyPolicyScopeCont", parent_mo_or_dn, **kwargs)

