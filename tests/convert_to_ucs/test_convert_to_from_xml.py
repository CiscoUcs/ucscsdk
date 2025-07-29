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

from ucscsdk.utils.converttopython import convert_to_ucs_python

def test_001_convert_to_from_xml_sp():
    xml_str = '''

<configConfMo
dn=""
cookie="SECURED"
inHierarchical="false">
    <inConfig>
<fabricUdldLinkPolicy
adminState="enabled"

descr="for testing"
dn="domaingroup-root/udld-link-pol-test_udldlink"
name="test_udldlink"

status="created">
</fabricUdldLinkPolicy>
    </inConfig>
</configConfMo>

    '''
    convert_to_ucs_python(xml=True, request=xml_str, dump_xml=True)
