"""This module contains the general information for BiosVfQPILinkFrequencySelect ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class BiosVfQPILinkFrequencySelectConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_QPILINK_FREQUENCY_SELECT_6400 = "6400"
    VP_QPILINK_FREQUENCY_SELECT_7200 = "7200"
    VP_QPILINK_FREQUENCY_SELECT_8000 = "8000"
    VP_QPILINK_FREQUENCY_SELECT_9600 = "9600"
    VP_QPILINK_FREQUENCY_SELECT_AUTO = "auto"
    VP_QPILINK_FREQUENCY_SELECT_PLATFORM_DEFAULT = "platform-default"
    VP_QPILINK_FREQUENCY_SELECT_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfQPILinkFrequencySelect(ManagedObject):
    """This is BiosVfQPILinkFrequencySelect class."""

    consts = BiosVfQPILinkFrequencySelectConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfQPILinkFrequencySelect", "biosVfQPILinkFrequencySelect", "QPI-Link-Frequency-Select", VersionMeta.Version121a, "InputOutput", 0x1f, [], ["read-only"], ['biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version121a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_qpi_link_frequency_select": MoPropertyMeta("vp_qpi_link_frequency_select", "vpQPILinkFrequencySelect", "string", VersionMeta.Version121a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["6400", "7200", "8000", "9600", "auto", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpQPILinkFrequencySelect": "vp_qpi_link_frequency_select", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_qpi_link_frequency_select = None

        ManagedObject.__init__(self, "BiosVfQPILinkFrequencySelect", parent_mo_or_dn, **kwargs)

