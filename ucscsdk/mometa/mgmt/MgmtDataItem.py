"""This module contains the general information for MgmtDataItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class MgmtDataItemConsts():
    OP_STATUS_ALL_SUCCESS = "all-success"
    OP_STATUS_DOMAIN_SUSPENDED = "domain-suspended"
    OP_STATUS_FAILED = "failed"
    OP_STATUS_NOT_STARTED = "not-started"
    OP_STATUS_PARTIAL_FAILED = "partial-failed"
    OP_STATUS_WORK_IN_PROGRESS = "work-in-progress"


class MgmtDataItem(ManagedObject):
    """This is MgmtDataItem class."""

    consts = MgmtDataItemConsts()
    naming_props = set(['sysid'])

    mo_meta = MoMeta("MgmtDataItem", "mgmtDataItem", "exp-provider-[sysid]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin"], ['mgmtDataExporter'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "local_file": MoPropertyMeta("local_file", "localFile", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 1, 128, None, [], []), 
        "op_status": MoPropertyMeta("op_status", "opStatus", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all-success", "domain-suspended", "failed", "not-started", "partial-failed", "work-in-progress"], []), 
        "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 1, 128, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "status_report": MoPropertyMeta("status_report", "statusReport", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 512, None, [], []), 
        "sysid": MoPropertyMeta("sysid", "sysid", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "localFile": "local_file", 
        "opStatus": "op_status", 
        "remoteFile": "remote_file", 
        "rn": "rn", 
        "status": "status", 
        "statusReport": "status_report", 
        "sysid": "sysid", 
    }

    def __init__(self, parent_mo_or_dn, sysid, **kwargs):
        self._dirty_mask = 0
        self.sysid = sysid
        self.child_action = None
        self.local_file = None
        self.op_status = None
        self.remote_file = None
        self.status = None
        self.status_report = None

        ManagedObject.__init__(self, "MgmtDataItem", parent_mo_or_dn, **kwargs)

