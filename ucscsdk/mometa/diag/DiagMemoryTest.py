"""This module contains the general information for DiagMemoryTest ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class DiagMemoryTestConsts():
    CPU_FILTER_ALL_CPUS = "all-cpus"
    CPU_FILTER_P0_P1_CPUS = "p0-p1-cpus"
    MEM_CHUNK_SIZE_5MB_CHUNK = "5mb-chunk"
    MEM_CHUNK_SIZE_BIG_CHUNK = "big-chunk"
    MEM_SIZE_ALL = "all"
    PATTERN_BUTTERFLY = "butterfly"
    PATTERN_KILLER = "killer"
    PATTERN_PRBS = "prbs"
    PATTERN_PRBS_ADDR = "prbs-addr"
    PATTERN_PRBS_KILLER = "prbs-killer"
    TYPE_DISK = "disk"
    TYPE_MEMTEST = "memtest"
    TYPE_PCI = "pci"
    TYPE_PMEM2 = "pmem2"
    TYPE_PROCESSOR = "processor"
    TYPE_STRESS = "stress"


class DiagMemoryTest(ManagedObject):
    """This is DiagMemoryTest class."""

    consts = DiagMemoryTestConsts()
    naming_props = set(['order'])

    mo_meta = MoMeta("DiagMemoryTest", "diagMemoryTest", "test-[order]", VersionMeta.Version201b, "InputOutput", 0xfff, [], ["admin", "pn-policy"], ['diagRunPolicy'], [], ["get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cpu_filter": MoPropertyMeta("cpu_filter", "cpuFilter", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["all-cpus", "p0-p1-cpus"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "loop_count": MoPropertyMeta("loop_count", "loopCount", "uint", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-1000"]), 
        "mem_chunk_size": MoPropertyMeta("mem_chunk_size", "memChunkSize", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["5mb-chunk", "big-chunk"], []), 
        "mem_size": MoPropertyMeta("mem_size", "memSize", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["all"], ["0-4096"]), 
        "order": MoPropertyMeta("order", "order", "byte", VersionMeta.Version201b, MoPropertyMeta.NAMING, 0x80, None, None, None, [], ["1-64"]), 
        "pattern": MoPropertyMeta("pattern", "pattern", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["butterfly", "killer", "prbs", "prbs-addr", "prbs-killer"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x200, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["disk", "memtest", "pci", "pmem2", "processor", "stress"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "cpuFilter": "cpu_filter", 
        "dn": "dn", 
        "id": "id", 
        "loopCount": "loop_count", 
        "memChunkSize": "mem_chunk_size", 
        "memSize": "mem_size", 
        "order": "order", 
        "pattern": "pattern", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, order, **kwargs):
        self._dirty_mask = 0
        self.order = order
        self.child_action = None
        self.cpu_filter = None
        self.id = None
        self.loop_count = None
        self.mem_chunk_size = None
        self.mem_size = None
        self.pattern = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "DiagMemoryTest", parent_mo_or_dn, **kwargs)

