# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This is an auto-generated module.
It contains supporting classes for Filter and External Method.

"""

from . import ucscgenutils
from . import ucsccoreutils as coreutils
from .ucscmethod import ExternalMethod
from .ucsccoremeta import WriteXmlOption
from .ucscconstants import YesOrNo


def aaa_change_self_password(cookie, in_confirm_new_password, in_new_password, in_old_password, in_user_name):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaChangeSelfPassword")

    method.cookie = cookie
    method.in_confirm_new_password = in_confirm_new_password
    method.in_new_password = in_new_password
    method.in_old_password = in_old_password
    method.in_user_name = in_user_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_check_compute_auth_token(cookie, in_token, in_user):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaCheckComputeAuthToken")

    method.cookie = cookie
    method.in_token = in_token
    method.in_user = in_user

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_check_compute_ext_access(cookie, in_dn, in_user):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaCheckComputeExtAccess")

    method.cookie = cookie
    method.in_dn = in_dn
    method.in_user = in_user

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_auth_token_client(in_cookie):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaGetAuthTokenClient")

    method.in_cookie = in_cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_auth_token_internal(cookie, in_id, in_ipv4, in_locales, in_parent_sess, in_priv, in_remote, in_role_list, in_user):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaGetAuthTokenInternal")

    method.cookie = cookie
    method.in_id = str(in_id)
    method.in_ipv4 = in_ipv4
    method.in_locales = in_locales
    method.in_parent_sess = in_parent_sess
    method.in_priv = in_priv
    method.in_remote = in_remote
    method.in_role_list = in_role_list
    method.in_user = in_user

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_compute_auth_token(cookie):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaGetComputeAuthToken")

    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_kvm_launch_url_internal(cookie, in_cimc_ipv4, in_ipv4, in_ipv6, in_locales, in_parent_sess, in_priv, in_remote, in_role_list, in_user):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaGetKVMLaunchUrlInternal")

    method.cookie = cookie
    method.in_cimc_ipv4 = in_cimc_ipv4
    method.in_ipv4 = in_ipv4
    method.in_ipv6 = in_ipv6
    method.in_locales = in_locales
    method.in_parent_sess = in_parent_sess
    method.in_priv = in_priv
    method.in_remote = in_remote
    method.in_role_list = in_role_list
    method.in_user = in_user

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_n_compute_auth_token_by_dn(cookie, in_cookie, in_dn, in_number_of):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaGetNComputeAuthTokenByDn")

    method.cookie = cookie
    method.in_dn = in_dn
    method.in_number_of = str(in_number_of)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_n_compute_auth_token_internal_by_dn(cookie, in_dn, in_id, in_ipv4, in_locales, in_number_of, in_parent_sess, in_priv, in_remote, in_role_list, in_user):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaGetNComputeAuthTokenInternalByDn")

    method.cookie = cookie
    method.in_dn = in_dn
    method.in_id = str(in_id)
    method.in_ipv4 = in_ipv4
    method.in_locales = in_locales
    method.in_number_of = str(in_number_of)
    method.in_parent_sess = in_parent_sess
    method.in_priv = in_priv
    method.in_remote = in_remote
    method.in_role_list = in_role_list
    method.in_user = in_user

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_remote_user_roles(cookie, in_remote_user_name):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaGetRemoteUserRoles")

    method.cookie = cookie
    method.in_remote_user_name = in_remote_user_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_get_user_locales(cookie, in_is_user_remote, in_user_name):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaGetUserLocales")

    method.cookie = cookie
    method.in_is_user_remote = in_is_user_remote
    method.in_user_name = in_user_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_keep_alive(cookie):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaKeepAlive")

    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_login(in_name, in_password):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaLogin")

    method.in_name = in_name
    method.in_password = in_password

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_login_by_token(cookie, in_name, in_token):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaLoginByToken")

    method.cookie = cookie
    method.in_name = in_name
    method.in_token = in_token

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_logout(in_cookie):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaLogout")

    method.in_cookie = in_cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_refresh(in_cookie, in_name, in_password):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaRefresh")

    method.in_cookie = in_cookie
    method.in_name = in_name
    method.in_password = in_password

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_token_login(cookie, in_name, in_token):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaTokenLogin")

    method.cookie = cookie
    method.in_name = in_name
    method.in_token = in_token

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def aaa_token_refresh(in_cookie, in_name):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("AaaTokenRefresh")

    method.in_cookie = in_cookie
    method.in_name = in_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def cliview_conf_mos(cookie, in_additional_methods, in_commit, in_configs, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("CliviewConfMos")

    method.cookie = cookie
    method.in_additional_methods = in_additional_methods
    method.in_commit = in_commit
    method.in_configs = in_configs
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def compute_get_qualified_servers(cookie, in_qual_dn, in_return_pool_configs, in_return_server_configs):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ComputeGetQualifiedServers")

    method.cookie = cookie
    method.in_qual_dn = in_qual_dn
    method.in_return_pool_configs = in_return_pool_configs
    method.in_return_server_configs = in_return_server_configs

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def compute_get_server_catalog(cookie, in_domain_group_list, in_equipment_filter, in_exclude_total_result_size, in_filter, in_include_filter_list_only, in_include_props, in_limit, in_offset, in_recursive, in_return_count_only):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ComputeGetServerCatalog")

    method.cookie = cookie
    method.in_domain_group_list = in_domain_group_list
    method.in_equipment_filter = in_equipment_filter
    method.in_exclude_total_result_size = in_exclude_total_result_size
    method.in_filter = in_filter
    method.in_include_filter_list_only = in_include_filter_list_only
    method.in_include_props = in_include_props
    method.in_limit = str(in_limit)
    method.in_offset = str(in_offset)
    method.in_recursive = in_recursive
    method.in_return_count_only = in_return_count_only

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def compute_re_qualify_membership(cookie, dn):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ComputeReQualifyMembership")

    method.cookie = cookie
    method.dn = dn

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_check_hardware_compatibility(cookie, class_id, in_target_blade_firmware_version, in_target_dn, in_target_modular_firmware_version, in_target_rack_firmware_version, in_target_ucs_firmware_version):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigCheckHardwareCompatibility")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucscgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_target_blade_firmware_version = in_target_blade_firmware_version
    method.in_target_dn = in_target_dn
    method.in_target_modular_firmware_version = in_target_modular_firmware_version
    method.in_target_rack_firmware_version = in_target_rack_firmware_version
    method.in_target_ucs_firmware_version = in_target_ucs_firmware_version

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_clone(cookie, dn, in_chassis_profile_name, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigClone")

    method.cookie = cookie
    method.dn = dn
    method.in_chassis_profile_name = in_chassis_profile_name
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_filtered(cookie, class_id, in_config, in_filter, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigConfFiltered")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucscgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_config = in_config
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_mo(cookie, dn, in_config, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigConfMo")

    method.cookie = cookie
    method.dn = dn
    method.in_config = in_config
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_mo_group(cookie, in_config, in_dns, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigConfMoGroup")

    method.cookie = cookie
    method.in_config = in_config
    method.in_dns = in_dns
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_mos(cookie, in_configs, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigConfMos")

    method.cookie = cookie
    method.in_configs = in_configs
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_conf_rename(cookie, dn, in_new_name, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigConfRename")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_new_name = in_new_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_delete_mo(cookie, dn, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigDeleteMo")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_find_dependencies(cookie, dn, in_return_configs):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigFindDependencies")

    method.cookie = cookie
    method.dn = dn
    method.in_return_configs = in_return_configs

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_find_dns_by_class_id(cookie, class_id, in_filter):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigFindDnsByClassId")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucscgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_filter = in_filter

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_find_policy_usage(cookie, in_policy_dn, in_policy_usage, in_return_configs):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigFindPolicyUsage")

    method.cookie = cookie
    method.in_policy_dn = in_policy_dn
    method.in_policy_usage = in_policy_usage
    method.in_return_configs = in_return_configs

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_ackables(cookie):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigGetAckables")

    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_connected_endpoints(cookie, in_equipment_dn, in_equpiment_id_filter):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigGetConnectedEndpoints")

    method.cookie = cookie
    method.in_equipment_dn = in_equipment_dn
    method.in_equpiment_id_filter = in_equpiment_id_filter

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_estimate_impact(cookie, in_configs, in_deleted_dns, in_impact_analyzer_id, in_is_policy_full_config, in_source_connector_id):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigGetEstimateImpact")

    method.cookie = cookie
    method.in_configs = in_configs
    method.in_deleted_dns = in_deleted_dns
    method.in_impact_analyzer_id = in_impact_analyzer_id
    method.in_is_policy_full_config = in_is_policy_full_config
    method.in_source_connector_id = str(in_source_connector_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_id_universe_usage(cookie, in_domain_group_dn, in_id_type, in_show_id_details):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigGetIdUniverseUsage")

    method.cookie = cookie
    method.in_domain_group_dn = in_domain_group_dn
    method.in_id_type = in_id_type
    method.in_show_id_details = in_show_id_details

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_last_backed_up_domains(cookie, in_backup_type, in_domains):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigGetLastBackedUpDomains")

    method.cookie = cookie
    method.in_backup_type = in_backup_type
    method.in_domains = in_domains

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_net_refs(cookie, in_org_dn, in_server_dn, in_type):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigGetNetRefs")

    method.cookie = cookie
    method.in_org_dn = in_org_dn
    method.in_server_dn = in_server_dn
    method.in_type = in_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_policy_domain_group(cookie, in_class_id, in_domain_id, in_policy_name):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigGetPolicyDomainGroup")

    method.cookie = cookie
    method.in_class_id = str(in_class_id)
    method.in_domain_id = str(in_domain_id)
    method.in_policy_name = in_policy_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_qualified_domains(cookie, in_qual_dn, in_return_domain_configs, in_return_policy_configs):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigGetQualifiedDomains")

    method.cookie = cookie
    method.in_qual_dn = in_qual_dn
    method.in_return_domain_configs = in_return_domain_configs
    method.in_return_policy_configs = in_return_policy_configs

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_get_token_requestors(cookie):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigGetTokenRequestors")

    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_instantiate_n_named_template(cookie, dn, in_error_on_existing, in_name_set, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigInstantiateNNamedTemplate")

    method.cookie = cookie
    method.dn = dn
    method.in_error_on_existing = in_error_on_existing
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_name_set = in_name_set
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_instantiate_n_template(cookie, dn, in_chassis_profile_name_prefix_or_empty, in_number_of, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigInstantiateNTemplate")

    method.cookie = cookie
    method.dn = dn
    method.in_chassis_profile_name_prefix_or_empty = in_chassis_profile_name_prefix_or_empty
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_number_of = str(in_number_of)
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_instantiate_template(cookie, dn, in_chassis_profile_name, in_error_on_existing, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigInstantiateTemplate")

    method.cookie = cookie
    method.dn = dn
    method.in_chassis_profile_name = in_chassis_profile_name
    method.in_error_on_existing = in_error_on_existing
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_mo_change_event(cookie, in_config, in_eid):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigMoChangeEvent")

    method.cookie = cookie
    method.in_config = in_config
    method.in_eid = str(in_eid)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_publish_vlan(cookie, in_domain, in_vlan_name):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigPublishVlan")

    method.cookie = cookie
    method.in_domain = in_domain
    method.in_vlan_name = in_vlan_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_publish_vsan(cookie, in_domain, in_switch_id, in_vsan_name):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigPublishVsan")

    method.cookie = cookie
    method.in_domain = in_domain
    method.in_switch_id = in_switch_id
    method.in_vsan_name = in_vsan_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_refresh_identity(cookie, dn, in_id_type, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigRefreshIdentity")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_id_type = in_id_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_release_resolve_context(cookie, in_context):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigReleaseResolveContext")

    method.cookie = cookie
    method.in_context = str(in_context)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_remote_search(cookie, in_context, in_domain_id, in_domain_name, in_fetch_size, in_name, in_object_type, in_policy_owner, in_recursive_context, in_recursive_domain_group, in_search_domain_group, in_search_type):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigRemoteSearch")

    method.cookie = cookie
    method.in_context = in_context
    method.in_domain_id = str(in_domain_id)
    method.in_domain_name = in_domain_name
    method.in_fetch_size = str(in_fetch_size)
    method.in_name = in_name
    method.in_object_type = in_object_type
    method.in_policy_owner = in_policy_owner
    method.in_recursive_context = in_recursive_context
    method.in_recursive_domain_group = in_recursive_domain_group
    method.in_search_domain_group = in_search_domain_group
    method.in_search_type = in_search_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_renew_resolve_context(cookie, in_context):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigRenewResolveContext")

    method.cookie = cookie
    method.in_context = str(in_context)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_ancestor(cookie, dn, in_class, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveAncestor")

    method.cookie = cookie
    method.dn = dn
    method.in_class = in_class
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_children(cookie, class_id, in_dn, in_filter, in_include_props=None, in_return_count_only=None, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveChildren")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucscgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_dn = in_dn
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    if in_include_props is not None:
        method.in_include_props = in_include_props
    if in_return_count_only is not None:
        method.in_return_count_only = in_return_count_only

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_children_sorted(cookie, class_id, in_dn, in_filter, in_size, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveChildrenSorted")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucscgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_dn = in_dn
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_size = str(in_size)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_class(cookie, class_id, in_filter, in_include_props=None, in_return_count_only=None, in_limit=0, in_offset=0, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveClass")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucscgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    if in_include_props is not None:
        method.in_include_props = in_include_props
    if in_limit > 0:
        method.in_limit = in_limit
    if in_offset > 0:
        method.in_offset = in_offset
    if in_return_count_only is not None:
        method.in_return_count_only = in_return_count_only

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_class_db(cookie, class_id, in_filter, in_include_prop, in_key, in_limit, in_offset, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveClassDB")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucscgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_include_prop = in_include_prop
    method.in_key = in_key
    method.in_limit = str(in_limit)
    method.in_offset = str(in_offset)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_class_filter_idx(cookie, class_id, in_class, in_filter, in_include_prop, in_limit, in_offset, in_parent_dn, in_query, in_sort_str, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveClassFilterIdx")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucscgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_class = in_class
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_include_prop = in_include_prop
    method.in_limit = str(in_limit)
    method.in_offset = str(in_offset)
    method.in_parent_dn = in_parent_dn
    method.in_query = in_query
    method.in_sort_str = in_sort_str

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_class_idx(cookie, class_id, in_class, in_filter, in_include_prop, in_limit, in_offset, in_parent_dn, in_query, in_sort_str, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveClassIdx")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucscgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_class = in_class
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_include_prop = in_include_prop
    method.in_limit = str(in_limit)
    method.in_offset = str(in_offset)
    method.in_parent_dn = in_parent_dn
    method.in_query = in_query
    method.in_sort_str = in_sort_str

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_class_sorted(cookie, class_id, in_filter, in_size, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveClassSorted")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucscgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_size = str(in_size)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_classes(cookie, in_ids, in_return_count_only, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveClasses")

    method.cookie = cookie
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_ids = in_ids
    method.in_return_count_only = in_return_count_only

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_classes_sorted(cookie, in_ids, in_size, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveClassesSorted")

    method.cookie = cookie
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_ids = in_ids
    method.in_size = str(in_size)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_context(cookie, in_context, in_size):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveContext")

    method.cookie = cookie
    method.in_context = str(in_context)
    method.in_size = str(in_size)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_dn(cookie, dn, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveDn")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_dns(cookie, in_dns, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveDns")

    method.cookie = cookie
    method.in_dns = in_dns
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_domain_elements(cookie, in_assoc_state, in_class_id, in_domain_group_context, in_domain_id, in_fetch_size, in_filter, in_ignore_assoc_state, in_include_filter_list_only, in_include_props, in_instance_type, in_limit, in_name, in_offset, in_org_context, in_owner, in_recursive_domain_group, in_recursive_org_group, in_return_count_only):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveDomainElements")

    method.cookie = cookie
    method.in_assoc_state = in_assoc_state
    method.in_class_id = in_class_id
    method.in_domain_group_context = in_domain_group_context
    method.in_domain_id = str(in_domain_id)
    method.in_fetch_size = str(in_fetch_size)
    method.in_filter = in_filter
    method.in_ignore_assoc_state = in_ignore_assoc_state
    method.in_include_filter_list_only = in_include_filter_list_only
    method.in_include_props = in_include_props
    method.in_instance_type = in_instance_type
    method.in_limit = str(in_limit)
    method.in_name = in_name
    method.in_offset = str(in_offset)
    method.in_org_context = in_org_context
    method.in_owner = in_owner
    method.in_recursive_domain_group = in_recursive_domain_group
    method.in_recursive_org_group = in_recursive_org_group
    method.in_return_count_only = in_return_count_only

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_parent(cookie, dn, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveParent")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_resolve_spot_light_idx(cookie, class_id, in_class, in_filter, in_include_facet, in_include_prop, in_limit, in_offset, in_query, in_sort_str):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigResolveSpotLightIdx")

    meta_class_id = coreutils.find_class_id_in_mo_meta_ignore_case(class_id)
    if meta_class_id is not None:
        class_id = ucscgenutils.word_l(meta_class_id)
    method.class_id = class_id
    method.cookie = cookie
    method.in_class = in_class
    method.in_filter = in_filter
    method.in_include_facet = in_include_facet
    method.in_include_prop = in_include_prop
    method.in_limit = str(in_limit)
    method.in_offset = str(in_offset)
    method.in_query = in_query
    method.in_sort_str = in_sort_str

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_scope(cookie, dn, in_class, in_filter, in_recursive, in_return_count_only=None, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigScope")

    method.cookie = cookie
    method.dn = dn
    method.in_class = in_class
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_recursive = in_recursive
    if in_return_count_only is not None:
        method.in_return_count_only = in_return_count_only

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_send_app_impact_response(cookie, in_app_impact_response_set):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigSendAppImpactResponse")

    method.cookie = cookie
    method.in_app_impact_response_set = in_app_impact_response_set

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_tags(cookie, in_configs):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigTags")

    method.cookie = cookie
    method.in_configs = in_configs

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_templatise(cookie, dn, in_target_org, in_template_name, in_template_type, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigTemplatise")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org
    method.in_template_name = in_template_name
    method.in_template_type = in_template_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def config_uc_estimate_impact(cookie, in_configs, in_impact_analyzer_id):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("ConfigUCEstimateImpact")

    method.cookie = cookie
    method.in_configs = in_configs
    method.in_impact_analyzer_id = str(in_impact_analyzer_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def equipment_clone(cookie, dn, in_chassis_profile_name, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("EquipmentClone")

    method.cookie = cookie
    method.dn = dn
    method.in_chassis_profile_name = in_chassis_profile_name
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def equipment_instantiate_n_named_template(cookie, dn, in_error_on_existing, in_name_set, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("EquipmentInstantiateNNamedTemplate")

    method.cookie = cookie
    method.dn = dn
    method.in_error_on_existing = in_error_on_existing
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_name_set = in_name_set
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def equipment_instantiate_n_template(cookie, dn, in_chassis_profile_name_prefix_or_empty, in_number_of, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("EquipmentInstantiateNTemplate")

    method.cookie = cookie
    method.dn = dn
    method.in_chassis_profile_name_prefix_or_empty = in_chassis_profile_name_prefix_or_empty
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_number_of = str(in_number_of)
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def equipment_instantiate_template(cookie, dn, in_chassis_profile_name, in_error_on_existing, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("EquipmentInstantiateTemplate")

    method.cookie = cookie
    method.dn = dn
    method.in_chassis_profile_name = in_chassis_profile_name
    method.in_error_on_existing = in_error_on_existing
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def equipment_templatise(cookie, dn, in_target_org, in_template_name, in_template_type, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("EquipmentTemplatise")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org
    method.in_template_name = in_template_name
    method.in_template_type = in_template_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_send_heartbeat(cookie):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("EventSendHeartbeat")

    method.cookie = cookie

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_subscribe(cookie, in_filter):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("EventSubscribe")

    method.cookie = cookie
    method.in_filter = in_filter

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def event_subscribe_apps(cookie, in_app_list, in_filter):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("EventSubscribeApps")

    method.cookie = cookie
    method.in_app_list = in_app_list
    method.in_filter = in_filter

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fabric_permits_for_existing_vlan_names(cookie, in_org_dn):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("FabricPermitsForExistingVlanNames")

    method.cookie = cookie
    method.in_org_dn = in_org_dn

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fabric_resolve_vlan_permits(cookie, in_action, in_domain_group_list, in_from, in_org_list, in_pub_nw_name, in_to, in_vlan_list, in_vlan_name, in_vlan_prefix, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("FabricResolveVlanPermits")

    method.cookie = cookie
    method.in_action = in_action
    method.in_domain_group_list = in_domain_group_list
    method.in_from = str(in_from)
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_org_list = in_org_list
    method.in_pub_nw_name = in_pub_nw_name
    method.in_to = str(in_to)
    method.in_vlan_list = in_vlan_list
    method.in_vlan_name = in_vlan_name
    method.in_vlan_prefix = in_vlan_prefix

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fabric_vnet_id_ep_overlap_check(cookie, in_class_id, in_delimiter, in_id_type, in_ids_to_check, in_should_return_overlapping_vnets):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("FabricVnetIdEpOverlapCheck")

    method.cookie = cookie
    method.in_class_id = in_class_id
    method.in_delimiter = in_delimiter
    method.in_id_type = in_id_type
    method.in_ids_to_check = in_ids_to_check
    method.in_should_return_overlapping_vnets = in_should_return_overlapping_vnets

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fault_ack_fault(cookie, in_id):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("FaultAckFault")

    method.cookie = cookie
    method.in_id = str(in_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fault_ack_fault_by_dn(cookie, dn):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("FaultAckFaultByDn")

    method.cookie = cookie
    method.dn = dn

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fault_ack_faults(cookie, in_ids):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("FaultAckFaults")

    method.cookie = cookie
    method.in_ids = in_ids

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fault_ack_faults_by_dn(cookie, in_dns):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("FaultAckFaultsByDn")

    method.cookie = cookie
    method.in_dns = in_dns

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fault_resolve_fault(cookie, in_id):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("FaultResolveFault")

    method.cookie = cookie
    method.in_id = str(in_id)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def firmware_estimate_pack_impact(cookie, dn, in_group_dn, in_pack_configs):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("FirmwareEstimatePackImpact")

    method.cookie = cookie
    method.dn = dn
    method.in_group_dn = in_group_dn
    method.in_pack_configs = in_pack_configs

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def firmware_install_all(cookie, dn, in_concurrent_jobs, in_group_dn, in_honor_ls_maint, in_ignore_comp_check, in_packages, in_start_time, in_user_ack):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("FirmwareInstallAll")

    method.cookie = cookie
    method.dn = dn
    method.in_concurrent_jobs = str(in_concurrent_jobs)
    method.in_group_dn = in_group_dn
    method.in_honor_ls_maint = in_honor_ls_maint
    method.in_ignore_comp_check = in_ignore_comp_check
    method.in_packages = in_packages
    method.in_start_time = in_start_time
    method.in_user_ack = in_user_ack

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def fsm_debug_action(cookie, dn, in_directive):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("FsmDebugAction")

    method.cookie = cookie
    method.dn = dn
    method.in_directive = in_directive

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ident_get_block_report(cookie, in_block, in_pool):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("IdentGetBlockReport")

    method.cookie = cookie
    method.in_block = in_block
    method.in_pool = in_pool

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ident_get_id_usage(cookie, in_pool_dn):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("IdentGetIdUsage")

    method.cookie = cookie
    method.in_pool_dn = in_pool_dn

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ident_get_sorted_ids(cookie, in_block, in_pool):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("IdentGetSortedIds")

    method.cookie = cookie
    method.in_block = in_block
    method.in_pool = in_pool

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def logging_sync_ocns(cookie, in_from_or_zero, in_to_or_zero):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("LoggingSyncOcns")

    method.cookie = cookie
    method.in_from_or_zero = str(in_from_or_zero)
    method.in_to_or_zero = str(in_to_or_zero)

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ls_clone(cookie, dn, in_server_name, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("LsClone")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_server_name = in_server_name
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ls_instantiate_n_named_template(cookie, dn, in_error_on_existing, in_name_set, in_pool_name, in_qualifier_name, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("LsInstantiateNNamedTemplate")

    method.cookie = cookie
    method.dn = dn
    method.in_error_on_existing = in_error_on_existing
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_name_set = in_name_set
    method.in_pool_name = in_pool_name
    method.in_qualifier_name = in_qualifier_name
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ls_instantiate_n_template(cookie, dn, in_number_of, in_pool_name, in_qualifier_name, in_server_name_prefix_or_empty, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("LsInstantiateNTemplate")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_number_of = str(in_number_of)
    method.in_pool_name = in_pool_name
    method.in_qualifier_name = in_qualifier_name
    method.in_server_name_prefix_or_empty = in_server_name_prefix_or_empty
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ls_instantiate_template(cookie, dn, in_error_on_existing, in_server_name, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("LsInstantiateTemplate")

    method.cookie = cookie
    method.dn = dn
    method.in_error_on_existing = in_error_on_existing
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_server_name = in_server_name
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def ls_templatise(cookie, dn, in_target_org, in_template_name, in_template_type, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("LsTemplatise")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org
    method.in_template_name = in_template_name
    method.in_template_type = in_template_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def lstorage_clone(cookie, dn, in_array_name, in_target_org, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("LstorageClone")

    method.cookie = cookie
    method.dn = dn
    method.in_array_name = in_array_name
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_target_org = in_target_org

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def method_vessel(cookie, in_stimuli):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("MethodVessel")

    method.cookie = cookie
    method.in_stimuli = in_stimuli

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def org_get_domain_firmware_report(cookie, in_domain_group_dn, in_domain_list, in_firmware_type, in_maint_tag):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("OrgGetDomainFirmwareReport")

    method.cookie = cookie
    method.in_domain_group_dn = in_domain_group_dn
    method.in_domain_list = in_domain_list
    method.in_firmware_type = in_firmware_type
    method.in_maint_tag = in_maint_tag

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def org_get_domain_policy_report(cookie, in_config, in_domain_group_dn, in_domain_type):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("OrgGetDomainPolicyReport")

    method.cookie = cookie
    method.in_config = in_config
    method.in_domain_group_dn = in_domain_group_dn
    method.in_domain_type = in_domain_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def org_get_impacted_domains(cookie, in_config, in_domain_group_dn, in_domain_type, in_dynamic, in_firmware_type, in_maint_tag, in_profile_name):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("OrgGetImpactedDomains")

    method.cookie = cookie
    method.in_config = in_config
    method.in_domain_group_dn = in_domain_group_dn
    method.in_domain_type = in_domain_type
    method.in_dynamic = in_dynamic
    method.in_firmware_type = in_firmware_type
    method.in_maint_tag = in_maint_tag
    method.in_profile_name = in_profile_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def org_get_num_impacted_domains(cookie, in_config, in_domain_group_dn, in_dynamic, in_firmware_type, in_maint_tag, in_profile_name):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("OrgGetNumImpactedDomains")

    method.cookie = cookie
    method.in_config = in_config
    method.in_domain_group_dn = in_domain_group_dn
    method.in_dynamic = in_dynamic
    method.in_firmware_type = in_firmware_type
    method.in_maint_tag = in_maint_tag
    method.in_profile_name = in_profile_name

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def org_get_subscribed_domains(cookie, in_class_id, in_domain_group_dn, in_subscription_type):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("OrgGetSubscribedDomains")

    method.cookie = cookie
    method.in_class_id = str(in_class_id)
    method.in_domain_group_dn = in_domain_group_dn
    method.in_subscription_type = in_subscription_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def org_resolve_elements(cookie, dn, in_class, in_filter, in_single_level, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("OrgResolveElements")

    method.cookie = cookie
    method.dn = dn
    method.in_class = in_class
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_single_level = in_single_level

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def org_resolve_in_scope(cookie, dn, in_class, in_filter, in_single_level, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("OrgResolveInScope")

    method.cookie = cookie
    method.dn = dn
    method.in_class = in_class
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_single_level = in_single_level

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def org_resolve_logical_parents(cookie, dn, in_single_level, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("OrgResolveLogicalParents")

    method.cookie = cookie
    method.dn = dn
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_single_level = in_single_level

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def policy_resolve_names(cookie, in_client_connector_dn, in_context, in_filter, in_policy_type):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("PolicyResolveNames")

    method.cookie = cookie
    method.in_client_connector_dn = in_client_connector_dn
    method.in_context = in_context
    method.in_filter = in_filter
    method.in_policy_type = in_policy_type

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def pool_resolve_in_scope(cookie, dn, in_class, in_filter, in_single_level, in_hierarchical=YesOrNo.FALSE):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("PoolResolveInScope")

    method.cookie = cookie
    method.dn = dn
    method.in_class = in_class
    method.in_filter = in_filter
    method.in_hierarchical = (("false", "true")[in_hierarchical in ucscgenutils.AFFIRMATIVE_LIST])
    method.in_single_level = in_single_level

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def snmp_find_var(cookie, in_is_exact, in_oid):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("SnmpFindVar")

    method.cookie = cookie
    method.in_is_exact = in_is_exact
    method.in_oid = in_oid

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def stats_build_chart_result(cookie, dn):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("StatsBuildChartResult")

    method.cookie = cookie
    method.dn = dn

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def stats_build_custom_chart(cookie, in_aggregate_by_dn, in_end_time, in_overlay, in_resolve_dns, in_start_time, in_stats_types):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("StatsBuildCustomChart")

    method.cookie = cookie
    method.in_aggregate_by_dn = in_aggregate_by_dn
    method.in_end_time = str(in_end_time)
    method.in_overlay = in_overlay
    method.in_resolve_dns = in_resolve_dns
    method.in_start_time = str(in_start_time)
    method.in_stats_types = in_stats_types

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def stats_build_standard_chart(cookie, in_aggregation_property, in_context_class, in_count, in_end_time, in_overlay, in_parent_dn, in_report_type, in_start_time, in_stats_types):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("StatsBuildStandardChart")

    method.cookie = cookie
    method.in_aggregation_property = in_aggregation_property
    method.in_context_class = in_context_class
    method.in_count = str(in_count)
    method.in_end_time = str(in_end_time)
    method.in_overlay = in_overlay
    method.in_parent_dn = in_parent_dn
    method.in_report_type = in_report_type
    method.in_start_time = str(in_start_time)
    method.in_stats_types = in_stats_types

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def stats_clear_interval(cookie, in_dns):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("StatsClearInterval")

    method.cookie = cookie
    method.in_dns = in_dns

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def stats_subscribe(cookie, in_category, in_provider, in_schema_info, in_time_interval):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("StatsSubscribe")

    method.cookie = cookie
    method.in_category = in_category
    method.in_provider = in_provider
    method.in_schema_info = in_schema_info
    method.in_time_interval = in_time_interval

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def synthetic_fs_obj_inventory(cookie, dn, in_config):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("SyntheticFSObjInventory")

    method.cookie = cookie
    method.dn = dn
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def synthetic_fs_obj_inventory_b(cookie, in_config):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("SyntheticFSObjInventoryB")

    method.cookie = cookie
    method.in_config = in_config

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request


def synthetic_test_tx(cookie, in_config, in_test, in_what):
    """ Auto-generated UCSC XML API Method. """
    method = ExternalMethod("SyntheticTestTx")

    method.cookie = cookie
    method.in_config = in_config
    method.in_test = in_test
    method.in_what = in_what

    xml_request = method.to_xml(option=WriteXmlOption.DIRTY)
    return xml_request

