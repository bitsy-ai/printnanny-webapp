# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.135.1
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.system_info import SystemInfo  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestSystemInfo(unittest.TestCase):
    """SystemInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SystemInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.system_info.SystemInfo()  # noqa: E501
        if include_optional :
            return SystemInfo(
                id = 56, 
                bootfs_available = 56, 
                bootfs_available_pretty = '', 
                bootfs_used_pretty = '', 
                bootfs_size_pretty = '', 
                datafs_available = 56, 
                datafs_available_pretty = '', 
                datafs_used_pretty = '', 
                datafs_size_pretty = '', 
                rootfs_available = 56, 
                rootfs_available_pretty = '', 
                rootfs_size_pretty = '', 
                rootfs_used_pretty = '', 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                machine_id = '', 
                revision = '', 
                model = '', 
                serial = '', 
                cores = -2147483648, 
                ram = -9223372036854775808, 
                os_version_id = '', 
                os_build_id = '', 
                os_release_json = {
                    'key' : null
                    }, 
                uptime = -9223372036854775808, 
                rootfs_size = -9223372036854775808, 
                rootfs_used = -9223372036854775808, 
                bootfs_size = -9223372036854775808, 
                bootfs_used = -9223372036854775808, 
                datafs_size = -9223372036854775808, 
                datafs_used = -9223372036854775808, 
                pi = 56
            )
        else :
            return SystemInfo(
                id = 56,
                bootfs_available = 56,
                bootfs_available_pretty = '',
                bootfs_used_pretty = '',
                bootfs_size_pretty = '',
                datafs_available = 56,
                datafs_available_pretty = '',
                datafs_used_pretty = '',
                datafs_size_pretty = '',
                rootfs_available = 56,
                rootfs_available_pretty = '',
                rootfs_size_pretty = '',
                rootfs_used_pretty = '',
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                machine_id = '',
                revision = '',
                model = '',
                serial = '',
                cores = -2147483648,
                ram = -9223372036854775808,
                uptime = -9223372036854775808,
                rootfs_size = -9223372036854775808,
                rootfs_used = -9223372036854775808,
                bootfs_size = -9223372036854775808,
                bootfs_used = -9223372036854775808,
                datafs_size = -9223372036854775808,
                datafs_used = -9223372036854775808,
                pi = 56,
        )

    def testSystemInfo(self):
        """Test SystemInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
