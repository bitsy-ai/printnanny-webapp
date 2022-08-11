# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.100.5
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.system_info_request import SystemInfoRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestSystemInfoRequest(unittest.TestCase):
    """SystemInfoRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SystemInfoRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.system_info_request.SystemInfoRequest()  # noqa: E501
        if include_optional :
            return SystemInfoRequest(
                machine_id = '0', 
                revision = '0', 
                model = '0', 
                serial = '0', 
                cores = -2147483648, 
                ram = -9223372036854775808, 
                os_version_id = '0', 
                os_build_id = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                os_variant_id = '0', 
                os_release_json = {
                    'key' : null
                    }, 
                pi = 56
            )
        else :
            return SystemInfoRequest(
                machine_id = '0',
                revision = '0',
                model = '0',
                serial = '0',
                cores = -2147483648,
                ram = -9223372036854775808,
                os_version_id = '0',
                os_build_id = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                os_variant_id = '0',
                pi = 56,
        )

    def testSystemInfoRequest(self):
        """Test SystemInfoRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
