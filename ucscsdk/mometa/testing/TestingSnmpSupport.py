"""This module contains the general information for TestingSnmpSupport ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class TestingSnmpSupportConsts():
    pass


class TestingSnmpSupport(ManagedObject):
    """This is TestingSnmpSupport class."""

    consts = TestingSnmpSupportConsts()
    naming_props = set(['version'])

    mo_meta = MoMeta("TestingSnmpSupport", "testingSnmpSupport", "snmp-support-[version]", VersionMeta.Version101a, "InputOutput", 0x7f, [], ["admin", "read-only"], ['testingSnmpPolicy'], ['testingSnmpCommunity', 'testingSnmpTrap'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-65535"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "sys_contact": MoPropertyMeta("sys_contact", "sysContact", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []), 
        "sys_location": MoPropertyMeta("sys_location", "sysLocation", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "port": "port", 
        "rn": "rn", 
        "status": "status", 
        "sysContact": "sys_contact", 
        "sysLocation": "sys_location", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, version, **kwargs):
        self._dirty_mask = 0
        self.version = version
        self.child_action = None
        self.port = None
        self.status = None
        self.sys_contact = None
        self.sys_location = None

        ManagedObject.__init__(self, "TestingSnmpSupport", parent_mo_or_dn, **kwargs)

