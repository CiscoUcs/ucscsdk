"""This module contains the general information for BiosVfProcessorC3Report ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfProcessorC3ReportConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_PROCESSOR_C3_REPORT_ACPI_C2 = "acpi-c2"
    VP_PROCESSOR_C3_REPORT_ACPI_C3 = "acpi-c3"
    VP_PROCESSOR_C3_REPORT_DISABLED = "disabled"
    VP_PROCESSOR_C3_REPORT_ENABLED = "enabled"
    VP_PROCESSOR_C3_REPORT_PLATFORM_DEFAULT = "platform-default"
    VP_PROCESSOR_C3_REPORT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfProcessorC3Report(ManagedObject):
    """This is BiosVfProcessorC3Report class."""

    consts = BiosVfProcessorC3ReportConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfProcessorC3Report", "biosVfProcessorC3Report", "Processor-C3-Report", VersionMeta.Version111a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_processor_c3_report": MoPropertyMeta("vp_processor_c3_report", "vpProcessorC3Report", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["acpi-c2", "acpi-c3", "disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpProcessorC3Report": "vp_processor_c3_report", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_processor_c3_report = None

        ManagedObject.__init__(self, "BiosVfProcessorC3Report", parent_mo_or_dn, **kwargs)

