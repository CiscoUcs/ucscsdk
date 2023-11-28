"""This module contains the general information for FlowctrlItem ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class FlowctrlItemConsts():
    PRIO_AUTO = "auto"
    PRIO_ON = "on"
    RCV_OFF = "off"
    RCV_ON = "on"
    SND_OFF = "off"
    SND_ON = "on"


class FlowctrlItem(ManagedObject):
    """This is FlowctrlItem class."""

    consts = FlowctrlItemConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("FlowctrlItem", "flowctrlItem", "policy-[name]", VersionMeta.Version111a, "InputOutput", 0xff, [], ["admin", "ls-network", "ls-network-policy", "ls-qos-policy"], ['flowctrlDefinition'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "prio": MoPropertyMeta("prio", "prio", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["auto", "on"], []), 
        "rcv": MoPropertyMeta("rcv", "rcv", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["off", "on"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "snd": MoPropertyMeta("snd", "snd", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["off", "on"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "name": "name", 
        "prio": "prio", 
        "rcv": "rcv", 
        "rn": "rn", 
        "snd": "snd", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.prio = None
        self.rcv = None
        self.snd = None
        self.status = None

        ManagedObject.__init__(self, "FlowctrlItem", parent_mo_or_dn, **kwargs)

