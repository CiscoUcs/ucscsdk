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

import os
from nose.plugins.skip import SkipTest
try:
    import ConfigParser
except:
    import configparser as ConfigParser


def custom_setup():
    from ucscsdk.ucschandle import UcscHandle
    host = "ucscentral"

    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))

    hostname = config.get(host, "hostname")
    username = config.get(host, "username")
    password = config.get(host, "password")
    try:
        port = config.get(host, "port")
    except:
        port = 443
    handle = UcscHandle(hostname, username, password, port=port)
    handle.login()
    return handle


def custom_teardown(handle):
    handle.logout()


def get_local_config_params(section):

    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    local = {}
    try:
        local['file_dir'] = config.get(section, "file_dir")
        local['file_name'] = config.get(section, "file_name")
        for value in local.values():
            if not value or value.isspace():
                raise
    except:
        local = None
    return local


def get_remote_config_params(section):

    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    remote = {}
    try:
        remote['hostname'] = config.get(section, "hostname")
        remote['username'] = config.get(section, "username")
        remote['password'] = config.get(section, "password")
        remote['protocol'] = config.get(section, "protocol")
        remote['file_dir'] = config.get(section, "file_dir")
        remote['file_name'] = config.get(section, "file_name")
        for value in remote.values():
            if not value or value.isspace():
                raise
    except:
        remote = None
    return remote


def get_domain_params(number_of_domains=1):
    section = "domain"

    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    domains = []
    try:
        for x in range(number_of_domains):
            domain = {}
            domain['ip'] = config.get(section, "domain_ip_%s" % x)
            domain['username'] = config.get(section, "domain_username_%s" % x)
            domain['password'] = config.get(section, "domain_password_%s" % x)
            for value in domain.values():
                if not value or value.isspace():
                    raise
            domains.append(domain)
    except:
        domains = None
    return domains


def get_cisco_account_params():
    section = "cisco_account"

    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'connection',
                             'connection.cfg'))
    cisco_account = {}
    try:
        cisco_account['username'] = config.get(section, "username")
        cisco_account['password'] = config.get(section, "password")
        cisco_account['proxy_host'] = config.get(section, "proxy_host")
        cisco_account['proxy_port'] = config.get(section, "proxy_port")
        cisco_account['proxy_username'] = config.get(section, "proxy_username")
        cisco_account['proxy_password'] = config.get(section, "proxy_password")
        for value in cisco_account.values():
            if not value or value.isspace():
                raise
    except:
        cisco_account = None
    return cisco_account


def skipped(reason=None):
    def wrap(func):
        def f():
            raise SkipTest("Test %s is skipped, reason: '%s'"
                           % (func.__name__,
                              "Not specified" if reason is None else reason))
        f.__name__ = func.__name__
        return f
    return wrap
