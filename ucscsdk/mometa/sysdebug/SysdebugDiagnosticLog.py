"""This module contains the general information for SysdebugDiagnosticLog ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SysdebugDiagnosticLogConsts():
    OPER_STATE_ALLOCATED = "allocated"
    OPER_STATE_CREATED = "created"
    OPER_STATE_UNKNOWN = "unknown"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    SWITCH_ID_MGMT = "mgmt"


class SysdebugDiagnosticLog(ManagedObject):
    """This is SysdebugDiagnosticLog class."""

    consts = SysdebugDiagnosticLogConsts()
    naming_props = set(['name', 'switchId'])

    mo_meta = MoMeta("SysdebugDiagnosticLog", "sysdebugDiagnosticLog", "diag-log-[name]-[switch_id]", VersionMeta.Version201b, "InputOutput", 0x7f, [], ["admin", "operations"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x8, 1, 128, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "created", "unknown"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x40, None, None, None, ["A", "B", "NONE", "mgmt"], []), 
        "tftp_uri": MoPropertyMeta("tftp_uri", "tftpUri", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "ts": MoPropertyMeta("ts", "ts", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "uri": MoPropertyMeta("uri", "uri", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "ip": "ip", 
        "name": "name", 
        "operState": "oper_state", 
        "rn": "rn", 
        "size": "size", 
        "status": "status", 
        "switchId": "switch_id", 
        "tftpUri": "tftp_uri", 
        "ts": "ts", 
        "uri": "uri", 
    }

    def __init__(self, parent_mo_or_dn, name, switch_id, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.switch_id = switch_id
        self.child_action = None
        self.descr = None
        self.ip = None
        self.oper_state = None
        self.size = None
        self.status = None
        self.tftp_uri = None
        self.ts = None
        self.uri = None

        ManagedObject.__init__(self, "SysdebugDiagnosticLog", parent_mo_or_dn, **kwargs)

