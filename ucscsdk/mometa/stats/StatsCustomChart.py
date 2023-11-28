"""This module contains the general information for StatsCustomChart ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class StatsCustomChartConsts():
    CHART_DOMAIN_COOLING = "cooling"
    CHART_DOMAIN_NETWORK = "network"
    CHART_DOMAIN_POWER = "power"
    CHART_DOMAIN_TEMP = "temp"
    CHART_TYPE_DYNAMIC = "dynamic"
    CHART_TYPE_STATIC = "static"
    COOLING_ENDPOINT_CHASSIS_FANS = "chassisFans"
    COOLING_ENDPOINT_FI_FANS = "fiFans"
    COOLING_ENDPOINT_RACK_UNIT_FANS = "rackUnitFans"
    DEFAULT_VIEW_CHART = "chart"
    DEFAULT_VIEW_TABLE = "table"
    NETWORK_ENDPOINT_ETH_PORTS = "ethPorts"
    NETWORK_ENDPOINT_FC_PORTS = "fcPorts"
    NETWORK_ENDPOINT_HBAS = "hbas"
    NETWORK_ENDPOINT_NICS = "nics"
    OVERLAY_FALSE = "false"
    OVERLAY_NO = "no"
    OVERLAY_TRUE = "true"
    OVERLAY_YES = "yes"
    POWER_ENDPOINT_BLADES = "blades"
    POWER_ENDPOINT_CHASSIS = "chassis"
    POWER_ENDPOINT_RACKS = "racks"
    THERMAL_ENDPOINT_SERVERS = "servers"


class StatsCustomChart(ManagedObject):
    """This is StatsCustomChart class."""

    consts = StatsCustomChartConsts()
    naming_props = set(['name', 'chartDomain'])

    mo_meta = MoMeta("StatsCustomChart", "statsCustomChart", "custom-chart-[name]domain-[chart_domain]", VersionMeta.Version111b, "InputOutput", 0x1fffff, [], ["admin", "stats-management"], ['statsChartContainer', 'statsCustomEp'], [], ["Get"])

    prop_meta = {
        "chart_domain": MoPropertyMeta("chart_domain", "chartDomain", "string", VersionMeta.Version111b, MoPropertyMeta.NAMING, 0x2, None, None, None, ["cooling", "network", "power", "temp"], []), 
        "chart_interval": MoPropertyMeta("chart_interval", "chartInterval", "uint", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "chart_type": MoPropertyMeta("chart_type", "chartType", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["dynamic", "static"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cooling_endpoint": MoPropertyMeta("cooling_endpoint", "coolingEndpoint", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["chassisFans", "fiFans", "rackUnitFans"], []), 
        "default_view": MoPropertyMeta("default_view", "defaultView", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["chart", "table"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x80, 0, 256, None, [], []), 
        "end_time": MoPropertyMeta("end_time", "endTime", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "ether_type": MoPropertyMeta("ether_type", "etherType", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((unspecified|total|unicast|multicast|broadcast|jumbo),){0,5}(unspecified|total|unicast|multicast|broadcast|jumbo){0,1}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111b, MoPropertyMeta.NAMING, 0x400, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "network_endpoint": MoPropertyMeta("network_endpoint", "networkEndpoint", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["ethPorts", "fcPorts", "hbas", "nics"], []), 
        "overlay": MoPropertyMeta("overlay", "overlay", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["false", "no", "true", "yes"], []), 
        "parent_dns": MoPropertyMeta("parent_dns", "parentDns", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x2000, 0, 510, None, [], []), 
        "power_endpoint": MoPropertyMeta("power_endpoint", "powerEndpoint", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["blades", "chassis", "racks"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111b, MoPropertyMeta.READ_ONLY, 0x8000, 0, 256, None, [], []), 
        "start_time": MoPropertyMeta("start_time", "startTime", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x10000, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x20000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "thermal_endpoint": MoPropertyMeta("thermal_endpoint", "thermalEndpoint", "string", VersionMeta.Version112a, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, ["servers"], []), 
        "timezone": MoPropertyMeta("timezone", "timezone", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x80000, 0, 510, None, [], []), 
        "xtype": MoPropertyMeta("xtype", "xtype", "string", VersionMeta.Version111b, MoPropertyMeta.READ_WRITE, 0x100000, None, None, r"""((unspecified|tx|rx|avp|agp|pt|pfs),){0,6}(unspecified|tx|rx|avp|agp|pt|pfs){0,1}""", [], []), 
    }

    prop_map = {
        "chartDomain": "chart_domain", 
        "chartInterval": "chart_interval", 
        "chartType": "chart_type", 
        "childAction": "child_action", 
        "coolingEndpoint": "cooling_endpoint", 
        "defaultView": "default_view", 
        "descr": "descr", 
        "dn": "dn", 
        "endTime": "end_time", 
        "etherType": "ether_type", 
        "name": "name", 
        "networkEndpoint": "network_endpoint", 
        "overlay": "overlay", 
        "parentDns": "parent_dns", 
        "powerEndpoint": "power_endpoint", 
        "rn": "rn", 
        "startTime": "start_time", 
        "status": "status", 
        "thermalEndpoint": "thermal_endpoint", 
        "timezone": "timezone", 
        "xtype": "xtype", 
    }

    def __init__(self, parent_mo_or_dn, name, chart_domain, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.chart_domain = chart_domain
        self.chart_interval = None
        self.chart_type = None
        self.child_action = None
        self.cooling_endpoint = None
        self.default_view = None
        self.descr = None
        self.end_time = None
        self.ether_type = None
        self.network_endpoint = None
        self.overlay = None
        self.parent_dns = None
        self.power_endpoint = None
        self.start_time = None
        self.status = None
        self.thermal_endpoint = None
        self.timezone = None
        self.xtype = None

        ManagedObject.__init__(self, "StatsCustomChart", parent_mo_or_dn, **kwargs)

