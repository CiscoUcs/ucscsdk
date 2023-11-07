"""This module contains the general information for LsSPMeta ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsSPMetaConsts():
    GLOBALIZATION_STATE_GLOBALIZED = "Globalized"
    GLOBALIZATION_STATE_GLOBALIZING = "globalizing"
    GLOBALIZATION_STATE_NO_OP = "no-op"
    IS_RENAME_FALSE = "false"
    IS_RENAME_NO = "no"
    IS_RENAME_TRUE = "true"
    IS_RENAME_YES = "yes"
    NEED_ID_RE_EVALUATE_NO = "no"
    NEED_ID_RE_EVALUATE_YES = "yes"
    OPERATION_CODE_ASSOCIATE = "associate"
    OPERATION_CODE_DELETION = "deletion"
    OPERATION_CODE_DISASSOCIATE = "disassociate"
    OPERATION_CODE_GLOBALIZATION = "globalization"
    OPERATION_CODE_NO_OP = "no-op"
    OPERATION_CODE_RENAME = "rename"
    OPERATION_CODE_CLEARANCE_DISABLED = "disabled"
    OPERATION_CODE_CLEARANCE_ENABLED = "enabled"
    OWNERSHIP_STATE_DELETE_PENDING = "delete-pending"
    OWNERSHIP_STATE_DISASSOC_PENDING = "disassoc-pending"
    OWNERSHIP_STATE_GLOBAL_CONTROLLED = "global-controlled"
    OWNERSHIP_STATE_LOCALIZED = "localized"
    SP_REFRESH_DISABLED = "disabled"
    SP_REFRESH_ENABLED = "enabled"


class LsSPMeta(ManagedObject):
    """This is LsSPMeta class."""

    consts = LsSPMetaConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsSPMeta", "lsSPMeta", "spmeta", VersionMeta.Version111a, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-oper", "ls-server-policy"], ['lsServer'], ['faultInst', 'messageEntry', 'messageEp'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|ungrouped-domain),){0,2}(defaultValue|not-applicable|ungrouped-domain){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "globalization_state": MoPropertyMeta("globalization_state", "globalizationState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Globalized", "globalizing", "no-op"], []), 
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "is_rename": MoPropertyMeta("is_rename", "isRename", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "need_id_re_evaluate": MoPropertyMeta("need_id_re_evaluate", "needIdReEvaluate", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "new_spdn": MoPropertyMeta("new_spdn", "newSPDN", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "old_spdn": MoPropertyMeta("old_spdn", "oldSPDN", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "operation_code": MoPropertyMeta("operation_code", "operationCode", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["associate", "deletion", "disassociate", "globalization", "no-op", "rename"], []), 
        "operation_code_clearance": MoPropertyMeta("operation_code_clearance", "operationCodeClearance", "string", VersionMeta.Version131a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["disabled", "enabled"], []), 
        "ownership_state": MoPropertyMeta("ownership_state", "ownershipState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["delete-pending", "disassoc-pending", "global-controlled", "localized"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "server_dn": MoPropertyMeta("server_dn", "serverDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "sp_refresh": MoPropertyMeta("sp_refresh", "spRefresh", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["disabled", "enabled"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "dn": "dn", 
        "globalizationState": "globalization_state", 
        "guid": "guid", 
        "isRename": "is_rename", 
        "needIdReEvaluate": "need_id_re_evaluate", 
        "newSPDN": "new_spdn", 
        "oldSPDN": "old_spdn", 
        "operationCode": "operation_code", 
        "operationCodeClearance": "operation_code_clearance", 
        "ownershipState": "ownership_state", 
        "rn": "rn", 
        "serverDn": "server_dn", 
        "spRefresh": "sp_refresh", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.config_qualifier = None
        self.globalization_state = None
        self.guid = None
        self.is_rename = None
        self.need_id_re_evaluate = None
        self.new_spdn = None
        self.old_spdn = None
        self.operation_code = None
        self.operation_code_clearance = None
        self.ownership_state = None
        self.server_dn = None
        self.sp_refresh = None
        self.status = None

        ManagedObject.__init__(self, "LsSPMeta", parent_mo_or_dn, **kwargs)

