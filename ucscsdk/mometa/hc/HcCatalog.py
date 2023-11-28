"""This module contains the general information for HcCatalog ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class HcCatalogConsts():
    pass


class HcCatalog(ManagedObject):
    """This is HcCatalog class."""

    consts = HcCatalogConsts()
    naming_props = set(['id'])

    mo_meta = MoMeta("HcCatalog", "hcCatalog", "hc-catalog-[id]", VersionMeta.Version151a, "InputOutput", 0xfffff, [], ["admin"], ['hcHolder'], [], [None])

    prop_meta = {
        "adapter_model": MoPropertyMeta("adapter_model", "adapterModel", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "adapter_pid": MoPropertyMeta("adapter_pid", "adapterPid", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []), 
        "bundle": MoPropertyMeta("bundle", "bundle", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "driver_protocol": MoPropertyMeta("driver_protocol", "driverProtocol", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []), 
        "driver_vendor": MoPropertyMeta("driver_vendor", "driverVendor", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40, 0, 510, None, [], []), 
        "driver_version": MoPropertyMeta("driver_version", "driverVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []), 
        "firmware": MoPropertyMeta("firmware", "firmware", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x200, 1, 510, None, [], []), 
        "note": MoPropertyMeta("note", "note", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, None, [], []), 
        "os_vendor": MoPropertyMeta("os_vendor", "osVendor", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x800, 0, 510, None, [], []), 
        "os_version": MoPropertyMeta("os_version", "osVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, None, [], []), 
        "processor_name": MoPropertyMeta("processor_name", "processorName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x2000, 0, 510, None, [], []), 
        "processor_version": MoPropertyMeta("processor_version", "processorVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x4000, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8000, 0, 256, None, [], []), 
        "server_model": MoPropertyMeta("server_model", "serverModel", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10000, 0, 510, None, [], []), 
        "server_pid": MoPropertyMeta("server_pid", "serverPid", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x20000, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x40000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "ucs_version": MoPropertyMeta("ucs_version", "ucsVersion", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80000, 0, 510, None, [], []), 
    }

    prop_map = {
        "adapterModel": "adapter_model", 
        "adapterPid": "adapter_pid", 
        "bundle": "bundle", 
        "childAction": "child_action", 
        "dn": "dn", 
        "driverProtocol": "driver_protocol", 
        "driverVendor": "driver_vendor", 
        "driverVersion": "driver_version", 
        "firmware": "firmware", 
        "id": "id", 
        "note": "note", 
        "osVendor": "os_vendor", 
        "osVersion": "os_version", 
        "processorName": "processor_name", 
        "processorVersion": "processor_version", 
        "rn": "rn", 
        "serverModel": "server_model", 
        "serverPid": "server_pid", 
        "status": "status", 
        "ucsVersion": "ucs_version", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.adapter_model = None
        self.adapter_pid = None
        self.bundle = None
        self.child_action = None
        self.driver_protocol = None
        self.driver_vendor = None
        self.driver_version = None
        self.firmware = None
        self.note = None
        self.os_vendor = None
        self.os_version = None
        self.processor_name = None
        self.processor_version = None
        self.server_model = None
        self.server_pid = None
        self.status = None
        self.ucs_version = None

        ManagedObject.__init__(self, "HcCatalog", parent_mo_or_dn, **kwargs)

