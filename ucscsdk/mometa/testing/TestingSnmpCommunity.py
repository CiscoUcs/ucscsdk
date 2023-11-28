"""This module contains the general information for TestingSnmpCommunity ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class TestingSnmpCommunityConsts():
    pass


class TestingSnmpCommunity(ManagedObject):
    """This is TestingSnmpCommunity class."""

    consts = TestingSnmpCommunityConsts()
    naming_props = set(['community'])

    mo_meta = MoMeta("TestingSnmpCommunity", "testingSnmpCommunity", "snmp-community-[community]", VersionMeta.Version101a, "InputOutput", 0x3f, [], ["admin", "read-only"], ['testingSnmpSupport'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "community": MoPropertyMeta("community", "community", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x2, 1, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "role": MoPropertyMeta("role", "role", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "community": "community", 
        "dn": "dn", 
        "rn": "rn", 
        "role": "role", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, community, **kwargs):
        self._dirty_mask = 0
        self.community = community
        self.child_action = None
        self.role = None
        self.status = None

        ManagedObject.__init__(self, "TestingSnmpCommunity", parent_mo_or_dn, **kwargs)

