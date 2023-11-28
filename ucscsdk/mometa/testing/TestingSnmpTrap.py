"""This module contains the general information for TestingSnmpTrap ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class TestingSnmpTrapConsts():
    pass


class TestingSnmpTrap(ManagedObject):
    """This is TestingSnmpTrap class."""

    consts = TestingSnmpTrapConsts()
    naming_props = set(['hostname'])

    mo_meta = MoMeta("TestingSnmpTrap", "testingSnmpTrap", "snmp-trap-[hostname]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin", "read-only"], ['testingSnmpSupport'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "community": MoPropertyMeta("community", "community", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-65535"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "community": "community", 
        "dn": "dn", 
        "hostname": "hostname", 
        "port": "port", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, hostname, **kwargs):
        self._dirty_mask = 0
        self.hostname = hostname
        self.child_action = None
        self.community = None
        self.port = None
        self.status = None

        ManagedObject.__init__(self, "TestingSnmpTrap", parent_mo_or_dn, **kwargs)

