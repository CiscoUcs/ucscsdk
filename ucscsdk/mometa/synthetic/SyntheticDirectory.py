"""This module contains the general information for SyntheticDirectory ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class SyntheticDirectoryConsts():
    pass


class SyntheticDirectory(ManagedObject):
    """This is SyntheticDirectory class."""

    consts = SyntheticDirectoryConsts()
    naming_props = set(['ino'])

    mo_meta = MoMeta("SyntheticDirectory", "syntheticDirectory", "dir-[ino]", VersionMeta.Version101a, "InputOutput", 0x7ffff, [], ["admin"], ['syntheticDirectory', 'topSystem'], ['syntheticDirectory', 'syntheticFile'], ["Get"])

    prop_meta = {
        "atime": MoPropertyMeta("atime", "atime", "ulong", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], []), 
        "blksize": MoPropertyMeta("blksize", "blksize", "ulong", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "blocks": MoPropertyMeta("blocks", "blocks", "ulong", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "ctime": MoPropertyMeta("ctime", "ctime", "ulong", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "dev": MoPropertyMeta("dev", "dev", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "gid": MoPropertyMeta("gid", "gid", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []), 
        "ino": MoPropertyMeta("ino", "ino", "ulong", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x100, None, None, None, [], []), 
        "mode": MoPropertyMeta("mode", "mode", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []), 
        "mtime": MoPropertyMeta("mtime", "mtime", "ulong", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, [], []), 
        "nlink": MoPropertyMeta("nlink", "nlink", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], []), 
        "path": MoPropertyMeta("path", "path", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x2000, 0, 510, None, [], []), 
        "rdev": MoPropertyMeta("rdev", "rdev", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8000, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "ulong", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "uid": MoPropertyMeta("uid", "uid", "uint", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, [], []), 
    }

    prop_map = {
        "atime": "atime", 
        "blksize": "blksize", 
        "blocks": "blocks", 
        "childAction": "child_action", 
        "ctime": "ctime", 
        "dev": "dev", 
        "dn": "dn", 
        "gid": "gid", 
        "ino": "ino", 
        "mode": "mode", 
        "mtime": "mtime", 
        "name": "name", 
        "nlink": "nlink", 
        "path": "path", 
        "rdev": "rdev", 
        "rn": "rn", 
        "size": "size", 
        "status": "status", 
        "uid": "uid", 
    }

    def __init__(self, parent_mo_or_dn, ino, **kwargs):
        self._dirty_mask = 0
        self.ino = ino
        self.atime = None
        self.blksize = None
        self.blocks = None
        self.child_action = None
        self.ctime = None
        self.dev = None
        self.gid = None
        self.mode = None
        self.mtime = None
        self.name = None
        self.nlink = None
        self.path = None
        self.rdev = None
        self.size = None
        self.status = None
        self.uid = None

        ManagedObject.__init__(self, "SyntheticDirectory", parent_mo_or_dn, **kwargs)

