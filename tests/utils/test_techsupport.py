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

from ucscsdk.utils.ucsctechsupport import *
from nose.plugins.attrib import attr
from ..connection.info import custom_setup, custom_teardown, \
    get_local_config_params, get_domain_params, skipped


local_download = get_local_config_params("techsupport_download")
domain_params = get_domain_params(1)


handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)

@attr('slow')
def test_001_get_techsupport():
    if local_download is None:
        skipped("Arguments missing in config file")(test_001_get_techsupport)()
    get_tech_support(handle, file_dir=local_download['file_dir'],
                     file_name=local_download['file_name'],
                     remove_from_ucsc=True)


@attr('slow')
def test_002_get_domain_techsupport():
    if domain_params is None:
        skipped("Arguments missing in config file")(
            test_002_get_domain_techsupport)()
    get_domain_tech_support(handle, domain_ip=domain_params[0]['ip'])
