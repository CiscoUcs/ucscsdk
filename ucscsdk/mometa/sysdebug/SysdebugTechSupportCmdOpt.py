"""This module contains the general information for SysdebugTechSupportCmdOpt ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SysdebugTechSupportCmdOptConsts():
    CHASSIS_CARTRIDGE_ID_ALL = "all"
    CHASSIS_CIMC_ID_ALL = "all"
    CHASSIS_IOM_ID_ALL = "all"
    CIMC_ADAPTER_ID_ALL = "all"
    IS_EXCLUDE_DATA_FALSE = "false"
    IS_EXCLUDE_DATA_NO = "no"
    IS_EXCLUDE_DATA_TRUE = "true"
    IS_EXCLUDE_DATA_YES = "yes"
    MAJOR_OPT_TYPE_CHASSIS = "chassis"
    MAJOR_OPT_TYPE_FEX = "fex"
    MAJOR_OPT_TYPE_SERVER = "server"
    MAJOR_OPT_TYPE_SERVER_MEMORY = "server-memory"
    MAJOR_OPT_TYPE_UCSM = "ucsm"
    MAJOR_OPT_TYPE_UCSM_MGMT = "ucsm-mgmt"
    RACK_SERVER_ADAPTER_ID_ALL = "all"


class SysdebugTechSupportCmdOpt(ManagedObject):
    """This is SysdebugTechSupportCmdOpt class."""

    consts = SysdebugTechSupportCmdOptConsts()
    naming_props = set([])

    mo_meta = MoMeta("SysdebugTechSupportCmdOpt", "sysdebugTechSupportCmdOpt", "tech-support-cmd-opt", VersionMeta.Version101a, "InputOutput", 0x3ffff, [], ["admin", "operations"], ['sysdebugTechSupport', 'sysdebugTechSupportOp', 'sysdebugTechSupportOperation'], [], ["Add", "Get", "Set"])

    prop_meta = {
        "cartridge_cimc_id": MoPropertyMeta("cartridge_cimc_id", "cartridgeCIMCId", "ushort", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["1-2"]), 
        "chassis_cartridge_id": MoPropertyMeta("chassis_cartridge_id", "chassisCartridgeId", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["all"], ["0-8"]), 
        "chassis_cimc_id": MoPropertyMeta("chassis_cimc_id", "chassisCimcId", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["all"], ["0-8"]), 
        "chassis_id": MoPropertyMeta("chassis_id", "chassisId", "ushort", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-255"]), 
        "chassis_iom_id": MoPropertyMeta("chassis_iom_id", "chassisIomId", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["all"], ["0-2"]), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cimc_adapter_id": MoPropertyMeta("cimc_adapter_id", "cimcAdapterId", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["all"], ["0-8"]), 
        "command_options": MoPropertyMeta("command_options", "commandOptions", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((defaultValue|none|ucsm-exclude-commands),){0,2}(defaultValue|none|ucsm-exclude-commands){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "fab_ext_id": MoPropertyMeta("fab_ext_id", "fabExtId", "ushort", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["1-255"]), 
        "is_exclude_data": MoPropertyMeta("is_exclude_data", "isExcludeData", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["false", "no", "true", "yes"], []), 
        "major_opt_type": MoPropertyMeta("major_opt_type", "majorOptType", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["chassis", "fex", "server", "server-memory", "ucsm", "ucsm-mgmt"], []), 
        "rack_server_adapter_id": MoPropertyMeta("rack_server_adapter_id", "rackServerAdapterId", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["all"], ["0-8"]), 
        "rack_server_id": MoPropertyMeta("rack_server_id", "rackServerId", "ushort", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, [], ["1-255"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4000, 0, 256, None, [], []), 
        "scope": MoPropertyMeta("scope", "scope", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, r"""((mgmt-controller|service-reg|operation-mgr|identifier-mgr|resource-mgr|policy-mgr|storage-broker|stats-mgr|all|defaultValue),){0,9}(mgmt-controller|service-reg|operation-mgr|identifier-mgr|resource-mgr|policy-mgr|storage-broker|stats-mgr|all|defaultValue){0,1}""", [], []), 
        "server_id_list": MoPropertyMeta("server_id_list", "serverIdList", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10000, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "cartridgeCIMCId": "cartridge_cimc_id", 
        "chassisCartridgeId": "chassis_cartridge_id", 
        "chassisCimcId": "chassis_cimc_id", 
        "chassisId": "chassis_id", 
        "chassisIomId": "chassis_iom_id", 
        "childAction": "child_action", 
        "cimcAdapterId": "cimc_adapter_id", 
        "commandOptions": "command_options", 
        "dn": "dn", 
        "fabExtId": "fab_ext_id", 
        "isExcludeData": "is_exclude_data", 
        "majorOptType": "major_opt_type", 
        "rackServerAdapterId": "rack_server_adapter_id", 
        "rackServerId": "rack_server_id", 
        "rn": "rn", 
        "scope": "scope", 
        "serverIdList": "server_id_list", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.cartridge_cimc_id = None
        self.chassis_cartridge_id = None
        self.chassis_cimc_id = None
        self.chassis_id = None
        self.chassis_iom_id = None
        self.child_action = None
        self.cimc_adapter_id = None
        self.command_options = None
        self.fab_ext_id = None
        self.is_exclude_data = None
        self.major_opt_type = None
        self.rack_server_adapter_id = None
        self.rack_server_id = None
        self.scope = None
        self.server_id_list = None
        self.status = None

        ManagedObject.__init__(self, "SysdebugTechSupportCmdOpt", parent_mo_or_dn, **kwargs)

