"""This module contains the general information for EquipmentCPMeta ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentCPMetaConsts():
    CP_REFRESH_DISABLED = "disabled"
    CP_REFRESH_ENABLED = "enabled"
    IS_RENAME_FALSE = "false"
    IS_RENAME_NO = "no"
    IS_RENAME_TRUE = "true"
    IS_RENAME_YES = "yes"
    NEED_ID_RE_EVALUATE_NO = "no"
    NEED_ID_RE_EVALUATE_YES = "yes"
    OPERATION_CODE_ASSOCIATE = "associate"
    OPERATION_CODE_DELETION = "deletion"
    OPERATION_CODE_DISASSOCIATE = "disassociate"
    OPERATION_CODE_NO_OP = "no-op"
    OPERATION_CODE_RENAME = "rename"
    OPERATION_CODE_CLEARANCE_DISABLED = "disabled"
    OPERATION_CODE_CLEARANCE_ENABLED = "enabled"
    OWNERSHIP_STATE_DELETE_PENDING = "delete-pending"
    OWNERSHIP_STATE_DISASSOC_PENDING = "disassoc-pending"
    OWNERSHIP_STATE_GLOBAL_CONTROLLED = "global-controlled"
    OWNERSHIP_STATE_LOCALIZED = "localized"


class EquipmentCPMeta(ManagedObject):
    """This is EquipmentCPMeta class."""

    consts = EquipmentCPMetaConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentCPMeta", "equipmentCPMeta", "cpmeta", VersionMeta.Version151a, "InputOutput", 0x3f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['equipmentChassisProfile'], ['messageEp'], ["Get"])

    prop_meta = {
        "chassis_dn": MoPropertyMeta("chassis_dn", "chassisDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable),){0,1}(defaultValue|not-applicable){0,1}""", [], []), 
        "cp_refresh": MoPropertyMeta("cp_refresh", "cpRefresh", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "is_rename": MoPropertyMeta("is_rename", "isRename", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "need_id_re_evaluate": MoPropertyMeta("need_id_re_evaluate", "needIdReEvaluate", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "new_cpdn": MoPropertyMeta("new_cpdn", "newCPDN", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "old_cpdn": MoPropertyMeta("old_cpdn", "oldCPDN", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "operation_code": MoPropertyMeta("operation_code", "operationCode", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["associate", "deletion", "disassociate", "no-op", "rename"], []), 
        "operation_code_clearance": MoPropertyMeta("operation_code_clearance", "operationCodeClearance", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["disabled", "enabled"], []), 
        "ownership_state": MoPropertyMeta("ownership_state", "ownershipState", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["delete-pending", "disassoc-pending", "global-controlled", "localized"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "chassisDn": "chassis_dn", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "cpRefresh": "cp_refresh", 
        "dn": "dn", 
        "guid": "guid", 
        "isRename": "is_rename", 
        "needIdReEvaluate": "need_id_re_evaluate", 
        "newCPDN": "new_cpdn", 
        "oldCPDN": "old_cpdn", 
        "operationCode": "operation_code", 
        "operationCodeClearance": "operation_code_clearance", 
        "ownershipState": "ownership_state", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.chassis_dn = None
        self.child_action = None
        self.config_qualifier = None
        self.cp_refresh = None
        self.guid = None
        self.is_rename = None
        self.need_id_re_evaluate = None
        self.new_cpdn = None
        self.old_cpdn = None
        self.operation_code = None
        self.operation_code_clearance = None
        self.ownership_state = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentCPMeta", parent_mo_or_dn, **kwargs)

