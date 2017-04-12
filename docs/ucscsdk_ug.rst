Table of Contents
=================

1.  `Overview <#overview>`__
2.  `Management Information Model <#management-information-model>`__

    1. `Managed Objects <#managed-objects>`__
    2. `References To Managed
       Objects <#references-to-managed-objects>`__
    3. `Properties Of Managed
       Objects <#properties-of-managed-objects>`__
    4. `Methods <#methods>`__

3.  `Installation <#installation>`__

    1. `Pre-install Checklist <#pre-install-checklist>`__
    2. `Installation Steps <#installation-steps>`__

4.  `Uninstallation <#uninstallation>`__

    1. `Uninstallation Steps <#uninstallation-steps>`__

5.  `Getting Started <#getting-started>`__

    1. `Connecting Disconnecting <#connecting-disconnecting>`__
    2. `Base APIs <#basic-apis>`__
    3. `Creating Objects <#creating-objects>`__
    4. `Querying Objects <#querying-objects>`__
    5. `Querying Objects With
       Filters <#querying-objects-with-filters>`__
    6. `Modifying Objects <#modifying-objects>`__
    7. `Deleting Objects <#deleting-objects>`__
    8. `Transaction <#transaction>`__

6.  `Retrieving Meta Information <#retrieving-meta-information>`__
7.  `Watch UCS Central Events <#watch-ucs-central-events>`__

    1. `Wait Until Condition <#wait-until-condition>`__

8.  `Backup And Import <#backup-and-import>`__

    1. `Backup UCS Central and UCS domain <#backup-ucs-central-and-ucs-domain>`__
    2. `Export Config UCS Central and UCS domain <#export-config-ucs-central-and-ucs-domain>`__
    3. `Import Config UCS Central and UCS domain <#import-config-ucs-central-and-ucs-domain>`__

9. `Technical Support <#technical-support>`__

10. `Domain Management <#domain-management>`__

11. `Firmware Management <#firmware-management>`__

12. `Advanced Features <#advanced-features>`__

    1. `Multiple Parallel
       Transactions <#multiple-parallel-transactions>`__
    2. `Threading Mode <#threading-mode>`__

Overview
--------

Cisco UCS Central Python SDK is a python module which helps automate all aspects
of Cisco UCS Central including policies for server, network, storage and
UCS domain management.

Bulk of the Cisco UCS Central Python SDK work on the UCS Central’s Management
Information Tree (MIT), performing create, modify or delete actions on
the Managed Objects (MO) in the tree. The next chapter provides an
overview of the Cisco UCS Central Information Model (MIM).

Management Information Model
----------------------------

All the physical and logical components that comprise Cisco UCS Central are
represented in a hierarchical Management Information Model, referred to
as the Management Information Tree (MIT). Each node in the tree
represents a Managed Object (MO), uniquely identified by its
Distinguished Name. (DN)

The figure below illustrates a sample (partial) MIT for three chassis.

::

    Tree (topRoot)                      Distinguished Name
    |— sys                              sys
        |— fw-catalogue                 sys/fw-catalogue
        |— auth-realm                   sys/auth-realm
            |— console-auth             sys/auth-realm/console-auth
    |— org-root                         org-root
        |— boot-policy-global-default   org-root/boot-policy-global-default
            |— lan                      org-root/boot-policy-global-default/lan
    |— domaingroup-root         domaingroup-root
        |— fw-infra-policy      domaingroup-root/fw-infra-policy
        |— dns-svc              domaingroup-root/dns-svc

Managed Objects
~~~~~~~~~~~~~~~

Managed Objects (MO) are abstractions of Cisco UCS Central resources, such as
policies for controlling sever, network and storage related operations for UCS domains,
fabric interconnects, chassis, blades, rack-mounted servers. Managed
Objects represent any physical or logical entity that is configured /
managed in the Cisco UCS Central MIT. For example, physical entities such as
Servers, Chassis, I/O cards, Processors and logical entities such as
Resource pools, User roles, Service profiles, and Policies are
represented as Managed Objects.

Every Managed Object is uniquely identified in the tree with its
Distinguished Name (Dn) and can be uniquely identified within the
context of its parent with its Relative Name (Rn). The Dn identifies the
place of the MO in the MIT. A Dn is a concatenation of all the relative
names starting from the root to the MO itself. Essentially, Dn =
[Rn]/[Rn]/[Rn]/…/[Rn].

In the example below, Dn provides a fully qualified name for test_vlan created
under domaingroup in the model.

::

    <dn = “domaingroup-root/fabric/lan/net-vlan-100” />

The above written Dn is composed of the following Rn:

::

    topSystem MO: rn="domaingroup-root"
    fabricEP MO: rn="fabric"
    fabricLanCloud MO: rn ="lan"
    fabricVlan MO: rn="net-[vlanName]"

A Relative Name (Rn) may have the value of one or more of the MO’s
properties embedded in it. This allows in differentiating multiple MOs
of the same type within the context of the parent. Any properties that
form part of the Rn as described earlier are referred to as Naming
properties.

For instance, multiple blade MOs reside under a chassis MO. The blade MO
contains the blade identifier as part of its Rn (blade-[Id]), thereby
uniquely identifying each blade MO in the context of a chassis.

In the example below, Dn provides a fully qualified name for chassis-1 created
under Cisco UCS domain 1009 (this is internal domainId).

::

    <dn = “compute/sys-1009/chassis-1” />

The above written Dn is composed of the following Rn:

::

    topSystem MO: rn="computeResourceAggrEp"
    computeSystem MO: rn="sys-[domainId]"
    equipmentChassis MO: rn ="chassis-[chassisId]"

References To Managed Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The contents of the Managed Objects are referred to during the operation
of UCS Central. Some of the MOs are referred to implicitly (PreLoginBanner
during login) or as part of deployment of another MO (The Service
Profile MO may refer to a template or a VNIC refers to a number of VLAN
MOs).

A singleton MO type is found utmost once in the entire MIT and is
typically referred to implicitly.

Non-Singleton MO type may be instantiated one or more times in the MIT.
In many cases, when an MO refers to another, the reference is made by
name. Depending on the type of the referenced MO, the resolution may be
hierarchical. For instance, a service profile template is defined under
an Org. Since an org may contain sub-orgs, a sub org may have a service
profile template defined with the same name. Now, when a service profile
instance refers to a service profile template (by name), the name is
looked up hierarchically from the org of the service profile instance up
until the root org. The first match is used. If no match is found, then
the name “default” is looked up in the similar way and the first match
is used.

Properties of Managed Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Properties of Managed Objects can be classified as Configuration or
Operational.

Configuration properties may be classified as:

-  Naming properties: Form part of the Rn. **Needs** to be specified
   only during MO creation and cannot be modified later.
-  Create-Only properties: **May** be specified only during MO creation
   and cannot be modified later. If the property is not specified, a
   default value is assumed.
-  Read / Write properties: **May** be specified during MO creation and
   can also be modified subsequently.

Operational properties indicate the current status of the MO / system
and are hence read-only.

Methods
~~~~~~~

Methods are Cisco UCS Central XML APIs, used to manage and monitor the system.
There are methods supported for:

-  Authentication

   -  AaaLogin
   -  AaaRefresh
   -  AaaLogout

-  Configuration

   -  ConfigConfMo(s)
   -  LsClone
   -  LsInstantiate\*
   -  FaultAckFaults

-  Query

   -  ConfigResolveDn(s)
   -  ConfigResolveClass(es)
   -  ConfigResolveChildren

-  Event Monitor

   -  EventSubscribe

The class query methods (ConfigResolveClass(es), ConfigResolveChildren)
allow a filter to be specified so that a specific set of MOs are matched
and returned by the method.

The supported filters are:

-  allbits – Match if all specified values are present in a multi-valued
   property
-  anybit – Match if any of the specified values are present in a
   multi-valued property
-  bw – Match if the property’s value lies between the two values
   specified
-  eq – Match if property’s value is the same as the specified value
-  ge – Match if property’s value is greater than or equal to the
   specified value
-  gt - Match if property’s value is greater than the specified value
-  le – Match if property’s value is lesser than or equal to the
   specified value
-  lt – Match if property’s value is lesser than the specified value
-  ne – Match if property’s value is not equal to the specified value
-  wcard – Match if property’s value matches the pattern specified

Installation
------------

Pre-install Checklist
~~~~~~~~~~~~~~~~~~~~~

Ensure the following are available

::

    python >= 2.7
    pip

Installation Steps
~~~~~~~~~~~~~~~~~~

-  Installing the last released version of the SDK from pypi

::

    pip install ucscsdk

-  Installing the latest developer version from github

::

    git clone https://github.com/CiscoUcs/ucscsdk/
    cd ucscsdk
    sudo make install

Uninstallation
--------------

Uninstallation Steps
~~~~~~~~~~~~~~~~~~~~

Irrespective of the method that was used to install the SDK, it can be
uninstalled using the below command,

::

    pip uninstall ucscsdk

Getting Started
---------------

Connecting Disconnecting
~~~~~~~~~~~~~~~~~~~~~~~~

::

    from ucscsdk.ucschandle import UcscHandle

    # Create a connection handle
    handle = UcscHandle("192.168.1.1", "admin", "password")

    # Login to the server
    handle.login()

    # Logout from the server
    handle.logout()

Refer `UcscHandle API
Reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.html#module-ucscsdk.ucschandle>`__
for detailed parameter sets to ``UcscHandle``

Base APIs
~~~~~~~~~

The SDK provides APIs to enable CRUD operations.

-  **C**\ reate an object - ``add_mo``
-  **R**\ etrieve an object -
   ``query_dn``,\ ``query_classid``,\ ``query_dns``,\ ``query_classids``
-  **U**\ pdate an object - ``set_mo``
-  **D**\ elete an object - ``delete_mo``

The above APIs can be bunched together in a transaction (All or None).
``commit_mo`` commits the changes made using the above APIs.

All these methods are invoked on a ``UcscHandle`` instance. We refer it
by ``handle`` in all the examples here-after. Refer to the `Connecting
Disconnecting <#connecting-disconnecting>`__ to create a new handle.

Creating Objects
~~~~~~~~~~~~~~~~

Creating managed objects is done via ``add_mo`` API.

Example:

The below example creates a new Service Profile(\ ``LsServer``) Object
under the parent ``org-root``

::

    from ucscsdk.mometa.ls.LsServer import LsServer

    sp = LsServer(parent_mo_or_dn="org-root", name="sp_demo")
    handle.add_mo(sp)

**Note**: the changes will only be sent to server when
``handle.commit()`` is called.

`Add Mo API
reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.html#ucscsdk.ucschandle.UcscHandle.add_mo>`__

Querying Objects
~~~~~~~~~~~~~~~~

-  Querying Objects via Distinguished Name (DN)

   ::

       object = handle.query_dn("org-root/ls-sp_demo")

-  Querying Multiple Objects via Multiple Distinguished Names (DN)

   The returned object is a dictionary in ``{dn:object}`` format

   ::

       object_dict = handle.query_dn("org-root/ls-sp_demo", "org-root")

-  Querying Objects via class Id

   The below returns all objects of type ``orgOrg``

   ::

       object_array = handle.query_classid("orgOrg")

-  Querying Objects via multiple class Ids

   The below returns all objects of type ``orgOrg`` and ``fabricVlan``.
   The output is a dictionary of format ``{classId: [objects]}``

   ::

       object_dict = handle.query_classid("orgOrg", "fabricVlan")

`Query DN API
reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.html#ucscsdk.ucschandle.Ucschandle.query_dn>`__

`Query DNs API
reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.html#ucscsdk.ucschandle.Ucschandle.query_dns>`__

`Query Class Id API
reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.html#ucscsdk.ucschandle.Ucschandle.query_classid>`__

`Query Class Ids API
reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.html#ucscsdk.ucschandle.Ucschandle.query_classids>`__

Querying Objects With Filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Filter is passed as string parameter to
``query_dn``,\ ``query_dns``,\ ``query_classid``,\ ``query_classids``
methods

-  Basic usage:

   A basic filter string is of ``(prop_name, prop_value)`` format,

   ::

       filter_str = '(name, "demo_1")'
       sp = handle.query_classid(class_id="LsServer", filter_str=filter_str)

-  Specific usage:

   To have more control on the filter behaviour use the extended filter
   format, ``(prop_name, prop_value, filter_type)``

   **filter\_type**:

   -  ``re``: Default, regex match.
   -  ``eq``: equal, exact match.
   -  ``ne``: not equal
   -  ``ge``: greater than and equal to
   -  ``gt``: greater than
   -  ``le``: less than and equal to
   -  ``lt``: less than

   An example of an exact match,

   ::

       filter_str = '(name, "demo_1", type="eq")'
       sp = handle.query_classid(class_id="LsServer", filter_str=filter_str)

-  Complex filters - combination of multiple conditions:

   The below checks for ``(name == "demo")`` or
   ``(name == *demo_1* and name == [0-9]_1)``

   ::

       filter_str = '''(name, "demo", type="eq") or ((name, "demo_1") and
                                                   (name, "[0-9]_1"))'''
       sp = handle.query_classid(class_id="LsServer", filter_str=filter_str)

   **note**: ``'''`` here is used as a multiline string

Modifying Objects
~~~~~~~~~~~~~~~~~

``set_mo`` is used for updating an existing object

::

    # Query for an existing Mo
    sp = handle.query_dn("org-root/ls-sp_demo")

    # Update description of the service profile
    sp.descr = "demo_descr"

    # Add it to the on-going transaction
    handle.set_mo(sp)

**Note**: The changes will not be sent to the server until a
``commit()`` is invoked.

`Set Mo API
reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.html#ucscsdk.ucschandle.Ucschandle.set_mo>`__

Deleting Objects
~~~~~~~~~~~~~~~~

``remove_mo`` is used for removing an object

::

    # Query for an existing Mo
    sp = handle.query_dn("org-root/ls-sp_demo")

    # Remove the object
    handle.remove_mo(sp)

**Note**: The changes will not be sent to the server until a
``commit()`` is invoked.

`Remove Mo API
reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.html#ucscsdk.ucschandle.Ucschandle.remove_mo>`__

Transaction
~~~~~~~~~~~

API operations are batched together by default until a ``commit()`` is
invoked.

In the below code, the objects are created only when ``commit`` is
invoked. If there is a failure in one of the steps, then no changes are
committed to the server.

::

    from ucscsdk.mometa.ls.LsServer import LsServer

    sp1 = LsServer(parent_mo_or_dn="org-root", name="sp_demo1")
    handle.add_mo(sp1)

    sp2 = LsServer(parent_mo_or_dn="org-root", name="sp_demo2")
    handle.add_mo(sp2)

    # commit the changes to server
    handle.commit()

Retrieving Meta Information
---------------------------

``get_meta_info`` is useful for getting information about a Managed
object.

::

    from ucscsdk.ucsccoreutils import get_meta_info

    class_meta = get_meta_info("FabricVlan")
    print class_meta

The below sample output starts with a tree view of where FabricVlan
fits, its parents and children, followed by its MO information which
includes all of MO properties and its configurable properties. It then
shows detailed information about each property of the MO.

-  MO information:

   -  ``xml_attribute`` - the name of the MO as expected by the
      server.
   -  ``rn`` - type of the field
   -  ``min_version`` - Ucs Central release in which the MO was
      first introduced
   -  ``parents`` - list of parent MOs
   -  ``children`` - list of child MOs
   -  ``properties`` - all properties of the MO
   -  ``configurable properties`` - all configurable properties of MO

-  MO Property information:

   -  ``xml_attribute`` - the name of the property as expected by the
      server.
   -  ``field_type`` - type of the field
   -  ``min_version`` - Ucs server release in which the property was
      first introduced
   -  ``access`` - defines if a property is interal/user-readable/user-writable
   -  property restrictions:

      -  ``min_length`` - minimum length for string property type
      -  ``max_length`` - maximum length for string property type
      -  ``pattern`` - allowed patterns, regexs
      -  ``value_set`` - set of allowed values for this property
      -  ``range_val`` - range for int/uint values

sample output: (truncated)

::

    |-FabricEthEstcCloud
    |-FabricLanCloud
      |-FabricVlan
         |-FabricConsumer
         |-FabricEthMonSrcEp
         |-FabricEthMonSrcEpOperation
         |  |-FaultInst
         |-FabricEthVlanPc
         |-FabricEthVlanPortEp
         |-FabricEtherRef
         |-FabricExtension
         |-FabricSwSubGroup
         |  |-FabricEthVlanPortEp
         |  |-FabricFcoeVsanPortEp
         |-FaultInst

         ClassId                         FabricVlan
        -------                         ----------
        xml_attribute                   :fabricVlan
        rn                              :net-[name]
        min_version                     :1.1(1a)
        access                          :InputOutput
        access_privilege                :['admin', 'ext-lan-config', 'ext-lan-policy']
        parents                         :['fabricEthEstcCloud', 'fabricLanCloud']
        children                        :['fabricConsumer', 'fabricEthMonSrcEp', 'fabricEthMonSrcEpOperation']
        properties                      :['assoc_primary_vlan_state', 'assoc_primary_vlan_switch_id']
        configurable properties         :['compression_type', 'default_net', 'id', 'mcast_policy_name', 'policy_owner', 'pub_nw_name', 'sharing', 'status']

        Property                        assoc_primary_vlan_state
        --------                        ------------------------
        xml_attribute                   :assocPrimaryVlanState
        field_type                      :string
        min_version                     :1.2(1a)
        access                          :READ_ONLY
        min_length                      :None
        max_length                      :None
        pattern                         :None
        value_set                       :['does-not-exists', 'is-empty', 'is-in-error-state', 'is-not-primary-type', 'ok']
        range_val                       :[]

        Property                        assoc_primary_vlan_switch_id
        --------                        ----------------------------
        xml_attribute                   :assocPrimaryVlanSwitchId
        field_type                      :string
        min_version                     :1.2(1a)
        access                          :READ_ONLY
        min_length                      :None
        max_length                      :None
        pattern                         :None
        value_set                       :['A', 'B', 'NONE', 'mgmt']
        range_val                       :[]

Watch UCS Central Events
------------------------

Wait Until Condition
~~~~~~~~~~~~~~~~~~~~

``wait_for_event`` is used to wait until a specific condition.

It works by monitoring the UCS Central Event Channel or by periodically polling
the server. Polling mode is used when ``poll_sec`` argument is specified.
Specifying a timeout is highly recommended.

Arguments:

-  mo: object that is monitored
-  prop: prop to check
-  value: success value
-  cb: done callback
-  timeout: (Optional) timeout in seconds
-  poll_sec: (Optional) polling interval in seconds when using poll mode

::

    def done_callback(mo_change_event):
        print mo_change_event.mo


    sp_mo = handle.query_dn("org-root/ls-sp_demo")

    # call done_callback when (sp_mo.descr == "demo")
    handle.wait_for_event(sp_mo, "descr", "demo", done_callback)


Backup And Import
-----------------

Backup UCS Central and UCS domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``backup_local`` is used to take full-state backup of UCS Central to your
local machine
``backup_remote`` is used to take full-state backup of UCS Central to remote
location
``backup_domain_remote`` is used to take full-state backup of UCS domain to
remote location

::

    from ucscsdk.utils.ucscbackup import backup_local,backup_remote, \
        backup_domain_remote

    file_dir = "/home/user/backup"
    file_name = "full-state_backup.tgz"

    backup_local(handle, file_dir=file_dir, file_name=file_name)
    backup_remote(handle, file_dir=file_dir, file_name=file_name,
                  protocol='scp',hostname='192.168.1.1',
                  username='admin',password='password'))
    backup_domain_remote(handle, file_dir=file_dir, file_name=file_name,
                    domain_ip='10.10.10.1', protocol='scp',
                    hostname='192.168.1.1',
                    username='admin',password='password')

**Note**: Backup of UCS domain to local machine is not supported.

`Backup UCS Central API
Reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.utils.html#ucscsdk.utils.ucscbackup.backup_local>`__

Export config UCS Central and UCS domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``export_config_local`` is used to take config-all backup of UCS Central to your
local machine
``export_config_remote`` is used to take config-all backup of UCS Central to remote
location
``export_config_domain_remote`` is used to take config-all backup of UCS domain to
remote location

::

    from ucscsdk.utils.ucscbackup import export_config_local,export_config_remote, \
        export_config

    file_dir = "/home/user/backup"
    file_name = "config-all_backup.tgz"

    export_config_local(handle, file_dir=file_dir, file_name=file_name)
    export_config_remote(handle, file_dir=file_dir, file_name=file_name,
                  protocol='scp',hostname='192.168.1.1',
                  username='admin',password='password'))
    export_config_domain_remote(handle, file_dir=file_dir, file_name=file_name,
                    domain_ip='10.10.10.1', protocol='scp',
                    hostname='192.168.1.1',
                    username='admin',password='password')

**Note**: Export config of UCS domain to local machine is not supported.

`Export config UCS Central API
Reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.utils.html#ucscsdk.utils.ucscbackup.export_config_local>`__

Import config UCS Central and UCS domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``import_config_ucscentral`` is used to import an backup existing on UCS Central
to UCS Central
``import_config_local`` is used to import an backup existing on local machine
to UCS Central
``import_config_remote`` is used to import an backup existing on remote location
to UCS Central
``import_config_domain`` is used to import an UCS domain backup existing on
UCS Central to one of the UCS domains (same or different)

::

    from ucscsdk.utils.ucscbackup import import_config_ucscentral, import_config_local, \
        import_config_remote, import_config_domain

    file_dir = "/home/user/backup"\n
    file_name = "config_all_backup.tgz"\n

    import_config_ucscentral(handle, file_name=file_name)
    import_config_local(handle, file_name=file_name,
                        file_dir=file_dir,
                        merge=True)\n
                         file_dir=file_dir
    import_config_remote(handle, file_name=file_name,
                         protocol='scp',hostname='192.168.1.1',
                         username='admin',password='password')
    import_config_domain(handle, to_domain_ip="10.10.10.100",
                         from_domain_ip="192.168.1.1",
                         config_file="all-cfg.1.tgz")

`Import config UCS Central API
Reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.utils.html#ucscsdk.utils.ucscbackup.import_config_ucscentral>`__

**Note**: Import config of UCS domain is only supported from backups available on UCS Central.

Technical Support
-----------------

``get_tech_support`` facilitates technical support for UCS Central.

``get_domain_tech_support`` facilitates technical support for UCS Domain.
Here, ``option`` parameter defines the type of technical support that is
desired. ``**kwargs`` are ``key1=val1, key2=val2`` type named arguments that
need to be specified depending on the component for which technical support is
being triggered.
For example, if the user wants to trigger technical support for
``option=chassis``, then he/she will also need to pass
``chassis_id=1, cimc_id=1`` or ``chassis_id=1, iom_id=1``.

The below examples show the corresponding arguments that apply to the
component for which tech support is being taken. Please note that these
parameters should only be specified towards the end and not before the existing
named parameters.

::

    from ucscsdk.utils.ucsctechsupport import get_tech_support, \
        get_domain_tech_support

    get_tech_support(handle, file_dir=file_dir, file_name=file_name)

    get_domain_tech_support(handle, domain_ip = '192.168.1.1'
                     option="ucsm-mgmt",
                     timeout=1800)

    get_domain_tech_support(handle, domain_ip = '192.168.1.1',
                         option="chassis",
                         file_dir=".",
                         file_name="techsupport.tar",
                         chassis_id=1,
                         cimc_id=1,
                         adapter_id=1)

    get_domain_tech_support(handle, domain_ip = '192.168.1.1',
                     option="rack-server",
                     timeout=1800,
                     rack_server_id=1,
                     rack_adapter_id="all"
                     )

`Technical Support UCS Central API
Reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.utils.html#ucscsdk.utils.ucsctechsupport.get_tech_support>`__

**Note**: Download technical support of UCS domain is not supported from UCS Central.

Domain Management
-----------------

``domain_register`` is used to register UCS domain to UCS Central.
``domain_unregister`` is used to register UCS domain to UCS Central.
``get_domain`` is used to get domain object of the particular UCS domain.
``domain_group_create`` is used to create domain group in UCS Central.
``domain_assign_to_domaingroup`` is used to assign UCS domain to existing domain group.

::

   from ucscsdk.utils.ucscdomain import domain_register, \
        domain_unregister, get_domain, domain_group_create, \
        domain_assign_to_domaingroup

   domain_register(handle, domain_name_or_ip="192.168.1.1",
                    username="admin",password="password")
   domain_unregister(handle, domain_name_or_ip="192.168.1.1")
   get_domain(handle, domain_ip="192.168.1.1", domain_name=" ")
   domain_group_create(handle, name="sample_dom_grp")
   domain_assign_to_domaingroup(handle, domain_ip="192.168.1.1",
                                domain_group="root/sample_dom_grp")

**Note**: Domain register and unregister are available only from UCS Central version 1.5 onwards.

`Domain Management UCS Central API
Reference <https://ciscoucs.github.io/ucscsdk_docs/ucscsdk.utils.html#ucscsdk.utils.ucscdomain.domain_register>`__

Firmware Management
-------------------

``get_firmware_bundles`` helps to get the list of firmware bundles imported or
available for import to UCS Central.
It optionally takes bundle_type or fw_platform as argument to list only the
interested bundles.
``get_cco_firmware_image`` helps to download the UCS Central image from CCO.
It takes mdf_id_list as argument through which download of UCS infra bundle and
B-series and C-series bundle is also possible.
``firmware_add_local`` helps to import firmware from local machine to UCS Central.
``firmware_add_remote`` helps to import firmware from remote machine to UCS Central.
``firmware_remove`` helps to remove firmware bundle from UCS Central.
``schedule_infra_fw_update`` helps to schedule infra firmware update
for the domain group.
``sync_firmware_update_from_cisco`` helps to synchronize domain firmware updates
from Cisco.

::

    from ucscsdk.utils.ucscfirmware import get_firmware_bundles, \
        get_cco_firmware_image, firmware_add_local, firmware_add_remote,\
        firmware_remove, schedule_infra_fw_update, \
        sync_firmware_update_from_cisco

    get_firmware_bundles(handle, bundle_type="b-series-bundle")
    get_firmware_bundles(handle, bundle_type="infrastructure-bundle",
                         fw_platform="mini")

    get_cco_firmware_image(image_name='ucs-central-bundle.1.5.1a.bin',
                          username='guest', password='password',
                          download_dir='/Users/guest/Downloads/')
    firmware_add_local(handle,"/Users/guest/Downloads/",
                       "ucs-k9-bundle-b-series.3.1.1h.B.bin")
    firmware_add_remote(handle,
                        file_name="ucs-k9-bundle-b-series.3.1.1h.B.bin",
                        remote_path="/ws/remote_path/", hostname="10.10.1.1",
                        protocol="scp",username="guest",password="password")
    firmware_remove(handle,
                    image_name="ucs-k9-bundle-b-series.3.1.1h.B.bin")
    schedule_infra_fw_update(handle, domain_group="root", schedule="now")
    schedule_infra_fw_update(handle, domain_group="root",
                             schedule="2016-08-31T22:33:07",
                             fi_mini_6300_ver="3.1(1j)A",
                             catalog_ver="3.1(1)T")
    sync_firmware_update_from_cisco(handle, cisco_username = "guest",
                                    cisco_password="password",
                                    sync_enable = True,
                                    sync_frequencey= "weekly",
                                    proxy_enable = False)

Advanced Features
-----------------

Multiple Parallel Transactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional ``tag`` parameter in ``add_mo``, ``set_mo``, ``remove_mo``,
``commit`` provides a scope to transaction.

This enables multiple parallel transactions,

::

    handle.add_mo(mo1, tag="trans_1")
    handle.add_mo(mo2, tag="trans_2")
    handle.add_mo(mo3, tag="trans_1")
    handle.remove_mo(mo4, tag="trans_2")

    # Commit transaction #2
    handle.commit(tag="trans_2")

    handle.add_mo(mo5, tag="trans_1")

    # Commit transaction #1
    handle.commit(tag="trans_1")

Threading Mode
~~~~~~~~~~~~~~

This mode is useful, when the application that uses the SDK is threaded
and it intends to use the SDK using its multiple threads.

-  Enable threaded mode

   ::

       handle.set_mode_threading()

-  Disable threaded mode

   ::

       handle.unset_mode_threading()

When threading mode is enabled the transaction context isolation is
automatically provided on a thread level (even when the ``tag``
parameter is not explicitly specified). Thread names are automatically
used as ``tag`` parameter internally.
